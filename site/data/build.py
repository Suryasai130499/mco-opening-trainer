# -*- coding: utf-8 -*-
"""Expand the authored SAN lines into per-ply positions and write ../openings.js.

    pip install chess
    python data/build.py
"""
import os, sys, io, json, re, importlib
import chess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, os.pardir, 'openings.js')
sys.path.insert(0, HERE)

from sides import side_of, SIDES

MODULES = ['data_p1', 'data_p2', 'data_p3', 'data_p4', 'data_p5', 'data_p6']


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def legal_of(board):
    """Every legal move in this position as "e2e4" text, space separated.

    The trainer has no engine, so without this a board cannot tell an illegal
    move from a wrong one - and the difference matters: dragging a knight to a
    square it cannot reach should do nothing, while playing a real move that is
    not this line's move is a mistake worth reporting."""
    return ' '.join(sorted(
        chess.square_name(m.from_square) + chess.square_name(m.to_square)
        for m in board.legal_moves))


def play(board, tokens):
    """Push each SAN onto board, returning one record per ply."""
    plies = []
    for tok in tokens:
        lm = legal_of(board)
        mv = board.parse_san(tok)
        san = board.san(mv)
        board.push(mv)
        plies.append({
            "san": san,
            "from": chess.square_name(mv.from_square),
            "to": chess.square_name(mv.to_square),
            "fen": board.fen(),
            "chk": board.is_check(),
            # legal moves in the position this ply is played *from*
            "lm": lm,
        })
    return plies


def pgn_of(plies, start_ply=0):
    """Numbered move text; a line starting on Black's move opens with '7...'."""
    out = []
    for i, p in enumerate(plies):
        ply = start_ply + i
        if ply % 2 == 0:
            out.append("%d.%s" % (ply // 2 + 1, p['san']))
        elif i == 0:
            out.append("%d...%s" % (ply // 2 + 1, p['san']))
        else:
            out.append(p['san'])
    return ' '.join(out)


def expand(sanline):
    """Return (plies, numbered PGN) for a line from the starting position."""
    plies = play(chess.Board(), sanline.split())
    return plies, pgn_of(plies)


# Sidelines recovered from the book's footnotes (see extract_sublines.py).
SUBS = {}
_subpath = os.path.join(HERE, 'sublines.json')
if os.path.exists(_subpath):
    for s in json.load(io.open(_subpath, encoding='utf-8')):
        SUBS.setdefault((s['chapter'], s['var']), []).append(s)


parts, n_ch, n_var, n_sub, seen = [], 0, 0, 0, set()
ch_ids = set()

for mname in MODULES:
    P = importlib.import_module(mname).PART
    chapters = []
    for ch in P['chapters']:
        cplies, cpgn = expand(ch['line']) if ch['line'] else ([], '')
        variations = []
        for (name, page, sanline, note) in ch['variations']:
            plies, pgn = expand(sanline)
            vid = ch['id'] + '--' + slug(name)
            assert vid not in seen, 'duplicate id: ' + vid
            seen.add(vid)

            subs = []
            for s in sorted(SUBS.get((ch['id'], name), []), key=lambda x: (x['fromPly'], x['key'])):
                fp = s['fromPly']
                assert fp <= len(plies), 'sideline branches past the end of ' + vid
                board = chess.Board(plies[fp - 1]['fen']) if fp else chess.Board()
                sp = play(board, s['line'])
                subs.append({
                    "id": vid + "--s" + str(len(subs) + 1),
                    "fromPly": fp, "page": s['page'], "key": s['key'],
                    "cite": s['cite'], "verdict": s['verdict'],
                    "pgn": pgn_of(sp, fp), "plies": sp,
                })
                n_sub += 1

            variations.append({"id": vid, "name": name, "page": page,
                               "note": note, "pgn": pgn, "plies": plies,
                               "subs": subs})
            n_var += 1
        chapters.append({
            "id": ch['id'], "num": ch['num'], "name": ch['name'],
            "side": side_of(ch['id']),
            "aka": ch.get('aka', ''), "eco": ch.get('eco', ''), "page": ch['page'],
            "line": ch['line'], "linePgn": cpgn, "linePlies": cplies,
            "summary": ch['summary'], "whitePlan": ch['white_plan'],
            "blackPlan": ch['black_plan'], "variations": variations,
        })
        ch_ids.add(ch['id'])
        n_ch += 1
    parts.append({"id": P['id'], "num": P['num'], "name": P['name'],
                  "line": P['line'], "blurb": P['blurb'], "chapters": chapters})

extra = sorted(set(SIDES) - ch_ids)
assert not extra, 'sides.py names chapters that do not exist: %s' % extra

data = {
    "meta": {
        "source": "Modern Chess Openings, 15th Edition",
        "author": "Nick de Firmian",
        "publisher": "Random House Puzzles & Games / David McKay (2008)",
        "parts": len(parts), "chapters": n_ch, "variations": n_var,
        "white": sum(1 for p in parts for c in p['chapters'] if c['side'] == 'w'),
        "black": sum(1 for p in parts for c in p['chapters'] if c['side'] == 'b'),
        "sublines": n_sub,
        "note": "Chapters, named variations and page references follow the book's contents "
                "and index. Sidelines come from the book's footnotes. Every move sequence "
                "has been machine-verified as legal chess.",
    },
    "parts": parts,
}

io.open(OUT, 'w', encoding='utf-8').write(
    "/* Modern Chess Openings, 15th Edition - structured opening data.\n"
    "   Generated by data/build.py; every line machine-verified legal. */\n"
    "window.MCO_DATA = " + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ";\n"
)
print("parts=%d chapters=%d variations=%d sidelines=%d -> %s (%d bytes)"
      % (len(parts), n_ch, n_var, n_sub, os.path.normpath(OUT), os.path.getsize(OUT)))

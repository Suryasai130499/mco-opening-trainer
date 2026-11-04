# -*- coding: utf-8 -*-
"""Recover the sidelines in MCO-15's footnotes and attach them to our variations.

    pip install chess pypdf
    python site/data/extract_sublines.py "<path to the MCO-15 pdf>"

Writes sublines.json next to this file. build.py folds that into openings.js.

How it works, and why it is this careful
----------------------------------------
The scan's column tables are unusable - "Nf3" comes out as "МЗ", "Nc6" as "Nc8" -
but the footnotes under them survived, because they are ordinary prose lines. Each
footnote is a short piece of analysis: a move number, a run of moves, often a
verdict and the game it came from.

Two things have to be right for a footnote to be worth keeping:

1. Reading the moves. The scan drops spaces ("8 d4Nh5"), so the text is parsed
   against a live board: at each step we ask which moves are legal and look for
   one of them in the text. Everything that comes out is legal chess by
   construction. No single-letter "repairs" are allowed - they turn Nc6 into Nb6
   and quietly produce a line that fits the wrong position.

2. Finding where it branches. The footnote gives a move number but not which
   column it belongs to, so each of our variations is tried at that move number
   and the reading that replays furthest wins. Three checks throw out bad fits:
   a match must sit within a couple of pages of the line it attaches to, it must
   leave that line rather than repeat it, and a footnote that disambiguates a
   move ("Nbd2") where this position needs none is rejected outright - it proves
   two pieces reach that square in the book's position and only one does here.
   A reading that stops while a well-formed move is still waiting is also
   dropped unless it already ran long, since stopping early means the position
   is wrong.

The result is about 300 sidelines from 1,700 footnotes. The rest branch from
column lines this project does not carry, and are left out rather than guessed at.
"""
import io, os, re, sys, json, statistics, importlib
import chess

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sanparse

MODULES = ['data_p1', 'data_p2', 'data_p3', 'data_p4', 'data_p5', 'data_p6']

MIN_PLY = 4             # a note starting at move 1-2 is a transposition remark
NEAR_PAGES, NEAR_MOVES = 2, 3
FAR_PAGES, FAR_MOVES = 6, 6
CUT_SHORT_MOVES = 8     # keep a note we could not finish only if it ran this long
INDEX_FIRST_PAGE = 741  # printed page where the index starts; chapters end before it

# ---------------------------------------------------------------- pdf -> text

HOMO = {
    'А': 'A', 'В': 'B', 'С': 'C', 'Е': 'E', 'Н': 'H', 'К': 'K', 'М': 'M', 'О': 'O',
    'Р': 'P', 'Т': 'T', 'Х': 'X', 'а': 'a', 'в': 'b', 'с': 'c', 'е': 'e', 'н': 'h',
    'к': 'k', 'м': 'm', 'о': 'o', 'р': 'p', 'т': 't', 'х': 'x', 'у': 'y', 'і': 'i',
    'Ь': 'b', 'Ё': 'E', 'З': '3', 'б': '6', 'Ј': 'J', 'Ѕ': 'S', 'ѕ': 's', 'Ү': 'Y',
    '‘': "'", '’': "'", '“': '"', '”': '"',
    '–': '-', '—': '-', '−': '-',
}
HOMO_RE = re.compile('|'.join(map(re.escape, HOMO)))


def normalise(s):
    s = HOMO_RE.sub(lambda m: HOMO[m.group(0)], s).replace('…', '...')
    s = re.sub(r'\b0-0-0\b', 'O-O-O', s)
    s = re.sub(r'\b0-0\b', 'O-O', s)
    # the scan renders the check dagger as a trailing 't'
    s = re.sub(r'\b([KQRBN]?[a-h]?[1-8]?x?[a-h][1-8])t\b', r'\1+', s)
    s = re.sub(r'\b(O-O-O|O-O)t\b', r'\1+', s)
    return re.sub(r'[ \t]+', ' ', s)


def printed_page(txt):
    """The running footer: the last standalone number on the page."""
    lines = [l.strip() for l in txt.strip().split('\n') if l.strip()]
    for l in reversed(lines[-4:]):
        if re.fullmatch(r'\d{1,3}', l):
            return int(l)
    return None


FN_START = re.compile(r'\(([a-z])\)\s')
FN_LINE = re.compile(r'\s*\(([a-z])\)\s')


def footnotes_on(txt):
    """Split a page's footnote block into (letter, text) pairs.

    A set of notes usually runs over two pages - (a)...(f) under the columns,
    then (g) onwards on the next page - so the block is not required to open at
    (a); it opens at whatever letter starts the first footnote line. Letters only
    have to increase, not be consecutive, so one marker the scan mangled does not
    discard the rest of the page.
    """
    txt = normalise(txt)
    lines = txt.split('\n')
    start = next((i for i, l in enumerate(lines) if FN_LINE.match(l)), None)
    if start is None:
        return []
    body = re.sub(r'\s+', ' ', ' '.join(l.strip() for l in lines[start:]))
    kept, last = [], None
    for m in FN_START.finditer(body):
        ch = m.group(1)
        if last is None or ch > last:
            kept.append((m.start(), ch))
            last = ch
    out = []
    for i, (pos, ch) in enumerate(kept):
        end = kept[i + 1][0] if i + 1 < len(kept) else len(body)
        out.append((ch, body[pos + 4:end].strip()))
    return out


def read_notes(pdf_path):
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    notes = []
    for i, page in enumerate(reader.pages):
        try:
            txt = page.extract_text() or ''
        except Exception:
            continue
        pp = printed_page(txt)
        for letter, body in footnotes_on(txt):
            notes.append({"pdf": i + 1, "page": pp, "key": letter, "text": body})
    offs = [n['page'] - n['pdf'] for n in notes if n['page']]
    offset = int(statistics.median(offs)) if offs else 0
    for n in notes:
        if not n['page']:
            n['page'] = n['pdf'] + offset
    return notes


# ------------------------------------------------------------- note anatomy

PARENS = re.compile(r'\([^()]*\)')
ALT = re.compile(r'\(([A-E])\)')
GAME = re.compile(
    r"\b([A-Z][A-Za-zÀ-ɏ.'’\- ]{1,22}?\s*[-–]\s*"
    r"[A-Z][A-Za-zÀ-ɏ.'’\- ]{1,22}?),\s*"
    r"([A-Za-zÀ-ɏ.'\- ]{0,26}?)\s*(\d{4})")
TAILMOVE = re.compile(
    r'\s*(?:\d{1,3}\s*\.{0,3}\s*)?'
    r'(?:O-O-O|O-O|[KQRBN][a-h1-8]?x?[a-h][1-8]|[a-h]x[a-h][1-8]|[a-h][1-8])'
    r'(?![A-Za-z])')

# The scan destroys the book's evaluation symbols, so a symbol is never guessed
# at; only a verdict spelled out in words is kept, normalised to a short label.
VERDICTS = [(re.compile(p, re.I), label) for p, label in [
    (r'\bunclear\b|\bmurky\b', 'unclear'),
    (r'\bchances for both sides\b|\bdouble[- ]edged\b', 'chances for both sides'),
    (r'\b(?:is|are|about|approximately|roughly)\s+(?:even|equal)\b|\bequalize', 'equal'),
    (r'\bgood for Black\b|\bfavou?r(?:s|ed|ing)? Black\b|\bBlack is better\b', 'good for Black'),
    (r'\bgood for White\b|\bfavou?r(?:s|ed|ing)? White\b|\bWhite is better\b', 'good for White'),
    (r'\b(?:slight(?:ly)?|small|a little|an edge).{0,24}\bfor Black\b|\bedge for Black\b', 'a little better for Black'),
    (r'\b(?:slight(?:ly)?|small|a little|an edge).{0,24}\bfor White\b|\bedge for White\b', 'a little better for White'),
    (r'\badvantage to White\b|\bterrific attack\b|\bstrong attack\b.{0,20}White', 'advantage to White'),
    (r'\badvantage to Black\b', 'advantage to Black'),
    (r'\bsolid\b.{0,20}\bBlack\b|\bfine for Black\b|\bokay for Black\b|\bBlack (?:is )?fine\b', 'fine for Black'),
    (r'\bwins?\b(?!\w)', 'wins'),
]]


def first_alternative(s):
    """Notes listing (A) ... (B) ...: keep the first, so (B)'s game is not
    credited to (A)'s moves."""
    marks = [m.start() for m in ALT.finditer(s)]
    if len(marks) >= 2:
        return s[marks[0]:marks[1]]
    return s[marks[0]:] if marks else s


def strip_asides(s):
    prev = None
    while prev != s:
        prev = s
        s = PARENS.sub(' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def citation(text, start=0):
    m = GAME.search(text, start)
    if not m or m.start() - start > 90:
        return ""
    who = re.sub(r'(\w)-\s+(\w)', r'\1\2', re.sub(r'\s*-\s*', '–', m.group(1).strip()))
    where = re.sub(r'(\w)-\s+(\w)', r'\1\2', m.group(2).strip(' .,'))
    return (who + ", " + where + " " + m.group(3)).replace("  ", " ").strip(" ,")


def verdict(text):
    for rx, label in VERDICTS:
        if rx.search(text):
            return label
    return ""


# ------------------------------------------------------------------- anchor

def load_chapters():
    chapters = []
    for mn in MODULES:
        part = importlib.import_module(mn).PART
        for ch in part['chapters']:
            variations = []
            for (name, page, sanline, _note) in ch['variations']:
                b = chess.Board()
                sans, fens = [], [b.fen()]
                for tok in sanline.split():
                    b.push_san(tok)
                    sans.append(tok)
                    fens.append(b.fen())
                variations.append({"name": name, "page": page, "sans": sans, "fens": fens})
            chapters.append({"id": ch['id'], "page": ch['page'], "vars": variations})
    chapters.sort(key=lambda c: c['page'])
    for i, c in enumerate(chapters):
        c['to'] = (chapters[i + 1]['page'] - 1) if i + 1 < len(chapters) else INDEX_FIRST_PAGE - 1
    return chapters


def divergence(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i


def main(pdf_path):
    chapters = load_chapters()
    notes = read_notes(pdf_path)
    print("footnotes found:", len(notes))

    results = []
    for n in notes:
        ch = next((c for c in chapters if c['page'] <= n['page'] <= c['to']), None)
        if not ch:
            continue
        body = strip_asides(first_alternative(n['text']))
        mark = sanparse.first_move_marker(body)
        if not mark:
            continue
        idx, num, black = mark
        ply = (num - 1) * 2 + (1 if black else 0)
        if ply < MIN_PLY:
            continue

        cands = []
        for v in ch['vars']:
            if ply >= len(v['fens']):
                continue
            dist = abs(v['page'] - n['page'])
            if dist > FAR_PAGES:
                continue
            sans, _rep, end, conflict = sanparse.parse(
                chess.Board(v['fens'][ply]), body, idx, allow_repair=False)
            if conflict:
                continue
            need = NEAR_MOVES if dist <= NEAR_PAGES else FAR_MOVES
            if TAILMOVE.match(body, end):
                need = max(need, CUT_SHORT_MOVES)
            if len(sans) < need:
                continue
            if v['sans'][ply:ply + len(sans)] == sans:    # just the main line again
                continue
            cands.append(((len(sans), -dist), v, sans, end))

        if not cands:
            continue
        top = max(c[0] for c in cands)
        tied = [c for c in cands if c[0] == top]
        # The same move text can be legal from two different positions. Where the
        # tied anchors are the same position the sideline is identical chess and
        # only its filing differs, but where they are different positions the book
        # means one of them and the text cannot say which, so drop it.
        if len({c[1]['fens'][ply] for c in tied}) > 1:
            continue
        _score, v, sans, end = tied[0]
        full = v['sans'][:ply] + sans
        d = divergence(full, v['sans'])
        results.append({
            "chapter": ch['id'], "var": v['name'], "page": n['page'], "key": n['key'],
            "fromPly": d, "line": full[d:],
            "cite": citation(body, end), "verdict": verdict(body),
        })

    results.sort(key=lambda r: (r['chapter'], r['var'], r['fromPly'], r['key']))
    out = os.path.join(HERE, 'sublines.json')
    io.open(out, 'w', encoding='utf-8').write(json.dumps(results, ensure_ascii=False, indent=1))
    print("sidelines kept: %d, attached to %d variations"
          % (len(results), len(set((r['chapter'], r['var']) for r in results))))
    print("wrote", out)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("usage: python extract_sublines.py <mco15.pdf>")
    main(sys.argv[1])

# -*- coding: utf-8 -*-
"""Parse OCR'd move text by matching against the legal moves of a live board.

The scan loses spaces ("8 d4Nh5") and mangles letters ("Nad4" for "Nxd4"), so a
plain tokeniser is useless. Instead we walk the string and, at each step, ask the
board which moves are legal and look for one of them in the text. A single-letter
repair is allowed only when exactly one legal move is that close.
"""
import re
import chess

TRAIL = "!?+#†‡"


_CACHE = {}


def _cands(board):
    """{text -> move} for every legal move, with and without the check mark."""
    key = board.board_fen() + " " + ("w" if board.turn else "b") + " " + \
        board.castling_xfen() + " " + str(board.ep_square)
    hit = _CACHE.get(key)
    if hit is not None:
        return hit
    out = {}
    for mv in board.legal_moves:
        san = board.san(mv)
        out.setdefault(san, mv)
        out.setdefault(san.rstrip("+#"), mv)
    if len(_CACHE) > 60000:
        _CACHE.clear()
    _CACHE[key] = out
    return out


def _sub1(a, b):
    """True when a and b are the same length and differ in exactly one character.

    Deliberately *not* edit distance: allowing an insertion or deletion lets
    "Nbd2" repair to "Nd2", which silently accepts a position where only one
    knight reaches d2 — i.e. the wrong position. Same-length substitution still
    catches the real scan errors ("Neb" for "Ne5", "Nad4" for "Nxd4").
    """
    return len(a) == len(b) and a != b and sum(1 for x, y in zip(a, b) if x != y) == 1


NUM = re.compile(r'\d{1,3}')
TOKEN = re.compile(r'[A-Za-z][A-Za-z0-9]*(?:=[QRBN])?|O-O-O|O-O')
DISAMB = re.compile(r'^[KQRBN][a-h1-8]x?[a-h][1-8]')
PLAIN = re.compile(r'^[KQRBN]x?[a-h][1-8]')


def over_specified(tok, san):
    """The book disambiguates ("Nbd2") where this position needs none ("Nd2").

    That means two pieces reach the square there and only one does here, so the
    anchor is wrong and the parse must stop rather than repair.
    """
    return bool(DISAMB.match(tok)) and bool(PLAIN.match(san))


def parse(board, s, i=0, limit=40, allow_repair=True):
    """Read moves from s[i:] onto a copy of board.

    Returns (sans, repairs, end_index, conflict). Stops at the first thing that
    is not a legal move, so everything returned is legal chess from the given
    position. `conflict` means the text disambiguated a move that needs no
    disambiguation here — the position is wrong, so the caller should discard
    this anchor rather than keep the moves read so far.
    """
    b = board.copy()
    sans, repairs, conflict = [], 0, False
    n = len(s)
    while len(sans) < limit:
        j = i
        # skip separators and any move number / ellipsis in between
        while j < n and (s[j] in " ., " or s[j] == '\n'):
            j += 1
        m = NUM.match(s, j)
        if m:
            j = m.end()
            while j < n and s[j] in " . ":
                j += 1
        if j >= n:
            break

        cands = _cands(b)
        # longest literal match wins ("Nxd4" before "Nd4" style collisions)
        best = None
        for text in sorted(cands, key=len, reverse=True):
            if s.startswith(text, j):
                nxt = s[j + len(text):j + len(text) + 1]
                if nxt and (nxt.isdigit() or nxt.isalpha()):
                    # would swallow part of the next token unless it is a new move
                    if not any(s.startswith(t2, j + len(text)) for t2 in cands):
                        continue
                best = (text, cands[text])
                break

        if best is None and allow_repair:
            tm = TOKEN.match(s, j)
            if tm:
                tok = tm.group(0).rstrip(TRAIL)
                if any(over_specified(tok, t) for t in cands):
                    conflict = True
                    break
                near = {cands[t] for t in cands if _sub1(tok, t)}
                if len(near) == 1:
                    mv = next(iter(near))
                    best = (tm.group(0), mv)
                    repairs += 1

        if best is None:
            break

        text, mv = best
        sans.append(b.san(mv))
        b.push(mv)
        i = j + len(text)
        while i < n and s[i] in TRAIL:
            i += 1
    return sans, repairs, i, conflict


def first_move_marker(s):
    """Where the analysis starts: (index, move number, black_to_move) or None."""
    for m in re.finditer(r'(?<![\d.])(\d{1,3})\s*(\.{0,3}|\s*\.\s*\.\s*\.)\s*', s):
        num = int(m.group(1))
        if not (1 <= num <= 40):
            continue
        dots = m.group(2).replace(' ', '')
        rest = s[m.end():m.end() + 10]
        if not re.match(r'[KQRBNOa-h]', rest):
            continue
        return m.start(), num, len(dots) >= 2
    return None

# -*- coding: utf-8 -*-
"""Replay every authored SAN line from the starting position and report illegal moves.

    pip install chess
    python data/validate.py
"""
import os, sys, importlib
import chess

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

MODULES = ['data_p1', 'data_p2', 'data_p3', 'data_p4', 'data_p5', 'data_p6']

bad = total = 0
for mname in MODULES:
    part = importlib.import_module(mname).PART
    for ch in part['chapters']:
        targets = [("[chapter line] " + ch['name'], ch['line'])] if ch['line'] else []
        targets += [(ch['name'] + " / " + v[0], v[2]) for v in ch['variations']]
        for label, sanline in targets:
            total += 1
            board = chess.Board()
            toks = sanline.split()
            for i, tok in enumerate(toks):
                try:
                    board.push_san(tok)
                except Exception:
                    bad += 1
                    print("ILLEGAL  " + label)
                    print("         move %d '%s' in: %s" % (i + 1, tok, sanline))
                    print("         fen:   " + board.fen())
                    print("         legal: " + ", ".join(sorted(board.san(m) for m in board.legal_moves)))
                    print()
                    break

print("checked %d lines, %d bad" % (total, bad))
sys.exit(1 if bad else 0)

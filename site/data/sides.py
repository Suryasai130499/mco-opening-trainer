# -*- coding: utf-8 -*-
"""Which colour each chapter is a repertoire for.

The trainer plays the opponent's replies for you, so every chapter has to say
whose moves the learner is responsible for. The rule is the one a player would
use out loud: the opening belongs to the side whose choice defines it. A
*Defense* or a *Counter Gambit* is named for Black's decision, so you drill it
as Black; an *Opening*, *Game*, *Attack* or a gambit White offers is White's.

A few need a word:
  two-knights      Black's answer to 3 Bc4; White's attacking tries are the
                   replies you have to be ready for.
  latvian-gambit   Black's gambit (2...f5), not White's.
  qgd / qga        Named for Black's decision to decline or accept.
  queens-pawn-games  White's 1 d4 systems (London, Colle, Trompowsky, Veresov).
  unusual-double-king-pawn  White's offbeat tries after 1 e4 e5.
  unusual-kings-pawn        Black's offbeat answers to 1 e4.
  misc-flank       White's first moves, so White.
"""

SIDES = {
    # Part I - Double King Pawn
    'kings-gambit': 'w',
    'giuoco-piano': 'w',
    'evans-gambit': 'w',
    'two-knights': 'b',
    'ruy-lopez': 'w',
    'petrov': 'b',
    'scotch': 'w',
    'vienna': 'w',
    'four-knights': 'w',
    'three-knights': 'w',
    'philidor': 'b',
    'ponziani': 'w',
    'goring-gambit': 'w',
    'danish-gambit': 'w',
    'latvian-gambit': 'b',
    'bishops-opening': 'w',
    'center-game': 'w',
    'unusual-double-king-pawn': 'w',

    # Part II - Semi-Open Games: every one is Black's answer to 1 e4
    'alekhines-defense': 'b',
    'caro-kann': 'b',
    'french': 'b',
    'sicilian': 'b',
    'pirc': 'b',
    'robatsch': 'b',
    'center-counter': 'b',      # Scandinavian Defense
    'nimzovich-defense': 'b',
    'unusual-kings-pawn': 'b',

    # Part III - Double Queen Pawn: all named for Black's reply to the gambit
    'qgd': 'b',
    'tarrasch': 'b',
    'qga': 'b',
    'slav': 'b',
    'chigorin': 'b',

    # Part IV - Other Queen Pawn
    'dutch': 'b',
    'budapest': 'b',
    'queens-pawn-games': 'w',

    # Part V - Indian Openings
    'catalan': 'w',
    'nimzo-indian': 'b',
    'queens-indian': 'b',
    'bogo-indian': 'b',
    'kings-indian': 'b',
    'old-indian': 'b',
    'grunfeld': 'b',
    'benoni': 'b',
    'benko': 'b',

    # Part VI - Flank Openings: White's systems
    'english': 'w',
    'reti': 'w',
    'kia': 'w',
    'larsen': 'w',
    'bird': 'w',
    'misc-flank': 'w',
}


def side_of(chapter_id):
    """'w' or 'b'. Raises rather than guessing, so a new chapter can't ship
    silently defaulting to the wrong colour."""
    try:
        return SIDES[chapter_id]
    except KeyError:
        raise KeyError("no side recorded for chapter %r - add it to sides.py" % chapter_id)

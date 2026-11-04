# -*- coding: utf-8 -*-
# Part IV — Other Queen Pawn Openings (1 d4, Black replies other than ...d5 / ...Nf6+...)

PART = {
    "id": "other-queen-pawn",
    "num": "IV",
    "name": "Other Queen Pawn Openings",
    "line": "d4",
    "blurb": "Black's independent answers to 1 d4 — the aggressive Dutch, the tricky Budapest — "
             "together with White's many ways of avoiding the Queen's Gambit altogether: the "
             "Trompowsky, Torre, Colle and Blackmar-Diemer.",
    "chapters": [
        {
            "id": "dutch", "num": 1, "name": "Dutch Defense", "eco": "A80–A99",
            "page": 493, "line": "d4 f5",
            "summary": "Black's most aggressive answer to 1 d4: the f-pawn fights for e4 and opens "
                       "the f-file for an attack. It weakens the king, so the Dutch is an "
                       "unbalanced, fighting defence by nature.",
            "white_plan": "Fianchetto with g3 and Bg2 to control e4 and the long diagonal, or hit "
                          "immediately with the Staunton Gambit (e4) or Bg5.",
            "black_plan": "Choose a structure — Leningrad (...g6), Stonewall (...d5, ...e6) or "
                          "Classical (...e6, ...d6) — and attack on the kingside with ...e5 or ...f4.",
            "variations": [
                ("Leningrad Variation", 495, "d4 f5 g3 Nf6 Bg2 g6 Nf3 Bg7 O-O O-O c4 d6 Nc3 Qe8 d5 Na6",
                 "A King's-Indian-style Dutch: the bishop on g7 and the ...e5 break give Black real attacking chances."),
                ("Leningrad: 7...c6", 497, "d4 f5 g3 Nf6 Bg2 g6 Nf3 Bg7 O-O O-O c4 d6 Nc3 c6 d5 e5",
                 "Black prepares ...e5 with ...c6, taking the fight directly to the centre."),
                ("Leningrad: 7...Nc6", 498, "d4 f5 g3 Nf6 Bg2 g6 Nf3 Bg7 O-O O-O c4 d6 Nc3 Nc6 d5 Ne5",
                 "An ambitious knight placement aiming for ...Ne5 and ...c6 pressure."),
                ("Stonewall Variation", 499, "d4 f5 g3 Nf6 Bg2 e6 Nf3 d5 O-O Bd6 c4 c6 b3 Qe7 Bb2 O-O",
                 "The rock-solid Stonewall: pawns on c6, d5, e6 and f5 give Black an iron grip on e4 and a kingside attack with ...Ne4 and ...Qh5."),
                ("Modern Stonewall (...Bd6 and ...b6)", 500, "d4 f5 g3 Nf6 Bg2 e6 Nf3 d5 O-O Bd6 c4 c6 Qc2 O-O Bf4 Bxf4 gxf4 b6",
                 "The modern treatment: Black trades the bad bishop via b7 or d6 and then attacks."),
                ("Ilyin-Zhenevsky System", 499, "d4 f5 g3 Nf6 Bg2 e6 Nf3 Be7 O-O O-O c4 d6 Nc3 Qe8 Re1 Qh5",
                 "The classical Dutch: Black plays ...d6 and ...Qe8–h5, preparing ...e5 and a direct kingside attack."),
                ("Staunton Gambit", 501, "d4 f5 e4 fxe4 Nc3 Nf6 Bg5 Nc6 d5 Ne5 Qd4 Nf7",
                 "White sacrifices a pawn to blow open the centre before Black develops. The most direct test of the Dutch."),
                ("Staunton Gambit: 4...d5", 502, "d4 f5 e4 fxe4 Nc3 Nf6 Bg5 d5 Bxf6 exf6 Qh5+ g6 Qxd5 Qxd5 Nxd5 Kd8",
                 "Black returns the pawn and heads for an endgame where the bishops compensate for the structure."),
                ("Minor Variations (2 Bg5)", 502, "d4 f5 Bg5 h6 Bh4 g5 e3 Nf6 Bg3 d6",
                 "An immediate, annoying bishop sortie that provokes Black into loosening the kingside."),
                ("Minor Variations (2 Nc3)", 502, "d4 f5 Nc3 d5 e4 fxe4 Nxe4 Nf6 Bd3",
                 "White supports e4 with the knight and strikes at once."),
            ],
        },
        {
            "id": "budapest", "num": 2, "name": "Budapest Defense", "eco": "A51–A52",
            "page": 503, "line": "d4 Nf6 c4 e5",
            "summary": "A surprise gambit: Black offers the e-pawn to gain time and open lines for "
                       "the pieces. It has never been refuted and is an excellent practical choice "
                       "against unprepared opponents.",
            "white_plan": "Hold the pawn with 4 Bf4 or give it back with 4 Nf3, then develop and "
                          "use the extra space and centre.",
            "black_plan": "Regain the pawn with ...Ng4 or ...Ne4, pressure e5 and d4, and exploit "
                          "the loosened dark squares.",
            "variations": [
                ("Main Line (4 Bf4)", 503, "d4 Nf6 c4 e5 dxe5 Ng4 Bf4 Nc6 Nf3 Bb4+ Nbd2 Qe7 a3 Ngxe5",
                 "The main line: White defends e5 with the bishop and Black regains the pawn with good play."),
                ("Rubinstein Variation (4 Bf4 Bb4+ 5 Nd2)", 504, "d4 Nf6 c4 e5 dxe5 Ng4 Bf4 Bb4+ Nd2 Qe7 a3 Ngxe5 axb4 Nd3+",
                 "A sharp line with a knight fork trick on d3; both sides must know the details."),
                ("Adler Variation (4 Nf3)", 504, "d4 Nf6 c4 e5 dxe5 Ng4 Nf3 Bc5 e3 Nc6 Be2 Ngxe5",
                 "White gives the pawn back and plays for a quiet space edge."),
                ("Alekhine Variation (4 e4)", 505, "d4 Nf6 c4 e5 dxe5 Ng4 e4 Nxe5 f4 Nec6 Be3 Bb4+",
                 "The most ambitious: White builds a huge centre at the cost of some weaknesses."),
                ("Fajarowicz Variation", 505, "d4 Nf6 c4 e5 dxe5 Ne4 Nf3 Nc6 a3 d6 Qc2 Bf5",
                 "The knight jumps to e4 instead of g4 — very sharp, very tricky and almost unknown to most opponents."),
            ],
        },
        {
            "id": "queens-pawn-games", "num": 3, "name": "Queen's Pawn Games and Gambits",
            "eco": "A40–A46, D00–D05", "page": 506, "line": "d4",
            "summary": "White's practical systems that sidestep the Queen's Gambit entirely — the "
                       "Trompowsky, Torre, London, Colle and Veresov — plus Black's offbeat "
                       "counter-gambits. Low on theory, high on understanding.",
            "white_plan": "Reach a sound, familiar structure quickly (Bf4/Bg5 with e3 and c3) and "
                          "play chess rather than memory.",
            "black_plan": "Exploit the fact that White has not challenged the centre with c4: take "
                          "space with ...d5 and ...c5, or ...e5.",
            "variations": [
                ("Trompowsky Attack", 508, "d4 Nf6 Bg5 e6 e4 h6 Bxf6 Qxf6 Nc3 d6 Qd2 g5",
                 "An immediate bishop sortie. White usually trades on f6 and plays for the centre with e4."),
                ("Trompowsky: 2...d5", 508, "d4 Nf6 Bg5 d5 Bxf6 exf6 e3 Bf5 c4 c6",
                 "Black allows the trade and gets the bishop pair with a doubled but solid pawn mass."),
                ("Trompowsky: 2...Ne4", 508, "d4 Nf6 Bg5 Ne4 Bf4 d5 e3 c5 Bd3 Nc6",
                 "A direct challenge: the knight hits the bishop and fights for the centre."),
                ("Veresov's Opening", 508, "d4 d5 Nc3 Nf6 Bg5 Nbd7 Nf3 e6 e4 dxe4 Nxe4 Be7",
                 "The 'Richter-Veresov Attack': White plays Nc3 and Bg5 and aims for e4. An aggressive, low-theory system."),
                ("Veresov with 3...Bf5", 509, "d4 d5 Nc3 Nf6 Bg5 Bf5 f3 Nbd7 Nxd5 Nxd5 e4",
                 "Black develops the bishop actively; White strikes with f3 and e4."),
                ("Torre Attack", 508, "d4 Nf6 Nf3 e6 Bg5 c5 e3 Be7 Nbd2 b6 Bd3 Bb7 c3 O-O",
                 "The Torre: Nf3, Bg5, e3 and Nbd2 — a safe, flexible system aimed at a later e4 or kingside attack."),
                ("Torre Attack vs ...d5", 510, "d4 Nf6 Nf3 d5 Bg5 e6 e3 Be7 Nbd2 Nbd7 Bd3 c5 c3 b6",
                 "A model Torre structure where White slowly prepares e4."),
                ("Colle System", 511, "d4 d5 Nf3 Nf6 e3 e6 Bd3 c5 c3 Nc6 Nbd2 Bd6 O-O O-O",
                 "The Colle: a compact set-up that aims for the e4 break and the Bxh7 sacrifice. Very easy to learn."),
                ("Zukertort / Rubinstein Colle", 511, "d4 d5 Nf3 Nf6 e3 e6 Bd3 c5 b3 Nc6 Bb2 Bd6 Nbd2 O-O",
                 "The Zukertort variant with b3 and Bb2 instead of c3, aiming at the long diagonal."),
                ("Polish Defense", 511, "d4 b5 e4 a6 Nf3 Bb7 Bd3 e6 O-O Nf6",
                 "Black grabs queenside space immediately with ...b5. Eccentric and rare."),
                ("Queen's Knight Defense", 512, "d4 Nc6 d5 Ne5 e4 e6 f4 Ng6",
                 "Black develops the knight to c6 and lets White chase it for space."),
                ("Englund Gambit", 512, "d4 e5 dxe5 Nc6 Nf3 Qe7 Bf4 Qb4+ Bd2 Qxb2",
                 "A pawn sacrifice to grab b2 with the queen. Unsound but startling."),
                ("Reversed Stonewall", 506, "d4 d5 e3 Nf6 Bd3 c5 c3 Nc6 f4 Bg4 Nf3 e6",
                 "White plays the Stonewall structure with colours reversed and an extra tempo."),
                ("Albin Counter Gambit", 513, "d4 d5 c4 e5 dxe5 d4 Nf3 Nc6 g3 Bg4 Bg2 Qd7",
                 "Black sacrifices a pawn for the advanced d4 wedge and the ...dxe3 trap (the Lasker trap with ...e2 and ...exf1 promoting to a knight)."),
                ("Blackmar-Diemer Gambit", 513, "d4 d5 e4 dxe4 Nc3 Nf6 f3 exf3 Nxf3 e6 Bg5 Be7",
                 "White offers a pawn for development and open lines. A fierce practical weapon at club level."),
                ("Blackmar-Diemer: Euwe Defense", 514, "d4 d5 e4 dxe4 Nc3 Nf6 f3 exf3 Nxf3 e6 Bd3 Be7 O-O O-O",
                 "The soundest defence: Black develops solidly and consolidates the extra pawn."),
                ("Blackmar-Diemer: Lemberger Counter Gambit", 514, "d4 d5 e4 dxe4 Nc3 e5 dxe5 Qxd1+ Nxd1 Nc6",
                 "Black hits back in the centre immediately and trades queens to defuse the attack."),
            ],
        },
    ],
}

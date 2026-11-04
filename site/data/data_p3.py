# -*- coding: utf-8 -*-
# Part III — Double Queen Pawn Openings (1 d4 d5 2 c4)

PART = {
    "id": "double-queen-pawn",
    "num": "III",
    "name": "Double Queen Pawn Openings",
    "line": "d4 d5 c4",
    "blurb": "The Queen's Gambit complex. White offers the c-pawn to deflect Black's d5 pawn and "
             "take over the centre. These are the great classical openings — the backbone of "
             "world championship chess for a hundred years.",
    "chapters": [
        {
            "id": "qgd", "num": 1, "name": "Queen's Gambit Declined", "eco": "D30–D69",
            "page": 389, "line": "d4 d5 c4 e6",
            "summary": "The most classical defence in chess. Black supports d5 with the e-pawn, "
                       "accepting a passive light-squared bishop for an impregnable centre. Decided "
                       "more world championship matches than any other opening.",
            "white_plan": "Build with Nc3, Nf3 and Bg5, play cxd5 at the right moment and launch "
                          "the minority attack with b4–b5, or press with Rc1 and Bd3.",
            "black_plan": "Free the game with ...dxc4 and ...c5, or ...Ne4 and ...c6, and solve the "
                          "problem of the c8 bishop via ...b6/...Bb7 or ...Nf8–g6.",
            "variations": [
                ("Orthodox Defense", 393, "d4 d5 c4 e6 Nc3 Nf6 Bg5 Be7 e3 O-O Nf3 Nbd7 Rc1 c6 Bd3 dxc4 Bxc4 Nd5",
                 "The classical main line with Capablanca's freeing manoeuvre ...Nd5. Black unravels by trading pieces."),
                ("Orthodox: Capablanca Freeing Manoeuvre", 394, "d4 d5 c4 e6 Nc3 Nf6 Bg5 Be7 e3 O-O Nf3 Nbd7 Rc1 c6 Bd3 dxc4 Bxc4 Nd5 Bxe7 Qxe7 O-O Nxc3 Rxc3 e5",
                 "The point of the Orthodox: Black trades off two pairs of pieces and frees the position with ...e5."),
                ("Orthodox: 8 Qc2", 397, "d4 d5 c4 e6 Nc3 Nf6 Bg5 Be7 e3 O-O Nf3 Nbd7 Qc2 c6 Rd1 dxc4 Bxc4 b5",
                 "White puts the queen on c2 and the rook on d1 before deciding about the bishop."),
                ("Petrosian Variation", 400, "d4 d5 c4 e6 Nc3 Nf6 Bg5 Be7 e3 O-O Nf3 h6 Bf4 b6 cxd5 Nxd5 Nxd5 exd5 Bd3 Bb7",
                 "White retreats to f4 after ...h6 and plays for a bind on the queenside and the c-file."),
                ("Modern Variants (5 Bf4)", 403, "d4 d5 c4 e6 Nc3 Nf6 Nf3 Be7 Bf4 O-O e3 Nbd7 c5 Nh5 Bd3 Nxf4 exf4",
                 "The bishop avoids the ...Ne4 and ...h6 tricks; White gains space with c5."),
                ("Lasker's Defense", 406, "d4 d5 c4 e6 Nc3 Nf6 Bg5 Be7 e3 O-O Nf3 h6 Bh4 Ne4 Bxe7 Qxe7 cxd5 Nxc3 bxc3 exd5",
                 "Black trades off into a simplified position. Extremely solid and still a top-level drawing weapon."),
                ("Cambridge Springs Variation", 409, "d4 d5 c4 e6 Nc3 Nf6 Bg5 Nbd7 Nf3 c6 e3 Qa5 Nd2 Bb4 Qc2 O-O",
                 "Black's ...Qa5 and ...Bb4 create a double attack on c3 and g5. Sharp and tricky — full of traps for White."),
                ("Tartakower Variation", 412, "d4 d5 c4 e6 Nc3 Nf6 Bg5 Be7 e3 O-O Nf3 h6 Bh4 b6 cxd5 Nxd5 Bxe7 Qxe7 Nxd5 exd5 Rc1 Be6",
                 "The Tartakower-Makogonov-Bondarevsky system: Black solves the bishop problem with ...b6 and ...Bb7/...Be6. A main line for decades."),
                ("Exchange Variation", 415, "d4 d5 c4 e6 Nc3 Nf6 cxd5 exd5 Bg5 c6 e3 Be7 Bd3 Nbd7 Qc2 O-O Nf3 Re8",
                 "White releases the tension to play the minority attack with b4–b5. A model positional structure every player should know."),
                ("Exchange: Minority Attack", 418, "d4 d5 c4 e6 Nc3 Nf6 cxd5 exd5 Bg5 Be7 e3 c6 Bd3 O-O Qc2 Nbd7 Nf3 Re8 O-O Nf8 Rab1 a5",
                 "The classic plan: White advances b4–b5 to give Black a weak c-pawn; Black counters in the centre or on the kingside."),
                ("Classical Variation (5 Bf4)", 420, "d4 d5 c4 e6 Nc3 Nf6 Nf3 Be7 Bf4 O-O e3 c5 dxc5 Bxc5 Qc2 Nc6 Rd1 Qa5",
                 "The modern main line of the QGD: White's Bf4 and Rd1 give pressure without allowing ...Ne4."),
                ("Vienna Variation", 426, "d4 d5 c4 e6 Nc3 Nf6 Nf3 Bb4 Bg5 dxc4 e4 c5 Bxc4 cxd4 Nxd4 Qa5",
                 "A wild hybrid: Black grabs c4 and White blasts the centre open with e4. Sharp tactics from move six."),
                ("Ragozin Variation", 427, "d4 d5 c4 e6 Nc3 Nf6 Nf3 Bb4 Bg5 h6 Bxf6 Qxf6 e3 O-O Rc1 dxc4 Bxc4 c5",
                 "Black combines QGD and Nimzo-Indian ideas with the early ...Bb4. Very popular at the top level."),
                ("Semi-Tarrasch Variation", 432, "d4 d5 c4 e6 Nc3 Nf6 Nf3 c5 cxd5 Nxd5 e3 Nc6 Bd3 cxd4 exd4 Be7 O-O O-O",
                 "Black recaptures on d5 with the knight to avoid the isolated pawn, accepting a slightly cramped but sound game."),
                ("Semi-Tarrasch: 5 e4", 435, "d4 d5 c4 e6 Nc3 Nf6 Nf3 c5 cxd5 Nxd5 e4 Nxc3 bxc3 cxd4 cxd4 Nc6 Bc4 b5",
                 "White builds the big centre with e4 and d4; Black must hit it at once with ...b5 and ...Bb7."),
                ("Semi-Tarrasch: 5 cxd5 exd5", 438, "d4 d5 c4 e6 Nc3 Nf6 Nf3 c5 cxd5 exd5 Bg5 Be7 dxc5 Bxc5 e3 O-O",
                 "Recapturing with the pawn gives Black an isolated queen's pawn with active pieces."),
                ("3 Nc3 (early alternatives)", 446, "d4 d5 c4 e6 Nc3 c6 Nf3 Nf6 Bg5 dxc4 e4 b5",
                 "Black can switch into Semi-Slav structures by inserting ...c6."),
                ("Marshall Defense (3...Nf6 4 cxd5)", 448, "d4 d5 c4 e6 Nc3 Nf6 cxd5 exd5 Nf3 c6 Qc2 Be7 Bg5 O-O",
                 "A quiet handling of the Exchange where White delays the bishop."),
            ],
        },
        {
            "id": "tarrasch", "num": 2, "name": "Tarrasch Defense", "eco": "D32–D34",
            "page": 440, "line": "d4 d5 c4 e6 Nc3 c5",
            "summary": "Black accepts an isolated queen's pawn in return for free piece play and "
                       "open lines. Tarrasch insisted activity beats structure; Kasparov used it "
                       "successfully at the highest level.",
            "white_plan": "Fianchetto with g3 and Bg2 to pressure d5, trade pieces, and win the "
                          "isolated pawn in an endgame.",
            "black_plan": "Use the open files and the active bishops, play ...d4 or ...Bg4/...Ne4, "
                          "and generate a kingside attack before the endgame arrives.",
            "variations": [
                ("Rubinstein Variation", 442, "d4 d5 c4 e6 Nc3 c5 cxd5 exd5 Nf3 Nc6 g3 Nf6 Bg2 Be7 O-O O-O Bg5 cxd4 Nxd4 h6",
                 "The main line: White's fianchetto is the most effective way to pressure the isolated d-pawn."),
                ("Rubinstein: 9 Bg5 c4", 444, "d4 d5 c4 e6 Nc3 c5 cxd5 exd5 Nf3 Nc6 g3 Nf6 Bg2 Be7 O-O O-O Bg5 c4",
                 "Black pushes past to avoid the isolated pawn, accepting a space deficit instead."),
                ("Rubinstein: 9...Be6", 445, "d4 d5 c4 e6 Nc3 c5 cxd5 exd5 Nf3 Nc6 g3 Nf6 Bg2 Be7 O-O O-O Bg5 Be6 dxc5 Bxc5",
                 "A sound set-up where Black defends d5 solidly and keeps the pieces active."),
                ("Symmetrical Variation (6 e3)", 446, "d4 d5 c4 e6 Nc3 c5 cxd5 exd5 Nf3 Nc6 e3 Nf6 Be2 Be7 O-O O-O dxc5 Bxc5",
                 "A quiet treatment where White develops modestly and plays against d5 with Nb5 or b3."),
                ("Swedish Variation", 447, "d4 d5 c4 e6 Nc3 c5 cxd5 exd5 Nf3 Nc6 g3 c4 Bg2 Bb4 O-O Nge7",
                 "Black pushes the pawn to c4, gaining space and avoiding the isolani — the Folkestone Variation."),
                ("Schara-von Hennig Gambit", 447, "d4 d5 c4 e6 Nc3 c5 cxd5 cxd4 Qxd4 Nc6 Qd1 exd5 Qxd5 Bd7",
                 "A genuine pawn sacrifice for rapid development and attacking chances against the white king."),
                ("Tarrasch with 4 cxd5 exd5 5 Nf3 Nf6", 448, "d4 d5 c4 e6 Nc3 c5 cxd5 exd5 Nf3 Nf6 g3 Be7 Bg2 O-O O-O Nc6",
                 "A flexible move order where Black develops the knight to f6 first."),
            ],
        },
        {
            "id": "qga", "num": 3, "name": "Queen's Gambit Accepted", "eco": "D20–D29",
            "page": 449, "line": "d4 d5 c4 dxc4",
            "summary": "Black takes the pawn, not to keep it, but to give up the centre and then "
                       "undermine it with ...c5 or ...e5. A clean, logical and very popular modern "
                       "defence based on quick development.",
            "white_plan": "Recapture the pawn with e3 and Bxc4, build the ideal centre with e4, and "
                          "use the extra space.",
            "black_plan": "Develop quickly with ...Nf6, ...e6 and ...a6, then hit the centre with "
                          "...c5 and ...b5, aiming for full equality.",
            "variations": [
                ("Main Line (Classical)", 450, "d4 d5 c4 dxc4 Nf3 Nf6 e3 e6 Bxc4 c5 O-O a6 Qe2 b5 Bb3 Bb7 Rd1 Nbd7",
                 "The modern main line: Black plays ...a6 and ...b5 for queenside space and solid equality."),
                ("Main Line with 7 Qe2", 451, "d4 d5 c4 dxc4 Nf3 Nf6 e3 e6 Bxc4 c5 O-O a6 Qe2 Nc6 Nc3 cxd4 Rd1 Be7",
                 "White centralises the queen and rook and prepares the e4 and d5 advances."),
                ("Classical with 4 e3 Be6", 453, "d4 d5 c4 dxc4 Nf3 Nf6 e3 Be6 Nbd2 c5 Bxc4 Bxc4 Nxc4 e6",
                 "Black defends the pawn with the bishop, accepting a trade and a slightly passive game."),
                ("3 e4 (Central Variation)", 455, "d4 d5 c4 dxc4 e4 Nf6 Nc3 e5 Nf3 exd4 Qxd4 Qxd4 Nxd4 Bd6",
                 "White takes the whole centre at once; the resulting positions are concrete and open."),
                ("3 e3 (Alekhine System)", 456, "d4 d5 c4 dxc4 e3 Nf6 Bxc4 e6 Nf3 c5 O-O Nc6",
                 "A simple move order that heads straight for the main-line structures."),
                ("3 Nf3 a6 (Modern)", 457, "d4 d5 c4 dxc4 Nf3 a6 e3 Bg4 Bxc4 e6 Nc3 Nf6",
                 "Black plays ...a6 before ...Nf6, keeping ...b5 ideas and the ...Bg4 pin available."),
                ("3 Nc3 (Third-move alternatives)", 458, "d4 d5 c4 dxc4 Nc3 Nf6 e4 e5 Nf3 exd4 Qxd4 Qxd4 Nxd4 Bb4",
                 "An unusual move order in which White develops the knight before regaining the pawn."),
                ("3 e4 e5 4 Nf3 (Mannheim)", 459, "d4 d5 c4 dxc4 e4 e5 Nf3 exd4 Bxc4 Nc6 O-O Be6",
                 "A sharp open game where both sides' pieces come out fast."),
                ("3 Qa4+ (Mannheim Variation)", 459, "d4 d5 c4 dxc4 Qa4+ c6 Qxc4 Nf6 Nf3 Be6",
                 "The queen recovers the pawn at once at the cost of time and queen safety."),
            ],
        },
        {
            "id": "slav", "num": 4, "name": "Slav and Semi-Slav Defense", "eco": "D10–D19, D43–D49",
            "page": 460, "line": "d4 d5 c4 c6",
            "summary": "Black supports d5 with the c-pawn, keeping the c8 bishop's diagonal open — "
                       "the great advantage over the QGD. The Semi-Slav (adding ...e6) is one of "
                       "the richest and sharpest opening complexes in all of chess.",
            "white_plan": "Press with Nf3, Nc3 and e3 or Bg5, and either build the big centre with "
                          "e4 or clamp down on b5 with a4.",
            "black_plan": "Hold d5, develop the bishop to f5 or g4, and look for the ...dxc4/...b5 "
                          "expansion or the ...c5 and ...e5 breaks.",
            "variations": [
                # Semi-Slav (Meran complex)
                ("Meran Variation", 463, "d4 d5 c4 c6 Nf3 Nf6 Nc3 e6 e3 Nbd7 Bd3 dxc4 Bxc4 b5 Bd3 a6 e4 c5",
                 "The classic Semi-Slav: Black gains queenside space with ...b5 and ...c5 while White builds e4. Enormously rich."),
                ("Meran: Reynolds Variation", 467, "d4 d5 c4 c6 Nf3 Nf6 Nc3 e6 e3 Nbd7 Bd3 dxc4 Bxc4 b5 Bd3 a6 e4 c5 d5 c4",
                 "White pushes d5 to blow up the centre; Black's ...c4 locks the bishop out. Famously double-edged."),
                ("Meran: Blumenfeld Variation (8...a6)", 470, "d4 d5 c4 c6 Nf3 Nf6 Nc3 e6 e3 Nbd7 Bd3 dxc4 Bxc4 b5 Bd3 a6 e4 c5 e5 cxd4 Nxb5",
                 "A forcing line where White sacrifices for an attack with e5 and Nxb5."),
                ("Meran: Wade Variation (8...Bb7)", 472, "d4 d5 c4 c6 Nf3 Nf6 Nc3 e6 e3 Nbd7 Bd3 dxc4 Bxc4 b5 Bd3 Bb7 O-O a6 e4 c5",
                 "Black develops the bishop to b7 before ...a6, keeping some flexibility."),
                ("Romih Variation", 474, "d4 d5 c4 c6 Nf3 Nf6 Nc3 e6 e3 Nbd7 Bd3 dxc4 Bxc4 Bb4",
                 "Black develops the bishop to b4 instead of playing ...b5 — a solid, less-charted alternative."),
                ("Anti-Meran Gambit", 476, "d4 d5 c4 c6 Nf3 Nf6 Nc3 e6 Bg5 h6 Bxf6 Qxf6 e3 Nd7 Bd3 dxc4 Bxc4 g6",
                 "White plays Bg5 to prevent the Meran. The Moscow and Anti-Moscow complexes stem from here."),
                ("Botvinnik Variation", 478, "d4 d5 c4 c6 Nf3 Nf6 Nc3 e6 Bg5 dxc4 e4 b5 e5 h6 exf6 hxg5 fxg7 Bxg7",
                 "One of the most complex and forcing lines in chess: both sides shed pawns and the position is a tactical maze from move eight."),
                ("Moscow Variation (5 Bg5 h6 6 Bxf6)", 479, "d4 d5 c4 c6 Nf3 Nf6 Nc3 e6 Bg5 h6 Bxf6 Qxf6 Qb3 Nd7 e4 dxe4 Nxe4 Qf4",
                 "Black inserts ...h6 to force the trade on f6, avoiding the Botvinnik maze."),
                # Slav proper
                ("Slav: Main Line (Czech)", 480, "d4 d5 c4 c6 Nf3 Nf6 Nc3 dxc4 a4 Bf5 e3 e6 Bxc4 Bb4 O-O Nbd7",
                 "The Slav main line. Black's bishop is outside the chain on f5 and the position is balanced and strategic."),
                ("Slav: 6 Ne5 (Krause Attack)", 482, "d4 d5 c4 c6 Nf3 Nf6 Nc3 dxc4 a4 Bf5 Ne5 Nbd7 Nxc4 Qc7 g3 e5",
                 "White jumps to e5 to harass Black's development; the play becomes concrete."),
                ("Slav: Dutch Variation (6 e3 e6)", 483, "d4 d5 c4 c6 Nf3 Nf6 Nc3 dxc4 a4 Bf5 e3 e6 Bxc4 Bb4 O-O O-O",
                 "A sound main-line structure with normal development on both sides."),
                ("Slav: Geller Gambit", 484, "d4 d5 c4 c6 Nf3 Nf6 Nc3 dxc4 e4 b5 e5 Nd5 a4 e6",
                 "White offers a pawn for a space-grabbing centre and an attack."),
                ("Slav: 4...a6 (Chebanenko)", 485, "d4 d5 c4 c6 Nf3 Nf6 Nc3 a6 e3 Bf5 Be2 e6 O-O Be7",
                 "The hugely popular modern ...a6 line: Black keeps ...b5 and ...dxc4 options and avoids all forced theory."),
                ("Slav: Exchange Variation", 486, "d4 d5 c4 c6 cxd5 cxd5 Nc3 Nf6 Nf3 Nc6 Bf4 Bf5 e3 e6 Bb5",
                 "A symmetrical, solid line — White's only edge is the extra tempo."),
                ("Abrahams-Noteboom Variation", 486, "d4 d5 c4 c6 Nf3 Nf6 Nc3 e6 e3 dxc4 Bxc4 b5 Bd3 a6 e4 c5 d5 c4",
                 "Black grabs queenside pawns and fights for the passed-pawn race on the wing."),
                ("Marshall Gambit (Slav)", 487, "d4 d5 c4 c6 Nc3 e6 e4 dxe4 Nxe4 Bb4+ Bd2 Qxd4 Bxb4 Qxe4+ Be2 Na6",
                 "White sacrifices the d-pawn for a development lead and pressure on the dark squares. Extremely sharp."),
                ("Slav: Schlechter Variation (4...g6)", 487, "d4 d5 c4 c6 Nf3 Nf6 Nc3 g6 Bf4 Bg7 e3 O-O Be2 Bf5",
                 "A Grünfeld-style fianchetto within the Slav structure."),
            ],
        },
        {
            "id": "chigorin", "num": 5, "name": "Chigorin's Defense", "eco": "D07",
            "page": 488, "line": "d4 d5 c4 Nc6",
            "summary": "Black develops the knight to c6, attacking d4 and making ...e5 possible — "
                       "an unorthodox, piece-based defence that deliberately ignores classical "
                       "pawn-structure rules.",
            "white_plan": "Push past with d5 or trade on d5, develop with Nf3 and Nc3, and exploit "
                          "the slightly loose black pieces and the bishop-for-knight trades.",
            "black_plan": "Trade the c6 knight for the d4 pawn or the f3 knight, open lines for the "
                          "bishops, and play for dynamic rather than structural equality.",
            "variations": [
                ("Main Line (3 Nf3)", 488, "d4 d5 c4 Nc6 Nf3 Bg4 cxd5 Bxf3 gxf3 Qxd5 e3 e5 Nc3 Bb4",
                 "The sharpest line: Black gives up the bishop pair to damage White's structure."),
                ("3 cxd5 Qxd5", 489, "d4 d5 c4 Nc6 cxd5 Qxd5 Nc3 Qa5 Nf3 Bg4 Bd2 Bxf3 exf3 e6",
                 "White gains time on the queen and keeps a space advantage."),
                ("3 Nc3 dxc4", 489, "d4 d5 c4 Nc6 Nc3 dxc4 d5 Ne5 Qd4 Ng6 e4 e5",
                 "A forcing central advance that chases the knight and seizes space."),
                ("3 e3 (Quiet Line)", 490, "d4 d5 c4 Nc6 e3 e5 Nc3 exd4 exd4 Nf6 Nf3 Bg4",
                 "White takes a modest approach and plays for a small structural plus."),
                ("3 cxd5 (Exchange with ...Nxd5)", 490, "d4 d5 c4 Nc6 cxd5 Qxd5 e3 e5 Nc3 Bb4 Bd2 Bxc3 Bxc3 exd4",
                 "A simplifying treatment where the tension releases quickly."),
            ],
        },
    ],
}

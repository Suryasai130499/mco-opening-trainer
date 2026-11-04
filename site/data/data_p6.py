# -*- coding: utf-8 -*-
# Part VI — Flank Openings

PART = {
    "id": "flank",
    "num": "VI",
    "name": "Flank Openings",
    "line": "c4",
    "blurb": "White opens on a wing instead of the centre. The English and Réti are fully "
             "respectable main-line openings; the rest of this section covers everything from "
             "the King's Indian Attack to Bird's, Larsen's and the Sokolsky.",
    "chapters": [
        {
            "id": "english", "num": 1, "name": "English Opening", "eco": "A10–A39",
            "page": 675, "line": "c4",
            "summary": "A reversed Sicilian with an extra tempo. White controls d5 from the flank "
                       "and keeps maximum flexibility — the English can transpose into almost any "
                       "queen's pawn opening or stay completely independent.",
            "white_plan": "Fianchetto with g3 and Bg2, control d5, and choose between a central "
                          "d4 break, a queenside b4 expansion, or a slow kingside build-up.",
            "black_plan": "Fight for d4 and d5 — with ...e5 (reversed Sicilian), ...c5 "
                          "(symmetrical), ...Nf6 and ...e6 (Indian structures), or ...e6 and ...d5.",
            "variations": [
                # 1...e5 — reversed Sicilian
                ("Four Knights' Variation", 680, "c4 e5 Nc3 Nf6 Nf3 Nc6 g3 d5 cxd5 Nxd5 Bg2 Nb6 O-O Be7 d3 O-O",
                 "The main line of the reversed Sicilian: Black plays ...d5 and the structures mirror the Sicilian a tempo down."),
                ("Four Knights': 4 g3 Bb4", 682, "c4 e5 Nc3 Nf6 Nf3 Nc6 g3 Bb4 Bg2 O-O O-O Re8 Nd5 Nxd5 cxd5 Nd4",
                 "Black develops the bishop actively and fights for the centre with ...e4 ideas."),
                ("Carls's 'Bremen' System", 684, "c4 e5 Nc3 Nf6 g3 d5 cxd5 Nxd5 Bg2 Nb6 Nf3 Nc6 O-O Be7 d3 O-O",
                 "White delays Nf3 and fianchettos at once — also called the Keres Variation."),
                ("Accelerated Fianchetto", 685, "c4 e5 Nc3 Nf6 g3 Bb4 Bg2 O-O Nf3 Re8 O-O Nc6 d3 h6",
                 "A flexible reversed-Dragon treatment where White's bishop goes to g2 immediately."),
                ("Closed Variation", 686, "c4 e5 Nc3 Nc6 g3 g6 Bg2 Bg7 Rb1 Nf6 b4 d6 d3 O-O",
                 "A reversed Closed Sicilian with White an extra tempo up: Rb1 and b4 give real queenside pressure."),
                ("Closed Variation: 4 Bg2 Bg7 5 d3", 688, "c4 e5 Nc3 Nc6 g3 g6 Bg2 Bg7 d3 d6 Rb1 f5 e3 Nf6",
                 "A slow build-up where White expands on the queenside and Black on the kingside."),
                ("Keres Variation", 685, "c4 e5 Nc3 Nf6 g3 c6 Nf3 e4 Nd4 d5 cxd5 Qxd5 Nb3",
                 "A sharp central push by Black; White's knight manoeuvres around the e4 pawn."),
                ("King's Indian English", 699, "c4 Nf6 Nc3 g6 g3 Bg7 Bg2 O-O Nf3 d6 d4 Nbd7 O-O e5",
                 "Black sets up a King's Indian; the game often transposes into the Fianchetto KID."),
                ("Grünfeld English (Romanishin)", 701, "c4 Nf6 Nc3 g6 g3 Bg7 Bg2 O-O Nf3 d5 cxd5 Nxd5 Nxd5 Qxd5 O-O Nc6",
                 "Black plays ...d5 against the fianchetto for a Grünfeld-like structure without d4."),
                ("Double Fianchetto Defense", 702, "c4 Nf6 Nc3 g6 g3 Bg7 Bg2 O-O Nf3 b6 O-O Bb7 d4 e6",
                 "Black fianchettos both bishops and waits — an ultra-flexible hedgehog-style set-up."),
                ("Nimzo-Indian English", 695, "c4 Nf6 Nc3 e6 Nf3 Bb4 Qc2 O-O a3 Bxc3 Qxc3 b6 b4 d6 Bb2 Bb7",
                 "Black plays a Nimzo-Indian without White having played d4 — the pin is still annoying."),
                ("Queen's Indian English", 694, "c4 Nf6 Nc3 e6 Nf3 b6 g3 Bb7 Bg2 Be7 O-O O-O d4 d5",
                 "A Queen's-Indian structure reached via the English move order."),
                ("Mikenas-Carls Attack", 697, "c4 Nf6 Nc3 e6 e4 d5 cxd5 exd5 e5 Ne4 Nf3 Bb4 Qc2 d4",
                 "An immediate e4 for maximum central space. Very sharp and surprisingly dangerous."),
                # Symmetrical
                ("Symmetrical Variation", 703, "c4 c5 Nf3 Nf6 Nc3 Nc6 g3 g6 Bg2 Bg7 O-O O-O d3 a6 Bd2 Rb8",
                 "Both sides fianchetto and develop identically. Subtle manoeuvring — small inaccuracies decide the game."),
                ("Symmetrical Four Knights'", 704, "c4 c5 Nf3 Nf6 Nc3 Nc6 d4 cxd4 Nxd4 e6 g3 Qb6 Nb3 Ne5 e4 Bb4",
                 "White opens the centre with d4 and the play becomes concrete and tactical."),
                ("Symmetrical: Rubinstein System", 706, "c4 c5 Nf3 Nf6 Nc3 Nc6 d4 cxd4 Nxd4 e6 g3 Bb4 Bg2 O-O O-O d5",
                 "Black develops the bishop to b4 and strikes with ...d5 for immediate equality."),
                ("Keres Defense", 707, "c4 c5 Nf3 Nf6 Nc3 e6 g3 b6 Bg2 Bb7 O-O Be7 d4 cxd4 Qxd4 d6",
                 "A hedgehog-style defence: Black concedes space and waits for ...b5 and ...d5."),
                ("Hedgehog Defense", 709, "c4 c5 Nf3 Nf6 Nc3 e6 g3 b6 Bg2 Bb7 O-O Be7 d4 cxd4 Qxd4 d6 Rd1 a6 b3 Nbd7 e4 Qb8",
                 "The classic Hedgehog: Black's pawns on a6, b6, d6 and e6 look passive but the ...b5 and ...d5 breaks are explosive."),
                ("Rubinstein/Botvinnik Variation", 711, "c4 c5 Nc3 Nc6 g3 g6 Bg2 Bg7 e4 e6 Nge2 Nge7 d3 O-O O-O d6",
                 "The Botvinnik set-up: pawns on c4, d3 and e4 give a permanent grip on d5."),
                ("Ultra-Symmetrical Variation", 713, "c4 c5 Nc3 Nc6 g3 g6 Bg2 Bg7 Nf3 Nf6 O-O O-O d3 d6 Rb1 a6 a3 Rb8",
                 "Complete symmetry, broken only by White's extra tempo. A pure test of understanding."),
                ("Ultra-Symmetrical: 5 Nf3 e5", 715, "c4 c5 Nc3 Nc6 g3 g6 Bg2 Bg7 Nf3 e5 d3 Nge7 O-O O-O",
                 "Black grabs the centre with ...e5, giving the game a reversed-Closed-Sicilian character."),
                # Other replies
                ("Anglo-Indian (1...Nf6 2 Nc3)", 718, "c4 Nf6 Nc3 e5 Nf3 Nc6 g3 Bb4 Bg2 O-O O-O Re8",
                 "The most common move order, keeping d4 and the reversed Sicilian both in reserve."),
                ("Anglo-Slav (1...c6)", 733, "c4 c6 d4 d5 Nf3 Nf6 Nc3 dxc4 a4 Bf5 Ne5 e6",
                 "Black plays ...c6 and ...d5 for a Slav structure without allowing the Queen's Gambit move order."),
                ("Anglo-Dutch (1...f5)", 734, "c4 f5 Nf3 Nf6 g3 g6 Bg2 Bg7 O-O O-O d4 d6",
                 "A Leningrad Dutch set-up against the English."),
                ("1...e6 (Agincourt Defense)", 734, "c4 e6 Nf3 d5 g3 Nf6 Bg2 Be7 O-O O-O d4 dxc4",
                 "Black builds a Catalan-style structure and often transposes into the Queen's Gambit."),
                ("1...b6 / 1...g6 (Flexible replies)", 734, "c4 g6 Nc3 Bg7 g3 e5 Bg2 Ne7 d3 d6",
                 "Black fianchettos immediately, keeping every structure available."),
            ],
        },
        {
            "id": "reti", "num": 2, "name": "Réti Opening", "eco": "A04–A09",
            "page": 718, "line": "Nf3 d5 c4",
            "summary": "The purest hypermodern opening: White attacks d5 from the flank without "
                       "putting a pawn in the centre at all, then fianchettos both bishops and "
                       "works on the long diagonals.",
            "white_plan": "Fianchetto with g3 and Bg2 (and often b3 and Bb2), pressure d5 and e5 "
                          "from distance, and break with a later d4, e4 or c5.",
            "black_plan": "Support d5 with ...c6 or ...e6, develop the bishop outside the chain to "
                          "f5 or g4, and aim for ...e5 to take the centre.",
            "variations": [
                ("Réti Accepted", 719, "Nf3 d5 c4 dxc4 e3 Nf6 Bxc4 e6 O-O c5 b3 Nc6 Bb2 Be7",
                 "Black takes the pawn; White regains it with e3 and Bxc4 and plays a QGA-style position."),
                ("Réti: Main Line (2...e6)", 720, "Nf3 d5 c4 e6 g3 Nf6 Bg2 Be7 O-O O-O b3 c5 e3 Nc6 Bb2 b6",
                 "The classic double-fianchetto Réti: slow, rich and very hard to play against well."),
                ("Réti: 2...c6", 721, "Nf3 d5 c4 c6 b3 Nf6 g3 Bf5 Bg2 e6 O-O Be7 Bb2 O-O",
                 "Black supports d5 with ...c6 and develops the bishop outside the pawn chain."),
                ("Réti: 2...d4 (Advance)", 721, "Nf3 d5 c4 d4 e3 Nc6 exd4 Nxd4 Nxd4 Qxd4 Nc3 Nf6",
                 "Black pushes past; White undermines the pawn with e3 immediately."),
                ("London System (via Réti)", 720, "Nf3 d5 d4 Nf6 Bf4 e6 e3 c5 c3 Nc6 Nbd2 Bd6 Bg3 O-O",
                 "The London: Bf4, e3, c3 and Nbd2. Low theory, easy to play, and a genuine top-level weapon."),
                ("Reversed Benoni", 720, "Nf3 d5 c4 d4 b4 f6 e3 e5 c5 a5",
                 "Black's advanced d-pawn gives a Benoni structure with colours reversed."),
                ("Barcza System", 722, "Nf3 d5 g3 Nf6 Bg2 c6 O-O Bf5 d3 e6 Nbd2 Be7 Qe1 O-O e4",
                 "White fianchettos without c4 and prepares e4 — a King's-Indian-Attack hybrid."),
                ("Neo-Catalan", 723, "Nf3 d5 c4 e6 g3 Nf6 Bg2 Be7 O-O O-O d4 dxc4 Qc2 a6 Qxc4 b5",
                 "The Réti move order transposing into an Open Catalan once White plays d4."),
                ("Réti vs King's Indian set-up", 723, "Nf3 Nf6 c4 g6 g3 Bg7 Bg2 O-O O-O d6 d4 Nbd7",
                 "Black fianchettos too; the game usually becomes a Fianchetto King's Indian."),
            ],
        },
        {
            "id": "kia", "num": 3, "name": "King's Indian Attack", "aka": "King's Indian Reversed",
            "eco": "A07–A08", "page": 724, "line": "Nf3 d5 g3",
            "summary": "A King's Indian Defense with colours reversed: Nf3, g3, Bg2, O-O, d3, Nbd2 "
                       "and then e4. A complete system you can play against almost anything — "
                       "Fischer used it to devastating effect.",
            "white_plan": "Complete the set-up, push e4 and then e5, and attack the kingside with "
                          "Nf1–h2, h4 and f4 while Black is busy elsewhere.",
            "black_plan": "Take queenside space with ...c5 and ...b5, contest e4 early, and avoid "
                          "letting White's e5 wedge become a free attack.",
            "variations": [
                ("Main Line vs ...e6", 725, "Nf3 d5 g3 Nf6 Bg2 c5 d3 Nc6 O-O e6 Nbd2 Be7 e4 O-O Re1 Qc7 e5 Nd7",
                 "The classic KIA attacking formation: the e5 wedge, then Nf1–h2 and f4 with a kingside assault."),
                ("Main Line vs ...g6", 726, "Nf3 d5 g3 g6 Bg2 Bg7 d3 Nf6 O-O O-O Nbd2 c5 e4 Nc6 Re1 e5",
                 "When Black fianchettos too, the position becomes symmetrical and White's attack is slower."),
                ("KIA vs French (2 d3)", 727, "Nf3 d5 g3 Nf6 Bg2 c6 O-O Bg4 d3 Nbd7 Nbd2 e5 e4 Bd6",
                 "Black plays a Caro-Kann-style set-up; White still gets the e4 and e5 plan."),
                ("KIA vs Sicilian structures", 728, "Nf3 c5 g3 g6 Bg2 Bg7 O-O Nc6 d3 e5 e4 Nge7 Nc3 O-O",
                 "A reversed Closed Sicilian where White attacks on the kingside and Black on the queenside."),
                ("Reversed Benoni / KIA with c4", 728, "Nf3 Nf6 g3 g6 Bg2 Bg7 O-O O-O d3 d5 Nbd2 c5 e4 dxe4 dxe4 Nc6",
                 "The purest reversal of the King's Indian Defense, with White a tempo ahead."),
            ],
        },
        {
            "id": "larsen", "num": 4, "name": "Larsen's Opening", "aka": "Nimzovich-Larsen Attack",
            "eco": "A01", "page": 729, "line": "b3",
            "summary": "White fianchettos the queen's bishop on move one to fight for e5 along the "
                       "long diagonal. Offbeat but principled, and Larsen used it to beat the very "
                       "best players in the world.",
            "white_plan": "Put the bishop on b2, fight for e5, and follow with e3, Nf3, c4 and d4 "
                          "or f4 depending on Black's set-up.",
            "black_plan": "Take the centre with ...d5 and ...e5, and use the time White spent on "
                          "the flank to develop faster.",
            "variations": [
                ("Main Line (1...e5)", 729, "b3 e5 Bb2 Nc6 e3 Nf6 Bb5 Bd6 Na3 O-O Nf3 Re8",
                 "Black takes the centre at once; White's bishop fights it from b2."),
                ("1...d5", 730, "b3 d5 Bb2 Nf6 Nf3 e6 e3 Be7 c4 O-O Nc3 c5",
                 "A sound, classical answer: Black builds the centre and develops normally."),
                ("1...Nf6 (Indian set-up)", 730, "b3 Nf6 Bb2 g6 g3 Bg7 Bg2 O-O Nf3 d5 O-O c5",
                 "A double-fianchetto game where White's extra tempo means very little."),
                ("Polish/Sokolsky transposition", 731, "b3 e5 Bb2 d6 e3 Nf6 c4 Be7 Nf3 O-O Be2 c5",
                 "White combines b3 and c4 for a hybrid English/Larsen structure."),
            ],
        },
        {
            "id": "bird", "num": 5, "name": "Bird's Opening", "eco": "A02–A03",
            "page": 732, "line": "f4",
            "summary": "A Dutch Defense with colours reversed. White takes e5 and the f-file but "
                       "weakens the king, which gives Black the dangerous From's Gambit as an "
                       "immediate test.",
            "white_plan": "Control e5, develop with Nf3, e3, b3 and Bb2, and attack on the kingside "
                          "with the f-file and Qe1–h4.",
            "black_plan": "Either strike at once with the From's Gambit (1...e5), or take the "
                          "centre with ...d5 and punish the loosened king later.",
            "variations": [
                ("From's Gambit", 732, "f4 e5 fxe5 d6 exd6 Bxd6 Nf3 g5 g3 g4 Nh4 Ne7",
                 "Black gives a pawn to open lines at the white king. Dangerous — many games end quickly."),
                ("From's Gambit: Lasker Variation", 733, "f4 e5 fxe5 d6 exd6 Bxd6 Nf3 Nf6 d4 Nh5",
                 "Black develops the knight and hits g3 and f4, keeping the attack going."),
                ("From's Gambit Declined (2 e4)", 733, "f4 e5 e4 exf4 Nf3 d5 exd5 Qxd5 Nc3 Qe6+",
                 "White declines by transposing into a King's Gambit — the safest practical choice."),
                ("Main Line (1...d5)", 734, "f4 d5 Nf3 Nf6 e3 g6 b3 Bg7 Bb2 O-O Be2 c5",
                 "A reversed Dutch where White plays the Stonewall-style structure with an extra tempo."),
                ("Bird's with 1...Nf6", 734, "f4 Nf6 Nf3 g6 g3 Bg7 Bg2 O-O O-O d5 d3 c5",
                 "A quiet double-fianchetto set-up with a Leningrad structure reversed."),
            ],
        },
        {
            "id": "misc-flank", "num": 6, "name": "Miscellaneous Flank Openings", "eco": "A00",
            "page": 735, "line": "",
            "summary": "MCO's final chapter: every remaining first move. Some are serious "
                       "surprise weapons, some are outright jokes, but each one has been played "
                       "by a strong player at some point.",
            "white_plan": "Get the opponent out of their preparation on move one and rely on "
                          "general understanding.",
            "black_plan": "Occupy the centre and develop quickly — almost every one of these moves "
                          "loses a little time or weakens something.",
            "variations": [
                ("Grünfeld Reversed (1 g3)", 736, "g3 d5 Nf3 Nf6 Bg2 c6 O-O Bf5 d3 e6 Nbd2",
                 "A flexible waiting move that usually becomes a Réti or King's Indian Attack."),
                ("King's Fianchetto Opening (1 g3 e5)", 736, "g3 e5 Bg2 d5 d3 Nf6 Nf3 Nc6 O-O Be7 c4",
                 "The pure fianchetto start; Black takes the centre and White plays a reversed Modern."),
                ("Queen's Indian Reversed (1 b3 / 1 Nf3 b3)", 736, "Nf3 d5 b3 Nf6 Bb2 e6 e3 Be7 c4 O-O",
                 "A hybrid Réti/Larsen set-up based entirely on the b2 bishop."),
                ("Grob's Attack (Spike)", 738, "g4 d5 Bg2 c6 h3 e5 d4 e4",
                 "One of the wildest first moves there is. White grabs space on the kingside and hopes for chaos."),
                ("Grob: 1...e5", 738, "g4 e5 Bg2 d5 h3 Nf6 d4 exd4 Qxd4 Nc6",
                 "Black takes the centre and White's loosened kingside becomes a liability."),
                ("Queen's Knight (Dunst) Attack", 738, "Nc3 d5 e4 d4 Nce2 e5 Ng3 Bd6",
                 "An eccentric knight move that keeps every structure available and avoids all theory."),
                ("Sokolsky Opening (1 b4)", 739, "b4 Nf6 Bb2 e6 b5 d5 e3 Bd6 Nf3 O-O",
                 "Also called the Orangutan or Polish Opening: White grabs queenside space on move one."),
                ("Sokolsky: 1...e5", 739, "b4 e5 Bb2 Bxb4 Bxe5 Nf6 Nf3 Nc6 Bb2 d5",
                 "Black takes the pawn and gets quick development while White has the better centre."),
                ("Van't Kruijs Opening (1 e3)", 739, "e3 e5 Nc3 d5 d4 exd4 exd4 Nf6",
                 "A modest, non-committal first move that gives Black a free hand in the centre."),
                ("Saragossa Opening (1 c3)", 739, "c3 d5 d4 Nf6 Bf4 e6 Nf3 Bd6",
                 "A waiting move that usually becomes a slow queen's pawn game."),
                ("Anderssen's Opening (1 a3)", 739, "a3 e5 c4 Nf6 Nc3 d5 cxd5 Nxd5",
                 "Played by Anderssen in his match with Morphy; it becomes a reversed Sicilian."),
                ("Durkin / Paris and other rarities", 739, "Na3 e5 e4 Nf6 Nc4 Nc6 d3 d5",
                 "MCO notes that 1 h3, 1 h4, 1 Na3 and 1 Nh3 'require no opening analysis'."),
            ],
        },
    ],
}

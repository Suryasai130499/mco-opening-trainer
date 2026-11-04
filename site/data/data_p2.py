# -*- coding: utf-8 -*-
# Part II — Semi-Open Games (1 e4, Black replies other than ...e5)

PART = {
    "id": "semi-open",
    "num": "II",
    "name": "Semi-Open Games",
    "line": "e4",
    "blurb": "Black answers 1 e4 with something other than 1...e5, accepting an asymmetrical "
             "struggle. These are the fighting defences — the Sicilian, French and Caro-Kann are "
             "the three most-played replies to 1 e4 in the world.",
    "chapters": [
        {
            "id": "alekhines-defense", "num": 1, "name": "Alekhine's Defense", "eco": "B02–B05",
            "page": 159, "line": "e4 Nf6",
            "summary": "Black provokes White into chasing the knight and overextending in the centre. "
                       "Hypermodern in spirit: Black invites White to build a big pawn front and then "
                       "attacks it with ...c5, ...e6 and ...f6.",
            "white_plan": "Gain space with e5, d4 and c4, chase the knight to b6, and either keep "
                          "the big centre or trade into a space advantage.",
            "black_plan": "Undermine the advanced pawns with ...d6, ...c5 and ...f6, and exploit "
                          "White's loosened squares once the centre dissolves.",
            "variations": [
                ("Modern Variation (4 Nf3)", 161, "e4 Nf6 e5 Nd5 d4 d6 Nf3 dxe5 Nxe5 c6 Be2 Bf5",
                 "The main line and the most sensible: White simply develops and keeps a small but lasting space edge."),
                ("Modern Variation with 4...Bg4", 162, "e4 Nf6 e5 Nd5 d4 d6 Nf3 Bg4 Be2 c6 O-O Bxf3 Bxf3 dxe5",
                 "Black trades off the good bishop to reduce White's attacking potential."),
                ("Modern Variation with 4...g6", 163, "e4 Nf6 e5 Nd5 d4 d6 Nf3 g6 Bc4 Nb6 Bb3 Bg7",
                 "A fianchetto treatment: Black puts the bishop on the long diagonal against the e5 pawn."),
                ("Exchange Variation", 165, "e4 Nf6 e5 Nd5 d4 d6 c4 Nb6 exd6 cxd6 Nc3 g6 Be3 Bg7",
                 "White releases the tension on e5 for a clean space advantage; Black's structure is sound."),
                ("Exchange Variation with ...exd6", 166, "e4 Nf6 e5 Nd5 d4 d6 c4 Nb6 exd6 exd6 Nc3 Be7 Be3 O-O",
                 "Taking with the e-pawn gives Black a solid but passive structure and a free c-file."),
                ("Four Pawns' Attack", 167, "e4 Nf6 e5 Nd5 d4 d6 c4 Nb6 f4 dxe5 fxe5 Nc6 Be3 Bf5",
                 "The most ambitious line: White builds a wall of pawns. Double-edged — if Black breaks it, White's position collapses."),
                ("Two Pawns' Attack (Lasker)", 169, "e4 Nf6 e5 Nd5 c4 Nb6 d4 d6 exd6 cxd6",
                 "White plays c4 before d4 to kick the knight immediately."),
                ("Minor Variations (2 Nc3)", 170, "e4 Nf6 Nc3 d5 e5 Nfd7 d4 e6",
                 "White simply defends e4 and heads for a French-like structure."),
                ("Minor Variations (2 e5 Nd5 3 Bc4)", 170, "e4 Nf6 e5 Nd5 Bc4 Nb6 Bb3 c5",
                 "A quiet developing move that avoids all the theory."),
            ],
        },
        {
            "id": "caro-kann", "num": 2, "name": "Caro-Kann Defense", "eco": "B10–B19",
            "page": 171, "line": "e4 c6",
            "summary": "Black prepares ...d5 with the c-pawn, so that after the exchange the "
                       "light-squared bishop is free — the key difference from the French. Famously "
                       "solid and structurally sound, the Caro-Kann is the choice of players who "
                       "want a strong endgame.",
            "white_plan": "Take space with d4 and either keep the tension (3 Nc3), advance (3 e5), "
                          "or open the centre (Panov with c4).",
            "black_plan": "Reach a healthy structure, develop the light-squared bishop actively "
                          "to f5 or g6, and look for ...c5 or ...e5 at the right moment.",
            "variations": [
                ("Main Line (Classical)", 174, "e4 c6 d4 d5 Nc3 dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 Nf3 Nd7 h5 Bh7 Bd3 Bxd3 Qxd3 e6",
                 "The classical main line. White gains kingside space, Black has a flawless structure and the better endgame prospects."),
                ("Main Line with 11...Qc7", 176, "e4 c6 d4 d5 Nc3 dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 Nf3 Nd7 h5 Bh7 Bd3 Bxd3 Qxd3 Qc7",
                 "Black develops the queen to c7 to prepare ...e6, ...O-O-O or ...Ngf6 flexibly."),
                ("Smyslov Variation (4...Nd7)", 180, "e4 c6 d4 d5 Nc3 dxe4 Nxe4 Nd7 Nf3 Ngf6 Nxf6+ Nxf6 Bd3 Bg4",
                 "Black develops the knight first and only then decides about the bishop. Very solid and modern."),
                ("Bronstein-Larsen Variation", 182, "e4 c6 d4 d5 Nc3 dxe4 Nxe4 Nf6 Nxf6+ gxf6 Nf3 Bf5 Be2 Qc7",
                 "Black accepts a broken kingside for the open g-file and dynamic chances. A real fighting line."),
                ("Tartakower Variation (4...Nf6 5 Nxf6+ exf6)", 183, "e4 c6 d4 d5 Nc3 dxe4 Nxe4 Nf6 Nxf6+ exf6 Bc4 Bd6 Qh5 O-O",
                 "Recapturing with the e-pawn gives Black a solid, slightly passive position with easy development."),
                ("Panov-Botvinnik Attack", 185, "e4 c6 d4 d5 exd5 cxd5 c4 Nf6 Nc3 e6 Nf3 Be7 cxd5 Nxd5",
                 "White opens the centre and plays with an isolated queen's pawn for piece activity. Transposes into Nimzo/QGD structures."),
                ("Panov with 5...Nc6", 186, "e4 c6 d4 d5 exd5 cxd5 c4 Nf6 Nc3 Nc6 Nf3 Bg4 cxd5 Nxd5",
                 "Black develops with maximum pressure on d4 instead of blocking with ...e6."),
                ("Panov with 5...g6", 188, "e4 c6 d4 d5 exd5 cxd5 c4 Nf6 Nc3 g6 Qb3 Bg7 cxd5 O-O",
                 "A Grünfeld-style treatment: Black fianchettos and hits the centre from the flank."),
                ("Advance Variation", 189, "e4 c6 d4 d5 e5 Bf5 Nf3 e6 Be2 c5 Be3 Qb6 Nc3 Nc6",
                 "White takes space; Black gets the bishop outside the pawn chain first — the big advantage over the French."),
                ("Advance Variation (Short System)", 190, "e4 c6 d4 d5 e5 Bf5 Nf3 e6 Be2 Nd7 O-O h6 Nbd2 Ne7 Nb3 Bh7 c4",
                 "Nigel Short's quiet, powerful set-up: castle first, then squeeze with c4 and Nb3."),
                ("Two Knights' Variation", 191, "e4 c6 Nc3 d5 Nf3 Bg4 h3 Bxf3 Qxf3 e6 d4 Nf6",
                 "White develops both knights before committing the d-pawn, avoiding the main lines entirely."),
                ("Two Knights' with 3...dxe4", 192, "e4 c6 Nc3 d5 Nf3 dxe4 Nxe4 Nf6 Qe2 Nxe4 Qxe4 Qd5",
                 "Black simplifies at once and trades into a level position."),
                ("Exchange Variation", 193, "e4 c6 d4 d5 exd5 cxd5 Bd3 Nc6 c3 Nf6 Bf4 Bg4 Qb3 Qd7",
                 "A simple, solid line: White keeps a small structural edge and plays for a minority attack."),
                ("Hybrid Caro-Pirc (3...g6)", 194, "e4 c6 d4 d5 Nc3 g6 Nf3 Bg7 h3 Nf6 Bf4 O-O",
                 "Black blends Caro-Kann and Pirc ideas, keeping the centre fluid."),
                ("Fantasy Variation", 195, "e4 c6 d4 d5 f3 dxe4 fxe4 e5 Nf3 exd4 Bc4",
                 "White supports e4 with the f-pawn. Wild and underexplored — a genuine practical weapon."),
                ("Lines without 2 d4 (2 c4)", 196, "e4 c6 c4 d5 exd5 cxd5 cxd5 Nf6 Nc3 Nxd5",
                 "An Accelerated Panov, trading pawns early for an open game."),
                ("Lines without 2 d4 (2 Nf3)", 196, "e4 c6 Nf3 d5 exd5 cxd5 d4 Nf6 Bd3 Bg4",
                 "A quiet transpositional move order avoiding the 3 Nc3 main lines."),
            ],
        },
        {
            "id": "french", "num": 3, "name": "French Defense", "eco": "C00–C19",
            "page": 197, "line": "e4 e6",
            "summary": "Black prepares ...d5 with the e-pawn, accepting a slightly cramped "
                       "light-squared bishop in exchange for a rock-solid pawn chain and clear "
                       "counterplay against d4. One of the most strategically rich openings in chess.",
            "white_plan": "Clamp the centre with e5 and attack on the kingside, or release it with "
                          "exd5 and play for structure.",
            "black_plan": "Attack the base of the pawn chain with ...c5 and ...f6, activate the "
                          "problem bishop via ...b6/...Ba6 or ...Bd7–b5, and play on the queenside.",
            "variations": [
                ("Advance Variation", 203, "e4 e6 d4 d5 e5 c5 c3 Nc6 Nf3 Qb6 a3 Nh6 b4 cxd4 cxd4 Nf5",
                 "White locks the centre and takes space; the whole game revolves around d4 and the c-file."),
                ("Advance Variation with 5...Bd7", 204, "e4 e6 d4 d5 e5 c5 c3 Nc6 Nf3 Bd7 Be2 Nge7 Na3 cxd4 cxd4 Nf5",
                 "A flexible modern treatment, keeping ...Qb6 in reserve and developing the bad bishop."),
                ("Milner-Barry Gambit", 205, "e4 e6 d4 d5 e5 c5 c3 Nc6 Nf3 Qb6 Bd3 cxd4 cxd4 Bd7 O-O Nxd4 Nxd4 Qxd4 Nc3",
                 "White gives up the d-pawn for a fierce attack on the light squares and the black king."),
                ("Classical Variation", 206, "e4 e6 d4 d5 Nc3 Nf6 Bg5 Be7 e5 Nfd7 Bxe7 Qxe7 f4 O-O Nf3 c5",
                 "The classical set-up: White advances and attacks, Black undermines with ...c5 and ...f6."),
                ("Alekhine-Chatard Attack", 207, "e4 e6 d4 d5 Nc3 Nf6 Bg5 Be7 e5 Nfd7 h4 Bxg5 hxg5 Qxg5 Nh3 Qe7 Nf4",
                 "White offers the h-pawn to rip open the h-file. Sharp and still dangerous."),
                ("Burn's Variation", 209, "e4 e6 d4 d5 Nc3 Nf6 Bg5 dxe4 Nxe4 Be7 Bxf6 Bxf6 Nf3 O-O",
                 "Black releases the centre early and heads for a sound, simplified position with the bishop pair."),
                ("MacCutcheon Variation", 210, "e4 e6 d4 d5 Nc3 Nf6 Bg5 Bb4 e5 h6 Bd2 Bxc3 bxc3 Ne4 Qg4 g6",
                 "Black pins the knight instead of retreating. The structures become unique and double-edged."),
                ("Rubinstein Variation", 212, "e4 e6 d4 d5 Nc3 dxe4 Nxe4 Nd7 Nf3 Ngf6 Nxf6+ Nxf6 Be3 Be7",
                 "Black gives up the centre for a completely solid position. Dull-looking, but very hard to beat."),
                ("Steinitz Variation", 214, "e4 e6 d4 d5 Nc3 Nf6 e5 Nfd7 f4 c5 Nf3 Nc6 Be3 cxd4 Nxd4 Bc5",
                 "White supports e5 with f4 and keeps a big centre; Black hammers at d4."),
                ("Steinitz with 6 Nf3", 216, "e4 e6 d4 d5 Nc3 Nf6 e5 Nfd7 f4 c5 Nf3 cxd4 Nxd4 Nc6 Be3 Nxd4 Bxd4 Bc5",
                 "A main-line tabiya: Black trades on d4 and fights for the dark squares."),
                ("Winawer Variation", 217, "e4 e6 d4 d5 Nc3 Bb4 e5 c5 a3 Bxc3+ bxc3 Ne7 Qg4 Qc7 Qxg7 Rg8 Qxh7 cxd4",
                 "The Poisoned Pawn: both sides grab pawns and race. The sharpest line in the French and one of the most analysed in chess."),
                ("Winawer Poisoned Pawn Main Line", 218, "e4 e6 d4 d5 Nc3 Bb4 e5 c5 a3 Bxc3+ bxc3 Ne7 Qg4 Qc7 Qxg7 Rg8 Qxh7 cxd4 Ne2 Nbc6 f4 dxc3 Qd3",
                 "The critical tabiya. White's extra pawns versus Black's queenside initiative and the open files."),
                ("Winawer with 7 Nf3", 222, "e4 e6 d4 d5 Nc3 Bb4 e5 c5 a3 Bxc3+ bxc3 Ne7 Nf3 Bd7 a4 Qa5 Bd2 Nbc6",
                 "A quieter handling where White develops instead of grabbing on g7."),
                ("Winawer Exchange (5 exd5)", 226, "e4 e6 d4 d5 Nc3 Bb4 exd5 exd5 Bd3 Nc6 Nge2 Nge7 O-O Bf5",
                 "White defuses the Winawer by releasing the centre; a quiet, symmetrical game."),
                ("Winawer with 4 exd5", 227, "e4 e6 d4 d5 Nc3 Bb4 Bd3 dxe4 Bxe4 Nf6 Bd3 c5",
                 "An old line where White keeps the bishop active instead of advancing."),
                ("Winawer with 4 Ne2", 229, "e4 e6 d4 d5 Nc3 Bb4 Ne2 dxe4 a3 Be7 Nxe4 Nf6",
                 "A clever move order: White unpins and recaptures on e4 with the knight."),
                ("Tarrasch Variation", 230, "e4 e6 d4 d5 Nd2 Nf6 e5 Nfd7 Bd3 c5 c3 Nc6 Ne2 cxd4 cxd4 f6",
                 "White develops the knight to d2 to avoid the Winawer pin. Leads to clear, instructive structures."),
                ("Tarrasch Open System", 232, "e4 e6 d4 d5 Nd2 c5 exd5 exd5 Ngf3 Nc6 Bb5 Bd6 dxc5 Bxc5 O-O Nge7",
                 "An isolated-queen's-pawn middlegame: Black gets activity, White gets a target."),
                ("Tarrasch with 3...c5 4 exd5 Qxd5", 234, "e4 e6 d4 d5 Nd2 c5 exd5 Qxd5 Ngf3 cxd4 Bc4 Qd6 O-O Nf6 Nb3",
                 "Black takes with the queen to avoid the isolated pawn, accepting some loss of time."),
                ("Guimard Line", 240, "e4 e6 d4 d5 Nd2 Nc6 Ngf3 Nf6 e5 Nd7 Be2 f6",
                 "Black develops the knight to c6 and attacks d4 directly, a rare but respectable line."),
                ("Exchange Variation", 242, "e4 e6 d4 d5 exd5 exd5 Nf3 Nf6 Bd3 Bd6 O-O O-O",
                 "Symmetrical and quiet. White hopes to use the small space edge; Black equalises easily."),
                ("Unusual Lines (2 d3 — King's Indian Attack)", 243, "e4 e6 d3 d5 Nd2 Nf6 Ngf3 c5 g3 Nc6 Bg2 Be7 O-O O-O",
                 "White avoids theory entirely with a King's Indian Attack set-up and plays for a kingside attack."),
                ("Unusual Lines (2 Qe2)", 243, "e4 e6 Qe2 c5 Nf3 Nc6 g3 d5 d3",
                 "Chigorin's move: White keeps the centre closed and plays a reversed Sicilian-type game."),
            ],
        },
        {
            "id": "sicilian", "num": 4, "name": "Sicilian Defense", "eco": "B20–B99",
            "page": 244, "line": "e4 c5",
            "summary": "The most popular and most analysed opening in chess. Black answers a king's "
                       "pawn with a queen's pawn, creating an immediate imbalance: White gets space "
                       "and a kingside attack, Black gets the half-open c-file and long-term "
                       "queenside play. MCO gives it seven sections.",
            "white_plan": "Open with d4, develop quickly, and attack on the kingside with f4, g4 "
                          "and Bg5 — or clamp down positionally with c4 and the Maróczy Bind.",
            "black_plan": "Trade the c-pawn for the d-pawn, press down the c-file, expand with "
                          "...b5 and ...a5, and strike with ...d5 or ...e5 when the time is right.",
            "variations": [
                # Section A: Najdorf
                ("Najdorf Variation", 246, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6",
                 "The starting point of the most famous Sicilian of all. ...a6 prepares ...b5 and ...e5 while taking b5 from White's pieces."),
                ("Najdorf: English Attack (6 Be3)", 248, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 Be3 e5 Nb3 Be6 f3 Be7 Qd2 O-O",
                 "The modern main line. White plays f3, Qd2 and g4 for a slow kingside pawn storm."),
                ("Najdorf: 6 Be3 Ng4", 250, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 Be3 Ng4 Bg5 h6 Bh4 g5 Bg3 Bg7",
                 "An immediate attempt to trade the strong e3 bishop or chase it offside."),
                ("Najdorf: 6 g3", 251, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 g3 e5 Nde2 Be7 Bg2 O-O",
                 "A positional fianchetto, playing against d5 rather than attacking directly."),
                ("Najdorf: Poisoned Pawn Variation", 252, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 Bg5 e6 f4 Qb6 Qd2 Qxb2 Rb1 Qa3",
                 "Fischer's favourite: Black grabs the b2 pawn with the queen and dares White to prove the attack. One of chess's great theoretical battlegrounds."),
                ("Najdorf: Poisoned Pawn Main Line", 253, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 Bg5 e6 f4 Qb6 Qd2 Qxb2 Rb1 Qa3 f5 Nc6 fxe6 fxe6 Nxc6 bxc6 Be2 h6",
                 "The critical continuation; both kings are in danger and every move is forced."),
                ("Najdorf: Old Main Line (7...Be7)", 255, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 Bg5 e6 f4 Be7 Qf3 Qc7 O-O-O Nbd7 g4 b5 Bxf6 Nxf6 g5 Nd7",
                 "The classical Najdorf: opposite-side castling and a pure race. The 1950s and 60s main line."),
                ("Najdorf: Polugaevsky Variation", 258, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 Bg5 e6 f4 b5 e5 dxe5 fxe5 Qc7 Qe2 Nfd7",
                 "An audacious idea: Black plays ...b5 before developing, inviting White to overextend."),
                ("Najdorf: 6 Bg5 Nbd7", 260, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 Bg5 e6 f4 Nbd7 Qf3 Qc7 O-O-O b5",
                 "A flexible modern treatment, keeping both ...Be7 and ...b5 available."),
                ("Najdorf: 6 Be2 (Opocensky)", 261, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 Be2 e5 Nb3 Be7 O-O O-O f4 Qc7",
                 "A quiet positional line where White plays for control of d5 and a slow f4 advance."),
                ("Najdorf: 6 Bc4 (Fischer-Sozin)", 264, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 Bc4 e6 Bb3 b5 O-O Be7 Qf3 Qc7 Bg5 Nbd7",
                 "The bishop goes straight for f7 and the a2–g8 diagonal. Fischer's speciality."),
                ("Najdorf: 6 f4", 267, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 f4 e5 Nf3 Nbd7 a4 Be7",
                 "An early f4 to blunt ...e5 and control e5 and g5."),
                ("Najdorf: 6 a4", 268, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 a4 Nc6 Be2 e5 Nf3 Be7",
                 "White stops ...b5 at the source, at the cost of weakening b4 and the b-file."),
                # Section B: Dragon
                ("Dragon Variation", 269, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 g6",
                 "Black fianchettos the bishop along the long diagonal. The most violent Sicilian: opposite-side castling and mutual mating attacks."),
                ("Dragon: Yugoslav Attack", 272, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 g6 Be3 Bg7 f3 O-O Qd2 Nc6 O-O-O d5",
                 "White castles long and storms with h4–h5 and g4; Black counters with ...Rc8, ...Ne5 and the ...Rxc3 exchange sacrifice. Famously forcing."),
                ("Dragon: Soltis Line", 272, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 g6 Be3 Bg7 f3 O-O Qd2 Nc6 Bc4 Bd7 h4 Rc8 Bb3 Ne5 O-O-O h5",
                 "Black's ...h5 stops White's pawn storm cold. The main modern defence to the Yugoslav."),
                ("Dragon: Yugoslav with 9 O-O-O", 276, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 g6 Be3 Bg7 f3 O-O Qd2 Nc6 O-O-O Nxd4 Bxd4 Be6",
                 "A direct approach: White castles immediately and goes for the throat."),
                ("Dragon: Classical Variation", 280, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 g6 Be2 Bg7 O-O O-O Be3 Nc6 Nb3 Be6 f4 Na5",
                 "White castles short and plays positionally. Less wild than the Yugoslav but still rich."),
                ("Dragon: Levenfish Variation", 282, "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 g6 f4 Nc6 Nxc6 bxc6 e5 Nd7",
                 "An immediate f4 to punish the early ...g6 before Black can fianchetto safely."),
                ("Accelerated Dragon", 284, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 g6 Nc3 Bg7 Be3 Nf6 Bc4 O-O Bb3 d6",
                 "Black delays ...d6 to keep ...d5 in reserve. White's accurate answer is the Maróczy Bind."),
                ("Maróczy Bind", 287, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 g6 c4 Bg7 Be3 Nf6 Nc3 Ng4 Qxg4 Nxd4 Qd1 Ne6",
                 "White's c4 and e4 clamp down on d5 permanently. The classic space-versus-flexibility struggle."),
                ("Maróczy Bind: Gurgenidze System", 288, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 g6 c4 Nf6 Nc3 d6 Be2 Nxd4 Qxd4 Bg7 Be3 O-O",
                 "Black trades a pair of knights and aims for the ...Be6/...Qa5 and ...a5 set-up."),
                # Section C: Scheveningen
                ("Scheveningen Variation", 290, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nf6 Nc3 d6",
                 "The 'small centre' with pawns on d6 and e6. Immensely flexible and solid — the structural heart of the whole Sicilian."),
                ("Scheveningen: Classical (6 Be2)", 292, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nf6 Nc3 d6 Be2 Be7 O-O O-O f4 Nc6 Be3 Bd7",
                 "White builds slowly with f4 and Kh1 and then launches e5 or g4."),
                ("Scheveningen: 6 Be2 a6 (Modern)", 294, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nf6 Nc3 d6 Be2 a6 O-O Qc7 f4 Nc6 Be3 Be7",
                 "A hybrid with the Najdorf: ...a6 first, keeping maximum flexibility."),
                ("Scheveningen: Keres Attack", 297, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nf6 Nc3 d6 g4 h6 h4 Nc6 Rg1 h5 gxh5 Nxh5",
                 "White throws the g-pawn forward before developing. The most aggressive line against the Scheveningen — the reason many players prefer the Najdorf move order."),
                ("Scheveningen: English Attack", 300, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nf6 Nc3 d6 Be3 a6 f3 b5 Qd2 Nbd7 g4 h6 O-O-O Ne5",
                 "The Be3/f3/Qd2/g4 set-up, transferable from the Najdorf. Currently one of White's main weapons."),
                ("Scheveningen: Fischer Attack (6 Bc4)", 301, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nf6 Nc3 d6 Bc4 a6 Bb3 Be7 f4 O-O",
                 "The bishop on b3 and f4 aim directly at the black king."),
                # Section D: 2...e6 systems
                ("Taimanov Variation", 304, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 Nc3 Qc7 Be3 a6 Bd3 Nf6 O-O Be7",
                 "Black develops the knight to c6 and queen to c7, keeping the d-pawn at home for flexibility."),
                ("Taimanov: 6 Be3 a6 7 Qd2", 306, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 Nc3 a6 Be3 Nf6 Qd2 Bb4 f3 Ne5",
                 "White prepares O-O-O and a kingside pawn storm against the Taimanov."),
                ("Taimanov: English Attack", 308, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 Nc3 Qc7 Be3 a6 Qd2 Nf6 O-O-O Bb4 f3 Ne5",
                 "Opposite castling again — one of the sharpest Taimanov battlegrounds."),
                ("Taimanov: 6 g3", 321, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 Nc3 a6 g3 d6 Bg2 Bd7 O-O Nf6",
                 "A positional fianchetto system aiming at d5 and the long diagonal."),
                ("Taimanov: 6 Be2", 323, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 Nc3 a6 Be2 Nf6 O-O Qc7 Be3 Bb4",
                 "A quiet developing scheme keeping all options open."),
                ("Kan (Paulsen) Variation", 310, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 a6 Nc3 Qc7 Bd3 Nf6 O-O Bc5 Nb3 Be7",
                 "Black plays ...a6 before committing any pieces — the most flexible Sicilian of all. Very hard for White to attack directly."),
                ("Kan: 5 Bd3 (Main Line)", 312, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 a6 Bd3 Bc5 Nb3 Ba7 Qe2 Nc6 Be3 d6",
                 "White develops the bishop to d3 and fights for the centre with c4 or Nc3."),
                ("Kan: 5 c4 (Maróczy-style)", 314, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 a6 c4 Nf6 Nc3 Qc7 Be2 Bb4 O-O Nc6",
                 "A space-grabbing bind against the Kan, preventing ...b5 and ...d5."),
                ("Four Knights' Variation", 315, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nf6 Nc3 Nc6 Ndb5 Bb4 Bf4 O-O Bxd6",
                 "Also called the Sicilian Counter Attack: four knights come out and the play turns tactical around d6 and e5."),
                ("Sicilian Counter Attack (4...Nf6 5 Nc3 Bb4)", 317, "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nf6 Nc3 Bb4 e5 Ne4 Qg4 Nxc3 a3",
                 "A sharp, direct attempt by Black to seize the initiative with the bishop pin."),
                # Section E: Classical
                ("Classical Variation", 318, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Nf6 Nc3 d6",
                 "The most natural Sicilian: Black develops both knights and keeps a small centre."),
                ("Richter-Rauzer Attack", 320, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Nf6 Nc3 d6 Bg5 e6 Qd2 a6 O-O-O Bd7 f4 b5",
                 "White's main line: Bg5 and Qd2 pressure d6 and prepare the long castle and f4–f5."),
                ("Richter-Rauzer: 7...Be7", 324, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Nf6 Nc3 d6 Bg5 e6 Qd2 Be7 O-O-O O-O f4 Nxd4 Qxd4 Qa5",
                 "Black castles short and counters in the centre with ...Qa5 and ...Rd8."),
                ("Richter-Rauzer: Neo-Rauzer", 326, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Nf6 Nc3 d6 Bg5 e6 Qd2 a6 f4 Be7 Nf3 b5",
                 "A modern handling where White keeps the knight flexible on f3."),
                ("Boleslavsky Variation", 328, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Nf6 Nc3 d6 Be2 e5 Nb3 Be7 O-O O-O Be3 Be6",
                 "Black plays ...e5 immediately, accepting a hole on d5 for free piece play."),
                ("Velimirović Attack", 330, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Nf6 Nc3 d6 Bc4 e6 Be3 Be7 Qe2 O-O O-O-O a6 f4",
                 "White combines the Sozin bishop with Qe2 and O-O-O for an all-out attack. Brutally direct."),
                ("Sozin Variation", 333, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Nf6 Nc3 d6 Bc4 e6 Be3 Be7 Bb3 O-O f4 Na5",
                 "The classical Sozin: White castles short and plays f4–f5 against the e6 point."),
                # Section F: 2...Nc6 with ...e5
                ("Sveshnikov Variation", 338, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Nf6 Nc3 e5 Ndb5 d6 Bg5 a6 Na3 b5",
                 "Black accepts a gaping hole on d5 for enormous dynamic play. One of the most important Sicilians in modern practice."),
                ("Sveshnikov Main Line", 340, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Nf6 Nc3 e5 Ndb5 d6 Bg5 a6 Na3 b5 Bxf6 gxf6 Nd5 f5",
                 "The critical position: Black's broken pawns are compensated by the bishops and the ...f5 and ...e4 pawn mass."),
                ("Pelikan Variation", 342, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Nf6 Nc3 e5 Ndb5 d6 Bg5 a6 Bxf6 gxf6 Na3 b5 Nd5 f5",
                 "The older name for the same complex, via a slightly different move order."),
                ("Kalashnikov Variation", 338, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 e5 Nb5 d6 N1c3 a6 Na3 b5 Nd5 Nge7",
                 "A cousin of the Sveshnikov where Black plays ...e5 before ...Nf6, saving a tempo."),
                ("Löwenthal Variation", 339, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 e5 Nb5 a6 Nd6+ Bxd6 Qxd6 Qf6",
                 "Black allows the knight into d6 and trades it off, gaining the bishops and time."),
                ("Sicilian with 4...Qb6", 344, "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Qb6 Nb3 Nf6 Nc3 e6 Be3 Qc7",
                 "An offbeat line hitting d4 and b2 at once, forcing White to commit early."),
                # Section G: non-open Sicilians
                ("Closed Sicilian", 348, "e4 c5 Nc3 Nc6 g3 g6 Bg2 Bg7 d3 d6 Be3 e6 Qd2 Nge7 Nge2 O-O",
                 "White avoids d4 entirely and builds a kingside attack with f4 and g4. Spassky's favourite — strategic rather than tactical."),
                ("Closed Sicilian: Traditional (6 f4)", 349, "e4 c5 Nc3 Nc6 g3 g6 Bg2 Bg7 d3 d6 f4 e6 Nf3 Nge7 O-O O-O",
                 "The straightforward plan: f4, Be3, Qd2 and a direct pawn storm."),
                ("Smith-Morra Gambit", 350, "e4 c5 d4 cxd4 c3 dxc3 Nxc3 Nc6 Nf3 d6 Bc4 e6 O-O Nf6 Qe2 Be7 Rd1 e5",
                 "White gives a pawn for fast development and pressure on the c- and d-files. A dangerous practical weapon."),
                ("Smith-Morra Declined (3...d5)", 351, "e4 c5 d4 cxd4 c3 d5 exd5 Qxd5 cxd4 Nc6 Nf3 e5",
                 "Black returns the pawn at once and reaches comfortable equality."),
                ("Alapin Variation (2 c3)", 352, "e4 c5 c3 Nf6 e5 Nd5 d4 cxd4 Nf3 Nc6 cxd4 d6 Bc4 Nb6 Bb5 dxe5",
                 "White supports d4 with the c-pawn. Solid and low-theory, aiming for a simple space advantage."),
                ("Alapin with 2...d5", 354, "e4 c5 c3 d5 exd5 Qxd5 d4 Nf6 Nf3 e6 Be2 Be7 O-O O-O",
                 "Black takes the centre; play resembles an improved French/Caro structure."),
                ("Rossolimo / 3 Bb5 Variation", 355, "e4 c5 Nf3 Nc6 Bb5 g6 O-O Bg7 Re1 Nf6 c3 O-O d4 cxd4 cxd4 d5",
                 "White trades the bishop for the knight to damage Black's structure and play positionally."),
                ("Moscow Variation (3 Bb5+)", 356, "e4 c5 Nf3 d6 Bb5+ Bd7 Bxd7+ Qxd7 O-O Nc6 c3 Nf6 Re1 e6 d4 cxd4",
                 "The 3 Bb5+ check against ...d6, exchanging the problem bishop and playing a quiet positional game."),
                ("Grand Prix (f4) Attack", 358, "e4 c5 Nc3 Nc6 f4 g6 Nf3 Bg7 Bc4 e6 f5 Nge7 fxe6 fxe6 d3 O-O",
                 "White plays an immediate f4 and aims for f5 and a kingside breakthrough."),
                ("Nimzovich Variation (2...Nf6)", 360, "e4 c5 Nf3 Nf6 e5 Nd5 Nc3 Nxc3 dxc3 d5 exd6 Qxd6",
                 "A provocative knight sortie inviting White to chase it."),
                ("O'Kelly's Line (2...a6)", 360, "e4 c5 Nf3 a6 c4 e6 d4 cxd4 Nxd4 Nf6 Nc3 Qc7",
                 "An immediate ...a6 to rule out Bb5 and keep every structure available."),
                ("Wing Gambit", 361, "e4 c5 b4 cxb4 a3 d5 exd5 Qxd5 Nf3 e5 axb4 Bxb4",
                 "White gives up a wing pawn to deflect Black's c-pawn and build a big centre. Rare and risky."),
                ("Unusual Second Moves (2 d3)", 361, "e4 c5 d3 Nc6 g3 g6 Bg2 Bg7 f4 d6 Nf3 Nf6",
                 "A King's Indian Attack set-up against the Sicilian."),
            ],
        },
        {
            "id": "pirc", "num": 5, "name": "Pirc Defense", "eco": "B07–B09",
            "page": 362, "line": "e4 d6 d4 Nf6",
            "summary": "Black gives up the centre voluntarily, fianchettos and attacks the big white "
                       "pawns later. The classic hypermodern defence — flexible, resilient and full "
                       "of counterattacking venom.",
            "white_plan": "Build the centre with e4, d4, Nc3 and f4 or Be3, then advance and open "
                          "lines against the fianchettoed king.",
            "black_plan": "Complete the ...g6/...Bg7/...O-O set-up, then hit the centre with ...c5 "
                          "or ...e5 and exploit any overextension.",
            "variations": [
                ("Austrian Attack", 365, "e4 d6 d4 Nf6 Nc3 g6 f4 Bg7 Nf3 O-O Bd3 Nc6 e5 dxe5 fxe5 Nd5",
                 "The sharpest line: White takes maximum space with f4 and e5 and attacks. Black must counter quickly or be steamrolled."),
                ("Austrian Attack: 5...c5", 366, "e4 d6 d4 Nf6 Nc3 g6 f4 Bg7 Nf3 c5 dxc5 Qa5 Bd3 Qxc5 Qe2 O-O",
                 "Black strikes the centre before castling, the most testing response to the Austrian."),
                ("Austrian Attack: 6 Bd3 Na6", 368, "e4 d6 d4 Nf6 Nc3 g6 f4 Bg7 Nf3 O-O Bd3 Na6 O-O c5 d5 Rb8",
                 "A modern plan: the knight goes to a6 and then c7 or b4 to hit d5 and e4."),
                ("Classical System", 369, "e4 d6 d4 Nf6 Nc3 g6 Nf3 Bg7 Be2 O-O O-O c6 h3 Qc7 Be3 e5",
                 "The quiet main line. White develops soundly and keeps a small space edge; Black manoeuvres patiently."),
                ("Classical with 6 Be3", 370, "e4 d6 d4 Nf6 Nc3 g6 Nf3 Bg7 Be3 c6 Qd2 O-O O-O-O b5",
                 "White castles long and goes for opposite-wing attacks."),
                ("Byrne Variation", 371, "e4 d6 d4 Nf6 Nc3 g6 Bg5 Bg7 Qd2 c6 O-O-O b5",
                 "An early Bg5 and Qd2, aiming for a quick O-O-O and h4–h5."),
                ("150 Attack", 371, "e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 O-O-O Nbd7",
                 "A simple, deadly recipe: Be3, Qd2, f3, O-O-O and h4 — popular because it needs little theory."),
                ("Minor Systems (4 Bc4)", 372, "e4 d6 d4 Nf6 Nc3 g6 Bc4 Bg7 Qe2 O-O Nf3 Nc6",
                 "White develops the bishop to c4 to discourage ...d5 and ...Nxe4 tricks."),
                ("Minor Systems (4 g3)", 372, "e4 d6 d4 Nf6 Nc3 g6 g3 Bg7 Bg2 O-O Nge2 e5",
                 "A double-fianchetto set-up that plays for a long positional squeeze."),
            ],
        },
        {
            "id": "robatsch", "num": 6, "name": "Robatsch Defense", "aka": "Modern Defense",
            "eco": "B06", "page": 373, "line": "e4 g6 d4 Bg7",
            "summary": "The Pirc without committing the knight to f6. Black's extreme flexibility "
                       "means White can build a huge centre — but also that Black can choose exactly "
                       "which structure to attack it with.",
            "white_plan": "Occupy the centre with c4 and f4 or Be3/Nf3, and punish Black's slow "
                          "development with a timely advance.",
            "black_plan": "Keep options open, strike with ...c5, ...d5 or ...e5 depending on what "
                          "White commits to, and use the long diagonal.",
            "variations": [
                ("Main Line (3 Nc3 d6)", 374, "e4 g6 d4 Bg7 Nc3 d6 Be3 a6 Qd2 Nd7 f4 b5 Nf3 Bb7",
                 "The 'Modern Defense proper': Black plays ...a6 and ...b5 for queenside counterplay."),
                ("Three Pawns' Attack", 375, "e4 g6 d4 Bg7 Nc3 d6 f4 Nf6 Nf3 O-O Bd3 Nc6",
                 "White takes the maximum space, transposing into Austrian Attack structures."),
                ("Averbakh System (3 c4)", 376, "e4 g6 d4 Bg7 c4 d6 Nc3 Nc6 Be3 e5 d5 Nce7",
                 "With c4 White builds the broadest possible centre; Black blocks it and manoeuvres."),
                ("Gurgenidze System", 376, "e4 g6 d4 Bg7 Nc3 c6 f4 d5 e5 h5",
                 "A unique idea: Black plays ...c6 and ...d5 to freeze the centre and attack with ...h5."),
                ("Modern with 3 Nf3", 377, "e4 g6 d4 Bg7 Nf3 d6 c3 Nf6 Bd3 O-O O-O Nc6",
                 "A quiet, flexible build-up that avoids any early commitment."),
            ],
        },
        {
            "id": "center-counter", "num": 7, "name": "Scandinavian Defense",
            "aka": "Center Counter Defense", "eco": "B01", "page": 378, "line": "e4 d5 exd5",
            "summary": "Black challenges e4 on move one. White wins a tempo chasing the queen (or "
                       "an extra move building the centre after 2...Nf6), but Black gets a clear, "
                       "sound game with no cramping and very little forced theory. MCO gives it six "
                       "columns; the lines below also carry the modern queen retreats — 3...Qd6 and "
                       "3...Qd8 — that have become main roads since the book went to press.",
            "white_plan": "Gain time on the black queen with Nc3 and d4, build the broad centre with "
                          "c4 against 2...Nf6, and use the extra space.",
            "black_plan": "Recapture on d5, get the light-squared bishop outside the pawn chain to "
                          "f5 or g4, play ...c6 and ...e6, and reach a Caro-Kann-like structure one "
                          "tempo down but with no weaknesses.",
            "variations": [
                # --- the book's own six columns (2...Qxd5 3 Nc3 Qa5) ---
                ("Mieses-Kotroc Variation (3...Qa5)", 378, "e4 d5 exd5 Qxd5 Nc3 Qa5",
                 "The historical main line. The queen is safe on a5 and makes way for ...Nf6, ...c6 "
                 "and ...Bf5 — the classical Scandinavian set-up."),
                ("Lasker Variation (5 Nf3 Bg4 6 h3)", 378,
                 "e4 d5 exd5 Qxd5 Nc3 Qa5 d4 Nf6 Nf3 Bg4 h3 Bh5 g4 Bg6 Ne5 e6 Bg2 c6 h4 Be4",
                 "MCO's first column. White gains space on the kingside with g4 and h4 and clamps "
                 "down with Ne5; Black's bishop lands actively on e4."),
                ("Main Line (5 Nf3 c6 6 Bc4)", 378,
                 "e4 d5 exd5 Qxd5 Nc3 Qa5 d4 Nf6 Nf3 c6 Bc4 Bf5 Ne5 e6 g4 Bg6 h4 Nbd7 Nxd7 Nxd7",
                 "MCO's second column and the most-played tabiya. Black finishes development while "
                 "White throws the kingside pawns forward."),
                ("Main Line (5 Bc4 c6 6 Bd2)", 379,
                 "e4 d5 exd5 Qxd5 Nc3 Qa5 d4 Nf6 Bc4 c6 Bd2 Bf5 Nd5 Qd8 Nxf6+ gxf6 Bf4 Qb6 Bb3 a5",
                 "MCO's third column. The jump to d5 forces the queen home and wrecks Black's "
                 "kingside, but the open g-file and bishop pair give real compensation."),
                # --- the book's 2...Nf6 columns ---
                ("Modern Variation (2...Nf6)", 379, "e4 d5 exd5 Nf6",
                 "Black develops instead of chasing the pawn. White can hold d5 for a moment but "
                 "not keep it, and ends up with a broad centre rather than a tempo."),
                ("Modern: 4 Nf3 g6 (Fianchetto)", 379,
                 "e4 d5 exd5 Nf6 d4 Nxd5 Nf3 g6 c4 Nb6 Nc3 Bg7 c5 Nd5 Bc4 c6 O-O Be6 Qb3 Nxc3",
                 "MCO's fourth column. White gains queenside space with c5 and Black's knight hops "
                 "back into d5, supported by ...c6, before trading it off on c3."),
                ("Modern: 4 Nf3 Bg4 5 Be2", 380,
                 "e4 d5 exd5 Nf6 d4 Nxd5 Nf3 Bg4 Be2 Nc6 c4 Nb6 d5 Bxf3 gxf3 Ne5 Nc3 e6 Be3 Bb4",
                 "MCO's fifth column. Black trades on f3 to damage the structure; White's broken "
                 "pawns are offset by the bishop pair and the big centre."),
                ("Anti-Scandinavian (3 Bb5+)", 380,
                 "e4 d5 exd5 Nf6 Bb5+ Bd7 Be2 Nxd5 d4 Bf5 Nf3 e6 a3 Be7 c4 Nb6 Be3 O-O Nc3 Bf6",
                 "MCO's sixth column. The check is a nuisance rather than a pawn-grab: MCO's advice "
                 "is that White should not try to hold d5 but retreat and build the centre."),
                # --- lines the book gives in its footnotes ---
                ("Gubinsky-Melts Defense (3...Qd6)", 378,
                 "e4 d5 exd5 Qxd5 Nc3 Qd6 Nf3 Nf6 d4 c6 Ne5 Nbd7 Bf4 Nd5 Bg3 Nxc3 bxc3 Nxe5 Bxe5 Qg6 Rb1",
                 "MCO calls 3...Qd6 'fashionable' and gives this line, where White comes out more "
                 "active. It has since become one of the two main roads in the whole opening."),
                ("3 Nf3 (Flexible)", 378, "e4 d5 exd5 Qxd5 Nf3 Bg4 Be2 Nc6 O-O O-O-O h3 Bh5 Nc3 Qd7",
                 "White develops before kicking the queen. Black castles long and the game takes on "
                 "an opposite-wings character."),
                ("3 d4 e5 (Counter-thrust)", 378, "e4 d5 exd5 Qxd5 d4 e5 dxe5 Qxd1+ Kxd1 Nc6",
                 "MCO's recommended answer to 3 d4: Black hits back at once, trades queens and the "
                 "misplaced white king makes the endgame comfortable."),
                ("Portuguese Variation (3...Bg4)", 380,
                 "e4 d5 exd5 Nf6 d4 Bg4 f3 Bf5 Bb5+ Nbd7 c4 e6 dxe6 Bxe6 c5 c6",
                 "MCO's 'very entertaining' gambit. Black ignores the pawn and develops with threats; "
                 "the book calls 5 Bb5+ the testing try, with 9 Ba4 giving White some advantage."),
                ("Portuguese: 5 c4 e6 (Vescovi)", 380,
                 "e4 d5 exd5 Nf6 d4 Bg4 f3 Bf5 c4 e6 dxe6 Nc6 Be3 Bb4+ Nc3 Qe7",
                 "Black gives a second pawn for a lead in development. De Firmian notes from his own "
                 "game against Vescovi that this gives Black fine play."),
                ("Scandinavian Gambit (3 c4 c6)", 380, "e4 d5 exd5 Nf6 c4 c6 dxc6 Nxc6 Nf3 e5 d3 Bc5",
                 "Black sacrifices a pawn for fast development and a grip on the centre — MCO judges "
                 "it good compensation."),
                ("3 Bb5+ Bd7 4 Bc4 (Zukertort)", 380,
                 "e4 d5 exd5 Nf6 Bb5+ Bd7 Bc4 b5 Bb3 a5 a3 Bg4 f3 Bc8 Nc3 Ba6",
                 "The old greedy try. Black gains time on the queenside and reroutes the bishop to "
                 "a6; MCO gives Black compensation for the pawn."),
                # --- modern theory, not in MCO-15 (page 0) ---
                ("Gubinsky-Melts: Main Line (5...a6 6 g3)", 0,
                 "e4 d5 exd5 Qxd5 Nc3 Qd6 d4 Nf6 Nf3 a6 g3 Bg4 h3 Bh5 Bg2 Nc6 O-O O-O-O",
                 "The original grandmaster handling of 3...Qd6: ...a6 stops Nb5, and Black castles "
                 "into the attack. Modern practice thinks 6 g3 gives White the better of it."),
                ("Gubinsky-Melts: Tiviakov System (5...c6)", 0,
                 "e4 d5 exd5 Qxd5 Nc3 Qd6 d4 Nf6 Nf3 c6 Bc4 Bf5 Bd2 e6 Qe2 Be7 O-O-O Nbd7",
                 "Sergei Tiviakov's life's work. The solid ...c6 set-up avoids weaknesses entirely "
                 "and has scored heavily for him at grandmaster level."),
                ("Gubinsky-Melts: 5...g6 6 Nb5", 0,
                 "e4 d5 exd5 Qxd5 Nc3 Qd6 d4 Nf6 Nf3 g6 Nb5 Qd8 Bf4 Na6 Qd2 Bg7",
                 "The critical test of the fianchetto treatment: Nb5 and Bf4 hit c7 at once and "
                 "Black must spend moves defending it."),
                ("Valencian Variation (3...Qd8)", 0,
                 "e4 d5 exd5 Qxd5 Nc3 Qd8 d4 Nf6 Nf3 Bf5 Bd3 Bxd3 Qxd3 e6 O-O Be7",
                 "The most solid retreat — all the way home. Black loses time but leaves no target; "
                 "Carlsen used it to beat Caruana at the 2014 Olympiad."),
                ("Valencian: 4...g6", 0, "e4 d5 exd5 Qxd5 Nc3 Qd8 d4 g6 Nf3 Bg7 Bc4 Nh6 O-O O-O",
                 "Black fianchettos and brings the knight out via h6. Offbeat, and theory is "
                 "sceptical, but it keeps the position closed and unfamiliar."),
                ("Kotrc-Mieses (Leonhardt) Gambit (4 b4)", 0,
                 "e4 d5 exd5 Qxd5 Nc3 Qa5 b4 Qxb4 Rb1 Qd6 d4 Nf6 Nf3 a6 Bc4 e6",
                 "White offers the b-pawn to open the b-file and gain time. Lasker, Capablanca and "
                 "Keres all tried it; against a prepared opponent it is no more than a surprise."),
                ("Mieses-Kotroc: Fianchetto (4 g3)", 0,
                 "e4 d5 exd5 Qxd5 Nc3 Qa5 g3 Nf6 Bg2 c6 Nf3 Bf5 O-O e6 Rb1 Be7 b4 Qc7",
                 "A quiet, modern squeeze: White fianchettos, castles, and expands with b4-b5 "
                 "against the queenside. Anand and Jobava have played it."),
                ("Grunfeld Variation (5...Bf5 6 Ne5)", 0,
                 "e4 d5 exd5 Qxd5 Nc3 Qa5 d4 Nf6 Nf3 Bf5 Ne5 c6 g4 Bg6 h4 Nbd7 Nxg6 hxg6",
                 "White goes straight for the bishop with Ne5 and g4. Black's doubled g-pawns come "
                 "with the half-open h-file in return."),
                ("Anderssen Counterattack (4...e5)", 0,
                 "e4 d5 exd5 Qxd5 Nc3 Qa5 d4 e5 dxe5 Bb4 Bd2 Nc6 Nf3 Bg4",
                 "An immediate central strike instead of the slow build-up. Black gives a pawn for "
                 "rapid development and pressure down the d-file."),
                ("Patzer Variation (3...Qe5+)", 0, "e4 d5 exd5 Qxd5 Nc3 Qe5+ Be2 c6 Nf3 Qc7 d4 Nf6 O-O Bg4",
                 "Unkindly named by Andrew Martin. The check costs time, but the queen reaches c7 "
                 "safely and Black's position is playable if passive."),
                ("3...Qe6+ (Kasparov-Letterman)", 0,
                 "e4 d5 exd5 Qxd5 Nc3 Qe6+ Be2 Qg6 Nf3 Qxg2 Rg1 Qh3 d4",
                 "Famous from Kasparov's 1990 exhibition game against David Letterman. Grabbing g2 "
                 "leaves the queen stranded and White's lead in development is overwhelming."),
                ("Modern: 4 c4 Nb6 (Main Line)", 0,
                 "e4 d5 exd5 Nf6 d4 Nxd5 c4 Nb6 Nf3 g6 Nc3 Bg7 Be3 O-O Be2 Nc6",
                 "The most active retreat: the knight eyes c4 and d5 from b6 while Black fianchettos "
                 "and hits the big centre with ...Bg4 and ...e5."),
                ("Marshall Retreat (4 c4 Nf6)", 0,
                 "e4 d5 exd5 Nf6 d4 Nxd5 c4 Nf6 Nc3 g6 Nf3 Bg7 Be2 O-O O-O Nc6",
                 "The knight goes back to f6 rather than the rim. Tartakower thought this the "
                 "soundest treatment; the cost is another tempo and a very big white centre."),
                ("Kiel Variation (4...Nb4)", 0,
                 "e4 d5 exd5 Nf6 d4 Nxd5 c4 Nb4 a3 N4c6 d5 Ne5 f4 Ng6 Bd3 e5",
                 "A speculative lunge: the knight heads for d3 or c2 and invites White to overextend. "
                 "Sharp, rare, and dangerous for whoever knows it less well."),
                ("Richter Variation (3...g6)", 0,
                 "e4 d5 exd5 Nf6 d4 g6 c4 Bg7 Nc3 O-O Nf3 Nbd7 Be2 Nb6",
                 "Kurt Richter's idea from the 1930s: Black fianchettos first and recovers d5 later, "
                 "or not at all, playing for piece pressure on the centre."),
                ("Icelandic-Palme Gambit", 380, "e4 d5 exd5 Nf6 c4 e6 dxe6 Bxe6 Nf3 Nc6 Be2 Bc5 O-O Qe7",
                 "Black gives up a pawn for rapid development and open lines against a white centre "
                 "that is not yet there — a genuine surprise weapon."),
                ("Modern: 3 Nf3", 380, "e4 d5 exd5 Nf6 Nf3 Nxd5 d4 Bf5 Bd3 Bxd3 Qxd3 e6",
                 "A flexible move order that usually transposes. Black recaptures with the knight "
                 "and trades off the problem bishop at once."),
                ("Alekhine Transposition (3 Nc3)", 0,
                 "e4 d5 exd5 Nf6 Nc3 Nxd5 Bc4 Nb6 Bb3 Nc6 Nf3 g6 d4 Bg7",
                 "The game becomes an Alekhine's Defense (1 e4 Nf6 2 Nc3 d5 3 exd5) and is generally "
                 "reckoned equal."),
                ("Blackburne-Kloosterboer Gambit (2...c6)", 0,
                 "e4 d5 exd5 c6 dxc6 Nxc6 Nf3 e5 Bc4 Nf6 d3 Bc5",
                 "Black offers the pawn before recapturing. Blackburne won with it, but after "
                 "3 dxc6 the gambit is thought unsound."),
                ("Tennison Gambit (2 Nf3)", 0, "e4 d5 Nf3 dxe4 Ng5 Nf6 Bc4 Bf5 Nc3 e6",
                 "White declines to recapture and gambits for the initiative. Dubious, but it dodges "
                 "every line in this chapter."),
                ("2 Nc3 (Dunst)", 0, "e4 d5 Nc3 dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 Nf3 Nd7",
                 "White defends e4 with a piece instead of trading. Black gets the bishop out and "
                 "the play resembles a Caro-Kann a tempo up."),
            ],
        },
        {
            "id": "nimzovich-defense", "num": 8, "name": "Nimzovich Defense", "eco": "B00",
            "page": 381, "line": "e4 Nc6",
            "summary": "A provocative knight move that invites d4 and then attacks the centre from "
                       "unusual angles. Rare, but genuinely playable and almost entirely free of "
                       "forced theory.",
            "white_plan": "Build the centre with d4 and either gain space with d5 or develop "
                          "naturally and take over the middle.",
            "black_plan": "Hit d4 with ...e5, ...d5 or ...f6 and steer the game into offbeat "
                          "positions where general understanding matters more than memory.",
            "variations": [
                ("Main Line (2 d4 d5)", 381, "e4 Nc6 d4 d5 Nc3 dxe4 d5 Ne5 Qd4 Ng6 Bb5+ c6",
                 "Black strikes in the centre immediately. White's d5 push gains space and time."),
                ("2 d4 e5 (Scandinavian-style)", 382, "e4 Nc6 d4 e5 dxe5 Nxe5 Nc3 Bb4 Qd4 Qf6",
                 "Black plays for the open centre and quick piece activity."),
                ("2 Nf3 (Transpositional)", 383, "e4 Nc6 Nf3 e5 Bb5 Nf6",
                 "White simply plays 2 Nf3 and reaches an ordinary Ruy Lopez if Black plays ...e5."),
                ("2 d4 d6 (Wheeler Gambit lines)", 383, "e4 Nc6 d4 d6 Nf3 Nf6 Nc3 g6 Be3 Bg7",
                 "Black transposes into a Pirc-like structure with the knight already on c6."),
            ],
        },
        {
            "id": "unusual-kings-pawn", "num": 9, "name": "Unusual King's Pawn Defenses",
            "eco": "B00", "page": 384, "line": "e4",
            "summary": "MCO's chapter for everything else after 1 e4 — the Owen, the Basman/St George "
                       "and other rare replies. Offbeat, but several are perfectly sound surprise weapons.",
            "white_plan": "Take the centre with d4 and develop; Black's unusual move order usually "
                          "costs a little time or space.",
            "black_plan": "Get out of theory immediately and play on understanding rather than "
                          "memorisation.",
            "variations": [
                ("Owen's Defense", 384, "e4 b6 d4 Bb7 Bd3 e6 Nf3 c5 c3 Nf6 Qe2 d5",
                 "Black fianchettos the queen's bishop at once. Slow but surprisingly resilient."),
                ("Basman's (St George) Defense", 385, "e4 a6 d4 b5 Nf3 Bb7 Bd3 e6 O-O Nf6",
                 "Famous for beating Karpov in 1977: Black grabs queenside space and ignores the centre."),
                ("Nimzovich-Larsen (1...b6 2 d4 e6)", 385, "e4 b6 d4 e6 Nf3 Bb7 Bd3 Nf6 Qe2 c5",
                 "A hedgehog-style set-up where Black concedes the centre and waits."),
                ("Borg / Norwegian Defense (1...g5)", 386, "e4 g5 d4 Bg7 Nc3 c5 dxc5 Qa5",
                 "A notorious joke that is nevertheless hard to refute at speed."),
                ("Fred Defense (1...f5)", 386, "e4 f5 exf5 Nf6 Nc3 d5 Qf3",
                 "Unsound: White simply takes and keeps the extra pawn."),
                ("Lemming / 1...Na6", 386, "e4 Na6 d4 d5 e5 c5 c3 Nc7",
                 "An eccentric knight development, included by MCO for completeness."),
            ],
        },
    ],
}

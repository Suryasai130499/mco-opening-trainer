# -*- coding: utf-8 -*-
# Part I of Modern Chess Openings, 15th ed. (de Firmian) — Double King Pawn Openings
# (name, book_page, SAN moves, note)

PART = {
    "id": "double-king-pawn",
    "num": "I",
    "name": "Double King Pawn Openings",
    "line": "e4 e5",
    "blurb": "Both sides stake a claim in the centre with a pawn. These are the oldest "
             "openings in chess and the most direct: open lines, fast development and early "
             "fights for the f7 and f2 squares.",
    "chapters": [
        {
            "id": "kings-gambit", "num": 1, "name": "King's Gambit", "eco": "C30–C39",
            "page": 3, "line": "e4 e5 f4",
            "summary": "White offers the f-pawn to rip open the f-file and seize the centre with "
                       "d4. It is the great romantic gambit: White gets a fierce initiative but a "
                       "permanently loose king, and modern defensive technique means Black is fine "
                       "with accurate play.",
            "white_plan": "Recapture the centre with d4, develop with Nf3 and Bc4, and aim at f7 "
                          "and the open f-file.",
            "black_plan": "Either hold the extra pawn with ...g5 and give the pawn back at the right "
                          "moment, or decline and hit back in the centre with ...d5.",
            "variations": [
                ("King's Gambit Accepted", 6, "e4 e5 f4 exf4",
                 "Black takes the pawn. White's whole game is now justified by the pace of the attack."),
                ("Kieseritzky Gambit", 6, "e4 e5 f4 exf4 Nf3 g5 h4 g4 Ne5",
                 "The main line of the classical King's Gambit: White plants the knight on e5 and plays for d4 and Bxf4."),
                ("Allgaier Gambit", 6, "e4 e5 f4 exf4 Nf3 g5 h4 g4 Ng5",
                 "A knight sacrifice on f7 to drag the black king out. Spectacular, but Black holds with 5...h6."),
                ("Muzio Gambit", 6, "e4 e5 f4 exf4 Nf3 g5 Bc4 g4 O-O gxf3 Qxf3",
                 "White gives up a whole knight for the open f-file and a raking bishop on c4. The most famous romantic gambit of all."),
                ("Salvio Gambit", 7, "e4 e5 f4 exf4 Nf3 g5 Bc4 g4 Ne5 Qh4+",
                 "Instead of the Muzio piece sacrifice White jumps into e5; Black's check on h4 is awkward for the white king."),
                ("Hanstein Gambit", 6, "e4 e5 f4 exf4 Nf3 g5 Bc4 Bg7 O-O",
                 "A sound, positional treatment: White castles into the open f-file and builds with d4 and c3."),
                ("Philidor Gambit", 6, "e4 e5 f4 exf4 Nf3 g5 Bc4 Bg7 h4",
                 "White hits the g5 pawn at once before castling, keeping the option of Rh1–h2."),
                ("Becker Defense", 8, "e4 e5 f4 exf4 Nf3 h6",
                 "A useful prophylactic move: Black prepares ...g5 while taking the h4 and g5 tricks out of White's hands."),
                ("Cunningham Defense", 8, "e4 e5 f4 exf4 Nf3 Be7",
                 "Black develops and threatens the annoying ...Bh4+, deflecting White from the centre."),
                ("King's Bishop Gambit", 12, "e4 e5 f4 exf4 Bc4",
                 "White develops the bishop before the knight, so that Black's ...Qh4+ costs time after Kf1 and g3."),
                ("Falkbeer Counter Gambit", 14, "e4 e5 f4 d5 exd5 e4",
                 "Black ignores the offered pawn and gives one back to jam White's development with the wedge on e4."),
                ("Falkbeer Modern Line (3...exf4 4 d3)", 15, "e4 e5 f4 d5 exd5 Nf6",
                 "The modern handling: Black regains d5 with the knight and plays simple, healthy development."),
                ("King's Gambit Declined (2...Bc5)", 16, "e4 e5 f4 Bc5",
                 "The soundest decline. The bishop eyes g1 and stops White from castling comfortably."),
                ("King's Gambit Declined (2...d6)", 17, "e4 e5 f4 d6",
                 "A solid, modest decline that keeps the e5 point and waits for White to commit."),
            ],
        },
        {
            "id": "giuoco-piano", "num": 2, "name": "Giuoco Piano", "aka": "Italian Game",
            "eco": "C50–C54", "page": 18, "line": "e4 e5 Nf3 Nc6 Bc4 Bc5",
            "summary": "The 'quiet game' — both sides develop naturally and fight over d4 and f7. "
                       "It ranges from the sharp Møller Attack to the slow manoeuvring of the "
                       "Giuoco Pianissimo, which is one of the most popular openings at every level today.",
            "white_plan": "Build the big centre with c3 and d4, or play the slow d3/Nbd2/Nf1–g3 "
                          "regrouping and attack on the kingside later.",
            "black_plan": "Hold e5, develop with ...Nf6 and ...d6, and look for ...d5 or the "
                          "...Na5/...c6 regrouping against the c4 bishop.",
            "variations": [
                ("Main Line (4 c3)", 19, "e4 e5 Nf3 Nc6 Bc4 Bc5 c3 Nf6 d4 exd4 cxd4 Bb4+",
                 "White grabs the centre; Black's check on b4 is the key resource that keeps the balance."),
                ("Møller Attack", 20, "e4 e5 Nf3 Nc6 Bc4 Bc5 c3 Nf6 d4 exd4 cxd4 Bb4+ Nc3 Nxe4 O-O",
                 "White sacrifices a pawn (and sometimes more) for a huge initiative with d5 and Qb3. Heavily analysed to a draw, but dangerous if you don't know it."),
                ("Greco Attack (7 Nc3 Nxe4 8 O-O Bxc3 9 d5)", 21, "e4 e5 Nf3 Nc6 Bc4 Bc5 c3 Nf6 d4 exd4 cxd4 Bb4+ Nc3 Nxe4 O-O Bxc3 d5",
                 "The point of the Møller: White shuts out the c6 knight and opens lines before recapturing."),
                ("Giuoco Pianissimo (4 d3)", 24, "e4 e5 Nf3 Nc6 Bc4 Bc5 d3 Nf6 O-O d6 c3",
                 "The modern main road. White keeps everything flexible, plays Re1, Nbd2, Nf1 and h3, and expands slowly with d4 or on the kingside."),
                ("4 O-O (Quiet Line)", 23, "e4 e5 Nf3 Nc6 Bc4 Bc5 O-O Nf6 d3 d6 c3",
                 "Castling first keeps the same slow plans while avoiding some of Black's early tricks."),
                ("4 d4 (Italian Gambit)", 22, "e4 e5 Nf3 Nc6 Bc4 Bc5 d4 exd4 Nxd4",
                 "An immediate central break; after the exchanges play becomes open and concrete."),
                ("4 Nc3 (Four Knights Italian)", 24, "e4 e5 Nf3 Nc6 Bc4 Bc5 Nc3 Nf6 d3 d6",
                 "A quiet symmetrical set-up that often transposes into Giuoco Pianissimo structures."),
                ("Hungarian Defense", 154, "e4 e5 Nf3 Nc6 Bc4 Be7",
                 "A modest alternative to 3...Bc5: solid, slightly passive, and very hard to break down."),
            ],
        },
        {
            "id": "evans-gambit", "num": 3, "name": "Evans Gambit", "eco": "C51–C52",
            "page": 26, "line": "e4 e5 Nf3 Nc6 Bc4 Bc5 b4",
            "summary": "White throws in the b-pawn to deflect the c5 bishop and then builds the "
                       "ideal centre with c3 and d4 at speed. A favourite of Morphy and later "
                       "Kasparov — one of the best practical gambits in the open games.",
            "white_plan": "Gain time on the bishop, play c3 and d4, castle and open the f-file or "
                          "the d-file against Black's uncastled king.",
            "black_plan": "Take the pawn, then give it back at the right moment (...d6 and ...Na5) "
                          "to reach a safe position with an extra pawn or clean development.",
            "variations": [
                ("Evans Gambit Accepted", 26, "e4 e5 Nf3 Nc6 Bc4 Bc5 b4 Bxb4 c3 Ba5 d4",
                 "The main line. White has the centre and the initiative in return for the pawn."),
                ("Compromised Defense", 26, "e4 e5 Nf3 Nc6 Bc4 Bc5 b4 Bxb4 c3 Ba5 d4 exd4 O-O dxc3",
                 "Black takes everything. White gets a raging attack with Qb3 and Nxc3 — the classic test of nerve."),
                ("Half-Compromised Defense", 27, "e4 e5 Nf3 Nc6 Bc4 Bc5 b4 Bxb4 c3 Ba5 d4 exd4 O-O d6",
                 "Black returns one pawn to blunt the attack and keep a solid structure."),
                ("Normal Defense (7...Bb6)", 28, "e4 e5 Nf3 Nc6 Bc4 Bc5 b4 Bxb4 c3 Ba5 d4 d6 Qb3 Qd7",
                 "A sound modern treatment: Black defends f7 with the queen and hangs on to the material."),
                ("Evans Gambit Declined", 29, "e4 e5 Nf3 Nc6 Bc4 Bc5 b4 Bb6",
                 "Simply stepping back. White gains space with a4 and b5 but has loosened the queenside."),
            ],
        },
        {
            "id": "two-knights", "num": 4, "name": "Two Knights' Defense", "eco": "C55–C59",
            "page": 30, "line": "e4 e5 Nf3 Nc6 Bc4 Nf6",
            "summary": "Black develops the knight and invites 4 Ng5, attacking f7 at once. The "
                       "resulting lines are the sharpest in the whole Italian complex — Black "
                       "usually gives a pawn for lasting activity.",
            "white_plan": "Either grab the pawn with 4 Ng5 and hold on, or play the positional 4 d4 "
                          "and 4 d3 lines for a normal game.",
            "black_plan": "Accept the pawn deficit after ...d5 and ...Na5 and use the time to "
                          "develop with ...Bc5/...Bd6, aiming at f2 and the centre.",
            "variations": [
                ("Main Line (4 Ng5 d5 5 exd5 Na5)", 31, "e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 d5 exd5 Na5 Bb5+ c6 dxc6 bxc6 Be2 h6",
                 "The principled line. Black is a pawn down but has the centre, open files and the initiative."),
                ("Fried Liver Attack", 36, "e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 d5 exd5 Nxd5 Nxf7 Kxf7 Qf3+",
                 "White sacrifices a knight to drag the king out. Terrifying for an unprepared Black, but objectively Black survives."),
                ("Lolli Attack (6 d4)", 36, "e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 d5 exd5 Nxd5 d4",
                 "A strong alternative to the knight sacrifice, opening the centre against the exposed knight."),
                ("Fritz Variation", 35, "e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 d5 exd5 Nd4",
                 "A razor-sharp pawn-grab line where Black's knight lands on d4 instead of a5."),
                ("Ulvestad Variation", 35, "e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 d5 exd5 b5",
                 "Black offers a second pawn to deflect the bishop and open the long diagonal."),
                ("Wilkes-Barre (Traxler) Variation", 35, "e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 Bc5",
                 "Black ignores f7 entirely and counter-attacks. One of the wildest replies in the openings — both kings come under fire."),
                ("4 Ng5 (Knight Attack)", 32, "e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 d5 exd5 Na5",
                 "The critical try: a genuine pawn-grab that Black must meet with energy."),
                ("Modern Bishop's Opening Line (4 d3)", 40, "e4 e5 Nf3 Nc6 Bc4 Nf6 d3 Bc5 c3 d6 O-O",
                 "Avoiding all the sharp stuff: a Giuoco Pianissimo structure with slow manoeuvring."),
                ("4 d4 exd4 5 O-O (Scotch Gambit lines)", 38, "e4 e5 Nf3 Nc6 Bc4 Nf6 d4 exd4 O-O Nxe4 Re1 d5 Bxd5 Qxd5 Nc3",
                 "White sacrifices for an attack on the centralised black queen and the e-file."),
                ("Max Lange Attack", 38, "e4 e5 Nf3 Nc6 Bc4 Nf6 d4 exd4 O-O Bc5 e5 d5 exf6 dxc4 Re1+ Be6 Ng5",
                 "A famous attacking line where White's pieces swarm around e6 and f7. Must be known move for move."),
                ("4 Nc3 (Four Knights)", 41, "e4 e5 Nf3 Nc6 Bc4 Nf6 Nc3 Nxe4 Nxe4 d5",
                 "A quiet transposition; the symmetry means little real danger for either side."),
            ],
        },
        {
            "id": "ruy-lopez", "num": 5, "name": "Ruy Lopez", "aka": "Spanish Game",
            "eco": "C60–C99", "page": 42, "line": "e4 e5 Nf3 Nc6 Bb5",
            "summary": "The deepest and most important of all the open games. White pressures the "
                       "knight that defends e5 and then builds a slow bind with c3, d4 and Nbd2–f1–g3. "
                       "MCO devotes three whole sections to it, and virtually every world champion "
                       "has played both sides.",
            "white_plan": "Castle, play Re1, c3, h3 and d4, keep the tension in the centre, then "
                          "manoeuvre the knight to g3/f5 and attack the kingside.",
            "black_plan": "Secure e5 with ...d6 and ...Be7, gain space with ...b5 and ...c5, and "
                          "find counterplay with ...d5, ...Na5–c4 or the ...exd4 break.",
            "variations": [
                # Section A: systems without ...a6
                ("Classical (Cordel) Defense", 45, "e4 e5 Nf3 Nc6 Bb5 Bc5",
                 "The most natural developing move. Black goes for quick play against f2 instead of the usual slow set-ups."),
                ("Berlin Defense", 47, "e4 e5 Nf3 Nc6 Bb5 Nf6 O-O Nxe4 d4 Nd6 Bxc6 dxc6 dxe5 Nf5 Qxd8+ Kxd8",
                 "The Berlin Wall. Black accepts a slightly worse structure and no castling for a rock-solid endgame — Kramnik's weapon against Kasparov in 2000."),
                ("Cozio Defense", 49, "e4 e5 Nf3 Nc6 Bb5 Nge7",
                 "An old, flexible system: Black keeps the f6 square free for the other knight or the f-pawn."),
                ("Bird's Defense", 49, "e4 e5 Nf3 Nc6 Bb5 Nd4",
                 "Black offers a knight trade immediately to kill White's pressure, at the cost of some time."),
                ("Old Steinitz Defense", 51, "e4 e5 Nf3 Nc6 Bb5 d6",
                 "Very solid but cramped: Black defends e5 directly and accepts a passive position."),
                ("Fianchetto Defense (3...g6)", 51, "e4 e5 Nf3 Nc6 Bb5 g6",
                 "Black treats the Spanish like a Modern Defense, putting the bishop on the long diagonal."),
                ("Schliemann (Jaenisch) Variation", 53, "e4 e5 Nf3 Nc6 Bb5 f5",
                 "An immediate counter-gambit. Black blows open the centre at the price of his king's safety."),
                # Section B: variants on moves 4-6 after 3...a6
                ("Exchange Variation", 58, "e4 e5 Nf3 Nc6 Bb5 a6 Bxc6 dxc6 O-O f6 d4 exd4 Nxd4 c5",
                 "White trades on c6 to give Black doubled pawns and play a structural endgame. Black gets the bishops and the centre."),
                ("Modern Steinitz Defense", 60, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 d6 c3 Bd7 d4 Nf6",
                 "With ...a6 inserted, the Steinitz becomes much more resilient — Black keeps the option of ...b5."),
                ("Siesta Variation", 60, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 d6 c3 f5",
                 "A sharp pawn thrust in the Steinitz, giving Black active play on the f-file."),
                ("Lines with 3...a6 and ...Bc5", 64, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Bc5",
                 "Black develops actively rather than with ...Be7, accepting a slightly loose bishop for more punch."),
                ("Arkangel (Counterthrust) Variation", 66, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O b5 Bb3 Bb7",
                 "Black puts the bishop on the long diagonal and plays for ...Bc5 and a direct attack. Very sharp and fully respectable."),
                ("Fifth-Move Variants (5 d3)", 68, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 d3 b5 Bb3 Bc5",
                 "A quiet modern choice: White keeps the bishop and plays a slow Italian-style build-up."),
                ("Worrall Attack", 70, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 Qe2 b5 Bb3 O-O c3 d5",
                 "White uses the queen instead of the rook to support e4, keeping Re1 in reserve for f1."),
                ("Center Variation (5 d4)", 70, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 d4 exd4 e5 Ne4 O-O Be7",
                 "An immediate central strike that leads to concrete, forcing play."),
                ("Exchange Variation Deferred", 70, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 Bxc6 dxc6 d3",
                 "Taking on c6 a move later, once Black has committed the knight to f6."),
                ("Open Variation", 72, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Nxe4 d4 b5 Bb3 d5 dxe5 Be6",
                 "Black grabs e4 and accepts an isolated, active position. Korchnoi's lifelong defence, full of concrete play."),
                ("Howell Attack", 72, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Nxe4 d4 b5 Bb3 d5 dxe5 Be6 Qe2",
                 "Against the Open Variation White develops the queen to e2 and prepares Rd1 and c4."),
                ("Dilworth Attack", 74, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Nxe4 d4 b5 Bb3 d5 dxe5 Be6 c3 Bc5 Nbd2 O-O Bc2 Nxf2",
                 "Black sacrifices a piece on f2 for two pawns and a dominating position — one of the most original ideas in the Spanish."),
                # Section C: main lines, closed and Marshall
                ("Closed Defense (minor systems)", 81, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 Re1 b5 Bb3 d6 c3 O-O",
                 "The starting position of the Closed Spanish — the most-played structure in classical chess."),
                ("Chigorin Variation", 83, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 Re1 b5 Bb3 d6 c3 O-O h3 Na5 Bc2 c5 d4 Qc7",
                 "The classical main line: Black's knight goes to a5 and the c-pawn hits the centre. The textbook Spanish manoeuvring battle."),
                ("Keres Variation", 85, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 Re1 b5 Bb3 d6 c3 O-O h3 Na5 Bc2 c5 d4 Nd7",
                 "A refinement of the Chigorin where the knight retreats to support ...cxd4 and ...Nb6."),
                ("Breyer Variation", 87, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 Re1 b5 Bb3 d6 c3 O-O h3 Nb8 d4 Nbd7",
                 "The paradoxical retreat ...Nb8, rerouting the knight to d7 and freeing the c-pawn and the b7 bishop. A modern main line."),
                ("Smyslov Variation", 89, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 Re1 b5 Bb3 d6 c3 O-O h3 h6 d4 Re8",
                 "A flexible waiting move that prepares ...Be6 or ...Nd7 without committing the knight."),
                ("Zaitsev (Fianchetto) Variation", 91, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 Re1 b5 Bb3 d6 c3 O-O h3 Bb7 d4 Re8",
                 "Black's bishop goes to b7 and the rook to e8, aiming at e4. Karpov's main defence for years."),
                ("Marshall Attack", 93, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 Re1 b5 Bb3 O-O c3 d5 exd5 Nxd5 Nxe5 Nxe5 Rxe5 c6",
                 "Black sacrifices a pawn for a long-term attack with ...Bd6, ...Qh4 and ...Bg4. The most respected gambit in modern chess."),
                ("Anti-Marshall Lines", 94, "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 Re1 b5 Bb3 O-O a4",
                 "White sidesteps the Marshall entirely by hitting b5 with 8 a4 instead of playing c3."),
            ],
        },
        {
            "id": "petrov", "num": 6, "name": "Petrov's Defense", "aka": "Russian Game / Petroff",
            "eco": "C42–C43", "page": 96, "line": "e4 e5 Nf3 Nf6",
            "summary": "Instead of defending e5, Black counter-attacks e4. The symmetry makes this "
                       "one of the soundest and most drawish replies to 1 e4 — a favourite of players "
                       "who want to neutralise White's first move.",
            "white_plan": "Take on e5 and then build with d4, Bd3, c4 or Re1, using the space edge "
                          "to press on the centre and the e-file.",
            "black_plan": "Trade pieces, complete development with ...Be7 and ...Bf5 or ...Nc6, and "
                          "equalise with ...d5 firmly in place.",
            "variations": [
                ("Classical Main Line", 97, "e4 e5 Nf3 Nf6 Nxe5 d6 Nf3 Nxe4 d4 d5 Bd3 Be7 O-O Nc6 Re1 Bg4 c3 f5",
                 "The central position of the Petroff. Black's e4 knight is well placed and the structures are symmetrical."),
                ("5 d4 Main Line", 98, "e4 e5 Nf3 Nf6 Nxe5 d6 Nf3 Nxe4 d4 d5 Bd3 Nc6 O-O Be7 c4 Nb4",
                 "White challenges the centre with c4; Black's ...Nb4 is the standard way to keep the balance."),
                ("5 Nc3 (Classical Attack)", 100, "e4 e5 Nf3 Nf6 Nxe5 d6 Nf3 Nxe4 Nc3 Nxc3 dxc3 Be7 Bf4 O-O Qd2",
                 "Simplifying into a slightly better structure for White — queenside majority and the bishop pair."),
                ("Steinitz Variation (3 d4)", 101, "e4 e5 Nf3 Nf6 d4 exd4 e5 Ne4 Qxd4 d5 exd6 Nxd6",
                 "White keeps more pieces on the board and plays for the extra central space."),
                ("3 Nxe5 Qe7 (Classical Defense)", 102, "e4 e5 Nf3 Nf6 Nxe5 Qe7 Nf3 Qxe4+ Be2",
                 "An old line in which Black regains the pawn with the queen, conceding development."),
                ("3 d4 Nxe4 (Modern Attack)", 103, "e4 e5 Nf3 Nf6 d4 Nxe4 Bd3 d5 Nxe5 Nd7",
                 "A sharper treatment where White keeps a strong knight on e5."),
            ],
        },
        {
            "id": "scotch", "num": 7, "name": "Scotch Game", "eco": "C44–C45",
            "page": 104, "line": "e4 e5 Nf3 Nc6 d4 exd4",
            "summary": "White opens the centre immediately. The resulting positions are clear and "
                       "concrete, which is exactly why Kasparov revived the Scotch at the top level "
                       "in the 1990s as an antidote to Spanish theory.",
            "white_plan": "Recapture on d4, develop quickly, and use the space and the half-open "
                          "d-file; in the 4 Nxd4 Bc5 lines play Be3 and c3 to hold the knight.",
            "black_plan": "Hit the d4 knight at once with ...Bc5 or ...Nf6, challenge e4, and trade "
                          "into comfortable structures.",
            "variations": [
                ("Schmidt / Main Line (4...Nf6)", 105, "e4 e5 Nf3 Nc6 d4 exd4 Nxd4 Nf6 Nxc6 bxc6 e5 Qe7 Qe2 Nd5 c4 Nb6",
                 "Kasparov's main line. White gets space, Black gets the bishops and a flexible structure."),
                ("Mieses Variation (5 Nxc6 bxc6 6 e5)", 106, "e4 e5 Nf3 Nc6 d4 exd4 Nxd4 Nf6 Nxc6 bxc6 e5 Qe7 Qe2 Nd5 c4 Ba6",
                 "The sharpest branch: Black puts the bishop on a6 and fights for c4 and the light squares."),
                ("Classical Variation (4...Bc5)", 108, "e4 e5 Nf3 Nc6 d4 exd4 Nxd4 Bc5 Be3 Qf6 c3 Nge7 Bc4 Ne5 Be2",
                 "Black develops with tempo. White must defend d4 carefully but keeps a small space edge."),
                ("Potter Variation (5 Nb3)", 109, "e4 e5 Nf3 Nc6 d4 exd4 Nxd4 Bc5 Nb3 Bb6 Nc3 Nf6 Bg5",
                 "White steps aside and plays for a quiet space advantage rather than tactics."),
                ("Steinitz Variation (4...Qh4)", 110, "e4 e5 Nf3 Nc6 d4 exd4 Nxd4 Qh4 Nc3 Bb4 Be2 Qxe4 Nb5",
                 "A provocative queen sortie that grabs a pawn and invites a dangerous attack."),
                ("Scotch Gambit", 112, "e4 e5 Nf3 Nc6 d4 exd4 Bc4 Bc5 c3 dxc3 Nxc3",
                 "Rather than recapture, White develops and offers the pawn for a quick attack on f7."),
                ("Göring Gambit", 138, "e4 e5 Nf3 Nc6 d4 exd4 c3 dxc3 Nxc3",
                 "White gives a pawn for two tempi and open lines — the Danish Gambit with the knights already out."),
                ("Göring Gambit Declined (4...d5)", 139, "e4 e5 Nf3 Nc6 d4 exd4 c3 d5 exd5 Qxd5 cxd4 Bg4",
                 "The safest answer: Black returns the pawn and trades into a comfortable position."),
            ],
        },
        {
            "id": "vienna", "num": 8, "name": "Vienna Game", "eco": "C25–C29",
            "page": 114, "line": "e4 e5 Nc3",
            "summary": "A flexible second move: White supports e4 and keeps f4 in reserve, so the "
                       "Vienna can become a King's Gambit with the knight out, or a slow positional "
                       "game with g3 and Bg2.",
            "white_plan": "Play f4 for a King's-Gambit-style attack, or g3/Bg2/Nge2 for a quiet "
                          "build-up; in either case e4 is already secure.",
            "black_plan": "Meet f4 with the solid ...d5, or play ...Nf6 and ...Nc6 and treat the "
                          "position like a Four Knights' Game.",
            "variations": [
                ("Frankenstein-Dracula Variation", 115, "e4 e5 Nc3 Nf6 Bc4 Nxe4 Qh5 Nd6 Bb3 Nc6 Nb5 g6 Qf3 f5 Qd5 Qe7 Nxc7+ Kd8 Nxa8 b6",
                 "Fittingly named: Black grabs a pawn and lets White's knight eat a rook, then traps it. Total chaos, and genuinely playable."),
                ("Vienna Gambit (3 f4)", 117, "e4 e5 Nc3 Nf6 f4 d5 fxe5 Nxe4 Nf3 Be7 d4 O-O Bd3",
                 "The main gambit line. Black's ...d5 is the correct answer, after which play is sharp but balanced."),
                ("Mieses Variation (3 g3)", 118, "e4 e5 Nc3 Nf6 g3 d5 exd5 Nxd5 Bg2 Nxc3 bxc3 Bd6",
                 "A calm fianchetto treatment, playing for pressure on the long diagonal."),
                ("Steinitz Gambit", 119, "e4 e5 Nc3 Nc6 f4 exf4 d4 Qh4+ Ke2",
                 "White walks the king to e2 to keep the extra centre pawn. Outrageous-looking, but it has real points."),
                ("Pierce Gambit", 119, "e4 e5 Nc3 Nc6 f4 exf4 Nf3 g5 d4",
                 "A double pawn sacrifice for a raging attack down the middle."),
                ("Hamppe-Allgaier Gambit", 120, "e4 e5 Nc3 Nc6 f4 exf4 Nf3 g5 h4 g4 Ng5",
                 "The Allgaier idea with the knight already on c3 — Nxf7 is coming."),
                ("Vienna with 2...Nc6 3 Nf3", 120, "e4 e5 Nc3 Nc6 Nf3 Nf6",
                 "A direct transposition into the Four Knights' Game."),
            ],
        },
        {
            "id": "four-knights", "num": 9, "name": "Four Knights' Game", "eco": "C47–C49",
            "page": 121, "line": "e4 e5 Nf3 Nc6 Nc3 Nf6",
            "summary": "All four knights come out before anything is decided. Famously solid and "
                       "symmetrical — the classic 'safety first' open game, but with some sharp "
                       "gambit exceptions.",
            "white_plan": "Play Bb5 and d3 for a Spanish-style bind, or break the symmetry with d4 "
                          "(Scotch Four Knights).",
            "black_plan": "Copy White's development and look for the freeing ...d5 or ...Nd4.",
            "variations": [
                ("Symmetrical (Double Spanish) Variation", 123, "e4 e5 Nf3 Nc6 Nc3 Nf6 Bb5 Bb4 O-O O-O d3 d6 Bg5 Bxc3 bxc3 Qe7",
                 "Perfect symmetry until White breaks it. Very solid; both sides manoeuvre slowly."),
                ("Svenonius Variation", 125, "e4 e5 Nf3 Nc6 Nc3 Nf6 Bb5 Nd4",
                 "Black goes for an immediate trade on d4 to relieve the pressure and gain space."),
                ("Rubinstein Variation", 125, "e4 e5 Nf3 Nc6 Nc3 Nf6 Bb5 Nd4 Nxd4 exd4 e5 dxc3 exf6 Qxf6 dxc3 Qe5+",
                 "Black's counter-gambit with ...Nd4 leads to a forcing sequence where the pawn structure shatters. The main theoretical line."),
                ("Scotch Four Knights", 126, "e4 e5 Nf3 Nc6 Nc3 Nf6 d4 exd4 Nxd4 Bb4 Nxc6 bxc6 Bd3 d5",
                 "White opens the centre; Black's ...Bb4 and ...d5 give good equalising chances."),
                ("Belgrade Gambit", 127, "e4 e5 Nf3 Nc6 Nc3 Nf6 d4 exd4 Nd5",
                 "A surprise weapon: White offers the e-pawn for a lead in development and tactics around f7 and e7."),
                ("Spanish Four Knights (4 Bb5 Bc5)", 128, "e4 e5 Nf3 Nc6 Nc3 Nf6 Bb5 Bc5 O-O O-O Nxe5 Nxe5 d4",
                 "Black develops actively and White strikes with the d4 fork trick."),
            ],
        },
        {
            "id": "three-knights", "num": 10, "name": "Three Knights' Game", "eco": "C46",
            "page": 129, "line": "e4 e5 Nf3 Nc6 Nc3",
            "summary": "Black avoids the symmetrical ...Nf6 and develops some other way — usually "
                       "...g6 or ...Bb4 — leading to independent, less-charted positions.",
            "white_plan": "Take the centre with d4 while Black's development is still unusual.",
            "black_plan": "Choose a set-up that dodges the main Four Knights' theory and play for a "
                          "sound, slightly offbeat game.",
            "variations": [
                ("3...g6 (Fianchetto Defense)", 129, "e4 e5 Nf3 Nc6 Nc3 g6 d4 exd4 Nd5 Bg7 Bg5 Nce7",
                 "Black builds a Modern-style set-up; White grabs the centre with d4 and Nd5."),
                ("3...Bb4 (Pin Variation)", 130, "e4 e5 Nf3 Nc6 Nc3 Bb4 Nd5 Nf6 Nxb4 Nxb4 c3",
                 "The bishop pin is met by Nd5, after which White gains time hitting the pieces."),
                ("3...Bc5", 131, "e4 e5 Nf3 Nc6 Nc3 Bc5 Nxe5 Nxe5 d4 Bd6 dxe5 Bxe5",
                 "A natural but slightly loose developing move that allows the fork trick on e5."),
                ("3...f5 (Steinitz)", 131, "e4 e5 Nf3 Nc6 Nc3 f5 exf5 e4 Ng5 Nf6 d3",
                 "An aggressive counter-gambit in the spirit of the Schliemann."),
            ],
        },
        {
            "id": "philidor", "num": 11, "name": "Philidor's Defense", "eco": "C41",
            "page": 132, "line": "e4 e5 Nf3 d6",
            "summary": "Black defends e5 with the d-pawn, giving a cramped but very hard-to-crack "
                       "position. Modern practice treats it as a move-order trick to reach good "
                       "versions of Pirc-like structures.",
            "white_plan": "Take space with d4, develop smoothly, and exploit the extra room with "
                          "Bc4, Qe2 and pressure on f7 or d6.",
            "black_plan": "Hold the centre with ...Nf6, ...Be7 and ...c6, then free the game with "
                          "...d5 or ...exd4 and ...Re8.",
            "variations": [
                ("Main Line (3 d4)", 132, "e4 e5 Nf3 d6 d4 exd4 Nxd4 Nf6 Nc3 Be7 Be2 O-O O-O",
                 "The standard treatment. White has more space; Black is solid and waits for ...d5 or ...Re8 and ...Bf8."),
                ("Hanham Variation", 133, "e4 e5 Nf3 d6 d4 Nd7 Bc4 c6 O-O Be7",
                 "Nimzowitsch's recommended set-up: a very compact, almost impenetrable formation around e5."),
                ("Larsen Variation (3...exd4 4 Nxd4 g6)", 133, "e4 e5 Nf3 d6 d4 exd4 Nxd4 g6 Nc3 Bg7 Be3 Nf6",
                 "A modern hybrid that aims for Pirc/Dragon-type counterplay on the long diagonal."),
                ("Philidor Counter Gambit", 134, "e4 e5 Nf3 d6 d4 f5",
                 "An old, wild line. Black opens the f-file immediately but weakens his king badly."),
                ("Queen's Pawn Counter Gambit", 155, "e4 e5 Nf3 d5",
                 "The Elephant Gambit, listed in MCO among the unusual king pawn lines: dubious but surprising."),
            ],
        },
        {
            "id": "ponziani", "num": 12, "name": "Ponziani's Opening", "eco": "C44",
            "page": 135, "line": "e4 e5 Nf3 Nc6 c3",
            "summary": "White prepares d4 with the modest c3. It is slow and slightly committal — "
                       "Black has several good answers — but it leads to fresh positions away from "
                       "mainstream theory.",
            "white_plan": "Play d4 and Qa4 or Bb5, using the big centre and the pressure on the "
                          "c6 knight.",
            "black_plan": "Strike at once with ...d5 or ...Nf6, exploiting the fact that c3 does "
                          "nothing for White's development.",
            "variations": [
                ("3...d5 (Main Line)", 135, "e4 e5 Nf3 Nc6 c3 d5 Qa4 Bd7 exd5 Nd4",
                 "The most testing answer: Black opens the centre while White's queen is drawn offside."),
                ("3...Nf6 (Jaenisch)", 136, "e4 e5 Nf3 Nc6 c3 Nf6 d4 Nxe4 d5 Ne7 Nxe5 Ng6",
                 "Black develops and takes on e4, leading to sharp play with the knights dancing."),
                ("3...f5 (Caro Counter Gambit)", 137, "e4 e5 Nf3 Nc6 c3 f5 d4 fxe4 Nxe5 Nf6",
                 "A sharp counter-gambit that immediately challenges White's set-up."),
            ],
        },
        {
            "id": "goring-gambit", "num": 13, "name": "Göring Gambit", "eco": "C44",
            "page": 138, "line": "e4 e5 Nf3 Nc6 d4 exd4 c3",
            "summary": "The Danish Gambit with knights developed: White offers one or two pawns for "
                       "a lead in development and a raking pair of bishops aimed at f7.",
            "white_plan": "Open lines with cxd3/Nxc3 and Bc4, castle fast and attack f7 and the "
                          "d-file before Black consolidates.",
            "black_plan": "Either take and give the pawn back with ...d6 and ...Be6, or decline "
                          "cleanly with 4...d5.",
            "variations": [
                ("Göring Gambit Accepted", 138, "e4 e5 Nf3 Nc6 d4 exd4 c3 dxc3 Nxc3 d6 Bc4 Be6",
                 "Black returns the pawn at the right moment with ...Be6 and reaches a solid position."),
                ("Double Pawn Sacrifice", 139, "e4 e5 Nf3 Nc6 d4 exd4 c3 dxc3 Bc4 cxb2 Bxb2",
                 "White gives up two pawns for two bishops raking at the black king — the pure Danish treatment."),
                ("Göring Gambit Declined (4...d5)", 140, "e4 e5 Nf3 Nc6 d4 exd4 c3 d5 exd5 Qxd5 cxd4 Bg4 Be2 Bb4+",
                 "Simply the best: Black gives the pawn back and develops with tempo."),
                ("Göring Gambit Declined (4...Nge7)", 140, "e4 e5 Nf3 Nc6 d4 exd4 c3 Nge7 cxd4 d5",
                 "A solid alternative decline, keeping the position closed."),
            ],
        },
        {
            "id": "danish-gambit", "num": 14, "name": "Danish Gambit", "eco": "C21",
            "page": 141, "line": "e4 e5 d4 exd4 c3",
            "summary": "Two pawns for two bishops and a tempo-rich attack. It is unsound against "
                       "precise defence but devastating in practical play if Black doesn't know the "
                       "refutation.",
            "white_plan": "Sacrifice both centre pawns to put bishops on c4 and b2 and blast open "
                          "the centre.",
            "black_plan": "Accept once and then return the material with ...d5, reaching an equal "
                          "or better endgame.",
            "variations": [
                ("Danish Gambit Accepted", 141, "e4 e5 d4 exd4 c3 dxc3 Bc4 cxb2 Bxb2 d5 Bxd5 Nf6",
                 "Black takes everything and then gives it back with ...d5 — the main refutation, leading to equality."),
                ("Schlechter Defense", 142, "e4 e5 d4 exd4 c3 dxc3 Bc4 cxb2 Bxb2 d5 Bxd5 Nf6 Bxf7+ Kxf7 Qxd8 Bb4+",
                 "A clean way to defuse the attack: Black trades queens by force and reaches a safe endgame."),
                ("Danish Gambit Declined (3...d5)", 143, "e4 e5 d4 exd4 c3 d5 exd5 Qxd5 cxd4 Nc6",
                 "Black returns the pawn immediately and develops naturally with equality."),
                ("Danish Gambit Declined (3...Qe7)", 143, "e4 e5 d4 exd4 c3 Qe7 cxd4 Qxe4+ Be2",
                 "Grabbing the e-pawn with the queen; White gets a big lead in development."),
            ],
        },
        {
            "id": "latvian-gambit", "num": 15, "name": "Latvian Gambit", "aka": "Greco Counter Gambit",
            "eco": "C40", "page": 144, "line": "e4 e5 Nf3 f5",
            "summary": "A mirror of the King's Gambit, played a move down. Objectively dubious, but "
                       "full of traps — a genuine surprise weapon for Black.",
            "white_plan": "Take with Nxe5 and defend accurately; the extra tempo means White should "
                          "end up with a clear advantage.",
            "black_plan": "Open the f-file and play for a direct attack on the white king before "
                          "White consolidates.",
            "variations": [
                ("Main Line (3 Nxe5 Qf6)", 144, "e4 e5 Nf3 f5 Nxe5 Qf6 d4 d6 Nc4 fxe4 Nc3 Qg6",
                 "The principled line: Black regains the pawn but his position stays loose."),
                ("3 Bc4 (Best Practical Answer)", 145, "e4 e5 Nf3 f5 Bc4 fxe4 Nxe5 Qg5 d4 Qxg2 Qh5",
                 "Declining the pawn and developing is the safest and strongest reply."),
                ("3 exf5 (Accepted)", 146, "e4 e5 Nf3 f5 exf5 e4 Ne5 Nf6 Be2 d6",
                 "White takes on f5 and tries to hold the extra pawn while Black builds a centre wedge."),
            ],
        },
        {
            "id": "bishops-opening", "num": 16, "name": "Bishop's Opening", "eco": "C23–C24",
            "page": 147, "line": "e4 e5 Bc4",
            "summary": "An old move that has come back strongly: White develops the bishop to its "
                       "best square and keeps the option of d3/Nf3 (an Italian) or f4 (a King's "
                       "Gambit) or Nc3 (a Vienna).",
            "white_plan": "Play d3 and Nf3 for a slow Italian build-up, or d4 and f4 for a sharp "
                          "central attack.",
            "black_plan": "Develop with ...Nf6 and ...c6/...d5, or play ...Bc5 and head for "
                          "Giuoco Piano structures.",
            "variations": [
                ("Berlin Defense (2...Nf6)", 147, "e4 e5 Bc4 Nf6 d3 c6 Nf3 d5 Bb3 Bd6",
                 "Black develops and immediately fights for d5 — the main modern answer."),
                ("Classical (2...Bc5)", 148, "e4 e5 Bc4 Bc5 Nf3 Nf6 d3 d6 c3 O-O",
                 "A direct transposition into a Giuoco Pianissimo."),
                ("Urusov Gambit", 149, "e4 e5 Bc4 Nf6 d4 exd4 Nf3 Nxe4 Qxd4",
                 "White gives the e-pawn for rapid development and attacking chances on the e-file."),
                ("Lewis Counter Gambit", 150, "e4 e5 Bc4 Bc5 d4 Bxd4 Nf3 Nc6",
                 "A sharp, old-fashioned line where the bishop snaps off the centre pawn."),
                ("Vienna Hybrid (2...Nf6 3 Nc3)", 150, "e4 e5 Bc4 Nf6 Nc3 Nxe4 Qh5 Nd6 Bb3",
                 "Transposing to the Frankenstein-Dracula complex of the Vienna Game."),
            ],
        },
        {
            "id": "center-game", "num": 17, "name": "Center Game", "eco": "C22",
            "page": 151, "line": "e4 e5 d4 exd4 Qxd4",
            "summary": "White recaptures with the queen, accepting a loss of time for an immediate "
                       "grip on the centre. Modern versions with Qe3 and O-O-O are a real practical "
                       "weapon.",
            "white_plan": "Reroute the queen to e3, play Nc3, Bd2 and O-O-O, then attack on the "
                          "kingside with f4 and g4.",
            "black_plan": "Gain time on the queen with ...Nc6, develop fast with ...Nf6 and ...Bb4, "
                          "and break with ...d5.",
            "variations": [
                ("Berger Variation (3...Nc6 4 Qe3)", 151, "e4 e5 d4 exd4 Qxd4 Nc6 Qe3 Nf6 Nc3 Bb4 Bd2 O-O O-O-O Re8",
                 "The main line: both sides castle on opposite wings and race. Richer than its reputation."),
                ("4 Qa4 (Hall Variation)", 152, "e4 e5 d4 exd4 Qxd4 Nc6 Qa4 Nf6 Nc3 Bb4 Bd2 O-O",
                 "The queen steps aside to a4 instead of e3, keeping the d-file clear."),
                ("Center Game with 4 Qc3", 153, "e4 e5 d4 exd4 Qxd4 Nc6 Qc3 Nf6 Nf3 Be7 Bc4 O-O O-O d6",
                 "A rarer square for the queen: it keeps e4 supported, but blocks the c3 knight and can be hit by ...Bb4."),
            ],
        },
        {
            "id": "unusual-double-king-pawn", "num": 18, "name": "Unusual Double King Pawn Openings",
            "eco": "C20–C40", "page": 154, "line": "e4 e5",
            "summary": "MCO's catch-all for the rare second and third moves after 1 e4 e5 — some "
                       "harmless, some genuinely tricky surprise weapons.",
            "white_plan": "Vary early to get Black out of preparation while keeping a sound structure.",
            "black_plan": "Develop sensibly and punish any loss of time in the centre.",
            "variations": [
                ("Alapin's Opening", 154, "e4 e5 Ne2",
                 "An eccentric knight development, keeping the f-pawn free for f4 but blocking the bishop."),
                ("Hungarian Defense", 154, "e4 e5 Nf3 Nc6 Bc4 Be7 d4 exd4 Nxd4 Nxd4 Qxd4 Nf6",
                 "Solid and passive: Black simply develops and keeps everything defended."),
                ("Elephant Gambit", 156, "e4 e5 Nf3 d5 exd5 e4 Qe2 Nf6 Nc3 Bf5",
                 "Black offers a pawn to open lines at once. Unsound but surprising."),
                ("Damiano's Defense", 156, "e4 e5 Nf3 f6",
                 "Historically famous as the worst reply to 2 Nf3 — Nxe5 wins material by force."),
                ("Portuguese / Napoleon Attack (2 Qf3)", 156, "e4 e5 Qf3 Nc6 Bc4 Nf6",
                 "An early queen sortie that achieves nothing against sensible play."),
                ("King's Pawn Opening (2 d3)", 157, "e4 e5 d3 Nf6 Nf3 Nc6 g3",
                 "A quiet King's-Indian-Attack set-up against 1...e5."),
                ("Lopez Opening (2 c3)", 157, "e4 e5 c3 Nf6 d3 d5",
                 "A slow build-up that cedes the initiative to Black."),
            ],
        },
    ],
}

# MCO-15 Opening Trainer

A static site for learning chess openings: **548 lines** and **639 sidelines** from *Modern
Chess Openings, 15th Edition*, each on a page of its own, each drilled move by move.

Live at **https://suryasai130499.github.io/mco-opening-trainer/**

## How the training works

Every opening belongs to one side. The Sicilian is Black's, the Ruy Lopez is White's — so
each chapter records which colour it is a repertoire for (see
[`site/data/sides.py`](site/data/sides.py)), and the trainer follows from that:

- the board is oriented to **your** side;
- you play only your side's moves — the opponent's replies play themselves;
- the coach names the move in words (*"Move the knight to f3"*) in **guided** mode, or asks
  you to recall it in **from memory** mode, with hints that escalate from the piece's square
  to the move itself;
- an illegal move does nothing; a legal move that is not this line's move is played on the
  board, marked wrong, and taken back;
- right-drag a piece to draw an **analysis arrow** — and only to a square that piece could
  really go to, so a knight's arrow bends into its L, a pawn on its home rank offers two
  squares and one thereafter, a pinned piece offers nothing, and en passant is offered to
  the side whose turn it is. Shift and Alt change the colour, a tap rings a square, a
  plain click wipes them, and the **Arrows** button makes an ordinary drag draw so it
  works on a phone.

The rules live in [`site/web/chess.js`](site/web/chess.js), about 200 lines and no
dependencies. [`site/web/rules-test.html`](site/web/rules-test.html) replays every position
in the book through it and demands the same answer python-chess gave at build time —
**14,263 positions, 0 mismatches**, which is why the site can ship positions alone and work
out the moves in the browser.

## The pages

```
/                               every opening, searchable
/o/sicilian/                    an opening: its lines, plans and your progress
/o/sicilian/najdorf-variation/  the trainer for one line
/quiz/                          name the opening from a position
```

600 pages in all. Each fetches only its own data — a line page is about 2.6 kB rather than
the whole book — while the stylesheet and script are shared and cached across the site.

## Building it

The page source lives in [`site/web/`](site/web/) (one stylesheet, one script) and the data
in [`site/data/`](site/data/). Two steps, and only the first needs anything installed:

```bash
pip install chess
```

```bash
python site/data/build.py
```

That reads the authored lines in `data_p1.py` … `data_p6.py`, replays every move to verify
it is legal, attaches the sidelines recovered from the book's footnotes, and writes
`site/openings.js` (committed, so CI needs no packages).

```bash
python site/data/make_site.py
```

That slices `openings.js` into `site/dist/` — the whole site, one page per opening and per
line. `site/dist/` is generated, so it is not committed.

```bash
python -m http.server 8788 --directory site/dist
```

To check the rules the browser applies against the ones the data was built with, serve
`site/` instead and open `web/rules-test.html`:

```bash
python -m http.server 8789 --directory site
```

## Deploying

[`.github/workflows/pages.yml`](.github/workflows/pages.yml) runs `make_site.py` and
publishes `site/dist/` on every push to `main`. Any other static host works too — point it
at `site/dist/`. Every path in the site is relative, so it serves correctly from a
subdirectory as well as from the root of a domain.

## Provenance

Opening names, move orders, game citations and page references are indexed from *Modern
Chess Openings, 15th Edition* by Nick de Firmian (Random House Puzzles & Games / David
McKay, 2008). Lines marked **Modern theory** are not from the book.

The explanatory notes and plans are written for this project. The book's own commentary
and evaluation symbols are **not** reproduced — the page references are there so a line
can be looked up in the book. The PDF is not in this repository and is excluded by
`.gitignore`.

Every move sequence has been machine-verified as legal chess with `python-chess`:

```bash
python site/data/validate.py
```

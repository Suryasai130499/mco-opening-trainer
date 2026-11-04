# MCO-15 Opening Trainer

An offline website for learning every opening in *Modern Chess Openings, 15th Edition*
(Nick de Firmian, Random House / David McKay, 2008) — the PDF in the parent folder.

## Running it

Open `index.html` directly in a browser, or serve the folder:

```bash
python -m http.server 8777 --directory site
```

Then visit <http://localhost:8777>.

## What's in it

| | |
|---|---|
| Parts | 6 |
| Chapters (named openings) | 50 |
| Variations with full move sequences | 548 |
| Sidelines recovered from the footnotes | 639, on 301 variations |
| Positions | ~17,000 |

The structure follows the book: the six parts and fifty chapters come from the table of
contents (pp. vi–vii), and the named variations and page references come from the book's
own index (pp. 741–748) and its column-page headers. The sidelines come from the
footnotes printed under the column tables.

## Three modes

- **Study** — replay any line move by move on the board, with the moves laid out in the
  book's own two-column White/Black table. Each chapter carries a summary and both sides'
  plans; each line carries a note and its MCO page number. Where the book has footnotes to
  a column, they appear as **sidelines**: pick one and the board plays the main line up to
  the branch and then the footnote's analysis, shown in amber in the move table.
- **Train** — play the line yourself on the board. Pick a side and the opponent answers
  automatically. Wrong moves are flagged; hints highlight the piece to move. Finishing a
  line marks it learned.
- **Quiz** — name the opening from a position.

Progress is kept in the browser's `localStorage`, so it survives reloads on the same
browser but is not shared between devices.

## Files

- `index.html` — the whole application (markup, styles and script)
- `openings.js` — the generated opening data, `window.MCO_DATA`
- `data/data_p1.py` … `data_p6.py` — the source for each of the book's six parts
- `data/sublines.json` — sidelines recovered from the book's footnotes
- `data/sanparse.py` — reads OCR'd move text against a live board
- `data/extract_sublines.py` — rebuilds `sublines.json` from the PDF
- `data/validate.py` — replays every line and reports any illegal move
- `data/build.py` — regenerates `openings.js` from the part files and `sublines.json`

To change or add a line, edit the relevant `data/data_pN.py`, then:

```bash
pip install chess
```

```bash
python site/data/validate.py
```

```bash
python site/data/build.py
```

To rebuild the sidelines from the PDF (needs `pypdf`, takes a couple of minutes):

```bash
python site/data/extract_sublines.py kupdf.net_modern-chess-openings-15th-edition_text.pdf
```

## How the data was made

Chapter and variation names, page references and the book's taxonomy were extracted from
the PDF's contents and index. The move sequences are standard main lines for each named
variation, written in SAN and then **verified move by move with `python-chess`** — every
one of the 518 lines was replayed from the starting position and rejected if any move was
illegal. Each position in `openings.js` is a precomputed FEN, so the site needs no chess
engine at runtime and works with no network connection.

The notes and plans are written explanations of each opening's ideas, not quotations from
the book.

### Lines newer than the book

MCO-15 is from 2008, so a few chapters have been brought up to date from current sources.
Those lines carry no page number: the trainer labels them **Modern theory** instead of
`MCO-15, p.N`, and lists them as `new` rather than `p.378`. They also take no part in
footnote matching, so a sideline from the book is never attached to one of them.

So far this covers the **Scandinavian Defense** (chapter II.7), rebuilt around the book's
six actual columns plus 19 researched lines — the 3...Qd6 (Gubinsky-Melts) systems
including Tiviakov's ...c6 set-up, the 3...Qd8 Valencian, the Kotrc-Mieses gambit, the
Kiel and Marshall Retreat, and White's various anti-Scandinavian tries.

### The sidelines

The column tables themselves are beyond recovery — the OCR turns `Nf3` into `МЗ` and
`Nc6` into `Nc8` — but the footnotes printed under them survived, because they are
ordinary prose. `extract_sublines.py` reads those 4,991 footnotes and keeps the 639 it can
place with confidence. Its header explains the method; the two problems it solves are:

- **Reading the moves.** The scan drops spaces (`8 d4Nh5`), so move text is parsed against
  a live board — at each step the parser asks which moves are legal and looks for one of
  them in the text. Single-character "repairs" are deliberately *not* allowed: they turn
  `Nc6` into `Nb6` and manufacture a line that fits the wrong position.
- **Finding the branch point.** A footnote gives a move number but not which column it
  belongs to, so every variation is tried at that move number and the reading that
  replays furthest wins. A match is thrown out if it sits more than a few pages from the
  line, if it merely repeats the line, if the footnote disambiguates a move (`Nbd2`) where
  this position needs none, or if the reading stops while a well-formed move is still
  waiting. It is also thrown out when two *different* positions both replay the moves
  equally well — the same text can be legal from more than one place, and the book means
  only one of them.

What ships per sideline is the move sequence, the game it is credited to and — only where
the book states one in words — a short verdict. The footnote prose and the book's
evaluation symbols are not reproduced; the page reference points at them in the PDF.

The other footnotes branch from column lines this project does not carry. They are left
out rather than guessed at: a sideline attached to the wrong position would teach
something false, which is worse than a gap. Adding a chapter's real columns is what makes
its footnotes land — rebuilding the Scandinavian around MCO's six columns took it from one
sideline to eight.

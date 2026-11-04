# MCO-15 Opening Trainer

A static site for learning chess openings: **548 lines** and **639 sidelines**, each
replayable on a board, drillable move by move, and quizzable.

Everything is in [`site/`](site/) — see [site/README.md](site/README.md) for what's in the
data and how it was built.

## Running it locally

```bash
python -m http.server 8777 --directory site
```

## Deploying

The page in `site/index.html` is written as a Claude Artifact body, so it has no
`<!doctype>` or `<head>` of its own — the Artifact platform supplies those. For a normal
web host it needs wrapping first:

```bash
python site/data/make_standalone.py
```

That writes `site/dist/` (a complete HTML document plus the data file), which is what the
GitHub Pages workflow in `.github/workflows/pages.yml` publishes on every push to `main`.
`site/dist/` is generated, so it is not committed.

To publish it on GitHub Pages:

```bash
gh auth login
```

```bash
gh repo create mco-opening-trainer --source . --public --push
```

Then set **Settings → Pages → Source** to **GitHub Actions**, and the workflow does the
rest. Any other static host works too — point it at `site/dist/`.

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

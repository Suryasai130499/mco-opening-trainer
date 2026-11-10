# -*- coding: utf-8 -*-
"""Generate the whole static site into site/dist/.

    python site/data/make_site.py

One page per opening and one per line, as separate documents with their own
URLs, titles and descriptions:

    /                          the hub - every opening, searchable
    /o/sicilian/               the opening - its lines, plans and progress
    /o/sicilian/najdorf-6-bg5/ the trainer for that one line

Each page fetches only its own data, so a line page downloads about 10 kB
rather than the whole book. The stylesheet and the script are shared by every
page, so they are fetched once and then cached.

Needs nothing but the standard library: site/openings.js is already built (by
data/build.py, which does need python-chess), and this only slices it up.
"""
import io, json, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.normpath(os.path.join(HERE, os.pardir))
WEB = os.path.join(SITE, 'web')
DIST = os.path.join(SITE, 'dist')

FONTS = ('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Spectral:ital,wght@0,500;0,600;1,400&'
         'family=Source+Sans+3:ital,wght@0,400;0,600;1,400&'
         'family=IBM+Plex+Mono:wght@400;600&display=swap">')

FAVICON = ("data:image/svg+xml,"
           "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='6' fill='%231c6a52'/%3E"
           "%3Ctext x='16' y='24' font-size='22' text-anchor='middle' fill='%23f2f4f0'%3E"
           "%E2%99%9E%3C/text%3E%3C/svg%3E")

COLOPHON = (
    '<footer class="foot"><p>Opening names, move orders, game citations and page '
    'references are indexed from <i>Modern Chess Openings, 15th Edition</i> by Nick de '
    'Firmian (Random House Puzzles &amp; Games / David McKay, 2008). Lines marked '
    '<b>Modern theory</b> are not from the book. The explanatory notes and plans here are '
    'written for this site; the book&rsquo;s own commentary and evaluation symbols are not '
    'reproduced. Every move sequence has been machine-verified as legal chess.</p></footer>'
)


def esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;')
            .replace('>', '&gt;').replace('"', '&quot;'))


def side_badge(side, big=False):
    return ('<span class="sidebadge%s"><i class="%s"></i>You play %s</span>'
            % (' lg' if big else '', side, 'White' if side == 'w' else 'Black'))


def page(title, desc, root, body, page_kind, src):
    """A complete HTML document. `root` is the relative path back to the site
    root, so the whole site works just as well under /mco-opening-trainer/ as
    at the top of a domain."""
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<title>' + esc(title) + '</title>\n'
        '<meta name="description" content="' + esc(desc) + '">\n'
        '<meta name="color-scheme" content="light dark">\n'
        '<meta property="og:title" content="' + esc(title) + '">\n'
        '<meta property="og:description" content="' + esc(desc) + '">\n'
        '<meta property="og:type" content="website">\n'
        '<link rel="icon" href="' + FAVICON + '">\n'
        + FONTS + '\n'
        '<link rel="stylesheet" href="' + root + 'assets/app.css">\n'
        '</head>\n'
        '<body data-page="' + page_kind + '" data-root="' + root + '" data-src="' + root + src + '">\n'
        + body +
        '\n<script src="' + root + 'assets/app.js" defer></script>\n'
        '</body>\n</html>\n'
    )


def topbar(root, crumbs):
    out = ['<header class="topbar">',
           '<a class="brand" href="' + root + '"><b>MCO&#8209;15</b><span>Opening Trainer</span></a>']
    if crumbs:
        # each crumb carries its own separator, so hiding the last one on a
        # phone does not leave a dangling slash behind
        out.append('<nav class="crumbs" aria-label="Breadcrumb">')
        last = len(crumbs) - 1
        for i, (label, href) in enumerate(crumbs):
            out.append('<span class="cr%s">' % (' here' if i == last and i else ''))
            inner = ('<a href="%s">%s</a>' % (href, esc(label))) if href else esc(label)
            out.append(inner)
            out.append('</span>')
        out.append('</nav>')
    out.append('<span class="spacer"></span>')
    out.append('<button class="iconbtn" id="themeBtn" aria-label="Switch light or dark theme" '
               'title="Light or dark">◐</button>')
    out.append('</header>')
    return ''.join(out)


def plans_card(ch):
    return ('<section class="card"><h2>What each side is trying to do</h2><div class="plan">'
            '<div><b>White</b><span>' + esc(ch['whitePlan']) + '</span></div>'
            '<div><b>Black</b><span>' + esc(ch['blackPlan']) + '</span></div>'
            '</div></section>')


def pager(prev, nxt, kind):
    if not prev and not nxt:
        return ''
    out = ['<nav class="pager">']
    if prev:
        out.append('<a href="%s"><span>Previous %s</span><b>%s</b></a>'
                   % (prev[1], kind, esc(prev[0])))
    if nxt:
        out.append('<a class="next" id="nextLink" href="%s"><span>Next %s</span><b>%s</b></a>'
                   % (nxt[1], kind, esc(nxt[0])))
    out.append('</nav>')
    return ''.join(out)


def slug_of(vid):
    return vid.split('--', 1)[1]


def thin(plies, keep_lm):
    """Drop what a given page will not read. `lm` is the bulk of the data and
    only the trainer needs it."""
    out = []
    for p in plies:
        q = {'san': p['san'], 'from': p['from'], 'to': p['to'], 'fen': p['fen']}
        if keep_lm:
            q['lm'] = p['lm']
        out.append(q)
    return out


def write(path, text):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(text)


def dump(path, obj):
    write(path, json.dumps(obj, ensure_ascii=False, separators=(',', ':')))


def main():
    raw = io.open(os.path.join(SITE, 'openings.js'), encoding='utf-8').read()
    data = json.loads(raw[raw.index('=') + 1:].rstrip().rstrip(';'))
    meta = data['meta']

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    # ---- flat lists, so every page can link to its neighbours ----
    chapters = []
    for part in data['parts']:
        for ch in part['chapters']:
            ch['part'] = part
            chapters.append(ch)

    n_pages = 0

    # ================= the hub =================
    index = {'meta': meta, 'parts': []}
    for part in data['parts']:
        index['parts'].append({
            'id': part['id'], 'num': part['num'], 'name': part['name'], 'line': part['line'],
            'chapters': [{
                'id': c['id'], 'name': c['name'], 'aka': c.get('aka', ''), 'eco': c['eco'],
                'side': c['side'], 'line': c['line'], 'linePgn': c['linePgn'],
                'n': len(c['variations']),
                'vars': [v['id'] for v in c['variations']],
            } for c in part['chapters']],
        })
    dump(os.path.join(DIST, 'd', 'index.json'), index)

    hub_body = (
        topbar('./', []) +
        '<div class="wrap">'
        '<h1 class="title">Every opening in <i>Modern Chess Openings</i>'
        '<small>' + str(meta['chapters']) + ' openings &middot; ' + str(meta['variations']) +
        ' main lines &middot; ' + str(meta['sublines']) + " sidelines from the book&rsquo;s notes</small></h1>"
        '<p class="lede">Each opening belongs to one side. Open one and you play that '
        'side&rsquo;s moves on the board while the opponent answers by itself &mdash; '
        '<b>' + str(meta['white']) + '</b> of them are White&rsquo;s, <b>' + str(meta['black']) +
        '</b> are Black&rsquo;s. Every line has a page of its own.</p>'
        '<div class="metarow" id="hubProgress"></div>'
        '<div class="searchbar"><input id="search" type="search" autocomplete="off" '
        'placeholder="Search openings, moves, ECO codes, or white / black…" '
        'aria-label="Search openings"></div>'
        '<div id="hubList"><p class="empty">Loading the index…</p></div>'
        '<section class="card" style="margin-top:26px"><h2>Test yourself</h2>'
        '<p>Can you tell them apart on sight? The quiz shows a position from one of the '
        'lines and asks which opening it came from.</p>'
        '<div class="btnrow" style="margin-top:12px">'
        '<a class="btn" href="./quiz/">Name the opening →</a></div></section>' +
        COLOPHON + '</div>'
    )
    write(os.path.join(DIST, 'index.html'), page(
        'MCO-15 Opening Trainer',
        'Learn every opening in Modern Chess Openings, 15th edition: %d openings, %d main lines '
        'and %d sidelines, each with a page of its own.' % (meta['chapters'], meta['variations'],
                                                            meta['sublines']),
        './', hub_body, 'hub', 'd/index.json'))
    n_pages += 1

    # ================= one page per opening =================
    for i, ch in enumerate(chapters):
        part = ch['part']
        cid = ch['id']
        root = '../../'
        n_sub = sum(len(v.get('subs') or []) for v in ch['variations'])
        side_word = 'White' if ch['side'] == 'w' else 'Black'

        dump(os.path.join(DIST, 'd', cid + '.json'), {
            'id': cid, 'name': ch['name'], 'side': ch['side'],
            'linePlies': thin(ch['linePlies'], False),
            'vars': [{
                'id': v['id'], 'slug': slug_of(v['id']), 'name': v['name'],
                'page': v['page'], 'pgn': v['pgn'], 'nsub': len(v.get('subs') or []),
            } for v in ch['variations']],
        })

        prev = (chapters[i-1]['name'], '../' + chapters[i-1]['id'] + '/') if i else None
        nxt = (chapters[i+1]['name'], '../' + chapters[i+1]['id'] + '/') if i + 1 < len(chapters) else None

        tags = ['<span class="tag">' + esc(ch['eco']) + '</span>',
                '<span class="tag">MCO-15, p.' + str(ch['page']) + '</span>',
                '<span class="tag">' + str(len(ch['variations'])) + ' lines</span>']
        if n_sub:
            tags.append('<span class="tag mark">+' + str(n_sub) + ' sidelines</span>')

        body = (
            topbar(root, [('All openings', root), (ch['name'], None)]) +
            '<div class="wrap">'
            '<p class="eyebrow">Part ' + esc(part['num']) + ' &middot; ' + esc(part['name']) +
            ' &middot; Chapter ' + str(ch['num']) + '</p>'
            '<h1 class="title">' + esc(ch['name']) +
            ('<small>' + esc(ch['linePgn'] or 'from the first move') + '</small>') + '</h1>'
            '<div class="metarow">' + side_badge(ch['side'], True) + ''.join(tags) +
            ('<span class="tag">also the ' + esc(ch['aka']) + '</span>' if ch.get('aka') else '') +
            '</div>'
            '<p class="lede">' + esc(ch['summary']) + '</p>'
            '<div class="cols">'
            '<div class="boardwrap"><div id="boardSlot"></div>'
            '<p class="plycount" id="boardCaption" style="margin-top:10px"></p></div>'
            '<div>'
            '<section class="card"><h2>Your progress in this opening</h2>'
            '<div class="metarow" id="chProgress"></div>'
            '<div class="btnrow"><a class="btn primary big" id="startBtn" href="./">'
            'Start training →</a></div>'
            '<p class="note" style="margin-top:11px">You play ' + side_word +
            ' in every line here; the other side answers by itself.</p></section>' +
            plans_card(ch) +
            '<section class="card"><h2>The lines in this chapter</h2>'
            '<div class="vlist" id="lineList"><p class="empty">Loading…</p></div></section>'
            '</div></div>' +
            pager(prev, nxt, 'opening') + COLOPHON + '</div>'
        )
        write(os.path.join(DIST, 'o', cid, 'index.html'), page(
            ch['name'] + ' — MCO-15 Opening Trainer',
            '%s (%s): %d main lines from Modern Chess Openings, trained as %s with the replies '
            'played for you.' % (ch['name'], ch['eco'], len(ch['variations']), side_word),
            root, body, 'opening', 'd/' + cid + '.json'))
        n_pages += 1

        # ================= one page per line =================
        vs = ch['variations']
        for j, v in enumerate(vs):
            slug = slug_of(v['id'])
            root = '../../../'
            subs = v.get('subs') or []

            dump(os.path.join(DIST, 'd', cid, slug + '.json'), {
                'ch': {'id': cid, 'name': ch['name'], 'side': ch['side']},
                'v': {
                    'id': v['id'], 'slug': slug, 'name': v['name'], 'page': v['page'],
                    'pgn': v['pgn'], 'plies': thin(v['plies'], True),
                    'subs': [{
                        'id': s['id'], 'fromPly': s['fromPly'], 'page': s['page'],
                        'key': s['key'], 'cite': s['cite'], 'pgn': s['pgn'],
                        'plies': thin(s['plies'], True),
                    } for s in subs],
                },
            })

            prev = (vs[j-1]['name'], '../' + slug_of(vs[j-1]['id']) + '/') if j else None
            nxt = (vs[j+1]['name'], '../' + slug_of(vs[j+1]['id']) + '/') if j + 1 < len(vs) else None

            vtags = ['<span class="tag">' + ('MCO-15, p.' + str(v['page']) if v['page']
                                             else 'Modern theory') + '</span>',
                     '<span class="tag">' + str(len(v['plies'])) + ' moves</span>']
            if subs:
                vtags.append('<span class="tag mark">+' + str(len(subs)) + ' sideline' +
                             ('s' if len(subs) != 1 else '') + '</span>')

            sub_card = ''
            if subs:
                sub_card = ('<section class="card"><h2>Sidelines from the book&rsquo;s notes</h2>'
                            '<p class="note" style="margin-bottom:11px">Pick one to drill it '
                            'instead: the line follows the column to the branch, then goes its '
                            'own way.</p><div id="subList"></div></section>')

            body = (
                topbar(root, [('All openings', root), (ch['name'], '../'), (v['name'], None)]) +
                '<div class="wrap">'
                '<p class="eyebrow">' + esc(ch['name']) + ' &middot; line ' + str(j + 1) +
                ' of ' + str(len(vs)) + '</p>'
                '<h1 class="title">' + esc(v['name']) + '<small>' + esc(v['pgn']) + '</small></h1>'
                '<div class="metarow">' + side_badge(ch['side'], True) + ''.join(vtags) + '</div>'
                '<div class="cols">'
                '<div class="boardwrap"><div id="boardSlot"></div>'
                '<div class="controls">'
                '<button class="iconbtn" id="flipBtn" aria-label="Flip the board" '
                'title="Flip the board (F)">⇅</button>'
                '<button class="btn" id="watchBtn" title="Play the line through (W)">Watch</button>'
                '<button class="btn" id="restartBtn" title="Start again (R)">Restart</button>'
                '<span class="plycount" id="plyCount"></span>'
                '<span class="tomove" id="toMove"></span>'
                '</div></div>'
                '<div id="panel">'
                '<section class="card"><h2>About this line</h2>'
                '<p class="note">' + esc(v['note']) + '</p>'
                '<div class="btnrow" style="margin-top:12px">'
                '<button class="btn" id="modeBtn">Mode</button>'
                '<span class="plycount"><span class="kbd">H</span> hint &middot; '
                '<span class="kbd">S</span> show &middot; <span class="kbd">W</span> watch '
                '&middot; <span class="kbd">F</span> flip &middot; '
                '<span class="kbd">R</span> restart</span>'
                '</div></section>'
                '<section class="card"><h2>The line</h2>'
                '<table class="movetable" id="moveTable"></table></section>' +
                sub_card + plans_card(ch) +
                '</div></div>' +
                pager(prev, nxt, 'line') + COLOPHON + '</div>'
            )
            write(os.path.join(DIST, 'o', cid, slug, 'index.html'), page(
                v['name'] + ' — ' + ch['name'],
                '%s in the %s: %s. Play it as %s move by move, with the replies played for you.'
                % (v['name'], ch['name'], v['pgn'], side_word),
                root, body, 'line', 'd/' + cid + '/' + slug + '.json'))
            n_pages += 1

    # ================= the quiz =================
    # One position per line, deep enough to have a character of its own, with
    # the opening it came from. Small enough (a few tens of kB) to be one file.
    quiz = {'chapters': [{'id': c['id'], 'name': c['name'], 'side': c['side']} for c in chapters],
            'items': []}
    for ci, ch in enumerate(chapters):
        for v in ch['variations']:
            n = min(10, len(v['plies']))
            if n < 6:
                continue                       # too early to be recognisable
            quiz['items'].append({
                'c': ci,
                'fen': v['plies'][n-1]['fen'],
                'pgn': ' '.join(v['pgn'].split()[:n]),
                'url': 'o/' + ch['id'] + '/' + slug_of(v['id']) + '/',
                'name': v['name'],
            })
    dump(os.path.join(DIST, 'd', 'quiz.json'), quiz)

    quiz_body = (
        topbar('../', [('All openings', '../'), ('Quiz', None)]) +
        '<div class="wrap narrow">'
        '<p class="eyebrow">Quiz</p>'
        '<h1 class="title">Name the opening<small>' + str(len(quiz['items'])) +
        ' positions, drawn from every chapter of the book</small></h1>'
        '<div class="cols">'
        '<div class="boardwrap"><div id="boardSlot"></div>'
        '<p class="plycount" id="quizMoves" style="margin-top:10px"></p></div>'
        '<div id="panel"></div>'
        '</div>' + COLOPHON + '</div>'
    )
    write(os.path.join(DIST, 'quiz', 'index.html'), page(
        'Name the opening — MCO-15 Opening Trainer',
        'Guess which opening a position came from, drawn from all %d chapters of Modern '
        'Chess Openings.' % meta['chapters'],
        '../', quiz_body, 'quiz', 'd/quiz.json'))
    n_pages += 1

    # ---- shared assets ----
    os.makedirs(os.path.join(DIST, 'assets'))
    for f in ('app.css', 'app.js'):
        shutil.copyfile(os.path.join(WEB, f), os.path.join(DIST, 'assets', f))
    shutil.copytree(os.path.join(SITE, 'pieces'), os.path.join(DIST, 'pieces'))
    write(os.path.join(DIST, '.nojekyll'), '')

    total = sum(os.path.getsize(os.path.join(r, f))
                for r, _, fs in os.walk(DIST) for f in fs)
    print('wrote %s' % DIST)
    print('  %d pages (hub + quiz + %d openings + %d lines)'
          % (n_pages, meta['chapters'], meta['variations']))
    print('  %.1f MB on disk' % (total / 1024.0 / 1024.0))


if __name__ == '__main__':
    main()

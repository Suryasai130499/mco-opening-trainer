# -*- coding: utf-8 -*-
"""Wrap the artifact body in a real HTML document for hosting on a plain web server.

    python site/data/make_standalone.py

site/index.html is written to be published as a Claude Artifact, where the
platform wraps it in a document skeleton (doctype, charset and viewport metas,
a small reset). Served raw by a normal web host there is no skeleton, so the
browser falls into quirks mode and the layout breaks. This writes site/dist/,
which is the same page inside the document it expects.
"""
import io, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.normpath(os.path.join(HERE, os.pardir))
DIST = os.path.join(SITE, 'dist')

DESCRIPTION = ("Learn every opening in Modern Chess Openings, 15th edition: 548 lines and "
               "639 sidelines to replay, drill and quiz yourself on.")

# A chess knight, so the tab has an icon without an extra request.
FAVICON = ("data:image/svg+xml,"
           "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='6' fill='%231c6a52'/%3E"
           "%3Ctext x='16' y='24' font-size='22' text-anchor='middle' fill='%23f2f4f0'%3E"
           "%E2%99%9E%3C/text%3E%3C/svg%3E")

# What the Artifact platform puts in the document for us, reproduced here.
SKELETON_RESET = """
    :root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);
      padding-bottom:env(safe-area-inset-bottom,0px)}
    body{margin:0;font:14px system-ui,-apple-system,sans-serif}
    img{max-width:100%}
    [hidden]{display:none!important}
"""


def main():
    body = io.open(os.path.join(SITE, 'index.html'), encoding='utf-8').read()

    m = re.search(r'<title>(.*?)</title>', body, re.S)
    title = m.group(1).strip() if m else 'MCO-15 Opening Trainer'
    # the document head carries these now, so drop them from the body
    body = re.sub(r'<title>.*?</title>\s*', '', body, count=1, flags=re.S)
    body = re.sub(r'<meta charset=["\']utf-8["\']>\s*', '', body, count=1, flags=re.I)
    body = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\s*', '', body, count=1)

    doc = (
        '<!doctype html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<title>' + title + '</title>\n'
        '<meta name="description" content="' + DESCRIPTION + '">\n'
        '<meta name="color-scheme" content="light dark">\n'
        '<meta property="og:title" content="' + title + '">\n'
        '<meta property="og:description" content="' + DESCRIPTION + '">\n'
        '<meta property="og:type" content="website">\n'
        '<link rel="icon" href="' + FAVICON + '">\n'
        '<style>' + SKELETON_RESET + '</style>\n'
        '</head>\n'
        '<body>\n'
        + body.strip() + '\n'
        '</body>\n'
        '</html>\n'
    )

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    io.open(os.path.join(DIST, 'index.html'), 'w', encoding='utf-8', newline='\n').write(doc)
    shutil.copyfile(os.path.join(SITE, 'openings.js'), os.path.join(DIST, 'openings.js'))
    # tell GitHub Pages to serve the files as they are
    io.open(os.path.join(DIST, '.nojekyll'), 'w', encoding='utf-8').write('')

    print("wrote %s" % DIST)
    for f in sorted(os.listdir(DIST)):
        print("  %-14s %d bytes" % (f, os.path.getsize(os.path.join(DIST, f))))


if __name__ == '__main__':
    main()

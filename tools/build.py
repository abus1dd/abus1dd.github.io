"""Build index.html for GitHub Pages from src/desk.html.

Run from the repo root:  python tools/build.py
Needs Python 3 and Node.js (uses `npx terser` to minify the script).

What it does:
  1. Wraps src/desk.html in a full HTML document (doctype, <head>, meta tags).
  2. Swaps the cdnjs GSAP scripts for the self-hosted copies in assets/js/.
  3. Moves the embedded dragon image to assets/dragon-hologram.webp (lazy-loaded).
  4. Minifies the main inline script with terser.
  5. Computes the SHA-256 hash of the inline script and writes the Content Security Policy.
Always edit src/desk.html, then rebuild: editing index.html by hand breaks the CSP hash.
"""
import base64, hashlib, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src', 'desk.html')
OUT = os.path.join(ROOT, 'index.html')

s = open(SRC, encoding='utf-8').read()
k = s.index('</style>') + len('</style>')
head = s[:k].replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
body = s[k:]

body = body.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>', '<script src="assets/js/gsap.min.js"></script>')
body = body.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>', '<script src="assets/js/ScrollTrigger.min.js"></script>')
if 'cdnjs' in body:
    sys.exit('A cdnjs script is still referenced: update tools/build.py')

m = re.search(r'src="data:image/webp;base64,([^"]+)"', body)
if m:
    with open(os.path.join(ROOT, 'assets', 'dragon-hologram.webp'), 'wb') as f:
        f.write(base64.b64decode(m.group(1)))
    body = body.replace(m.group(0), 'src="assets/dragon-hologram.webp" loading="lazy"')

npx = shutil.which('npx') or shutil.which('npx.cmd')
def mini(mt):
    src = mt.group(1)
    if len(src) < 2000 or not npx:
        return mt.group(0)
    out = subprocess.run([npx, '--yes', 'terser@5', '--compress', 'passes=2', '--mangle', '--ecma', '2020'],
                         input=src.encode('utf-8'), capture_output=True, check=True).stdout.decode('utf-8')
    return '<script>' + out + '</script>'
if not npx:
    print('npx not found: the script is left unminified (still works).')
body = re.sub(r'<script>(.*?)</script>', mini, body, flags=re.S)

hashes = ["'sha256-" + base64.b64encode(hashlib.sha256(m.group(1).encode('utf-8')).digest()).decode() + "'"
          for m in re.finditer(r'<script>(.*?)</script>', body, re.S)]
csp = ("default-src 'self'; "
       "script-src 'self' " + ' '.join(hashes) + " https://gc.zgo.at; "
       "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
       "font-src https://fonts.gstatic.com; "
       "img-src 'self' data: https://images.credly.com https://abus1dd.goatcounter.com; "
       "media-src 'self'; "
       "connect-src 'self' https://abu-assistant.abus1dd.workers.dev https://abus1dd.goatcounter.com; "
       "object-src 'none'; base-uri 'self'; form-action 'none'; upgrade-insecure-requests")

out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       '<meta http-equiv="Content-Security-Policy" content="' + csp + '">\n'
       '<meta name="referrer" content="strict-origin-when-cross-origin">\n'
       + head +
       '\n<script data-goatcounter="https://abus1dd.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>\n'
       '</head>\n<body>' + body + '\n</body>\n</html>\n')
with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
    f.write(out)
print('index.html written:', len(out.encode('utf-8')), 'bytes,', len(hashes), 'inline script(s) hashed')

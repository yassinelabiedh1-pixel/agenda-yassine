"""Builds index.html (the page GitHub Pages serves) from src/page.html.

src/page.html is the page body, the same file published as the Claude artifact.
This adds the <head> that turns it into an iPhone / Android home-screen app.
Run:  python build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

HEAD = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Agenda de Yassine : services Madeleine, cours et Kilua, ton assistant vocal.">
<meta name="theme-color" content="#F6F7FB" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#10121C" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Agenda">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
<style>
html,body{margin:0}
/* home-screen app: the page runs under the iPhone status bar, so keep content below it */
body{padding-top:env(safe-area-inset-top,0px)}
body::before{content:"";position:fixed;top:0;left:0;right:0;height:env(safe-area-inset-top,0px);background:var(--bg);z-index:60}
</style>
"""

TAIL = """
<script>
if ('serviceWorker' in navigator && location.protocol === 'https:') {
  window.addEventListener('load', function(){ navigator.serviceWorker.register('./sw.js').catch(function(){}); });
}
</script>
</html>
"""

page = (ROOT / "src" / "page.html").read_text(encoding="utf-8")
with open(ROOT / "index.html", "w", encoding="utf-8", newline="\n") as f:
    f.write(HEAD + page + TAIL)
print("index.html built")

"""Build static, translated pages with no runtime framework dependencies."""
from pathlib import Path
from html import escape
import json
ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / 'content.json').read_text())
LANGS = {'en': 'English', 'fr': 'Français', 'vi': 'Tiếng Việt'}
PAGES = {'index': 'home', 'guide': 'guide', 'privacy': 'privacy', 'terms': 'terms', 'support': 'support'}

def build():
    for page, key in PAGES.items():
        tabs = '\n'.join(f'<a id="tab-{lang}" role="tab" aria-controls="panel-{lang}" aria-selected="{str(lang == "en").lower()}" tabindex="{0 if lang == "en" else -1}" href="?lang={lang}" lang="{lang}">{name}</a>' for lang, name in LANGS.items())
        panels = []
        for lang, name in LANGS.items():
            data = DATA[lang]
            content = data['pages'][key]
            nav = ''.join(f'<a href="{p}.html?lang={lang}"'+(' aria-current="page"' if p == page else '')+f'>{escape(data["nav"][k])}</a>' for p,k in PAGES.items())
            body = ''.join(f'<section class="content-section"><h2>{escape(s[0])}</h2>{s[1]}</section>' for s in content['sections'])
            panels.append(f'''<section class="language-panel" id="panel-{lang}" role="tabpanel" aria-labelledby="tab-{lang}" lang="{lang}" data-title="{escape(content['title'])} — MPrint"{'' if lang == 'en' else ' hidden'}>
<nav aria-label="{escape(data['navigation'])}">{nav}</nav>
<header><p class="eyebrow">MPrint</p><h1>{escape(content['title'])}</h1>{content['intro']}</header>
{body}
<footer><p>{escape(data['updated'])}: <time datetime="2026-10-16">2026-10-16</time></p><p>© Vu Khac Muoi · <a href="mailto:apps.dreamingscientist@gmail.com">apps.dreamingscientist@gmail.com</a></p></footer>
</section>''')
        html = f'''<!doctype html>
<html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="MPrint help, privacy and terms in English, French and Vietnamese.">
<title>{escape(DATA['en']['pages'][key]['title'])} — MPrint</title>
<link rel="stylesheet" href="style.css"><script src="language.js" defer></script></head>
<body><main>
<div class="language-tabs" role="tablist" aria-label="Language / Langue / Ngôn ngữ">{tabs}</div>
{''.join(panels)}
</main></body></html>\n'''
        (ROOT / f'{page}.html').write_text(html)

if __name__ == '__main__': build()

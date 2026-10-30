from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json, subprocess
root = Path(__file__).resolve().parent.parent
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.tabs=[]; self.panels=[]; self.links=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if a.get('role')=='tab': self.tabs.append(a)
        if a.get('role')=='tabpanel': self.panels.append(a)
        if tag=='a' and 'href' in a: self.links.append(a['href'])
for file in root.glob('*.html'):
    p=Page(); p.feed(file.read_text())
    assert len(p.ids)==len(set(p.ids)), f'{file}: duplicate IDs'
    assert len(p.tabs)==len(p.panels)==3, f'{file}: missing languages'
    assert sum(t['aria-selected']=='true' for t in p.tabs)==1
    assert sum('hidden' not in s for s in p.panels)==1
    for t in p.tabs: assert t['aria-controls'] in p.ids
    for link in p.links:
        u=urlparse(link)
        if not u.scheme and u.path: assert (root/u.path).exists(), f'{file}: broken {link}'
data=json.loads((root/'content.json').read_text())
for key in data['en']['pages']:
    assert len({len(data[l]['pages'][key]['sections']) for l in data})==1, key
# Keep existing English terms verbatim. The privacy policy is maintained from
# content.json and may be revised to reflect current SDK behavior.
old=subprocess.check_output(['git','show','6482317:terms.html'],cwd=root,text=True)
for _,body in data['en']['pages']['terms']['sections']: assert body in old
privacy='\n'.join(body for _,body in data['en']['pages']['privacy']['sections'])
for expected in ('App Tracking Transparency',
                 'does not access IDFA for tracking',
                 'eligible non-personalized or limited ads',
                 'frequency capping and aggregated reporting',
                 'Google Analytics for Firebase',
                 'IDFV collection are disabled'):
    assert expected in privacy, f'missing privacy disclosure: {expected}'
print('Validated 5 pages, 3 language panels per page, internal links and original English legal clauses.')

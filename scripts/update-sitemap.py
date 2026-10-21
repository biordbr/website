"""Gera sitemap.xml a partir das páginas canônicas e seus hreflang.
Uso: python3 scripts/update-sitemap.py
Não inclui redirecionamentos, aliases nem o WordPress externo ao projeto.
Preserva lastmod já registrado; páginas novas entram sem data inventada.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://biord.com.br'
NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'
XHTML = 'http://www.w3.org/1999/xhtml'
ET.register_namespace('', NS)
ET.register_namespace('xhtml', XHTML)

class Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonical = None
        self.alternates = []
        self.noindex = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs['href']
        if tag == 'link' and attrs.get('rel') == 'alternate' and attrs.get('hreflang'):
            self.alternates.append((attrs['hreflang'], attrs['href']))
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.noindex = 'noindex' in attrs.get('content', '')

previous = {}
if (ROOT / 'sitemap.xml').exists():
    for item in ET.parse(ROOT / 'sitemap.xml').getroot().findall(f'{{{NS}}}url'):
        loc = item.findtext(f'{{{NS}}}loc')
        modified = item.findtext(f'{{{NS}}}lastmod')
        if modified:
            previous[loc] = modified

pages = {}
aliases = []
for language in ('pt', 'en', 'es'):
    for path in sorted((ROOT / language).rglob('index.html')):
        head = Head()
        head.feed(path.read_text())
        url = BASE + '/' + path.parent.relative_to(ROOT).as_posix() + '/'
        if head.noindex or head.canonical != url:
            aliases.append(url)
            continue
        if url in pages:
            raise ValueError(f'URL duplicada: {url}')
        pages[url] = head

root = ET.Element(f'{{{NS}}}urlset')
for url, head in pages.items():
    item = ET.SubElement(root, f'{{{NS}}}url')
    ET.SubElement(item, f'{{{NS}}}loc').text = url
    if url in previous:
        ET.SubElement(item, f'{{{NS}}}lastmod').text = previous[url]
    for language, alternate in head.alternates:
        if alternate not in pages:
            raise ValueError(f'Alternate sem página canônica local: {alternate}')
        target = ROOT / urlsplit(alternate).path.lstrip('/') / 'index.html'
        if not target.is_file():
            raise ValueError(f'Página ausente: {target}')
        ET.SubElement(item, f'{{{XHTML}}}link', rel='alternate',
                      hreflang=language, href=alternate)
ET.indent(root, space='  ')
ET.ElementTree(root).write(ROOT / 'sitemap.xml', encoding='UTF-8', xml_declaration=True)
print(f'{len(pages)} páginas canônicas no sitemap; {len(aliases)} alias excluído.')

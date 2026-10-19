"""Fetch unchanged Servier originals and retain their provenance locally."""
from pathlib import Path
from urllib.request import urlopen
from html.parser import HTMLParser
from io import BytesIO
from PIL import Image
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public' / 'art' / 'atlas'
SOURCES = {
    'erythrocyte': 'smart-erythrocyte',
    'kidney': 'smart-kidney',
    'stem-cell': 'hematopoietic-stem-cell',
    'specimen': 'smart-tube',
    'neutrophil': 'neutrophil-granulocyte',
    'platelet': 'smart-platelet',
}

class DownloadLink(HTMLParser):
    def __init__(self):
        super().__init__(); self.href = ''; self.download = ''; self.kit = ''
    def handle_starttag(self, tag, attrs):
        if tag == 'a': self.href = dict(attrs).get('href', '')
    def handle_data(self, data):
        if data.strip() == 'Download the image': self.download = self.href
        if data.strip() == 'Download the entire set': self.kit = self.href

OUT.mkdir(parents=True, exist_ok=True)
records = []
for name, slug in SOURCES.items():
    page = f'https://smart.servier.com/smart_image/{slug}/'
    parser = DownloadLink(); parser.feed(urlopen(page).read().decode())
    if not parser.download.startswith('https://smart.servier.com/'): raise ValueError(page)
    raw = urlopen(parser.download).read()
    im = Image.open(BytesIO(raw)); assert im.format == 'PNG'
    (OUT / f'{name}.png').write_bytes(raw)
    records.append(dict(id=name, file=f'/art/atlas/{name}.png', source=page,
        download=parser.download, illustrationSet=parser.kit, creator='Servier Medical Art', license='CC BY 4.0',
        licenseUrl='https://creativecommons.org/licenses/by/4.0/',
        credit='Illustrations from Servier Medical Art, licensed under CC BY 4.0.',
        modifications='Original PNG unchanged. Scaled, positioned, rotated, and animated in the presentation.',
        width=im.width, height=im.height, sha256=hashlib.sha256(raw).hexdigest()))
    print(name, im.size, len(raw))
    kit_path = ROOT / 'reference' / 'servier-kits' / parser.kit.rsplit('/', 1)[-1]
    kit_path.parent.mkdir(parents=True, exist_ok=True)
    if not kit_path.exists(): kit_path.write_bytes(urlopen(parser.kit).read())
(OUT / 'sources.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

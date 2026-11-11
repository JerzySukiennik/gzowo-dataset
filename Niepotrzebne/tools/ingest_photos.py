#!/usr/bin/env python3
"""Gzowo Dataset: copy and downsize source photos and brand assets into media/, write Niepotrzebne/src/ingest_photos.json."""
import json, os, re, shutil, subprocess, sys, unicodedata, zipfile
from PIL import Image, ImageOps

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MEDIA = os.path.join(ROOT, 'media')
PROJ = '/Users/jurek/Downloads/Claude/Projects'
GAL = '/Users/jurek/Gzowo_Gallery'
DUMP = '/Users/jurek/Downloads/Claude/Gzowo_Dataset'
SCRATCH = sys.argv[1]
MAXPX = 1600


def slug(s):
    s = s.replace('ł', 'l').replace('Ł', 'L')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:48]


def save_photo(src, rel):
    dst = os.path.join(MEDIA, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    im.thumbnail((MAXPX, MAXPX), Image.LANCZOS)
    im.save(dst, 'JPEG', quality=82, optimize=True, progressive=True)
    return {'file': 'media/' + rel, 'w': im.width, 'h': im.height, 'bytes': os.path.getsize(dst)}


def created(path):
    try:
        out = subprocess.run(['mdls', '-raw', '-name', 'kMDItemContentCreationDate', path], capture_output=True, text=True).stdout.strip()
        return out[:10] if re.match(r'\d{4}-\d{2}-\d{2}', out) else ''
    except Exception:
        return ''


def copytree(src, rel, exts=None):
    out = []
    for base, _, files in os.walk(src):
        for f in sorted(files):
            if f.startswith('.'):
                continue
            if exts and not f.lower().endswith(exts):
                continue
            s = os.path.join(base, f)
            r = os.path.join(rel, os.path.relpath(s, src))
            d = os.path.join(MEDIA, r)
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copy2(s, d)
            out.append({'file': 'media/' + r, 'bytes': os.path.getsize(d)})
    return out


result = {'gallery': [], 'beach': [], 'rockets': [], 'brand': {}, 'characters': [], 'geo': [], 'map': []}

raw = open(os.path.join(GAL, 'config.js'), encoding='utf-8').read()
cfg = json.loads(raw[raw.index('{'):raw.rindex('}') + 1])
manifest = json.load(open(os.path.join(GAL, 'manifest.json'), encoding='utf-8'))
seen = {}
for room in manifest['rooms']:
    for img in room['images']:
        stem = os.path.splitext(os.path.basename(img['file']))[0]
        meta = cfg['images'].get(img['file'], {})
        if stem in seen:
            seen[stem]['rooms'].append(room['slug'])
            continue
        clean = re.sub(r'[^A-Za-z0-9_-]', '', stem)
        name = clean + ('_' + slug(meta.get('title', '')) if meta.get('title') else '') + '.jpg'
        rec = save_photo(os.path.join(GAL, img['file']), 'photos/galeria/' + name)
        rec.update({'id': 'galeria/' + clean, 'source_name': stem, 'rooms': [room['slug']], 'title': meta.get('title', ''), 'caption': meta.get('desc', ''), 'who': meta.get('who', ''), 'where': meta.get('where', '')})
        m = re.match(r'IMG-(\d{4})(\d{2})(\d{2})-WA', stem)
        rec['date'] = f'{m.group(1)}-{m.group(2)}-{m.group(3)}' if m else ''
        seen[stem] = rec
        result['gallery'].append(rec)
result['gallery_rooms'] = {k: v for k, v in cfg['rooms'].items()}
result['gallery_dedication'] = cfg['dedication']

beach = os.path.join(PROJ, 'plaża w gzowie', 'photos')
for f in sorted(os.listdir(beach)):
    if f.lower().endswith(('.jpeg', '.jpg')):
        stem = os.path.splitext(f)[0]
        rec = save_photo(os.path.join(beach, f), f'photos/plaza/{stem}.jpg')
        rec.update({'id': 'plaza/' + stem, 'source_name': stem, 'date': created(os.path.join(beach, f))})
        result['beach'].append(rec)

zdir = os.path.join(SCRATCH, 'rakietomania')
os.makedirs(zdir, exist_ok=True)
z = zipfile.ZipFile(os.path.join(DUMP, [f for f in os.listdir(DUMP) if f.endswith('.zip')][0]))
gallery_stems = set(seen)
for info in z.infolist():
    base = os.path.basename(info.filename)
    if not base:
        continue
    target = os.path.join(zdir, base)
    with z.open(info) as s, open(target, 'wb') as d:
        shutil.copyfileobj(s, d)
    stem = os.path.splitext(base)[0]
    m = re.match(r'(IMG|VID)-(\d{4})(\d{2})(\d{2})-WA', stem)
    date = f'{m.group(2)}-{m.group(3)}-{m.group(4)}' if m else ''
    if base.lower().endswith('.jpg'):
        if stem in gallery_stems:
            continue
        clean = re.sub(r'[^A-Za-z0-9_-]', '', stem)
        rec = save_photo(target, f'photos/rakiety/{clean}.jpg')
        rec.update({'id': 'rakiety/' + clean, 'source_name': stem, 'date': date})
        result['rockets'].append(rec)

LABS = os.path.join(PROJ, 'gzowo-labs')
kit = os.path.join(LABS, 'logo', 'kit')
brand = []
for sub in ('svg', 'png', 'favicon', 'naklejki', 'awatar'):
    brand += copytree(os.path.join(kit, sub), f'brand/gzowo-labs/{sub}')
brand += copytree(os.path.join(kit, 'filmy'), 'brand/gzowo-labs/filmy')
for f in ('gzowo-labs-fire.gif', 'og.png', 'favicon.svg'):
    d = os.path.join(MEDIA, 'brand/gzowo-labs/strona', f)
    os.makedirs(os.path.dirname(d), exist_ok=True)
    shutil.copy2(os.path.join(LABS, 'site', 'assets', f), d)
    brand.append({'file': 'media/brand/gzowo-labs/strona/' + f, 'bytes': os.path.getsize(d)})
result['brand']['gzowo-labs'] = brand

gsp = []
d = os.path.join(MEDIA, 'brand/gsp/gsp-logo.png')
os.makedirs(os.path.dirname(d), exist_ok=True)
shutil.copy2(os.path.join(GAL, 'Images', 'Logo:s', 'Aerospace - GSP Logo.png'), d)
gsp.append({'file': 'media/brand/gsp/gsp-logo.png', 'bytes': os.path.getsize(d)})
for sub in ('gif', 'outro', 'pfp'):
    gsp += copytree(os.path.join(PROJ, 'gsp-brand-kit', 'ASSETS', sub), f'brand/gsp/{sub}')
result['brand']['gsp'] = gsp

result['map'] = copytree(os.path.join(LABS, 'site', 'assets', 'map'), 'mapa-pikselowa', ('.webp', '.png'))
ap = os.path.join(PROJ, 'Apogee/Sources/Apogee/Resources/Web/assets/gzowo-map.webp')
if os.path.exists(ap):
    d = os.path.join(MEDIA, 'mapa-pikselowa/_cala-mapa.webp')
    shutil.copy2(ap, d)
    result['map'].append({'file': 'media/mapa-pikselowa/_cala-mapa.webp', 'bytes': os.path.getsize(d)})

rend = os.path.join(PROJ, 'Osrodek-Daje/Niepotrzebne/blender/renders')
for f, name in (('portrait-ks.png', 'portrait-tata.png'), ('portrait-jurek.png', 'portrait-jurek.png'), ('portrait-rys.png', 'portrait-rys.png'), ('portrait-dropsik.png', 'portrait-dropsik.png'), ('characters-front.png', 'characters-front.png'), ('ks-closeup.png', 'tata-closeup.png')):
    s = os.path.join(rend, f)
    if os.path.exists(s):
        d = os.path.join(MEDIA, 'postacie/osrodek-daje', name)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copy2(s, d)
        result['characters'].append({'file': 'media/postacie/osrodek-daje/' + name, 'bytes': os.path.getsize(d)})
s = os.path.join(PROJ, 'Narew-Mascot/renders/narek_hero.png')
if os.path.exists(s):
    d = os.path.join(MEDIA, 'postacie/narek/narek_hero.png')
    os.makedirs(os.path.dirname(d), exist_ok=True)
    shutil.copy2(s, d)
    result['characters'].append({'file': 'media/postacie/narek/narek_hero.png', 'bytes': os.path.getsize(d)})

Image.MAX_IMAGE_PIXELS = None
MD = os.path.join(PROJ, 'Gzowo Meadow/data')
for src, name, px in (('orto_world.png', 'ortofoto-1km.jpg', 2000), ('preview_relief.png', 'rzezba-terenu-1km.jpg', 1400), ('preview_layers.png', 'pokrycie-terenu-1km.jpg', 1400), ('orto_20km.jpg', 'ortofoto-okolica-20km.jpg', 1600)):
    s = os.path.join(MD, src)
    if os.path.exists(s):
        im = Image.open(s).convert('RGB')
        im.thumbnail((px, px), Image.LANCZOS)
        d = os.path.join(MEDIA, 'geo', name)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        im.save(d, 'JPEG', quality=84, optimize=True)
        result['geo'].append({'file': 'media/geo/' + name, 'w': im.width, 'h': im.height, 'bytes': os.path.getsize(d)})
s = os.path.join(PROJ, 'Gzowo 34/Niepotrzebne/crop_ortho.png')
if os.path.exists(s):
    im = Image.open(s).convert('RGB')
    d = os.path.join(MEDIA, 'geo/ortofoto-dzialka-zblizenie.jpg')
    im.save(d, 'JPEG', quality=88)
    result['geo'].append({'file': 'media/geo/ortofoto-dzialka-zblizenie.jpg', 'w': im.width, 'h': im.height, 'bytes': os.path.getsize(d)})

json.dump(result, open(os.path.join(ROOT, 'Niepotrzebne/src/ingest_photos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(os.path.getsize(os.path.join(b, f)) for b, _, fs in os.walk(MEDIA) for f in fs)
print({k: (len(v) if isinstance(v, list) else {a: len(b) for a, b in v.items()} if k == 'brand' else '-') for k, v in result.items()}, 'total MB', round(tot / 1e6, 1))

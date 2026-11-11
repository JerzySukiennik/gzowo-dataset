#!/usr/bin/env python3
"""Gzowo Dataset: pull media described by Jurek in the describe tool (Niepotrzebne/src/opisy.json) into media/ and write Niepotrzebne/src/ingest_opisy.json."""
import json, math, os, re, subprocess, unicodedata
from PIL import Image, ImageOps

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(ROOT, 'Niepotrzebne', 'src')
MEDIA = os.path.join(ROOT, 'media')
HOME = (52.612806, 21.116)
PEOPLE = {'jurek': 'jurek', 'rysio': 'rysio', 'tata': 'jan', 'zofia': 'zofia', 'waldek': 'waldek', 'bożena': 'bozena', 'szamborski': 'szamborski', 'major': 'major', 'paweł': 'pawel', 'wójt': 'wojt', 'benny': 'benny', 'janek kunstler': 'janek-kunstler', 'czupryńscy': 'czuprynscy', 'bartek': 'ciszewscy', 'ola „clu”': 'ciszewscy', 'ignacy': 'ciszewscy', 'helena': 'ciszewscy'}
FIXES = {'jak działka była wasza': 'jak działka była Sukienników', '(chyba tata)': '(tata)'}


def slug(s):
    s = s.replace('ł', 'l').replace('Ł', 'L')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:48]


def run(cmd):
    return subprocess.run(['nice', '-n', '10'] + cmd, capture_output=True, text=True)


def near(lat, lon):
    d = math.hypot((lat - HOME[0]) * 111.2, (lon - HOME[1]) * 111.2 * math.cos(math.radians(HOME[0])))
    return 'Gzowo 34' if d < 0.4 else 'okolice Gzowa' if d < 3 else f'{d:.0f} km od Gzowa'


def gps(path, kind):
    try:
        if kind == 'video':
            tags = json.loads(run(['ffprobe', '-v', 'error', '-show_entries', 'format_tags', '-of', 'json', path]).stdout or '{}').get('format', {}).get('tags', {})
            m = re.match(r'([+-]\d+\.\d+)([+-]\d+\.\d+)', tags.get('com.apple.quicktime.location.ISO6709', ''))
            if m:
                return near(float(m.group(1)), float(m.group(2)))
        out = run(['mdls', '-raw', '-name', 'kMDItemLatitude', '-name', 'kMDItemLongitude', path]).stdout.split('\0')
        if len(out) == 2 and '(null)' not in out[0] + out[1]:
            return near(float(out[0]), float(out[1]))
    except Exception:
        pass
    return ''


def photo(src, rel):
    dst = os.path.join(MEDIA, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    tmp = dst + '.src.jpg'
    if src.lower().endswith(('.heic', '.heif')):
        run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '92', src, '--out', tmp])
        im = Image.open(tmp)
    else:
        im = Image.open(src)
    im = ImageOps.exif_transpose(im).convert('RGB')
    im.thumbnail((1600, 1600), Image.LANCZOS)
    im.save(dst, 'JPEG', quality=84, optimize=True, progressive=True)
    if os.path.exists(tmp):
        os.remove(tmp)
    return {'file': 'media/' + rel, 'w': im.width, 'h': im.height}


def video(src, vid):
    out = os.path.join(MEDIA, 'wideo', vid + '.mp4')
    if not os.path.exists(out):
        tmp = out + '.tmp.mp4'
        scale = "scale=w='if(gt(iw,ih),min(1280,iw),-2)':h='if(gt(iw,ih),-2,min(1280,ih))',fps=30,format=yuv420p"
        r = run(['ffmpeg', '-v', 'error', '-y', '-hwaccel', 'videotoolbox', '-i', src, '-map', '0:v:0', '-map', '0:a:0?', '-vf', scale, '-c:v', 'h264_videotoolbox', '-b:v', '1600k', '-c:a', 'aac', '-b:a', '96k', '-ac', '2', '-movflags', '+faststart', '-threads', '2', tmp])
        if r.returncode != 0:
            raise RuntimeError(r.stderr[-300:])
        os.replace(tmp, out)
    dur = float(run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out]).stdout.strip())
    fdir = os.path.join(MEDIA, 'klatki', vid)
    if not os.path.isdir(fdir):
        os.makedirs(fdir)
        n = max(4, min(10, round(dur / 5)))
        for i in range(1, n + 1):
            t = round((i - 0.5) * dur / n, 2)
            run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', out, '-frames:v', '1', '-vf', "scale=w='if(gt(iw,ih),960,-2)':h='if(gt(iw,ih),-2,960)'", '-q:v', '4', '-threads', '2', os.path.join(fdir, f'{i:02d}_{int(t):04d}s.jpg')])


saved = json.load(open(os.path.join(SRC, 'opisy.json'), encoding='utf-8'))
hints = json.load(open(os.path.join(SRC, 'opisy-podpowiedzi.json'), encoding='utf-8'))
result = {'note': saved.get('_notatka', {}).get('story', ''), 'photos': [], 'videos': []}
for key, e in saved.items():
    if key == '_notatka' or e.get('skip') or not (e.get('title') or e.get('story')):
        continue
    src, kind = e['source_path'], e['kind']
    when = e.get('when', '').strip()
    ident = (when if re.fullmatch(r'\d{4}-\d{2}-\d{2}', when) else 'bez-daty') + '_' + slug(e.get('title') or os.path.basename(key))
    story = e.get('story', '').strip()
    for a, b in FIXES.items():
        story = story.replace(a, b)
    who = [w.strip() for w in e.get('who', '').split(',') if w.strip()]
    rec = {
        'id': ('archiwum/' if kind == 'photo' else '') + ident, 'source_name': os.path.basename(key), 'title': e.get('title', '').strip(), 'caption': story,
        'sees': '' if story else hints.get(key, {}).get('story', ''), 'who': ', '.join(who), 'people': sorted({PEOPLE[w.lower()] for w in who if w.lower() in PEOPLE}),
        'where': e.get('where', '').strip(), 'date': when, 'gps': gps(src, kind), 'tags': sorted({slug(x).replace('-', ' ') for x in who + [e.get('where', '')] if x.strip()}),
    }
    if kind == 'photo':
        rec.update(photo(src, f'photos/archiwum/{ident}.jpg'))
        result['photos'].append(rec)
    else:
        video(src, ident)
        result['videos'].append(rec)
    print(kind, ident, flush=True)
json.dump(result, open(os.path.join(SRC, 'ingest_opisy.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

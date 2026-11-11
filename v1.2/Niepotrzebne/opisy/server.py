#!/usr/bin/env python3
"""Gzowo Dataset describe tool: local page that previews new photos and videos from the inbox folder and saves Jurek's descriptions to JSON."""
import hashlib, json, math, os, re, subprocess, sys, threading, time, unicodedata, zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8452
INBOXES = os.environ.get('GZOWO_INBOX', '/Users/jurek/Downloads/new-dataset-set:/Users/jurek/Downloads/Claude/Gzowo_Dataset').split(':')
SAVE = os.environ.get('GZOWO_OPISY', os.path.join(HERE, '..', 'src', 'opisy.json'))
SOURCES = os.environ.get('GZOWO_ZRODLA', os.path.join(HERE, '..', 'src', 'opisy-zrodla.txt'))
HINTS = os.path.join(HERE, '..', 'src', 'opisy-podpowiedzi.json')
CACHE = os.environ.get('GZOWO_CACHE', os.path.expanduser('~/Library/Caches/gzowo-dataset-opisy'))
KNOWN = {'2023-08-29 19-32-08.mkv', 'DANCE.mov', 'Jurek STRAREM___.mkv', 'Movie on 30-11-2020 at 19.45.mov', 'Rakietomania_nieuporządkowane-20261110T122229Z-1-001.zip'}
HOME = (52.612806, 21.116)
PHOTO = ('.jpg', '.jpeg', '.png', '.heic', '.heif', '.webp', '.gif', '.tif', '.tiff')
VIDEO = ('.mp4', '.mov', '.mkv', '.m4v', '.avi', '.webm')
PEOPLE = ['Jurek', 'Rysio', 'Tata', 'Waldek', 'Bożena', 'Bartek', 'Ola „Clu”', 'Ignacy', 'Helena', 'Czupryńscy', 'Janek Kunstler', 'Major', 'Szamborski', 'Paweł', 'Wójt', 'Benny', 'Dropsik', 'Beethoven']
PLACES = ['Dom', 'Taras', 'Wiata', 'Domki', 'Ognisko', 'Hamak', 'Plaża', 'Narew', 'Skarpa', 'Cypel', 'Kocia Wyspa', 'Kanał', 'GL Launch Site', 'Dom Waldka', 'Stacja Moya', 'Warszawa']

os.makedirs(CACHE, exist_ok=True)
lock = threading.Lock()
state = {}
queue = []
unzipped = set()


def key(path):
    st = os.stat(path)
    return hashlib.sha1(f'{path}|{st.st_size}|{int(st.st_mtime)}'.encode()).hexdigest()[:16]


def run(cmd, timeout=1800):
    return subprocess.run(['nice', '-n', '10'] + cmd, capture_output=True, text=True, timeout=timeout)


def near(lat, lon):
    d = math.hypot((lat - HOME[0]) * 111.2, (lon - HOME[1]) * 111.2 * math.cos(math.radians(HOME[0])))
    return 'Gzowo 34' if d < 0.4 else 'okolice Gzowa' if d < 3 else f'{d:.0f} km od Gzowa'


def file_info(path, kind):
    date, source, gps = '', '', ''
    try:
        if kind == 'photo':
            out = run(['sips', '-g', 'creation', path], 20).stdout
            m = re.search(r'creation: (\d{4}):(\d{2}):(\d{2})', out)
            if m:
                date, source = '-'.join(m.groups()), 'z pliku'
        else:
            tags = json.loads(run(['ffprobe', '-v', 'error', '-show_entries', 'format_tags', '-of', 'json', path], 20).stdout or '{}').get('format', {}).get('tags', {})
            shot, written = tags.get('com.apple.quicktime.creationdate', ''), tags.get('creation_time', '')
            if re.match(r'\d{4}-\d{2}-\d{2}', shot):
                date, source = shot[:10], 'z pliku'
            elif re.match(r'\d{4}-\d{2}-\d{2}', written):
                source = f'brak daty nagrania, plik zapisany {written[:10]}'
            m = re.match(r'([+-]\d+\.\d+)([+-]\d+\.\d+)', tags.get('com.apple.quicktime.location.ISO6709', ''))
            if m:
                gps = near(float(m.group(1)), float(m.group(2)))
        if not gps:
            out = run(['mdls', '-raw', '-name', 'kMDItemLatitude', '-name', 'kMDItemLongitude', path], 20).stdout.split('\0')
            if len(out) == 2 and '(null)' not in out[0] + out[1]:
                gps = near(float(out[0]), float(out[1]))
    except Exception:
        pass
    if not date:
        base = os.path.basename(path)
        m = re.search(r'(?:IMG|VID|PXL|Screenshot)[-_ ]?(20\d{2})[-_]?(\d{2})[-_]?(\d{2})', base) or re.match(r'(20\d{2})[-_]?(\d{2})[-_]?(\d{2})', base)
        if m:
            date, source = '-'.join(m.groups()), 'z nazwy pliku'
    return date, source, gps


def unzip(path):
    k = key(path)
    out = os.path.join(CACHE, 'zip', k)
    if k in unzipped or os.path.isdir(out):
        unzipped.add(k)
        return out
    os.makedirs(out, exist_ok=True)
    try:
        with zipfile.ZipFile(path) as z:
            for info in z.infolist():
                base = os.path.basename(info.filename)
                if not base or base.startswith('.') or not base.lower().endswith(PHOTO + VIDEO):
                    continue
                target = os.path.join(out, base)
                n = 1
                while os.path.exists(target):
                    stem, ext = os.path.splitext(base)
                    target = os.path.join(out, f'{stem}-{n}{ext}')
                    n += 1
                with z.open(info) as s, open(target, 'wb') as d:
                    while True:
                        chunk = s.read(1 << 20)
                        if not chunk:
                            break
                        d.write(chunk)
                os.utime(target, (time.time(), time.mktime(info.date_time + (0, 0, -1))))
    except Exception as e:
        print('zip error', path, e, flush=True)
    unzipped.add(k)
    return out


def add_file(rel, p, found):
    low = p.lower()
    if low.endswith('.zip'):
        out = unzip(p)
        for g in sorted(os.listdir(out)):
            found.append((f'{rel}/{g}', os.path.join(out, g)))
    elif low.endswith(PHOTO + VIDEO):
        found.append((rel, p))


def scan_dir(inbox, found):
    for base, dirs, files in os.walk(inbox):
        dirs[:] = sorted(d for d in dirs if not d.startswith('.'))
        for f in sorted(files):
            if f.startswith('.') or unicodedata.normalize('NFC', f) in KNOWN:
                continue
            p = os.path.join(base, f)
            add_file(os.path.join(os.path.basename(inbox.rstrip('/')), os.path.relpath(p, inbox)), p, found)


def scan():
    found = []
    extra = []
    try:
        extra = [l.strip() for l in open(SOURCES, encoding='utf-8') if l.strip()]
    except OSError:
        pass
    for src in INBOXES + extra:
        if os.path.isdir(src):
            scan_dir(src, found)
        elif os.path.isfile(src):
            add_file(os.path.join(os.path.basename(os.path.dirname(src)), os.path.basename(src)), src, found)
    seen = set()
    return [x for x in found if not (x[0] in seen or seen.add(x[0]))]


def refresh():
    items = scan()
    with lock:
        seen = set()
        for rel, path in items:
            seen.add(rel)
            try:
                k = key(path)
            except OSError:
                continue
            it = state.get(rel)
            if it and it['key'] == k:
                continue
            kind = 'video' if path.lower().endswith(VIDEO) else 'photo'
            ext = 'mp4' if kind == 'video' else 'jpg'
            ready = os.path.exists(os.path.join(CACHE, f'{k}.{ext}')) and (kind == 'photo' or os.path.exists(os.path.join(CACHE, f'{k}.poster.jpg')))
            state[rel] = {'id': rel, 'name': os.path.basename(rel), 'path': path, 'key': k, 'kind': kind, 'size': os.path.getsize(path), 'date': None, 'dateSource': '', 'gps': '', 'preview': 'ready' if ready else 'pending', 'duration': None}
            queue.append(rel)
        for rel in list(state):
            if rel not in seen:
                del state[rel]


def make_preview(it):
    src, k = it['path'], it['key']
    if it['kind'] == 'photo':
        out = os.path.join(CACHE, f'{k}.jpg')
        if not os.path.exists(out):
            tmp = out + '.tmp.jpg'
            r = run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '80', '-Z', '1600', src, '--out', tmp], 120)
            if r.returncode != 0 or not os.path.exists(tmp):
                from PIL import Image, ImageOps
                im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
                im.thumbnail((1600, 1600))
                im.save(tmp, 'JPEG', quality=80)
            os.replace(tmp, out)
        return
    out = os.path.join(CACHE, f'{k}.mp4')
    poster = os.path.join(CACHE, f'{k}.poster.jpg')
    if not os.path.exists(out):
        tmp = out + '.tmp.mp4'
        scale = "scale=w='if(gt(iw,ih),min(960,iw),-2)':h='if(gt(iw,ih),-2,min(960,ih))',fps=30,format=yuv420p"
        r = run(['ffmpeg', '-v', 'error', '-y', '-hwaccel', 'videotoolbox', '-i', src, '-map', '0:v:0', '-map', '0:a:0?', '-vf', scale, '-c:v', 'h264_videotoolbox', '-b:v', '1200k', '-c:a', 'aac', '-b:a', '96k', '-ac', '2', '-movflags', '+faststart', '-threads', '2', tmp])
        if r.returncode != 0 or not os.path.exists(tmp):
            raise RuntimeError(r.stderr[-300:])
        os.replace(tmp, out)
    if not os.path.exists(poster):
        dur = float(run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out], 30).stdout.strip() or 0)
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(min(1.0, dur / 2)), '-i', out, '-frames:v', '1', '-q:v', '4', poster], 60)


def worker():
    last = 0
    while True:
        if time.time() - last > 3:
            try:
                refresh()
            except Exception as e:
                print('scan error', e, flush=True)
            last = time.time()
        with lock:
            rel = next((r for r in queue if state.get(r, {}).get('kind') == 'photo'), queue[0]) if queue else None
            if rel:
                queue.remove(rel)
            it = dict(state[rel]) if rel and rel in state else None
        if not it:
            time.sleep(0.5)
            continue
        try:
            date, source, gps = file_info(it['path'], it['kind'])
            if it['preview'] != 'ready':
                make_preview(it)
            dur = None
            if it['kind'] == 'video':
                dur = round(float(run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', os.path.join(CACHE, it['key'] + '.mp4')], 30).stdout.strip() or 0), 1)
            with lock:
                if rel in state and state[rel]['key'] == it['key']:
                    state[rel].update({'date': date, 'dateSource': source, 'gps': gps, 'preview': 'ready', 'duration': dur})
        except Exception as e:
            print('preview error', rel, e, flush=True)
            with lock:
                if rel in state:
                    state[rel]['preview'] = 'error'


def load_json(path):
    try:
        return json.load(open(path, encoding='utf-8'))
    except Exception:
        return {}


def load_saved():
    return load_json(SAVE)


def save_entry(item_id, fields):
    with lock:
        data = load_saved()
        entry = {k: str(fields.get(k, ''))[:4000] for k in ('title', 'story', 'who', 'where', 'when')}
        entry['skip'] = bool(fields.get('skip'))
        entry['saved'] = time.strftime('%Y-%m-%d %H:%M')
        if item_id in state:
            entry['source_path'] = state[item_id]['path']
            entry['kind'] = state[item_id]['kind']
        data[item_id] = entry
        os.makedirs(os.path.dirname(os.path.abspath(SAVE)), exist_ok=True)
        tmp = SAVE + '.tmp'
        json.dump(data, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        os.replace(tmp, SAVE)


class H(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def log_message(self, *a):
        pass

    def send_json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def send_file(self, path, ctype, cache='no-store'):
        if not os.path.isfile(path):
            return self.send_json({'error': 'brak pliku'}, 404)
        size = os.path.getsize(path)
        start, end = 0, size - 1
        rng = self.headers.get('Range')
        m = re.match(r'bytes=(\d*)-(\d*)', rng or '')
        partial = False
        if m and (m.group(1) or m.group(2)):
            if m.group(1):
                start = int(m.group(1))
                end = int(m.group(2)) if m.group(2) else size - 1
            else:
                start = max(0, size - int(m.group(2)))
            end = min(end, size - 1)
            if start > end:
                self.send_response(416)
                self.send_header('Content-Range', f'bytes */{size}')
                self.send_header('Content-Length', '0')
                self.end_headers()
                return
            partial = True
        self.send_response(206 if partial else 200)
        self.send_header('Content-Type', ctype)
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(end - start + 1))
        self.send_header('Cache-Control', cache)
        if partial:
            self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.end_headers()
        if self.command == 'HEAD':
            return
        with open(path, 'rb') as f:
            f.seek(start)
            left = end - start + 1
            try:
                while left > 0:
                    chunk = f.read(min(1 << 18, left))
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    left -= len(chunk)
            except (BrokenPipeError, ConnectionResetError):
                pass

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if path == '/':
            return self.send_file(os.path.join(HERE, 'index.html'), 'text/html; charset=utf-8')
        if path == '/api/list':
            with lock:
                items = [{k: v for k, v in it.items() if k != 'path'} for it in state.values()]
            return self.send_json({'inbox': INBOXES[0], 'items': items, 'saved': load_saved(), 'hints': load_json(HINTS), 'people': PEOPLE, 'places': PLACES})
        m = re.fullmatch(r'/preview/([0-9a-f]{16})(\.poster)?\.(jpg|mp4)', path)
        if m:
            name = m.group(1) + (m.group(2) or '') + '.' + m.group(3)
            return self.send_file(os.path.join(CACHE, name), 'video/mp4' if m.group(3) == 'mp4' else 'image/jpeg', 'max-age=86400')
        self.send_json({'error': 'nie ma takiej strony'}, 404)

    def do_POST(self):
        if urlparse(self.path).path != '/api/save':
            return self.send_json({'error': 'nie ma takiej strony'}, 404)
        try:
            body = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))) or b'{}')
            save_entry(str(body['id'])[:500], body.get('fields', {}))
            self.send_json({'ok': True})
        except Exception as e:
            self.send_json({'error': str(e)}, 400)


threading.Thread(target=worker, daemon=True).start()
print(f'opisy: http://localhost:{PORT}  inbox: {INBOXES}', flush=True)
ThreadingHTTPServer(('127.0.0.1', PORT), H).serve_forever()

#!/usr/bin/env python3
"""Gzowo Dataset build: turns Niepotrzebne/src knowledge base and ingested media into data/*.json, gzowo-dataset.md, llms.txt, index.html and thumbnails."""
import glob, html, json, os, subprocess, sys
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'Niepotrzebne', 'src'))
import kb_facts as F
import kb_media as M

BASE = F.META['site'] + '/'
ING = json.load(open(os.path.join(ROOT, 'Niepotrzebne/src/ingest_photos.json'), encoding='utf-8'))
LABS = '/Users/jurek/Downloads/Claude/Projects/gzowo-labs/site/data/projects.json'


def w(rel, text):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p) or ROOT, exist_ok=True)
    open(p, 'w', encoding='utf-8').write(text)


def wj(rel, obj):
    w(rel, json.dumps(obj, ensure_ascii=False, indent=1) + '\n')


def thumb(rel):
    src = os.path.join(ROOT, rel)
    out_rel = rel.replace('media/photos/', 'media/miniatury/')
    out = os.path.join(ROOT, out_rel)
    if not os.path.exists(out):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        im = Image.open(src).convert('RGB')
        im.thumbnail((480, 480), Image.LANCZOS)
        im.save(out, 'JPEG', quality=72, optimize=True)
    return out_rel


def probe(path):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height:format=duration', '-of', 'json', path], capture_output=True, text=True)
    j = json.loads(r.stdout or '{}')
    s = (j.get('streams') or [{}])[0]
    return {'w': s.get('width'), 'h': s.get('height'), 'duration_s': round(float(j.get('format', {}).get('duration', 0)), 1)}


photos = []
for group, key in (('galeria', 'gallery'), ('plaza', 'beach'), ('rakiety', 'rockets')):
    for rec in ING[key]:
        d = M.PHOTOS.get(rec['id'], {})
        photos.append({
            'id': rec['id'], 'group': group, 'file': rec['file'], 'url': BASE + rec['file'], 'thumb': thumb(rec['file']),
            'w': rec['w'], 'h': rec['h'],
            'title': rec.get('title') or d.get('title', ''), 'caption': rec.get('caption', ''),
            'who_text': rec.get('who', ''), 'where': rec.get('where', '') or ('Plaża Gzowo 34' if group == 'plaza' else ''),
            'date': rec.get('date') or d.get('date', ''), 'rooms': rec.get('rooms', []),
            'sees': d.get('sees', ''), 'people': d.get('people', []), 'tags': d.get('tags', []),
        })

videos = []
for v in M.VIDEOS:
    rel = f"media/wideo/{v['id']}.mp4"
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        print('MISSING VIDEO', v['id'])
        continue
    frames = sorted(os.path.relpath(f, ROOT) for f in glob.glob(os.path.join(ROOT, 'media/klatki', v['id'], '*.jpg')))
    rec = dict(v)
    rec.update(probe(p))
    rec.update({'file': rel, 'url': BASE + rel, 'bytes': os.path.getsize(p), 'frames': frames, 'poster': frames[len(frames) // 2] if frames else ''})
    videos.append(rec)

rooms = {k: {'title': v['title'], 'motto': v['desc']} for k, v in ING['gallery_rooms'].items()}
folders = []
for e in M.EXTRA:
    files = sorted(os.path.relpath(os.path.join(b, f), ROOT) for b, _, fs in os.walk(os.path.join(ROOT, e['dir'])) for f in fs if not f.startswith('.'))
    folders.append({'dir': e['dir'], 'what': e['what'], 'count': len(files), 'files': files if len(files) <= 120 else files[:120] + ['...']})

labs_raw = json.load(open(LABS, encoding='utf-8'))
labs_list = labs_raw if isinstance(labs_raw, list) else labs_raw.get('projects', [])
labs = [{'name': p.get('name'), 'category': p.get('category'), 'year': p.get('year'), 'status': p.get('status'), 'url': p.get('url'), 'page': f"https://gzowo.fun/p/{p.get('slug')}/", 'blurb': p.get('blurb')} for p in labs_list if not p.get('hidden')]

media = {'groups': M.GROUPS, 'rooms_note': M.ROOMS_NOTE, 'rooms': rooms, 'dedication': ING['gallery_dedication'], 'photos': photos, 'videos': videos, 'folders': folders}
DATA = {
    'meta': F.META, 'sources': F.SOURCES, 'confidence': F.CONFIDENCE, 'place': F.PLACE, 'history': F.HISTORY, 'people': F.PEOPLE, 'fictional': F.FICTIONAL,
    'animals': F.ANIMALS, 'spots': F.SPOTS, 'objects': F.OBJECTS, 'rituals': F.RITUALS, 'sayings': F.SAYINGS, 'vocabulary': F.VOCABULARY, 'stories': F.STORIES,
    'rockets': {'note': F.ROCKETS_NOTE, 'fleet': F.ROCKETS}, 'brands': F.BRANDS, 'games_in_gzowo': F.GAMES_IN_GZOWO, 'game_kit': F.GAME_KIT, 'open_questions': F.OPEN_QUESTIONS,
}
for k in ('place', 'history', 'people', 'fictional', 'animals', 'spots', 'objects', 'rituals', 'sayings', 'vocabulary', 'stories', 'rockets', 'brands', 'games_in_gzowo', 'game_kit', 'open_questions'):
    wj(f"data/{k.replace('_', '-')}.json", DATA[k])
wj('data/meta.json', {'meta': F.META, 'sources': F.SOURCES, 'confidence': F.CONFIDENCE})
wj('data/media.json', media)
wj('data/gzowo-labs-projects.json', labs)
wj('data/all.json', dict(DATA, media=media, gzowo_labs_projects=labs))

STATS = {'photos': len(photos), 'videos': len(videos), 'people': len(F.PEOPLE), 'projects': len(labs)}
PROMPT = f"Przeczytaj cały Gzowo Dataset, zanim zaczniesz. Zacznij od {BASE}llms.txt. Cały tekst jest w {BASE}gzowo-dataset.md, opisy zdjęć i filmów w {BASE}data/media.json. Jeśli masz terminal, sklonuj {F.META['repo']} i czytaj pliki lokalnie (obrazy oglądaj sam). Trzymaj się faktów z datasetu i zwracaj uwagę na pola confidence."


def src(x):
    s = ', '.join(x.get('source', []))
    c = x.get('confidence', '')
    return f" _(źródło: {s}{'; ' + c if c else ''})_" if s else ''


md = []
A = md.append
A(f"# Gzowo Dataset\n\n> {F.META['purpose']}\n")
A(f"Wersja {F.META['version']}, {F.META['updated']}. Język: polski. Autor: {F.META['author']}.\n")
A("## Jak z tego korzystać (dla AI)\n")
A(f"- Ten plik zawiera **cały tekst** datasetu. Adres: {BASE}gzowo-dataset.md\n- To samo w JSON: {BASE}data/all.json (albo osobne pliki w {BASE}data/).\n- Zdjęcia i filmy: {BASE}data/media.json ma każdy plik z opisem, kto, gdzie, kiedy i co widać. Obrazy możesz otwierać i oglądać sam.\n- Masz terminal? `git clone {F.META['repo']}` daje wszystko lokalnie. Jeśli twoje narzędzie do stron streszcza treść, pobierz pliki przez `curl -L`.\n- Filmów nie musisz oglądać: każdy ma kadry w `media/klatki/<id>/` i opis.\n")
A(f"**Zasada prawdy:** {F.META['truth_policy']}\n")
A("Źródła:\n" + '\n'.join(f"- `{k}`: {v}" for k, v in F.SOURCES.items()) + '\n')
A("Pewność:\n" + '\n'.join(f"- `{k}`: {v}" for k, v in F.CONFIDENCE.items()) + '\n')

P = F.PLACE
A("## 1. Miejsce\n")
A(f"**{P['name']}** ({', '.join(P['nicknames'])}). {P['what']}\n")
A(f"- Adres: {P['address']}\n- Współrzędne: {P['coordinates']['lat']}, {P['coordinates']['lon']}\n- {P['from_warsaw']}\n")
R = P['river']
A(f"**Narew.** {R['role']} {R['character']} Poziom wody ok. {R['water_level_m']} m n.p.m. Co się na niej robi: {', '.join(R['uses'])}.\n")
T = P['terrain']
A(f"**Teren.** {T['summary']} {T['scarp']} W kwadracie 1 x 1 km wysokości od {T['elevation_in_1km_square_m']['min']} do {T['elevation_in_1km_square_m']['max']} m n.p.m. (różnica {T['elevation_in_1km_square_m']['difference']} m), sama działka ok. {T['plot_ground_m']} m. Drzewa: {T['trees']} {T['neighbourhood']}\n")
A("Pokrycie terenu w kwadracie 1 x 1 km: " + ', '.join(f"{k} {v}%" for k, v in T['landcover_1km_square_pct'].items()) + '.\n')
A(f"**Widok z góry.** {P['aerial_view']}\n")

A("## 2. Historia i oś czasu\n")
for h in F.HISTORY:
    A(f"- **{h['when']}**: {h['what']}{src(h)}")
A('')

A("## 3. Ludzie\n")
for g, label in (('rodzina', 'Rodzina (tylko te trzy osoby)'), ('przyjaciele', 'Przyjaciele i goście'), ('okolica', 'Okolica')):
    A(f"### {label}\n")
    for p in [x for x in F.PEOPLE if x['group'] == g]:
        names = p['name'] + (f" ({p['full_name']})" if p.get('full_name') and p['full_name'] != p['name'] else '')
        A(f"**{names}**" + (f", inaczej: {', '.join(p['aliases'])}" if p.get('aliases') else '') + f". {p['role']}{src(p)}")
        for f in p.get('facts', []):
            A(f"- {f}")
        if p.get('looks'):
            A(f"- Wygląd: {p['looks']}")
        if p.get('in_games'):
            A(f"- W grach: {p['in_games']}")
        A('')
A("### Postacie zmyślone (z gier i projektów)\n")
for x in F.FICTIONAL:
    A(f"- **{x['name']}** ({x['from']}): {x['what']}")
A('')

A("## 4. Zwierzęta\n")
for a in F.ANIMALS:
    A(f"**{a['name']}** ({a['kind']}, {a['status']}){src(a)}")
    for f in a.get('facts', []):
        A(f"- {f}")
    if a.get('in_games'):
        A(f"- W grach: {a['in_games']}")
    A('')

A("## 5. Miejsca na działce i w okolicy\n")
for s in F.SPOTS:
    A(f"**{s['name']}**" + (f" ({', '.join(s['aliases'])})" if s.get('aliases') else '') + f", {s['where']}{src(s)}")
    for f in s['facts']:
        A(f"- {f}")
    A('')

A("## 6. Sprzęt i rzeczy\n")
for o in F.OBJECTS:
    A(f"- **{o['name']}** ({'nasze' if o['ours'] else 'NIE nasze'}): {' '.join(o['facts'])}{src(o)}")
A('')

A("## 7. Rytuały\n")
for r in F.RITUALS:
    A(f"- **{r['name']}**: {r['what']}{src(r)}")
A('')

A("## 8. Powiedzonka i słownik\n")
for s in F.SAYINGS:
    A(f"- \"{s['text']}\" ({s['who']}). {s['note']}{src(s)}")
A('')
for v in F.VOCABULARY:
    A(f"- **{v['word']}**: {v['meaning']}")
A('')

A("## 9. Historie i wspomnienia\n")
for s in F.STORIES:
    A(f"- **{s['title']}**: {s['what']}{src(s)}")
A('')

A("## 10. Rakiety\n")
A(F.ROCKETS_NOTE + '\n')
for r in F.ROCKETS:
    A(f"- **{r['name']}** ({r['owner']}, {r['state']}): {' '.join(r['facts'])}{src(r)}")
A('')

A("## 11. Marki i logo\n")
for b in F.BRANDS:
    A(f"### {b['name']}\n")
    A(b['what'] + (f" Strona: {b['url']}" if b.get('url') else '') + '\n')
    for k, label in (('tagline', 'Hasło'), ('signature', 'Podpis strony'), ('site', 'Strona'), ('economy_on_site', 'Ekonomia na stronie'), ('fire_gif', 'Płonący GIF'), ('files', 'Pliki'), ('note', 'Uwaga')):
        if b.get(k):
            A(f"- {label}: {b[k]}")
    if b.get('sections'):
        A("- Działy: " + '; '.join(f"{k} (\"{v}\")" for k, v in b['sections'].items()))
    if b.get('logo'):
        L = b['logo']
        A(f"- Logo \"{L['name']}\": {L['idea']}\n- Kolory: " + ', '.join(f"{k} {v}" for k, v in L['colors'].items()) + f"\n- Kroje: napis {L['fonts']['napis']}, podpis {L['fonts']['podpis']}\n- Wersje: {L['versions']}\n- Zasady: {L['rules']}\n- Pliki: {L['files']}")
        A(f"- Najważniejsze pliki: {BASE}media/brand/gzowo-labs/svg/gzowo-labs-poziome-kolor.svg , {BASE}media/brand/gzowo-labs/svg/gzowo-labs-znak-kolor.svg , {BASE}media/brand/gzowo-labs/png/gzowo-labs-poziome-kolor.png")
    A('')
A(f"### Projekty Gzowo Labs ({len(labs)})\n")
for p in labs:
    A(f"- **{p['name']}** ({p['category']}, {p['year']}, {p['status']}): {p['blurb']} {p['url'] or ''}")
A('')

A("## 12. Gry i projekty osadzone w Gzowie\n")
for g in F.GAMES_IN_GZOWO:
    A(f"- **{g['name']}** ({g['author']}): {g['what']} {g['url']}")
A('')

A("## 13. Zdjęcia\n")
A(M.ROOMS_NOTE + '\n')
A("Pokoje Galerii: " + '; '.join(f"{v['title']} (\"{v['motto']}\")" for v in rooms.values()) + '\n')
for g in ('galeria', 'rakiety', 'plaza'):
    A(f"### {g}\n\n{M.GROUPS[g]}\n")
    for p in [x for x in photos if x['group'] == g]:
        head = f"**{p['title']}**. " if p['title'] else ''
        bits = [f"\"{p['caption']}\"" if p['caption'] else '', f"Kto: {p['who_text']}." if p['who_text'] else '', f"Gdzie: {p['where']}." if p['where'] else '', f"Data: {p['date']}." if p['date'] else '', f"Pokoje: {', '.join(p['rooms'])}." if p['rooms'] else '', f"Widać: {p['sees']}" if p['sees'] else '']
        A(f"- {head}{' '.join(b for b in bits if b)} Plik: {p['url']}")
    A('')

A("## 14. Filmy\n")
for v in videos:
    A(f"- **{v['title']}** ({v['date']}, {v['where']}, {v['duration_s']} s). {v['sees']} " + (f"Co mówią (transkrypcja automatyczna, poprawiona, przybliżona): {v['said']} " if v.get('said') else '') + f"{v['note']} Plik: {v['url']} Kadry: {BASE}media/klatki/{v['id']}/ ({len(v['frames'])} szt.)")
A('')

A("## 15. Pozostałe foldery z mediami\n")
for f in folders:
    A(f"- `{f['dir']}/` ({f['count']} plików): {f['what']}")
A('')

K = F.GAME_KIT
A("## 16. Pod grę (propozycje, nie fakty)\n")
A(K['note'] + '\n')
A("**Pola planszy:** " + '; '.join(K['board_spaces']) + '.\n')
A("**Postacie:** " + '; '.join(K['characters']) + '.\n')
A("**Przedmioty:** " + ', '.join(K['items']) + '.\n')
A("**Mechaniki:**\n" + '\n'.join(f"- {e}" for e in K.get('mechanics', [])) + '\n')
A("**Karty wydarzeń:**\n" + '\n'.join(f"- {e}" for e in K['event_cards']) + '\n')
A("**Pytania quizowe:**\n" + '\n'.join(f"- {q['q']} → {q['a']}" for q in K['quiz']) + '\n')

A("## 17. Czego jeszcze nie wiemy\n")
A('\n'.join(f"- {q}" for q in F.OPEN_QUESTIONS) + '\n')
w('gzowo-dataset.md', '\n'.join(md))

ll = [f"# Gzowo Dataset\n", f"> {F.META['purpose']}\n", f"Język: polski. Wersja {F.META['version']} z {F.META['updated']}. {F.META['truth_policy']}\n",
      "## Najpierw to", f"- [Cały tekst datasetu]({BASE}gzowo-dataset.md): wszystko w jednym pliku Markdown, czytaj w całości", f"- [Opis każdego zdjęcia i filmu]({BASE}data/media.json): kto, gdzie, kiedy, co widać, adresy plików", f"- [Wszystko w jednym JSON]({BASE}data/all.json)", f"- [Repozytorium do sklonowania]({F.META['repo']}): `git clone` daje teksty, dane i media lokalnie\n",
      "## Dane"]
for k, label in (('place', 'Miejsce, Narew, teren, współrzędne'), ('history', 'Oś czasu'), ('people', 'Ludzie'), ('animals', 'Zwierzęta'), ('spots', 'Miejsca na działce i w okolicy'), ('objects', 'Sprzęt i rzeczy'), ('rituals', 'Rytuały'), ('sayings', 'Powiedzonka'), ('vocabulary', 'Słownik'), ('stories', 'Historie i wspomnienia'), ('rockets', 'Rakiety'), ('brands', 'Marki, logo, kolory'), ('games-in-gzowo', 'Gry osadzone w Gzowie'), ('fictional', 'Postacie zmyślone z gier'), ('game-kit', 'Propozycje pod grę (nie fakty)'), ('open-questions', 'Czego jeszcze nie wiemy'), ('gzowo-labs-projects', 'Lista projektów Gzowo Labs'), ('meta', 'Źródła i poziomy pewności')):
    ll.append(f"- [{label}]({BASE}data/{k}.json)")
ll += ["\n## Media", f"- [Logo Gzowo Labs, SVG poziome]({BASE}media/brand/gzowo-labs/svg/gzowo-labs-poziome-kolor.svg)", f"- [Logo Gzowo Labs, sam znak SVG]({BASE}media/brand/gzowo-labs/svg/gzowo-labs-znak-kolor.svg)", f"- [Zdjęcie lotnicze działki]({BASE}media/geo/ortofoto-dzialka-zblizenie.jpg)", f"- [Ortofotomapa 1 x 1 km]({BASE}media/geo/ortofoto-1km.jpg)", f"- [Pikselowa mapa działki z gzowo.fun]({BASE}media/mapa-pikselowa/_cala-mapa.webp)", f"- [Postacie low-poly]({BASE}media/postacie/osrodek-daje/characters-front.png)", f"- Zdjęcia: `{BASE}media/photos/<grupa>/<plik>.jpg`, filmy: `{BASE}media/wideo/<id>.mp4`, kadry: `{BASE}media/klatki/<id>/`. Pełna lista w media.json.", "\n## Strona dla ludzi", f"- [Strona główna]({BASE})"]
w('llms.txt', '\n'.join(ll) + '\n')

E = html.escape


def badge(x):
    c = x.get('confidence')
    return f' <span class="b">{E(c)}</span>' if c in ('niepewne', 'prawdopodobne') else ''


def ul(items):
    return '<ul>' + ''.join(f'<li>{E(i)}</li>' for i in items) + '</ul>' if items else ''


def sec(i, title, body):
    return f'<section id="{i}"><h2>{E(title)}</h2>{body}</section>'


def card(title, sub, body, x=None):
    return f'<article class="c"><h3>{E(title)}{badge(x or {})}</h3>' + (f'<p class="s">{E(sub)}</p>' if sub else '') + body + '</article>'


def fig(p):
    cap = p['title'] or p['id'].split('/')[-1]
    alt = p['sees'] or cap
    tip = ' · '.join(b for b in (p['caption'], p['who_text'], p['where'], p['date']) if b)
    return f'<a class="ph" href="{E(p["file"])}" target="_blank" rel="noopener" title="{E(tip)}"><img src="{E(p["thumb"])}" alt="{E(alt)}" loading="lazy" width="240" height="240"><span>{E(cap)}</span></a>'


TOC = [('start', 'Start'), ('miejsce', 'Miejsce'), ('historia', 'Historia'), ('ludzie', 'Ludzie'), ('zwierzeta', 'Zwierzęta'), ('miejsca', 'Miejsca'), ('sprzet', 'Sprzęt'), ('rytualy', 'Rytuały'), ('powiedzonka', 'Powiedzonka'), ('historie', 'Historie'), ('rakiety', 'Rakiety'), ('marki', 'Marki i logo'), ('gry', 'Gry o Gzowie'), ('zdjecia', 'Zdjęcia'), ('filmy', 'Filmy'), ('mapy', 'Mapy i dane'), ('pod-gre', 'Pod grę'), ('pytania', 'Czego nie wiemy')]

S = []
S.append(f'''<section id="start"><p class="k">Gzowo 34 · nad Narwią · wersja {E(F.META['version'])} · {E(F.META['updated'])}</p><h1>Gzowo Dataset</h1><p class="lead">{E(F.META['purpose'])}</p>
<div class="nums"><div><b>{STATS['photos']}</b>zdjęć</div><div><b>{STATS['videos']}</b>filmów</div><div><b>{STATS['people']}</b>osób i grup</div><div><b>{STATS['projects']}</b>projektów Gzowo Labs</div></div>
<div class="ai"><h3>Dla Claude'a</h3><p>Wklej to swojemu Claude'owi, a będzie wiedział wszystko:</p><pre id="prompt">{E(PROMPT)}</pre><button id="copy" type="button">Kopiuj</button>
<p class="links"><a href="llms.txt">llms.txt</a><a href="gzowo-dataset.md">gzowo-dataset.md</a><a href="data/all.json">all.json</a><a href="data/media.json">media.json</a><a href="{E(F.META['repo'])}">repozytorium</a></p></div>
<p class="note">{E(F.META['truth_policy'])} Znaczek <span class="b">niepewne</span> oznacza rzeczy, których nikt nie potwierdził na sto procent.</p></section>''')

S.append(sec('miejsce', 'Miejsce', f'''<p><b>{E(P['name'])}</b>. {E(P['what'])}</p><p>{E(P['address'])}. Współrzędne {P['coordinates']['lat']}, {P['coordinates']['lon']}. {E(P['from_warsaw'])}</p>
<p><b>Narew.</b> {E(R['role'])} {E(R['character'])}</p><p><b>Teren.</b> {E(T['summary'])} {E(T['scarp'])} {E(T['trees'])}</p>
<a class="wide" href="media/geo/ortofoto-dzialka-zblizenie.jpg" target="_blank" rel="noopener"><img src="media/geo/ortofoto-dzialka-zblizenie.jpg" alt="Zdjęcie lotnicze działki Gzowo 34 nad Narwią" loading="lazy" width="700" height="700"></a><p class="s">{E(P['aerial_view'])}</p>'''))

S.append(sec('historia', 'Historia', '<ol class="tl">' + ''.join(f'<li><time>{E(h["when"])}</time><p>{E(h["what"])}{badge(h)}</p></li>' for h in F.HISTORY) + '</ol>'))

body = ''
for g, label in (('rodzina', 'Rodzina'), ('przyjaciele', 'Przyjaciele i goście'), ('okolica', 'Okolica')):
    body += f'<h4>{label}</h4><div class="g">' + ''.join(card(p['name'], p['role'], ul(p.get('facts', [])) + (f'<p class="s"><b>Wygląd:</b> {E(p["looks"])}</p>' if p.get('looks') else '') + (f'<p class="s"><b>W grach:</b> {E(p["in_games"])}</p>' if p.get('in_games') else ''), p) for p in F.PEOPLE if p['group'] == g) + '</div>'
body += '<h4>Postacie zmyślone</h4><div class="g">' + ''.join(card(x['name'], x['from'], f'<p>{E(x["what"])}</p>') for x in F.FICTIONAL) + '</div>'
body += '<a class="wide" href="media/postacie/osrodek-daje/characters-front.png" target="_blank" rel="noopener"><img src="media/postacie/osrodek-daje/characters-front.png" alt="KS, Jurek, Ryś i Dropsik jako postacie low-poly z gry Ośrodek Daje" loading="lazy" width="1280" height="800"></a><p class="s">KS, Jurek, Ryś i Dropsik w wersji z gry Ośrodek Daje.</p>'
S.append(sec('ludzie', 'Ludzie', body))

S.append(sec('zwierzeta', 'Zwierzęta', '<div class="g">' + ''.join(card(a['name'], f"{a['kind']}, {a['status']}", ul(a.get('facts', [])) + (f'<p class="s"><b>W grach:</b> {E(a["in_games"])}</p>' if a.get('in_games') else ''), a) for a in F.ANIMALS) + '</div>'))
S.append(sec('miejsca', 'Miejsca na działce i w okolicy', '<div class="g">' + ''.join(card(s['name'], s['where'], ul(s['facts']), s) for s in F.SPOTS) + '</div>'))
S.append(sec('sprzet', 'Sprzęt i rzeczy', '<div class="g">' + ''.join(card(o['name'], 'nasze' if o['ours'] else 'nie nasze', ul(o['facts'])) for o in F.OBJECTS) + '</div>'))
S.append(sec('rytualy', 'Rytuały', '<dl>' + ''.join(f'<dt>{E(r["name"])}</dt><dd>{E(r["what"])}</dd>' for r in F.RITUALS) + '</dl>'))
S.append(sec('powiedzonka', 'Powiedzonka i słownik', ''.join(f'<blockquote>{E(s["text"])}<cite>{E(s["who"])}. {E(s["note"])}{badge(s)}</cite></blockquote>' for s in F.SAYINGS) + '<dl>' + ''.join(f'<dt>{E(v["word"])}</dt><dd>{E(v["meaning"])}</dd>' for v in F.VOCABULARY) + '</dl>'))
S.append(sec('historie', 'Historie i wspomnienia', '<div class="g">' + ''.join(card(s['title'], '', f'<p>{E(s["what"])}</p>', s) for s in F.STORIES) + '</div>'))
S.append(sec('rakiety', 'Rakiety', f'<p>{E(F.ROCKETS_NOTE)}</p><div class="g">' + ''.join(card(r['name'], f"{r['owner']}, {r['state']}", ul(r['facts'])) for r in F.ROCKETS) + '</div>'))

body = ''
for b in F.BRANDS:
    inner = f'<p>{E(b["what"])}</p>'
    if b['id'] == 'gzowo-labs':
        L = b['logo']
        inner += f'<div class="logos"><a href="media/brand/gzowo-labs/svg/gzowo-labs-poziome-kolor.svg"><img src="media/brand/gzowo-labs/svg/gzowo-labs-poziome-kolor.svg" alt="Logo Gzowo Labs poziome" loading="lazy" width="320" height="120"></a><a href="media/brand/gzowo-labs/svg/gzowo-labs-znak-kolor.svg"><img src="media/brand/gzowo-labs/svg/gzowo-labs-znak-kolor.svg" alt="Znak Gzowo Labs" loading="lazy" width="120" height="120"></a><a class="dark" href="media/brand/gzowo-labs/svg/gzowo-labs-pionowe-ciemne-tlo.svg"><img src="media/brand/gzowo-labs/svg/gzowo-labs-pionowe-ciemne-tlo.svg" alt="Logo Gzowo Labs pionowe na ciemnym tle" loading="lazy" width="160" height="160"></a><a class="dark" href="media/brand/gzowo-labs/strona/gzowo-labs-fire.gif"><img src="media/brand/gzowo-labs/strona/gzowo-labs-fire.gif" alt="Płonący napis Gzowo Labs" loading="lazy" width="300" height="80"></a></div>'
        inner += f'<p><b>Logo Wschód.</b> {E(L["idea"])}</p><p class="s">Kolory: ' + ', '.join(f'{E(k)} {E(v)}' for k, v in L['colors'].items()) + f'. Kroje: {E(L["fonts"]["napis"])} i {E(L["fonts"]["podpis"])}. {E(L["versions"])} {E(L["rules"])}</p><p class="s">{E(b["site"])} {E(b["economy_on_site"])}</p>'
    if b.get('note'):
        inner += f'<p class="s">{E(b["note"])}</p>'
    if b.get('files'):
        inner += f'<p class="s">Pliki: {E(b["files"])}</p>'
    body += card(b['name'], b.get('url', ''), inner)
body += f'<details><summary>Wszystkie projekty Gzowo Labs ({len(labs)})</summary><ul class="pl">' + ''.join(f'<li><a href="{E(p["url"] or p["page"])}" target="_blank" rel="noopener">{E(p["name"])}</a> <span>{E(str(p["category"]))}, {E(str(p["year"]))}</span><br>{E(p["blurb"] or "")}</li>' for p in labs) + '</ul></details>'
S.append(sec('marki', 'Marki i logo', body))

S.append(sec('gry', 'Gry i projekty osadzone w Gzowie', '<div class="g">' + ''.join(card(g['name'], g['author'], f'<p>{E(g["what"])}</p>' + (f'<p class="s"><a href="{E(g["url"])}" target="_blank" rel="noopener">{E(g["url"].replace("https://", ""))}</a></p>' if g['url'] else '')) for g in F.GAMES_IN_GZOWO) + '</div>'))

body = f'<p>{E(M.ROOMS_NOTE)} Kliknięcie otwiera pełne zdjęcie, najechanie pokazuje podpis Jurka.</p>'
used = set()
for slug, r in rooms.items():
    ps = [p for p in photos if p['group'] == 'galeria' and slug in p['rooms']]
    if not ps:
        continue
    body += f'<h4>{E(r["title"])} <span>{E(r["motto"])}</span></h4><div class="pg">' + ''.join(fig(p) for p in ps) + '</div>'
body += f'<h4>Rakietomania <span>{E(M.GROUPS["rakiety"])}</span></h4><div class="pg">' + ''.join(fig(p) for p in photos if p['group'] == 'rakiety') + '</div>'
body += f'<h4>Plaża <span>{E(M.GROUPS["plaza"])}</span></h4><div class="pg">' + ''.join(fig(p) for p in photos if p['group'] == 'plaza') + '</div>'
S.append(sec('zdjecia', 'Zdjęcia', body))

S.append(sec('filmy', 'Filmy', '<div class="vg">' + ''.join(f'<article class="c"><video controls preload="none" playsinline poster="{E(v["poster"])}" src="{E(v["file"])}"></video><h3>{E(v["title"])}</h3><p class="s">{E(v["date"])} · {E(v["where"])} · {v["duration_s"]} s</p><p>{E(v["sees"])}</p>' + (f'<p class="s"><b>Co mówią:</b> {E(v["said"])}</p>' if v.get('said') else '') + (f'<p class="s">{E(v["note"])}</p>' if v['note'] else '') + '</article>' for v in videos) + '</div>'))

S.append(sec('mapy', 'Mapy i dane terenu', '<div class="pg big">' + ''.join(f'<a class="ph" href="{f}" target="_blank" rel="noopener"><img src="{f}" alt="{E(t)}" loading="lazy" width="400" height="400"><span>{E(t)}</span></a>' for f, t in (('media/geo/ortofoto-1km.jpg', 'Ortofotomapa 1 x 1 km'), ('media/geo/rzezba-terenu-1km.jpg', 'Rzeźba terenu, skarpa'), ('media/geo/pokrycie-terenu-1km.jpg', 'Pokrycie terenu'), ('media/geo/ortofoto-okolica-20km.jpg', 'Okolica z góry'))) + '</div><a class="wide" href="media/mapa-pikselowa/_cala-mapa.webp" target="_blank" rel="noopener"><img src="media/mapa-pikselowa/_cala-mapa.webp" alt="Pikselowa mapa działki ze strony gzowo.fun" loading="lazy" width="1600" height="480"></a><p class="s">Pikselowa mapa działki ze strony gzowo.fun. Pojedyncze sprite\'y leżą w media/mapa-pikselowa/.</p><dl>' + ''.join(f'<dt>{E(f["dir"])}/ <span>{f["count"]} plików</span></dt><dd>{E(f["what"])}</dd>' for f in folders) + '</dl>'))

S.append(sec('pod-gre', 'Pod grę', f'<p class="note">{E(K["note"])}</p><h4>Pola planszy</h4><p class="chips">' + ''.join(f'<span>{E(x)}</span>' for x in K['board_spaces']) + '</p><h4>Postacie</h4><p class="chips">' + ''.join(f'<span>{E(x)}</span>' for x in K['characters']) + '</p><h4>Przedmioty</h4><p class="chips">' + ''.join(f'<span>{E(x)}</span>' for x in K['items']) + '</p><h4>Mechaniki</h4>' + ul(K.get('mechanics', [])) + '<h4>Karty wydarzeń</h4>' + ul(K['event_cards']) + '<h4>Pytania quizowe</h4><dl>' + ''.join(f'<dt>{E(q["q"])}</dt><dd>{E(q["a"])}</dd>' for q in K['quiz']) + '</dl>'))
S.append(sec('pytania', 'Czego jeszcze nie wiemy', ul(F.OPEN_QUESTIONS) + '<h4>Źródła</h4><dl>' + ''.join(f'<dt>{E(k)}</dt><dd>{E(v)}</dd>' for k, v in F.SOURCES.items()) + '</dl>'))

CSS = open(os.path.join(ROOT, 'Niepotrzebne/src/site.css'), encoding='utf-8').read()
page = f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Gzowo Dataset</title>
<meta name="description" content="Cała wiedza o działce Gzowo 34 nad Narwią w jednym miejscu, dla ludzi i dla AI.">
<link rel="icon" href="media/brand/gzowo-labs/favicon/favicon.svg">
<link rel="alternate" type="text/markdown" href="gzowo-dataset.md" title="Cały dataset jako Markdown">
<style>{CSS}</style>
</head>
<body>
<nav id="toc" aria-label="Spis treści">{''.join(f'<a href="#{i}">{E(t)}</a>' for i, t in TOC)}</nav>
<main>{''.join(S)}<footer>Gzowo Dataset {E(F.META['version'])} · {E(F.META['updated'])} · zrobione w Gzowo Labs</footer></main>
<script>
const b=document.getElementById('copy');b.addEventListener('click',()=>{{navigator.clipboard.writeText(document.getElementById('prompt').textContent).then(()=>{{b.textContent='Skopiowane';setTimeout(()=>b.textContent='Kopiuj',1600)}})}});
</script>
</body>
</html>
'''
w('index.html', page)
w('CNAME', 'dataset.gzowo.fun\n')
w('.nojekyll', '')
w('robots.txt', 'User-agent: *\nAllow: /\n')
w('.gitignore', '.DS_Store\n__pycache__/\n*.tmp.mp4\n')
w('README.md', f"# Gzowo Dataset\n\nEverything known about Gzowo 34, a family plot on the Narew river in Poland: place, history, people, animals, gear, rituals, sayings, memories, brands (Gzowo Labs, GSP) and media. Built mainly as source material for a game about Gzowo. Content is in Polish.\n\n- Site: {BASE}\n- For AI agents: start with `llms.txt`, the full text is `gzowo-dataset.md`, structured data is in `data/`, every photo and video is described in `data/media.json`.\n- Rebuild: `python3 Niepotrzebne/tools/build.py` (sources in `Niepotrzebne/src/`).\n")
tot = sum(os.path.getsize(os.path.join(b, f)) for b, _, fs in os.walk(ROOT) for f in fs if '.git' not in b)
print(STATS, 'md kB', round(os.path.getsize(os.path.join(ROOT, 'gzowo-dataset.md')) / 1e3, 1), 'html kB', round(os.path.getsize(os.path.join(ROOT, 'index.html')) / 1e3, 1), 'total MB', round(tot / 1e6, 1))

#!/usr/bin/env python3
"""Gzowo Dataset: strip the media copy from every vX.Y snapshot folder and point its page at the shared root media, so the site stays small enough for GitHub Pages to deploy."""
import os, re, shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
for name in sorted(os.listdir(ROOT)):
    folder = os.path.join(ROOT, name)
    if not (os.path.isdir(folder) and re.fullmatch(r'v\d+(\.\d+)?', name)):
        continue
    media = os.path.join(folder, 'media')
    removed = os.path.isdir(media)
    if removed:
        shutil.rmtree(media)
    page = os.path.join(folder, 'index.html')
    changed = 0
    if os.path.isfile(page):
        html = open(page, encoding='utf-8').read()
        html, changed = re.subn(r'\b(src|href|poster)="media/', r'\1="../media/', html)
        if changed:
            open(page, 'w', encoding='utf-8').write(html)
    size = sum(os.path.getsize(os.path.join(b, f)) for b, _, fs in os.walk(folder) for f in fs)
    print(f'{name}: media {"removed" if removed else "already gone"}, {changed} links repointed, {size / 1e6:.1f} MB')

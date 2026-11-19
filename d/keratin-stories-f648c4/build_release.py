#!/usr/bin/env python3
"""Боевая сборка для keratinstories.ru: v3 → ~/Desktop/keratinstories/release/ (корень сайта).
Картинки из ../v2/img кладутся в img/, noindex убирается. Сначала: python3 build_pages.py"""
import re, shutil
from pathlib import Path

SRC = Path(__file__).parent
OUT = Path.home() / 'Desktop/keratinstories/release'

shutil.rmtree(OUT, ignore_errors=True)
shutil.copytree(SRC / 'v3', OUT, ignore=shutil.ignore_patterns('price-sketches', '.DS_Store'))
shutil.copytree(SRC / 'v2/img', OUT / 'img', dirs_exist_ok=True)

SITE = 'https://www.keratinstories.ru/'
# описания — только из текстов самого сайта
DESC = {
    '': 'Профессиональная студия выпрямления и реконструкции волос в Москве: кератин, ботокс, нанопластика, реконструкция. Ул. Большая Грузинская, 12, м. Баррикадная. Калькулятор стоимости и онлайн-запись.',
    'price/': 'Прайс-лист студии Кератин Сторис: стоимость выпрямления и реконструкции волос в зависимости от длины, густоты и мастера.',
    'offer/': 'Публичная оферта студии Кератин Сторис (ИП Матковская Ю. В.).',
    'offer/archive/': 'Архивная редакция публичной оферты студии Кератин Сторис, действовавшая до 1.06.2026.',
    'policy/': 'Политика обработки и защиты персональных данных студии Кератин Сторис (ИП Матковская Ю. В.).',
    'policy/appendix/': 'Приложение № 1 к Политике обработки персональных данных: цели, категории и сроки обработки.',
}

def meta(rel, s):
    title = re.search(r'<title>(.*?)</title>', s).group(1)
    tags = (f'<meta name="description" content="{DESC[rel]}">\n<link rel="canonical" href="{SITE}{rel}">\n'
            f'<meta property="og:type" content="website">\n<meta property="og:site_name" content="Кератин Сторис">\n'
            f'<meta property="og:title" content="{title}">\n<meta property="og:description" content="{DESC[rel]}">\n'
            f'<meta property="og:url" content="{SITE}{rel}">\n<meta property="og:image" content="{SITE}img/studio1.jpg">\n'
            f'<meta property="og:locale" content="ru_RU">\n')
    return s.replace('</title>\n', '</title>\n' + tags, 1)

for f in OUT.rglob('*.html'):
    s = f.read_text(encoding='utf-8')
    s = re.sub(r'((?:\.\./)*)\.\./v2/', r'\1', s)  # ../v2/img/ → img/, ../../v2/img/ → ../img/
    s = re.sub(r'\n<!--[^\n]*noindex[^\n]*-->', '', s)
    s = s.replace('\n<meta name="robots" content="noindex, nofollow">', '')
    rel = f.parent.relative_to(OUT).as_posix() + '/' if f.name == 'index.html' and f.parent != OUT else ''
    if f.name == 'index.html':
        s = meta(rel, s)
    assert 'v2/' not in s and 'noindex' not in s, f
    f.write_text(s, encoding='utf-8')

# Apache (обычный хостинг): www-домен канонический (как в sitemap), старые адреса Tilda → главная.
# HTTPS-редирект включать галочкой в панели хостинга: за их прокси %{HTTPS} ненадёжен.
OLD = 'keratin|botox|nanoplasty|reconstruction|warmbotox|recovery|spacare|spaprogram|polishing|additionalservices'
(OUT / '.htaccess').write_text(f"""ErrorDocument 404 /404.html
RewriteEngine On
RewriteCond %{{HTTP_HOST}} ^keratinstories\\.ru$ [NC]
RewriteRule ^(.*)$ https://www.keratinstories.ru/$1 [R=301,L]
RewriteRule ^({OLD})/?$ / [R=301,L]
""", encoding='utf-8')

print(OUT, sum(1 for _ in OUT.rglob('*') if _.is_file()), 'files')

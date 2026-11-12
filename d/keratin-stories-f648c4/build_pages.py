#!/usr/bin/env python3
"""Собирает price/index.html для v2 и v3 из одних данных.
Источник цен: ~/Desktop/leadgen/notes/keratin_price_2026-03.md (прайс от 1.03.2026).
Запуск: python3 build_pages.py  (из любой папки)."""
from pathlib import Path

ROOT = Path(__file__).parent
DIKIDI = 'https://dikidi.net/1005604'
L9 = ['до 30 см', 'до 35 см', 'до 40 см', 'до 45 см', 'до 50 см', 'до 55 см', 'до 60 см', 'до 65 см', 'до 70 см']
L4 = ['до 30 см', 'до 45 см', 'до 60 см', 'до 70 см']
LVL3 = ['Мастер', 'ТОП-мастер<small>Яна, Полина</small>', 'Юлия*<small>основатель</small>']
step = lambda a, d: [a + i * d for i in range(9)]
JULIA = '*к Юлии — только по предварительному бронированию'
O70 = 'свыше 70 см стоимость рассчитывается индивидуально'
DENS = 'доплата за густоту: 1 000 ₽ — 3 000 ₽'
DENS_S = ['доплата за густоту 9–10 см: 500 ₽', 'доплата за густоту от 11 см: 1 000 ₽']
SUB = 'подложка для сильно повреждённых волос: 2 000 ₽ — 3 000 ₽'
EXT = 'доплата за наращённые волосы: 1 500 ₽ — 3 000 ₽'

def cols(*c): return list(zip(*c))

# (id, заголовок, подзаголовок, описание[], таблица{head, rows}, сноски[], css-класс)
S = [
  ('keratin', 'Кератиновое выпрямление · Ботокс для волос', '', [
    '<b>Кератиновое выпрямление</b> — процедура, которая выпрямит волосы от лёгких волн до тугих завитков и избавит от пористости. Срок носки после первой процедуры 3–4 месяца, при накопительном эффекте — до 6 месяцев.',
    '<b>Ботокс для волос</b> — процедура, которая поможет избавиться от пушистости, разгладит волосы и сделает их более послушными, возможно выпрямление лёгкого завитка. Срок носки — до 3 месяцев.'],
   (LVL3, L9, cols([7000, 7500, 8000, 8500, 9000, 10000, 11000, 12000, 13000], [8500, 9000, 9500, 10000, 11000, 12000, 13000, 14000, 15000], step(11000, 1000))),
   [JULIA, O70, DENS, SUB, EXT], ''),
  ('nano', 'Нанопластика', 'в технике «полуперманент»', [
    'Процедура с самым сильным выпрямлением. Предназначена для волос хорошего качества, для выпрямления тугого завитка и гормональной волны.',
    'Волосы выпрямляются НАВСЕГДА, кудрявыми будут отрастать только корни. Техника «полуперманент» позволяет не только выпрямить, но и укрепить эффект более плотной плёнкой, что позволяет волосам больше сохранять мягкость и гладкость.'],
   (LVL3, L9, cols(step(11000, 1000), step(13000, 1000), step(16000, 1000))), [JULIA, O70, DENS, EXT], ''),
  ('total', 'Тотальная реконструкция', 'если у вас блонд либо сильно повреждённые волосы', [
    'Включает в себя холодную реконструкцию при помощи 2-х подложек (белковая и липидная) и закрытие горячей процедурой кератин/ботокс.'],
   (LVL3, L9, cols(step(11000, 1000), step(13000, 1000), step(16000, 1000))), [JULIA, O70, DENS, EXT], ''),
  ('disc', 'Разглаживание и дисциплина', 'new', [
    'Облегчённая процедура на базе ботокса с минимальными испарениями. Подойдёт тем, кому не нужна идеальная гладкость, кто предпочитает более натуральный эффект ухоженных волос без утяжеления, а также тем, кто любит объёмные укладки на стайлеры.',
    'Разглаживает лёгкую волну, устраняет несильную пушистость. Придаёт волосам мягкость, блеск, рассыпчатость и послушность. Срок носки 1,5–3 месяца в зависимости от типа волос. Имеет накопительный эффект.'],
   (LVL3, L9, cols([6000, 6500, 7000, 7500, 8000, 8500, 9000, 10000, 11000], [7500, 8000, 8500, 9000, 9500, 10000, 11000, 12000, 13000], [10000, 10500, 11000, 11500, 12000, 13000, 14000, 15000, 16000])),
   [JULIA, O70, DENS, SUB, EXT], ''),
  ('lebel', 'Абсолютное счастье для волос', 'от премиального японского бренда LEBEL', [
    'Комплексный спа-уход, состоящий из 12 последовательных шагов, направленный на восстановление и питание волос и уход за кожей головы.'],
   (LVL3, L4, cols([5000, 7000, 9000, 10000], [6000, 8000, 10000, 11000], [7000, 9000, 11500, 13000])), [JULIA, O70] + DENS_S, ''),
  ('cold', 'Комплексное холодное восстановление', '', [
    'Многоступенчатый холодный уход, направленный на восстановление повреждённых волос, увлажнение и питание. Не выпрямляет и не меняет структуру волос.',
    'Включает в себя белковую и липидную подложку и закрывается ламинирующим ботоксом. Срок носки до 4–6 недель. Имеет накопительный эффект.'],
   (LVL3, L9, cols([6000, 6500, 7000, 7500, 8000, 8500, 9000, 10000, 11000], [7500, 8000, 8500, 9000, 9500, 10000, 11000, 12000, 13000], [10000, 10500, 11000, 11500, 12000, 13000, 14000, 15000, 16000])),
   [JULIA, O70] + DENS_S + [EXT], ''),
  ('cbotox', 'Холодный ботокс', '', [
    'Насыщает волосы липидами и увлажняющими компонентами, делая их более упругими, плотными и блестящими. Не выпрямляет волосы. Подходит для всех типов волос. Срок носки — 2–4 недели.'],
   (LVL3, L4, cols([4000, 6000, 8000, 9000], [5000, 7000, 9000, 10000], [6000, 8000, 10000, 12000])), [JULIA, O70] + DENS_S, ''),
  ('peeling', 'Пилинг кожи головы', '', [
    'Диагностика кожи головы при помощи трихоскопа, процедура пилинга, массаж кожи головы, увлажняющая/питательная маска для волос.'],
   (None, ['Стоимость пилинга', 'Стоимость пилинга в комплексе с любой другой процедурой'], [(3500,), (2000,)]), [], ''),
  ('polishing', 'Комплексная стрижка (полировка) волос против сечения', 'комплекс мер, направленный на устранение сечения и ломкости по полотну без потери длины и густоты', [],
   (['Мастер', 'ТОП-мастер<small>Яна, Полина</small>'], ['до 50 см', 'свыше 50 см', '<b>В комплексе</b> с другими процедурами, до 50 см', '<b>В комплексе</b>, свыше 50 см'], [(4000, 5000), (5000, 6000), (2000, 2500), (2500, 3000)]),
   ['*густота свыше 10 см — 1 000 ₽',
    '<b>Процедура включает в себя:</b> детокс — очищение кожи головы; экспресс-spa-уход для волос; сушку волос; чистку полотна от сечения (сочетание машинной и ручной техники); ровный срез кончиков.'], ''),
  ('afro', 'Выпрямление АФРО', '', [
    'Выполняется в технике полуперманент.',
    'Стоимость рассчитывается индивидуально после очной консультации в студии либо по актуальной фотографии ваших волос.'],
   (None, ['Короткие волосы (до 30 см)'], [('от 20 000 ₽',)]), ['*в стоимость включена услуга в четыре руки по вашему желанию.'], ''),
  # ── окрашивание убирают с 01.01.2027: удалить два блока с классом coloring ──
  ('coloring-complex', 'Комплекс окрашивание | тонирование + холодный ампульный ботокс', '', [
    '<b>В услугу включено:</b> мытьё волос; процедура окрашивания | тонирования; уход: холодный ампульный ботокс (глубокое увлажнение и питание волос, без выпрямления); сушка.'],
   (None, ['Корни (до 2-х см)', 'Короткие волосы (до 35 см)', 'Средние волосы (до 50 см)', 'Длинные волосы (свыше 50 см)'], [(7500,), (9000,), (10500,), (12500,)]),
   ['свыше 65 см / густые волосы (свыше 9 см в обхвате) — +1 000 ₽'], 'coloring'),
  ('coloring', 'Окрашивание в 1 тон | тонирование', '*без осветления', [
    '<b>В услугу включено:</b> мытьё волос; процедура окрашивания | тонирования; базовый уход; сушка.'],
   (None, ['Корни (до 2-х см)', 'Короткие волосы (до 35 см)', 'Средние волосы (до 50 см)', 'Длинные волосы (свыше 50 см)'], [(5000,), (6500,), (8500,), (9500,)]),
   ['свыше 65 см / густые волосы (свыше 9 см в обхвате) — +1 000 ₽'], 'coloring'),
  ('extra', 'Дополнительные услуги', '', [],
   (None, ['Услуга «в 4 руки»', 'Выпрямление чёлки', 'Коррекция корней (до 10 см)', 'Стрижка кончиков совместно с любой из процедур', 'Стрижка кончиков отдельной процедурой'],
    [('+5 000 ₽ к прайсу',), (4000,), ('70% от полной стоимости работы',), (500,), (1500,)]), [], ''),
  ('density', 'Доплата за густоту', 'обхват хвоста', [],
   (None, ['до 6 см', '7–8 см', '9–10 см', '11–12 см', 'от 13 см'], [('без доплат',), (1000,), (1500,), (2000,), (3000,)]), [], ''),
  ('substrate', 'Подложка', '', ['*выполняется на осветлённые, повреждённые волосы либо на любые волосы по вашему желанию как дополнительный уход и защита'],
   (None, ['до 50 см', 'от 50 см'], [(2000,), (3000,)]), [], ''),
  ('extensions', 'Наращённые волосы', '', [],
   (None, ['до 100 капсул', 'до 200 капсул', 'свыше 200 капсул'], [(1500,), (2000,), (3000,)]), [], ''),
]
NAV = [('keratin', 'Кератин · ботокс'), ('nano', 'Нанопластика'), ('total', 'Реконструкция'), ('disc', 'Разглаживание'), ('lebel', 'Lebel'),
       ('cold', 'Холодное восстановление'), ('cbotox', 'Холодный ботокс'), ('peeling', 'Пилинг'), ('polishing', 'Комплексная стрижка'), ('afro', 'Афро'),
       ('coloring-complex', 'Окрашивание'), ('extra', 'Доп. услуги'), ('offer-complex', 'Акция')]

def money(v):
    return v if isinstance(v, str) else f'{v:,}'.replace(',', ' ') + ' ₽'

def table(t):
    head, labels, rows = t
    th = ''.join(f'<th scope="col">{h}</th>' for h in head) if head else ''
    body = ''.join(f'<tr><th scope="row">{l}</th>' + ''.join(f'<td>{money(v)}</td>' for v in r) + '</tr>' for l, r in zip(labels, rows))
    cls = 'grid' if head else 'list'
    return f'<table class="{cls}">' + (f'<thead><tr><th scope="col">Длина волос</th>{th}</tr></thead>' if head else '') + f'<tbody>{body}</tbody></table>'

def section(sid, title, sub, desc, tab, notes, cls):
    sub_html = '<span class="new">new!</span>' if sub == 'new' else (f'<span class="sub">{sub}</span>' if sub else '')
    notes_html = ('<ul class="notes">' + ''.join(f'<li>{n}</li>' for n in notes) + '</ul>') if notes else ''
    remark = '<!-- окрашивание убирают с 01.01.2027 -->' if cls else ''
    return f'''{remark}<section class="p {cls}" id="{sid}"><h2>{title}{sub_html}</h2>{''.join(f'<p>{d}</p>' for d in desc)}{table(tab)}{notes_html}</section>\n'''

BODY = ''.join(section(*s) for s in S) + '''<section class="p deal" id="offer-complex"><h2>Акция «Комплекс»</h2>
<p>Скидка на комплексную стрижку (полировку) волос против сечения и пилинг кожи головы при проведении в комплексе с другими процедурами.</p>
<table class="list"><tbody><tr><th scope="row">Комплексная стрижка, до 50 см</th><td><s>4 000 ₽</s> 2 000 ₽</td></tr><tr><th scope="row">Комплексная стрижка, свыше 50 см</th><td><s>5 000 ₽</s> 2 500 ₽</td></tr><tr><th scope="row">Пилинг в комплексе</th><td><s>3 500 ₽</s> 2 000 ₽</td></tr></tbody></table>
<ul class="notes"><li>цены комплексной стрижки — у мастера; у ТОП-мастера в комплексе 2 500 / 3 000 ₽</li></ul></section>
'''

MAIN = f'''<main class="wrap">
<div class="intro">
  <a class="back" href="../">← На главную</a>
  <h1>Прайс-лист</h1>
  <p class="date">действует с 1 марта 2026 года</p>
  <div class="lead">
    <p>Стоимость процедуры определяется исходя из длины и густоты волос.</p>
    <p>Перед началом процедуры мастер измерит длину и густоту ваших волос и озвучит точную стоимость услуги в соответствии с прайсом, <b>обязательно до начала работы</b>, на этапе консультации.</p>
    <p>Подбор составов и продуктов, на которых будет выполнена услуга, проводится мастером индивидуально в зависимости от вашего типа волос и пожеланий по результату. Выбор конкретных продуктов и составов не влияет на стоимость.</p>
  </div>
  <div class="cta"><a class="btn fill" href="{DIKIDI}" target="_blank" rel="noopener">Записаться онлайн</a><a class="btn" href="../#calc">Рассчитать по длине</a></div>
</div>
<nav class="toc" aria-label="Разделы прайса">{''.join(f'<a href="#{i}">{n}</a>' for i, n in NAV)}</nav>
{BODY}
</main>'''

FOOT = '''<footer><div class="wrap"><span>ИП Матковская Ю. В. · ИНН 774322019399 · <a href="tel:+79057025612">+7 (905) 702-56-12</a></span>
<nav aria-label="Документы"><a href="../">Главная</a><a href="../policy/">Политика конфиденциальности</a><a href="../offer/">Оферта</a></nav></div></footer>'''

HEAD = '''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
{icons}<style>
{fonts}
{base}
{skin}
</style>
</head>
<body>
<header class="top"><div class="wrap"><a class="logo" href="{home}" aria-label="Кератин Сторис, на главную"><img src="{img}logo.png" alt="KS Keratin Stories" width="700" height="461"></a>
<a class="btn sm fill" href="''' + DIKIDI + '''" target="_blank" rel="noopener">Записаться</a></div></header>
'''

# общая раскладка; отличия вариантов — в SKIN
BASE = '''* { box-sizing: border-box; margin: 0; }
html { scroll-padding-top: 150px; }
body { background: var(--bg); color: var(--tx); font: 400 16px/1.6 var(--sans); }
a { color: inherit; text-decoration: none; }
img { display: block; max-width: 100%; height: auto; }
:focus-visible { outline: 2px solid var(--tx); outline-offset: 3px; }
.wrap { max-width: 900px; margin: 0 auto; padding: 0 16px; }
.top { position: sticky; top: 0; z-index: 10; background: var(--bar); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border-bottom: 1px solid var(--line); }
.top .wrap { display: flex; justify-content: space-between; align-items: center; height: 60px; max-width: 1200px; }
.logo { width: 56px; }
h1, h2 { font-family: var(--serif); font-weight: 400; }
.intro { padding: 40px 0 26px; }
.back { font-size: 14px; color: var(--mute); }
h1 { font-size: clamp(44px, 9vw, 84px); line-height: 1.05; margin: 14px 0 4px; padding-bottom: .06em; }
.date { color: var(--mute); margin-bottom: 22px; }
.lead p { color: var(--soft); margin-bottom: 10px; max-width: 680px; }
.lead b { color: var(--tx); font-weight: 600; }
.cta { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 22px; }
.btn { display: inline-flex; align-items: center; justify-content: center; min-height: 46px; padding: 10px 22px; border: 1px solid var(--tx); border-radius: var(--r); font-weight: 500; font-size: 15px; transition: background .3s, color .3s; }
.btn:hover, .btn.fill { background: var(--tx); color: var(--bg); }
.btn.fill:hover { background: transparent; color: var(--tx); }
.btn.sm { min-height: 38px; padding: 6px 16px; font-size: 14px; }
.toc { position: sticky; top: 60px; z-index: 9; display: flex; gap: 8px; overflow-x: auto; scrollbar-width: none; padding: 12px 16px; margin: 0 -16px; background: var(--bar); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border-bottom: 1px solid var(--line); }
.toc::-webkit-scrollbar { display: none; }
.toc a { flex: none; padding: 6px 14px; border: 1px solid var(--line); border-radius: var(--r); font-size: 14px; white-space: nowrap; transition: border-color .3s, background .3s, color .3s; }
.toc a:hover, .toc a.on { border-color: var(--tx); }
.toc a.on { background: var(--tx); color: var(--bg); }
.p { padding: 44px 0 10px; border-bottom: 1px solid var(--line); }
.p h2 { font-size: clamp(28px, 4.6vw, 40px); line-height: 1.12; margin-bottom: 14px; padding-bottom: .05em; }
.p h2 .sub { display: block; font: 400 15px var(--sans); color: var(--mute); margin-top: 6px; }
.p h2 .new { margin-left: 10px; font: italic 500 18px var(--serif); color: var(--accent); }
.p > p { color: var(--soft); margin-bottom: 10px; }
.p > p b { color: var(--tx); font-weight: 600; }
table { width: 100%; border-collapse: collapse; margin: 18px 0 8px; font-variant-numeric: tabular-nums; }
th, td { padding: 11px 6px; border-bottom: 1px solid var(--line); text-align: right; font-weight: 400; white-space: nowrap; }
th[scope=row] { text-align: left; white-space: normal; color: var(--soft); }
thead th { font-size: 13px; color: var(--mute); vertical-align: bottom; line-height: 1.25; }
thead th small { display: block; font-size: 11px; }
thead th:first-child { text-align: left; }
td { font-weight: 500; }
table.list td { white-space: normal; }
td s { color: var(--mute); font-weight: 400; margin-right: 6px; }
.notes { list-style: none; padding: 0; margin: 6px 0 24px; font-size: 14px; color: var(--mute); display: grid; gap: 4px; }
.notes b { color: var(--soft); }
.deal { border-bottom: 0; }
footer { border-top: 1px solid var(--line); margin-top: 50px; padding: 26px 0 36px; font-size: 13px; color: var(--mute); }
footer .wrap { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px 30px; max-width: 1200px; }
footer nav { display: flex; flex-wrap: wrap; gap: 6px 20px; } footer a:hover { color: var(--tx); }
@media (max-width: 520px) { th, td { padding: 10px 3px; font-size: 14px; } thead th { font-size: 11px; } }
@media (prefers-reduced-motion: reduce) { * { transition: none !important; } }'''

PRICE_T = 'Прайс-лист — Кератин Сторис'
PRICE_D = 'Цены на кератиновое выпрямление, ботокс, нанопластику, реконструкцию и уходы для волос. Прайс действует с 1 марта 2026 года.'
# иконки — родные с её Tilda (светлая/тёмная тема, apple-touch); пока только v2
ICONS = '''<link rel="icon" href="{root}favicon.ico" sizes="any" media="(prefers-color-scheme: light)">
<link rel="icon" href="{img}favicon-dark.png" type="image/png" media="(prefers-color-scheme: dark)">
<link rel="apple-touch-icon" href="{img}apple-touch-icon.png">
'''

SCRIPT = '''<script>
// подсветка текущего раздела в оглавлении
const links = [...document.querySelectorAll('.toc a')], map = new Map(links.map(a => [a.hash.slice(1), a]));
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { links.forEach(a => a.classList.remove('on')); const a = map.get(e.target.id); if (a) { a.classList.add('on'); a.scrollIntoView({ block: 'nearest', inline: 'center' }); } } }), { rootMargin: '-140px 0px -70% 0px' });
document.querySelectorAll('.p[id]').forEach(s => map.has(s.id) && io.observe(s));
</script>'''

V = {
  'v2': dict(img='../img/', icons=ICONS, fonts=(ROOT / 'v2/index.html').read_text(encoding='utf-8'),
    skin=''':root { --bg: #161616; --tx: #f2efea; --mute: #a19c96; --soft: #d4cfc9; --line: rgba(242,239,234,.16); --bar: rgba(22,22,22,.9); --accent: #f2efea; --r: 0;
  --serif: 'Cormorant Garamond', Georgia, serif; --sans: Montserrat, system-ui, sans-serif; }
body { font-weight: 300; } .btn { font: 600 17px 'Cormorant Garamond', Georgia, serif; } .btn.sm { font-size: 16px; }'''),
  'v3': dict(img='../../v2/img/', fonts=(ROOT / 'v3/index.html').read_text(encoding='utf-8'),
    skin=''':root { --bg: #111112; --tx: #f3f1ee; --mute: #9e9a95; --soft: #d4cfc9; --line: rgba(243,241,238,.14); --bar: rgba(17,17,18,.88); --accent: #b8a6e0; --r: 999px;
  --serif: 'Playfair Display', Georgia, serif; --sans: 'Golos Text', system-ui, sans-serif; }
h1 { font-style: italic; } .p h2 { letter-spacing: -.01em; }'''),
}

# прайс обеих версий — build_price() ниже

# 404/offer/policy — для обеих версий; пути от корня домена (сервер отдаёт с любого адреса),
# в превью под /d/.../v2|v3/ картинки/фонты по этим путям не грузятся — это ок, страницы не для превью.
# offer/policy — временная заглушка (та же 404), пока не добыт юридический текст с Tilda.
ROBOTS = 'User-agent: *\nDisallow:\n\nSitemap: https://www.keratinstories.ru/sitemap.xml\n'
SITEMAP = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.keratinstories.ru/</loc></url>
  <url><loc>https://www.keratinstories.ru/price/</loc></url>
  <url><loc>https://www.keratinstories.ru/offer/</loc></url>
  <url><loc>https://www.keratinstories.ru/policy/</loc></url>
</urlset>
'''
for name, v in V.items():
    faces = '\n'.join(l for l in v['fonts'].splitlines() if l.startswith('@font-face')).replace('url(fonts/', 'url(/fonts/')
    NF = '''<main class="wrap nf"><h1>Страница не найдена</h1>
<p class="lead">Возможно, адрес изменился — сайт студии обновился. Все услуги и цены теперь на главной и в прайсе.</p>
<div class="cta"><a class="btn fill" href="/">На главную</a><a class="btn" href="/price/">Прайс-лист</a></div></main>
<style>.nf { padding: 80px 16px 40px; min-height: 60vh; } .nf .lead { color: var(--soft); max-width: 560px; margin-top: 16px; }</style>'''
    html = HEAD.format(fonts=faces, base=BASE, skin=v['skin'], img='/img/', home='/', title='Страница не найдена — Кератин Сторис', desc='Страница не найдена', icons=ICONS.format(img='/img/', root='/')) + NF + '\n' + FOOT.replace('../', '/') + '\n</body>\n</html>\n'
    (ROOT / name / '404.html').write_text(html, encoding='utf-8')
    print(ROOT / name / '404.html', len(html))
    for stub in ('offer', 'policy'):
        d = ROOT / name / stub
        d.mkdir(exist_ok=True)
        (d / 'index.html').write_text(html, encoding='utf-8')
        print(d / 'index.html', len(html))
    (ROOT / name / 'robots.txt').write_text(ROBOTS, encoding='utf-8')
    (ROOT / name / 'sitemap.xml').write_text(SITEMAP, encoding='utf-8')

# ═══════════ v2: прайс, новый дизайн (2026-11-06) ═══════════
# Одна шкала «Мастер / ТОП-мастер / Юлия» на всю страницу вместо трёх колонок в каждой таблице;
# услуги сгруппированы, у основных — фото с главной. Данные — те же S.
SD = {x[0]: x for x in S}
PHOTO = {'keratin': 's-keratin', 'nano': 's-nano', 'total': 's-total', 'disc': 's-disc', 'afro': 's-afro', 'lebel': 's-lebel', 'cold': 's-cold'}
GROUPS = [
  ('straight', 'Выпрямление и разглаживание', ['keratin', 'total', 'nano', 'disc', 'afro'], ''),
  ('care', 'Восстановление и уход', ['lebel', 'cold', 'cbotox', 'polishing', 'peeling'], ''),
  ('color', 'Окрашивание', ['coloring-complex', 'coloring'], 'coloring'),  # убрать с 01.01.2027: удалить группу
  ('add', 'Доплаты и дополнительные услуги', ['density', 'substrate', 'extensions', 'extra'], ''),
]
TOC2 = {'keratin': 'Кератин · ботокс', 'nano': 'Нанопластика', 'disc': 'Разглаживание и дисциплина', 'total': 'Тотальная реконструкция', 'afro': 'Выпрямление афро',
        'lebel': 'Счастье для волос Lebel', 'cold': 'Холодное восстановление', 'cbotox': 'Холодный ботокс', 'polishing': 'Комплексная стрижка', 'peeling': 'Пилинг кожи головы',
        'coloring-complex': 'Окрашивание + ботокс', 'coloring': 'Окрашивание в 1 тон', 'density': 'Доплата за густоту', 'substrate': 'Подложка',
        'extensions': 'Наращённые волосы', 'extra': 'Доп. услуги'}

def lv(vals):
    """цена по трём уровням: показываем одну, переключает body[data-lvl]"""
    return ''.join(f'<b class="l{i}">{money(v)}</b>' for i, v in enumerate(vals))

def card2(sid, img='../img/'):
    _, title, sub, desc, (head, labels, rows), notes, _ = SD[sid]
    notes = [n for n in notes if n != JULIA]
    over70 = O70 in notes
    notes = [n for n in notes if n != O70]
    if head == LVL3:
        items = ''.join(f'<li><span>{l}</span><i></i>{lv(r)}</li>' for l, r in zip(labels, rows))
        if over70: items += '<li class="ind"><span>свыше 70 см</span><i></i><b>индивидуально</b></li>'
        frm = '<p class="from">от ' + lv([min(r[i] for r in rows) for i in range(3)]) + '</p>'
        plist = f'<ul class="pl lvl3">{items}</ul>'
    elif head:  # полировка: два уровня, показываем оба
        hd = ''.join(f'<span>{h.split("<small>")[0]}</span>' for h in head)
        items = ''.join(f'<li><span>{l}</span><i></i>' + ''.join(f'<b>{money(v)}</b>' for v in r) + '</li>' for l, r in zip(labels, rows))
        frm = f'<p class="from">от {money(min(min(r) for r in rows))}</p>'
        plist = f'<div class="two"><div class="th"><span></span>{hd}</div><ul class="pl">{items}</ul></div>'
    else:
        items = ''.join(f'<li><span>{l}</span><i></i><b{" class=w" if len(money(r[0])) > 14 else ""}>{money(r[0])}</b></li>' for l, r in zip(labels, rows))
        frm, plist = '', f'<ul class="pl">{items}</ul>'
    tag = '<span class="new">New</span>' if sub == 'new' else ''
    sub_html = f'<p class="sub">{sub}</p>' if sub and sub != 'new' else ''
    desc_html = ''.join(f'<p>{d}</p>' for d in desc)
    notes_html = ('<ul class="nt">' + ''.join(f'<li>{n}</li>' for n in notes) + '</ul>') if notes else ''
    ph = PHOTO.get(sid)
    pic = f'<div class="ph"><img src="{img}{ph}.jpg" alt="" loading="lazy" width="900" height="900">{tag}</div>' if ph else ''
    act = f'<div class="act"><a class="btn sm fill" href="{DIKIDI}" target="_blank" rel="noopener">Записаться</a>' + \
          ('<a class="link" href="../#calc">Рассчитать по длине</a>' if head == LVL3 and labels == L9 else '') + '</div>' if ph or head else ''
    cls = 'card' + (' big' if ph else '') + (' wide' if sid in ('extra',) else '')
    return f'''<article class="{cls}" id="{sid}">{pic}<div class="bd">
<div class="hd"><h3>{title}{tag if not ph else ''}</h3>{frm}</div>{sub_html}{desc_html}{plist}{notes_html}{act}</div></article>\n'''

def group2(gid, name, ids, cls, img='../img/'):
    rem = '<!-- окрашивание убирают с 01.01.2027: удалить эту секцию и пункт в оглавлении -->\n' if cls else ''
    return f'{rem}<section class="grp {cls}" id="{gid}" aria-labelledby="{gid}-h"><h2 id="{gid}-h">{name}</h2>\n' + ''.join(card2(i, img) for i in ids) + '</section>\n'

TOC_HTML = ''.join(
    f'<div class="tg{" " + c if c else ""}"><a class="tgh" href="#{g}">{n}</a>' + ''.join(f'<a href="#{i}">{TOC2[i]}</a>' for i in ids) + '</div>'
    for g, n, ids, c in GROUPS) + '<div class="tg"><a class="tgh" href="#deal">Акция «Комплекс»</a></div>'
CHIPS = ''.join(f'<a class="{c}" href="#{g}">{n}</a>' for g, n, ids, c in GROUPS) + '<a href="#deal">Акция</a>'

P2_CSS = '''
:root { --bg: #161616; --card: #1e1e1e; --card2: #2a2a2a; --tx: #f2efea; --mute: #a19c96; --soft: #d4cfc9; --line: rgba(242,239,234,.14); --ease: cubic-bezier(.22,1,.36,1); }
* { box-sizing: border-box; margin: 0; }
html { scroll-behavior: smooth; scroll-padding-top: 84px; }
body { background: var(--bg); color: var(--tx); font: 300 16px/1.65 Montserrat, system-ui, sans-serif; overflow-x: hidden; }
a { color: inherit; text-decoration: none; }
img { display: block; max-width: 100%; height: auto; }
button { font: inherit; color: inherit; }
:focus-visible { outline: 2px solid var(--tx); outline-offset: 3px; }
.wrap { max-width: 1200px; margin: 0 auto; padding: 0 16px; }
h1, h2, h3 { font-family: 'Cormorant Garamond', Georgia, serif; font-weight: 400; padding-bottom: .06em; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; min-height: 48px; padding: 12px 26px; border: 1px solid var(--tx); background: transparent; cursor: pointer;
       font: 600 18px/1.2 'Cormorant Garamond', Georgia, serif; letter-spacing: .02em; text-align: center; transition: background .35s var(--ease), color .35s var(--ease); }
.btn:hover { background: var(--tx); color: var(--bg); }
.btn.fill { background: var(--tx); color: var(--bg); } .btn.fill:hover { background: transparent; color: var(--tx); }
.btn.sm { min-height: 40px; padding: 8px 18px; font-size: 16px; }
.link { font-size: 14px; border-bottom: 1px solid var(--line); padding-bottom: 2px; transition: border-color .3s; } .link:hover { border-bottom-color: var(--tx); }

/* шапка — как на главной */
.top { position: fixed; z-index: 40; inset: 0 0 auto; background: rgba(22,22,22,.9); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); box-shadow: 0 1px 0 var(--line); }
.top .wrap { display: flex; align-items: center; gap: 24px; height: 64px; }
.logo { width: 64px; flex: none; }
.top nav { display: flex; gap: 22px; margin-left: auto; font-size: 14px; }
.top nav a { opacity: .85; transition: opacity .3s; } .top nav a:hover, .top nav a[aria-current] { opacity: 1; }
.top nav a[aria-current] { border-bottom: 1px solid var(--tx); }
.burger { display: none; width: 44px; height: 44px; margin-left: auto; background: none; border: 0; cursor: pointer; position: relative; }
.burger i { position: absolute; left: 10px; right: 10px; height: 1px; background: currentColor; transition: transform .4s var(--ease); }
.burger i:first-child { top: 18px; } .burger i:last-child { top: 25px; }
.burger[aria-expanded=true] i:first-child { transform: translateY(3.5px) rotate(45deg); } .burger[aria-expanded=true] i:last-child { transform: translateY(-3.5px) rotate(-45deg); }

/* вступление */
.intro { padding: 130px 0 56px; text-align: center; }
.kick { font-size: 12px; font-weight: 500; letter-spacing: .2em; text-transform: uppercase; color: var(--mute); }
h1 { font-size: clamp(54px, 9vw, 104px); line-height: 1; margin: 14px 0 34px; }
.rules { padding: 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: var(--line); border: 1px solid var(--line); text-align: left; max-width: 1040px; margin: 0 auto; }
.rules li { list-style: none; background: var(--bg); padding: 22px 24px 24px; font-size: 14px; color: var(--soft); }
.rules em { display: block; font: italic 400 30px/1 'Cormorant Garamond', serif; color: var(--mute); margin-bottom: 12px; }
.rules b { color: var(--tx); font-weight: 500; }
.intro .cta { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin-top: 32px; }

/* раскладка: слева шкала мастера и оглавление, справа прайс */
.lay { display: grid; grid-template-columns: 250px 1fr; gap: 56px; align-items: start; }
.side { position: sticky; top: 88px; display: grid; gap: 26px; max-height: calc(100svh - 104px); overflow-y: auto; scrollbar-width: none; padding-bottom: 10px; }
.side::-webkit-scrollbar { display: none; }
.lvl { border: 0; padding: 0; }
.lvl legend { font-size: 12px; font-weight: 500; letter-spacing: .2em; text-transform: uppercase; color: var(--mute); margin-bottom: 10px; }
.lvl .opts { display: grid; gap: 6px; }
.lvl label { position: relative; display: block; padding: 10px 14px; border: 1px solid var(--line); cursor: pointer; font-size: 15px; line-height: 1.25; transition: border-color .3s, background .3s, color .3s; }
.lvl label:hover { border-color: var(--tx); }
.lvl small { display: block; font-size: 12px; color: var(--mute); transition: color .3s; }
.lvl input { position: absolute; opacity: 0; pointer-events: none; }
.lvl label:has(input:checked) { background: var(--tx); color: var(--bg); border-color: var(--tx); }
.lvl label:has(input:checked) small { color: #5d5853; }
.lvl label:has(input:focus-visible) { outline: 2px solid var(--tx); outline-offset: 3px; }
.lvl .jn { font-size: 12px; color: var(--mute); margin-top: 8px; }
.toc { display: grid; gap: 16px; font-size: 14px; }
.tg { display: grid; gap: 2px; }
.tg a { color: var(--mute); padding: 3px 0 3px 14px; border-left: 1px solid var(--line); transition: color .3s, border-color .3s; }
.tg a:hover { color: var(--tx); }
.tg a.on { color: var(--tx); border-left-color: var(--tx); }
.tg .tgh { font: 400 20px/1.15 'Cormorant Garamond', serif; color: var(--tx); border: 0; padding: 0 0 4px; }
.chips { display: none; }

/* группы и карточки */
.grp { padding-bottom: 40px; }
.grp + .grp { padding-top: 34px; }
.grp h2 { font-size: clamp(38px, 5vw, 56px); line-height: 1.05; margin-bottom: 22px; }
.card { background: var(--card); margin-bottom: 14px; padding: 26px 28px 24px; }
.card.big { display: grid; grid-template-columns: 210px 1fr; gap: 30px; padding: 16px 28px 24px 16px; }
.ph { position: relative; aspect-ratio: 1; overflow: hidden; background: var(--card2); align-self: start; }
.ph img { width: 100%; height: 100%; object-fit: cover; }
.new { display: inline-block; vertical-align: middle; margin-left: 10px; background: var(--tx); color: var(--bg); font: 600 11px/1 Montserrat, sans-serif; letter-spacing: .14em; text-transform: uppercase; padding: 6px 9px; }
.ph .new { position: absolute; top: 10px; left: 10px; margin: 0; }
.bd { min-width: 0; padding-top: 8px; }
.hd { display: flex; justify-content: space-between; align-items: baseline; gap: 8px 20px; flex-wrap: wrap; }
.card h3 { font-size: clamp(26px, 3vw, 32px); line-height: 1.1; }
.from { font: 400 24px/1.1 'Cormorant Garamond', serif; white-space: nowrap; }
.from b { font-weight: 500; }
.sub { font: italic 400 18px/1.3 'Cormorant Garamond', serif; color: var(--mute); margin-top: 4px; }
.bd > p:not(.sub) { font-size: 14.5px; color: var(--soft); margin-top: 10px; max-width: 640px; }
.bd > p b { color: var(--tx); font-weight: 500; }
.pl { list-style: none; padding: 0; margin: 18px 0 0; font-variant-numeric: tabular-nums; }
.pl.lvl3 { columns: 2; column-gap: 34px; }
.pl li { display: flex; align-items: baseline; gap: 10px; padding: 7px 0; break-inside: avoid; font-size: 15px; }
.pl span { color: var(--soft); }
.pl i { flex: 1; min-width: 16px; border-bottom: 1px dotted rgba(242,239,234,.28); transform: translateY(-4px); }
.pl b { font-weight: 500; white-space: nowrap; text-align: right; }
.pl b.w { white-space: normal; max-width: 48%; }
.pl li.ind b { font-weight: 400; color: var(--mute); }
.two .th { display: grid; grid-template-columns: 1fr 96px 96px; gap: 10px; margin-top: 18px; font-size: 12px; color: var(--mute); text-align: right; }
.two .pl { margin-top: 4px; } .two .pl li { display: grid; grid-template-columns: 1fr 96px 96px; gap: 10px; } .two .pl i { display: none; }
.two .pl span b { font-weight: 500; color: var(--tx); }
.nt { list-style: none; padding: 0; margin: 14px 0 0; font-size: 13px; color: var(--mute); display: grid; gap: 3px; }
.nt b { color: var(--soft); font-weight: 500; }
.act { display: flex; flex-wrap: wrap; align-items: center; gap: 12px 22px; margin-top: 20px; }
.grp#add { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0 14px; } .grp#add h2, .grp#add .wide { grid-column: 1 / -1; }
.grp#color { display: grid; grid-template-columns: 1fr 1fr; gap: 0 14px; } .grp#color h2 { grid-column: 1 / -1; }

/* шкала мастера: видна одна цена из трёх */
.l1, .l2 { display: none; }
body[data-lvl="1"] .l0, body[data-lvl="2"] .l0 { display: none; }
body[data-lvl="1"] .l1, body[data-lvl="2"] .l2 { display: inline; }

/* акция — как на главной */
.deal { background: var(--card); padding: clamp(28px, 5vw, 56px); text-align: center; margin: 30px 0 0; }
.deal .k { font: italic 400 24px 'Cormorant Garamond', serif; color: var(--mute); }
.deal h2 { font-size: clamp(40px, 6vw, 60px); letter-spacing: .04em; text-transform: uppercase; line-height: 1.05; margin: 2px 0 14px; }
.deal > p { max-width: 520px; margin: 0 auto; color: var(--soft); }
.deal ul { list-style: none; padding: 0; max-width: 560px; margin: 22px auto 0; text-align: left; }
.deal li { display: flex; justify-content: space-between; gap: 16px; padding: 13px 0; border-bottom: 1px solid var(--line); }
.deal s { color: var(--mute); margin-right: 8px; } .deal li b { font-weight: 600; white-space: nowrap; }
.deal .nt { margin-top: 14px; text-align: center; } .deal .nt li { display: block; border: 0; padding: 0; }

footer { border-top: 1px solid var(--line); margin-top: 80px; padding: 30px 0 40px; font-size: 13px; color: var(--mute); }
footer .wrap { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 14px 30px; }
footer nav { display: flex; flex-wrap: wrap; gap: 6px 20px; } footer a:hover { color: var(--tx); }
.up { position: fixed; right: 16px; bottom: 16px; z-index: 30; width: 46px; height: 46px; border: 1px solid var(--line); background: rgba(22,22,22,.85); cursor: pointer; font-size: 18px; opacity: 0; pointer-events: none; transition: opacity .3s, border-color .3s; }
.up.show { opacity: 1; pointer-events: auto; } .up:hover { border-color: var(--tx); }

@media (max-width: 1000px) {
  .top nav { display: none; position: fixed; inset: 64px 0 auto; flex-direction: column; gap: 0; padding: 8px 16px 20px; background: rgba(22,22,22,.97); font-size: 18px; }
  .top nav.open { display: flex; } .top nav a { padding: 12px 0; border-bottom: 1px solid var(--line); } .top nav a[aria-current] { border-bottom-color: var(--line); }
  .burger { display: block; } .top .wrap > .btn { display: none; }
  html { scroll-padding-top: 136px; }
  .lay { display: block; }
  .side { display: contents; }
  .lvl { position: sticky; top: 64px; z-index: 20; background: rgba(22,22,22,.94); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); margin: 0 -16px; padding: 10px 16px; border-bottom: 1px solid var(--line); }
  .lvl legend { float: left; width: 100%; font-size: 11px; margin-bottom: 6px; }
  .lvl .opts { grid-template-columns: repeat(3, 1fr); clear: both; }
  .lvl label { text-align: center; padding: 8px 4px; font-size: 14px; }
  .lvl small { font-size: 10.5px; }
  .lvl .jn { display: none; }
  .toc { display: none; }
  .chips { display: flex; gap: 8px; overflow-x: auto; scrollbar-width: none; margin: 18px -16px 26px; padding: 0 16px; }
  .chips::-webkit-scrollbar { display: none; }
  .chips a { flex: none; padding: 8px 14px; border: 1px solid var(--line); font-size: 14px; white-space: nowrap; }
  .jn-m { display: block; font-size: 12px; color: var(--mute); margin: -14px 0 22px; }
}
@media (min-width: 1001px) { .jn-m { display: none; } }
@media (max-width: 760px) {
  .intro { padding: 100px 0 34px; }
  h1 { margin-bottom: 24px; }
  .rules { grid-template-columns: 1fr; }
  .rules li { padding: 16px 18px; } .rules em { font-size: 24px; margin-bottom: 6px; }
  .card, .card.big { padding: 20px 18px; }
  .card.big { grid-template-columns: 1fr; gap: 0; padding: 0 0 20px; }
  .card.big .ph { aspect-ratio: 16 / 9; } .card.big .ph img { object-position: 50% 35%; }
  .card.big .bd { padding: 18px 18px 0; }
  .pl.lvl3 { columns: 1; }
  .grp#add, .grp#color { display: block; }
  .two .th, .two .pl li { grid-template-columns: 1fr 82px 82px; }
}
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } * { transition: none !important; } }'''

NAVLINKS = '<a href="../#services">Услуги</a><a href="../#calc">Стоимость</a><a href="../#offers">Акции</a><a href="../#about">О студии</a><a href="../#team">Команда</a><a href="../#reviews">Отзывы</a><a href="../#contacts">Контакты</a><a href="./" aria-current="page">Прайс</a>'
PV = {
  'v2': dict(css=P2_CSS, img='../img/', root='../', h1='Прайс-лист', header=f'''<header class="top" id="top"><div class="wrap">
<a class="logo" href="../" aria-label="Кератин Сторис, на главную"><img src="../img/logo.png" alt="KS Keratin Stories" width="700" height="461"></a>
<nav id="nav" aria-label="Разделы">{NAVLINKS}</nav>
<a class="btn sm" href="{DIKIDI}" target="_blank" rel="noopener">Записаться</a>
<button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="nav" aria-label="Меню"><i></i><i></i></button>
</div></header>'''),
}

def build_price(name):
    v = V[name]; P = PV[name]; img = P['img']
    faces = '\n'.join(l for l in v['fonts'].splitlines() if l.startswith('@font-face')).replace('url(fonts/', 'url(../fonts/')
    lvl = '''<fieldset class="lvl"><legend>Цены мастера</legend><div class="opts">
<label><input type="radio" name="lvl" value="0" checked>Мастер<small>&nbsp;</small></label>
<label><input type="radio" name="lvl" value="1">ТОП-мастер<small>Яна, Полина</small></label>
<label><input type="radio" name="lvl" value="2">Юлия*<small>основатель</small></label></div>
<p class="jn">''' + JULIA + '</p></fieldset>'
    deal = P.get('deal') or '''<section class="deal" id="deal"><p class="k">Акция</p><h2>«Комплекс»</h2>
<p>Скидка на комплексную стрижку (полировку) волос против сечения и пилинг кожи головы при проведении в комплексе с другими процедурами.</p>
<ul><li><span>Комплексная стрижка, до 50 см</span><b><s>4 000 ₽</s>2 000 ₽</b></li><li><span>Комплексная стрижка, свыше 50 см</span><b><s>5 000 ₽</s>2 500 ₽</b></li><li><span>Пилинг в комплексе</span><b><s>3 500 ₽</s>2 000 ₽</b></li></ul>
<ul class="nt"><li>цены комплексной стрижки — у мастера; у ТОП-мастера в комплексе 2 500 / 3 000 ₽</li></ul>
<div class="act" style="justify-content:center"><a class="btn fill" href="''' + DIKIDI + '''" target="_blank" rel="noopener">Записаться онлайн</a></div></section>'''
    html = f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- превью на demo.animemory.ru; при переносе на keratinstories.ru убрать noindex -->
<meta name="robots" content="noindex, nofollow">
<title>{PRICE_T}</title>
<meta name="description" content="{PRICE_D}">
{ICONS.format(img=img, root=P['root'])}<style>
{faces}
{P['css']}
</style>
</head>
<body data-lvl="0">
{P['header']}

<main class="wrap">
<div class="intro">
<p class="kick">действует с 1 марта 2026 года</p>
<h1>{P['h1']}</h1>
<ol class="rules">
<li><em>01</em>Стоимость процедуры определяется исходя из <b>длины и густоты волос</b>.</li>
<li><em>02</em>Перед началом процедуры мастер измерит длину и густоту ваших волос и озвучит точную стоимость услуги в соответствии с прайсом, <b>обязательно до начала работы</b>, на этапе консультации.</li>
<li><em>03</em>Подбор составов и продуктов, на которых будет выполнена услуга, проводится мастером индивидуально в зависимости от вашего типа волос и пожеланий по результату. <b>Выбор конкретных продуктов и составов не влияет на стоимость.</b></li>
</ol>
<div class="cta"><a class="btn fill" href="{DIKIDI}" target="_blank" rel="noopener">Записаться онлайн</a><a class="btn" href="../#calc">Рассчитать по длине</a></div>
</div>

<div class="lay">
<aside class="side">{lvl}<nav class="toc" aria-label="Разделы прайса">{TOC_HTML}</nav></aside>
<div class="list">
<nav class="chips" aria-label="Разделы прайса">{CHIPS}</nav>
<p class="jn-m">{JULIA}</p>
{''.join(group2(*g, img=img) for g in GROUPS)}{deal}
</div>
</div>
</main>

<footer><div class="wrap"><span>ИП Матковская Ю. В. · ИНН 774322019399 · <a href="tel:+79057025612">+7 (905) 702-56-12</a></span>
<nav aria-label="Документы"><a href="../">Главная</a><a href="../policy/">Политика конфиденциальности</a><a href="../offer/">Оферта</a></nav></div></footer>
<button class="up" id="up" type="button" aria-label="Наверх">↑</button>

<script>
const $ = id => document.getElementById(id);
const nav = $('nav'), burger = $('burger');
const setNav = o => {{ nav.classList.toggle('open', o); burger.setAttribute('aria-expanded', o); }};
burger.onclick = () => setNav(!nav.classList.contains('open'));
nav.querySelectorAll('a').forEach(a => a.onclick = () => setNav(false));
// шкала мастера: одна на страницу, запоминаем выбор
const radios = [...document.querySelectorAll('input[name=lvl]')];
const setLvl = v => {{ document.body.dataset.lvl = v; try {{ localStorage.setItem('ks-lvl', v); }} catch (e) {{}} }};
radios.forEach(r => r.onchange = () => setLvl(r.value));
try {{ const s = localStorage.getItem('ks-lvl'); if (s && radios[s]) {{ radios[s].checked = true; document.body.dataset.lvl = s; }} }} catch (e) {{}}
// подсветка раздела в оглавлении
const links = [...document.querySelectorAll('.toc a')], map = new Map(links.map(a => [a.hash.slice(1), a]));
const io = new IntersectionObserver(es => es.forEach(e => {{ if (!e.isIntersecting) return; const a = map.get(e.target.id); if (!a) return;
  links.forEach(x => x.classList.remove('on')); a.classList.add('on'); a.scrollIntoView({{ block: 'nearest' }}); }}), {{ rootMargin: '-90px 0px -65% 0px' }});
document.querySelectorAll('.card[id], .deal').forEach(s => io.observe(s));
const up = $('up');
addEventListener('scroll', () => up.classList.toggle('show', scrollY > 900), {{ passive: true }});
up.onclick = () => scrollTo({{ top: 0 }});
</script>
</body>
</html>
'''
    out = ROOT / name / 'price' / 'index.html'
    out.write_text(html, encoding='utf-8')
    print(out, len(html))


# ═══════════ v3: прайс — секция #price на главной (2026-11-12, сайт одностраничный по просьбе Юлии) ═══════════
# Лента карточек (листается как услуги): в каждой таблица сразу со всеми тремя мастерами, без переключателей.
# build_price_v3() вписывает CSS и HTML в v3/index.html между маркерами; v3/price/ — редирект на ../#price.
CALC = {'keratin': 'keratin', 'nano': 'nano', 'total': 'total', 'disc': 'disc', 'cold': 'cold', 'lebel': 'lebel', 'cbotox': 'cbotox'}

def card3(sid, group):
    _, title, sub, desc, (head, labels, rows), notes, _ = SD[sid]
    if head:
        th = ''.join(f'<th scope="col">{h}</th>' for h in head)
        first = 'Длина' if labels[0].startswith('до ') else ''
        body = ''.join(f'<tr><th scope="row">{l}</th>' + ''.join(f'<td>{money(v)}</td>' for v in r) + '</tr>' for l, r in zip(labels, rows))
        tab = f'<table class="t{len(head)}"><thead><tr><th scope="col">{first}</th>{th}</tr></thead><tbody>{body}</tbody></table>'
    else:
        body = ''.join(f'<tr><th scope="row">{l}</th><td{" class=w" if len(money(r[0])) > 14 else ""}>{money(r[0])}</td></tr>' for l, r in zip(labels, rows))
        tab = f'<table class="t1"><tbody>{body}</tbody></table>'
    tag = '<span class="new">new!</span>' if sub == 'new' else ''
    sub_html = f'<p class="sub">{sub}</p>' if sub and sub != 'new' else ''
    desc_html = ''.join(f'<p>{d}</p>' for d in desc)
    notes_html = ('<ul class="nt">' + ''.join(f'<li>{n}</li>' for n in notes) + '</ul>') if notes else ''
    act = f'<button class="link" type="button" data-calc="{CALC[sid]}">Рассчитать стоимость →</button>' if sid in CALC else ''
    return f'<article class="pc" id="p-{sid}"><span class="pg">{group}</span><h3>{title}{tag}</h3>{sub_html}{desc_html}{tab}{notes_html}{act}</article>\n'

PRICE_CSS = '''/* PRICE-CSS:START — генерирует build_pages.py, руками не править */
#price .prules { list-style: none; padding: 0; display: grid; gap: 4px; color: #d4cfc9; font-size: 14px; max-width: 980px; margin-top: 14px; }
#price .prules li::before { content: "— "; }
#price .prules b { color: var(--tx); font-weight: 500; }
#price .legend { margin-top: 16px; display: flex; flex-wrap: wrap; gap: 6px 10px; align-items: center; font-size: 13px; color: var(--mute); }
#price .legend span { padding: 5px 12px; border-radius: 999px; box-shadow: inset 0 0 0 1px var(--line); color: var(--tx); white-space: nowrap; }
#price .legend small { color: var(--mute); }
.pchips { display: flex; gap: 6px; overflow-x: auto; scrollbar-width: none; margin: 20px -16px 0; padding: 0 16px; }
.pchips::-webkit-scrollbar, .prail::-webkit-scrollbar { display: none; }
.pchips button { flex: none; min-height: 36px; padding: 6px 14px; border-radius: 999px; border: 0; box-shadow: inset 0 0 0 1px var(--line); background: none; cursor: pointer; font-size: 13px; white-space: nowrap; transition: background .3s, color .3s; }
.pchips button:hover { box-shadow: inset 0 0 0 1px rgba(243,241,238,.55); }
.pchips button.on { background: var(--tx); color: var(--bg); }
.prail { --g: 16px; display: flex; align-items: flex-start; gap: 14px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-inline: var(--g); padding: 18px var(--g) 10px; scrollbar-width: none; }
@media (min-width: 1272px) { .prail { --g: calc((100vw - 1240px) / 2 + 16px); } }
.pc { flex: none; width: min(88vw, 440px); scroll-snap-align: start; background: var(--card); border-radius: 22px; box-shadow: inset 0 0 0 1px var(--line); padding: 18px 18px 16px; display: grid; gap: 9px; }
.pc .pg { font-size: 11px; font-weight: 500; letter-spacing: .16em; text-transform: uppercase; color: var(--mute); }
.pc h3 { font-size: 19px; font-weight: 600; line-height: 1.2; }
.pc .new { font: italic 500 15px 'Playfair Display', serif; color: var(--lav); margin-left: 8px; }
.pc .sub { font-size: 13px; color: var(--mute); margin-top: -5px; }
.pc p { font-size: 13.5px; color: #d4cfc9; }
.pc .link { justify-self: start; color: var(--tx); border-bottom-color: var(--lav); font-weight: 500; }
.pc table { width: 100%; border-collapse: collapse; font-size: 14px; }
.pc th, .pc td { padding: 6px 0; border-bottom: 1px solid var(--line); text-align: right; white-space: nowrap; }
.pc tbody tr:last-child > * { border-bottom: 0; }
.pc tbody th { text-align: left; font-weight: 400; color: #d4cfc9; white-space: normal; padding-right: 10px; }
.pc td { font-weight: 500; padding-left: 8px; }
.pc thead th { font-size: 12px; font-weight: 500; color: var(--mute); vertical-align: bottom; line-height: 1.25; }
.pc thead th:first-child { text-align: left; }
.pc thead small { display: block; font-weight: 400; font-size: 11px; opacity: .8; }
.pc .t3 thead th:nth-child(4), .pc .t3 td:nth-child(4) { color: var(--lav); }
.pc .t1 td.w { white-space: normal; }
.pc .nt { list-style: none; padding: 0; font-size: 12px; color: var(--mute); display: grid; gap: 2px; }
.pfoot { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px 20px; margin-top: 14px; }
.pfoot .fine { margin: 0; }
@media (max-width: 600px) { .pc table { font-size: 13px; } .pc td { padding-left: 6px; } }
/* PRICE-CSS:END */'''

def build_price_v3():
    cards = ''.join(card3(i, n) for g, n, ids, c in GROUPS for i in ids)
    chips = ''.join(f'<button type="button" data-go="p-{i}">{TOC2[i]}</button>' for g, n, ids, c in GROUPS for i in ids)
    sec = f'''<!-- PRICE:START — генерирует build_pages.py (build_price_v3), руками не править -->
<section id="price">
  <div class="wrap">
    <div class="hs-head" style="margin-bottom:0"><div><span class="eb rv">Действует с 1 марта 2026 года</span><h2 class="rv">Прайс-<em>лист</em></h2></div>
      <div class="arrows"><button type="button" data-pdir="-1" aria-label="Назад">←</button><button type="button" data-pdir="1" aria-label="Вперёд">→</button></div></div>
    <ul class="prules">
      <li>Стоимость процедуры определяется исходя из <b>длины и густоты волос</b>.</li>
      <li>Перед началом процедуры мастер измерит длину и густоту ваших волос и озвучит точную стоимость услуги в соответствии с прайсом, <b>обязательно до начала работы</b>, на этапе консультации.</li>
      <li>Подбор составов и продуктов, на которых будет выполнена услуга, проводится мастером индивидуально в зависимости от вашего типа волос и пожеланий по результату. <b>Выбор конкретных продуктов и составов не влияет на стоимость.</b></li>
    </ul>
    <p class="legend">Цены в таблицах — по уровню мастера: <span>Мастер</span><span>ТОП-мастер <small>Яна, Полина</small></span><span>Юлия* <small>основатель</small></span></p>
    <nav class="pchips" id="pchips" aria-label="Процедуры прайса">{chips}</nav>
  </div>
  <div class="prail" id="prail">
{cards}  </div>
  <div class="wrap pfoot"><p class="fine">{JULIA}. Листайте карточки вбок — все процедуры и доплаты.</p><a class="btn" href="#calc">Калькулятор стоимости</a></div>
</section>
<!-- PRICE:END -->'''
    idx = ROOT / 'v3' / 'index.html'
    h = idx.read_text(encoding='utf-8')
    a, b = h.index('/* PRICE-CSS:START'), h.index('/* PRICE-CSS:END */') + len('/* PRICE-CSS:END */')
    h = h[:a] + PRICE_CSS + h[b:]
    a, b = h.index('<!-- PRICE:START'), h.index('<!-- PRICE:END -->') + len('<!-- PRICE:END -->')
    h = h[:a] + sec + h[b:]
    idx.write_text(h, encoding='utf-8')
    print(idx, len(h))
    # старый адрес /price/ — на секцию прайса главной
    (ROOT / 'v3' / 'price' / 'index.html').write_text('''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="robots" content="noindex">
<title>Прайс-лист — Кератин Сторис</title><meta http-equiv="refresh" content="0; url=../#price">
<script>location.replace('../#price')</script></head>
<body style="background:#111112;color:#f3f1ee;font-family:system-ui"><p><a href="../#price">Прайс-лист</a></p></body></html>
''', encoding='utf-8')

build_price('v2')
build_price_v3()


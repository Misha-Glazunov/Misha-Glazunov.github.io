// ── прайс: лента карточек ──
{ const pr = $('prail'), chips = [...$('pchips').children], cards = [...pr.children], step = () => cards[0].offsetWidth + 12;
  const pad = () => parseFloat(getComputedStyle(pr).scrollPaddingLeft) || 0;
  const go = el => pr.scrollTo({ left: el.offsetLeft - cards[0].offsetLeft, behavior: RM ? 'auto' : 'smooth' });
  chips.forEach(b => b.onclick = () => go($(b.dataset.go)));
  pr.querySelectorAll('.tags a').forEach(a => a.onclick = e => { e.preventDefault(); go($('p-dop')); });
  document.querySelectorAll('[data-pdir]').forEach(b => b.onclick = () => pr.scrollBy({ left: +b.dataset.pdir * step(), behavior: RM ? 'auto' : 'smooth' }));
  const mark = () => { const x = pr.getBoundingClientRect().left + pad() + 20;
    const i = Math.max(0, cards.findIndex(el => el.getBoundingClientRect().right > x)), c = cards[i];
    const vis = Math.max(1, Math.floor((pr.clientWidth - pad()) / step())), last = Math.min(cards.length, i + vis);
    $('pcnt').innerHTML = `<b>${i + 1}${vis > 1 ? '–' + last : ''}</b> / ${cards.length}`; $('pbar').style.width = last / cards.length * 100 + '%';
    chips.forEach(b => { const on = b.dataset.go === c.id; if (on !== b.classList.contains('on')) { b.classList.toggle('on', on); if (on) $('pchips').scrollTo({ left: b.offsetLeft - $('pchips').offsetLeft - 16, behavior: 'smooth' }); } }); };
  pr.addEventListener('scroll', () => requestAnimationFrame(mark), { passive: true }); addEventListener('resize', mark); mark(); }
typo(document.body);

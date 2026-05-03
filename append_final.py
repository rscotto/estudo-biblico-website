# -*- coding: utf-8 -*-
# Fix plague refs and add script block, footer, and final write

plague_fixes = [
    # II - source has "deusa-rã" not "deusa das rãs"
    (
        '<div class="plague-name">Rãs</div>\n          <div class="plague-ref">Êx 8.1–15 · Ataca Heqet (deusa das rãs)</div>',
        '<div class="plague-name">Frogs</div>\n          <div class="plague-ref">Exod 8:1–15 · Targets Heqet (frog goddess)</div>',
    ),
    # III - source has "Magos não reproduzem" not "Ataca Geb"
    (
        '<div class="plague-name">Piolhos / Mosquitos</div>\n          <div class="plague-ref">Êx 8.16–19 · Magos não reproduzem</div>',
        '<div class="plague-name">Gnats / Lice</div>\n          <div class="plague-ref">Exod 8:16–19 · Magicians cannot replicate</div>',
    ),
    # IV - source has "Moscas" (no "Enxame") and "Distinção: Gósen preservada"
    (
        '<div class="plague-name">Moscas</div>\n          <div class="plague-ref">Êx 8.20–32 · Distinção: Gósen preservada</div>',
        '<div class="plague-name">Flies</div>\n          <div class="plague-ref">Exod 8:20–32 · Distinction: Goshen preserved</div>',
    ),
    # V - source has "Peste no Gado" not "Morte do Gado"
    (
        '<div class="plague-name">Peste no Gado</div>\n          <div class="plague-ref">Êx 9.1–7 · Ataca Ápis (touro sagrado)</div>',
        '<div class="plague-name">Livestock Disease</div>\n          <div class="plague-ref">Exod 9:1–7 · Targets Apis (sacred bull)</div>',
    ),
    # VI - source has "Magos humilhados" not "Ataca Sekhmet"
    (
        '<div class="plague-name">Úlceras</div>\n          <div class="plague-ref">Êx 9.8–12 · Magos humilhados</div>',
        '<div class="plague-name">Boils</div>\n          <div class="plague-ref">Exod 9:8–12 · Magicians humiliated</div>',
    ),
    # VII - source has "Nut (céu) e Shu (ar)" not just "Nut"
    (
        '<div class="plague-name">Granizo</div>\n          <div class="plague-ref">Êx 9.13–35 · Ataca Nut (céu) e Shu (ar)</div>',
        '<div class="plague-name">Hail</div>\n          <div class="plague-ref">Exod 9:13–35 · Targets Nut (sky) and Shu (air)</div>',
    ),
    # VIII - source has "Devastação agrícola total" not "Ataca Osiris"
    (
        '<div class="plague-name">Gafanhotos</div>\n          <div class="plague-ref">Êx 10.1–20 · Devastação agrícola total</div>',
        '<div class="plague-name">Locusts</div>\n          <div class="plague-ref">Exod 10:1–20 · Total agricultural devastation</div>',
    ),
    # IX - correct already (Rá deus-sol) - but ref format differs; fix anyway
    (
        '<div class="plague-name">Trevas</div>\n          <div class="plague-ref">Êx 10.21–29 · Ataca Rá (deus-sol)</div>',
        '<div class="plague-name">Darkness</div>\n          <div class="plague-ref">Exod 10:21–29 · Targets Ra (sun god)</div>',
    ),
    # X - source has "Êx 11–12 · Ataca o próprio Faraó-deus"
    (
        '<div class="plague-name">Morte dos Primogênitos</div>\n          <div class="plague-ref">Êx 11–12 · Ataca o próprio Faraó-deus</div>',
        '<div class="plague-name">Death of the Firstborn</div>\n          <div class="plague-ref">Exod 11–12 · Targets Pharaoh himself — son of Ra</div>',
    ),
]

# Also fix plague I (already in generator but make sure)
plague_i_fix = [
    (
        '<div class="plague-name">Águas em Sangue</div>\n          <div class="plague-ref">Êx 7.14–25 · Ataca Hápi (deus do Nilo)</div>',
        '<div class="plague-name">Water to Blood</div>\n          <div class="plague-ref">Exod 7:14–25 · Targets Hapi (god of the Nile)</div>',
    ),
]

# Script block replacement
script_old = '''<script>
  const _lang = localStorage.getItem('lang') || 'pt';

  function applyLang(l) {
    document.querySelectorAll('[data-pt]').forEach(el => {
      el.innerHTML = l === 'en' ? el.dataset.en : el.dataset.pt;
    });
    document.getElementById('langLabel').textContent = l === 'en' ? 'PT' : 'EN';
    document.documentElement.lang = l === 'en' ? 'en' : 'pt-BR';
  }
  function toggleLang() {
    const next = localStorage.getItem('lang') === 'en' ? 'pt' : 'en';
    localStorage.setItem('lang', next);
    applyLang(next);
  }

  function showSection(id) {
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));

    const sec = document.getElementById(id);
    if (sec) {
      sec.classList.add('active');
      sec.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
    }

    document.querySelectorAll('.nav-item[data-section]').forEach(b => {
      if (b.dataset.section === id) b.classList.add('active');
    });

    // On mobile: close sidebar after selection
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    const toggle  = document.getElementById('menuToggle');
    if (sidebar.classList.contains('open')) {
      sidebar.classList.remove('open');
      overlay.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Mobile hamburger
  const menuToggle     = document.getElementById('menuToggle');
  const sidebar        = document.getElementById('sidebar');
  const sidebarOverlay = document.getElementById('sidebarOverlay');

  menuToggle.addEventListener('click', () => {
    const open = sidebar.classList.toggle('open');
    sidebarOverlay.classList.toggle('open', open);
    menuToggle.setAttribute('aria-expanded', open);
  });
  sidebarOverlay.addEventListener('click', () => {
    sidebar.classList.remove('open');
    sidebarOverlay.classList.remove('open');
    menuToggle.setAttribute('aria-expanded', 'false');
  });

  // Scroll reveal
  const revealEls = document.querySelectorAll('.reveal');
  const revealObs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.12 });
  revealEls.forEach(el => revealObs.observe(el));

  // Back to top
  const btt = document.getElementById('btt');
  window.addEventListener('scroll', () => {
    btt.classList.toggle('visible', window.scrollY > 400);
  });

  // Trigger reveals for the initially active section
  document.querySelectorAll('.section.active .reveal').forEach(el => {
    el.classList.add('visible');
  });

  if (_lang === 'en') applyLang('en');
  else document.getElementById('langLabel').textContent = 'EN';
</script>'''

script_new = '''<script>
  localStorage.setItem('lang', 'en');

  function goToPt() {
    localStorage.setItem('lang', 'pt');
    window.location.href = '/pt/at-pentateuco';
  }

  function showSection(id) {
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));

    const sec = document.getElementById(id);
    if (sec) {
      sec.classList.add('active');
      sec.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
    }

    document.querySelectorAll('.nav-item[data-section]').forEach(b => {
      if (b.dataset.section === id) b.classList.add('active');
    });

    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    const toggle  = document.getElementById('menuToggle');
    if (sidebar.classList.contains('open')) {
      sidebar.classList.remove('open');
      overlay.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  const menuToggle     = document.getElementById('menuToggle');
  const sidebar        = document.getElementById('sidebar');
  const sidebarOverlay = document.getElementById('sidebarOverlay');

  menuToggle.addEventListener('click', () => {
    const open = sidebar.classList.toggle('open');
    sidebarOverlay.classList.toggle('open', open);
    menuToggle.setAttribute('aria-expanded', open);
  });
  sidebarOverlay.addEventListener('click', () => {
    sidebar.classList.remove('open');
    sidebarOverlay.classList.remove('open');
    menuToggle.setAttribute('aria-expanded', 'false');
  });

  const revealEls = document.querySelectorAll('.reveal');
  const revealObs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.12 });
  revealEls.forEach(el => revealObs.observe(el));

  const btt = document.getElementById('btt');
  window.addEventListener('scroll', () => {
    btt.classList.toggle('visible', window.scrollY > 400);
  });

  document.querySelectorAll('.section.active .reveal').forEach(el => {
    el.classList.add('visible');
  });
</script>'''

# Lang button: change label from "EN" to "PT" and call goToPt
lang_btn_old = '''<button class="lang-btn" id="langBtn" onclick="toggleLang()" aria-label="Switch language">
  <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
  <span id="langLabel">EN</span>
</button>'''

lang_btn_new = '''<button class="lang-btn" id="langBtn" onclick="goToPt()" aria-label="Switch to Portuguese">
  <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
  <span id="langLabel">PT</span>
</button>'''

# Footer replacement
footer_old = 'Estudo Bíblico Panorâmico · Moisés · Pentateuco · © Material de Estudo'
footer_new = 'Panoramic Bible Study · Moses · Pentateuch · © Study Material'

# Build the lines to append
lines = []

lines.append('\n# ═══ plague fixes (correct refs) ═══\n')
for pt, en in plague_i_fix + plague_fixes:
    lines.append(f'out = out.replace(\n    {repr(pt)},\n    {repr(en)},\n    1\n)\n')

lines.append('\n# ═══ script block replacement ═══\n')
lines.append(f'out = out.replace(\n    {repr(script_old)},\n    {repr(script_new)},\n    1\n)\n')

lines.append('\n# ═══ lang button replacement ═══\n')
lines.append(f'out = out.replace(\n    {repr(lang_btn_old)},\n    {repr(lang_btn_new)},\n    1\n)\n')

lines.append('\n# ═══ footer replacement ═══\n')
lines.append(f'out = out.replace(\n    {repr(footer_old)},\n    {repr(footer_new)},\n    1\n)\n')

lines.append('''
# ═══ final write ═══
import os
os.makedirs('at-pentateuco', exist_ok=True)
with open('at-pentateuco/index.en.html', 'w', encoding='utf-8') as f:
    f.write(out)
print('Written at-pentateuco/index.en.html')
''')

with open('gen_en_pentateuco.py', 'a', encoding='utf-8') as f:
    f.writelines(lines)

print(f'Appended plague fixes + script block + footer + final write')

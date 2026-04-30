#!/usr/bin/env python3
import re, sys

with open('at-historicos/index.html', encoding='utf-8') as f:
    src = f.read()

def remove_pt_blocks(html):
    """Remove all <div class="lang-content" data-lang="pt">...</div> using depth counting."""
    pattern = re.compile(r'<div\s[^>]*data-lang=["\']pt["\'][^>]*>')
    result = []
    pos = 0
    while pos < len(html):
        m = pattern.search(html, pos)
        if not m:
            result.append(html[pos:])
            break
        result.append(html[pos:m.start()])
        depth = 1
        i = m.end()
        while i < len(html) and depth > 0:
            open_m = re.search(r'<div[\s>]', html[i:i+200])
            close_m = re.search(r'</div>', html[i:i+200])
            if open_m and close_m:
                if open_m.start() < close_m.start():
                    depth += 1
                    i += open_m.end()
                else:
                    depth -= 1
                    i += close_m.end()
            elif close_m:
                depth -= 1
                i += close_m.end()
            elif open_m:
                depth += 1
                i += open_m.end()
            else:
                i += 200
        if i < len(html) and html[i] == '\n':
            i += 1
        pos = i
    return ''.join(result)

def unwrap_en_blocks(html):
    """Remove wrapper div of <div class="lang-content" data-lang="en"...>, keep inner content."""
    pattern = re.compile(r'<div\s[^>]*data-lang=["\']en["\'][^>]*>')
    result = []
    pos = 0
    while pos < len(html):
        m = pattern.search(html, pos)
        if not m:
            result.append(html[pos:])
            break
        result.append(html[pos:m.start()])
        depth = 1
        i = m.end()
        inner_start = i
        while i < len(html) and depth > 0:
            open_m = re.search(r'<div[\s>]', html[i:i+200])
            close_m = re.search(r'</div>', html[i:i+200])
            if open_m and close_m:
                if open_m.start() < close_m.start():
                    depth += 1
                    i += open_m.end()
                else:
                    depth -= 1
                    i += close_m.end()
            elif close_m:
                depth -= 1
                i += close_m.end()
            elif open_m:
                depth += 1
                i += open_m.end()
            else:
                i += 200
        inner_end = i - len('</div>')
        inner = html[inner_start:inner_end]
        if inner.startswith('\n'):
            inner = inner[1:]
        result.append(inner)
        pos = i
    return ''.join(result)

# Step 1: remove PT blocks
out = remove_pt_blocks(src)
# Step 2: unwrap EN blocks
out = unwrap_en_blocks(out)

# Verify
pt_remaining = len(re.findall(r'data-lang=["\']pt["\']', out))
en_remaining = len(re.findall(r'data-lang=["\']en["\']', out))
print(f'PT blocks remaining: {pt_remaining}', file=sys.stderr)
print(f'EN wrappers remaining: {en_remaining}', file=sys.stderr)

# ── Structural fixes ──────────────────────────────────────────────────────────

# Fix html lang attribute
out = out.replace('<html lang="pt-BR">', '<html lang="en">', 1)

# Fix title
out = out.replace('<title>Livros Históricos — Estudo Bíblico</title>',
                  '<title>Historical Books — Bible Study</title>', 1)

# Fix hero title
out = re.sub(
    r'<h1 class="hero-title"[^>]*>[\s\S]*?</h1>',
    '<h1 class="hero-title"><span>Historical</span> Books</h1>',
    out, count=1, flags=re.DOTALL
)

# Fix hero desc — remove data-pt/data-en from paragraph, set English text
out = re.sub(
    r'<p class="hero-desc"[^>]*>[\s\S]*?</p>',
    '<p class="hero-desc">Twelve books narrating Israel\'s journey — from the conquest of Canaan to exile and restoration. Historical context, geography, and theological analysis of each work.</p>',
    out, count=1
)

# Remove data-pt / data-en / data-en attributes everywhere
out = re.sub(r'\s+data-pt="[^"]*"', '', out)
out = re.sub(r"\s+data-pt='[^']*'", '', out)
out = re.sub(r'\s+data-en="[^"]*"', '', out)
out = re.sub(r"\s+data-en='[^']*'", '', out)

# Fix aria-label for menu toggle
out = out.replace('aria-label="Abrir menu"', 'aria-label="Open menu"', 1)

# Fix sidebar back link text
out = out.replace('>Voltar à Bíblia<', '>Back to Bible<', 1)

# Fix sidebar-title and sidebar-subtitle visible text
out = out.replace('>Livros Históricos<', '>Historical Books<', 1)
out = out.replace('>Antigo Testamento · 12 Livros<', '>Old Testament · 12 Books<', 1)

# Fix sidebar-nav aria-label
out = out.replace('aria-label="Navegação dos livros históricos"',
                  'aria-label="Historical books navigation"', 1)

# Fix nav abbreviations (Portuguese → English)
nav_abbr = {
    '>Js<': '>Josh<',
    '>Jz<': '>Judg<',
    '>Rt<': '>Ruth<',
    '>1Sm<': '>1Sam<',
    '>2Sm<': '>2Sam<',
    '>1Rs<': '>1Kgs<',
    '>2Rs<': '>2Kgs<',
    '>1Cr<': '>1Chr<',
    '>2Cr<': '>2Chr<',
    '>Ed<': '>Ezra<',
    '>Ne<': '>Neh<',
    '>Et<': '>Esth<',
}
for pt_abbr, en_abbr in nav_abbr.items():
    out = out.replace(pt_abbr, en_abbr)

# Fix hero eyebrow
out = out.replace('>✦ Estudo Bíblico Aprofundado ✦<', '>✦ In-Depth Bible Study ✦<', 1)

# Fix nav names (data-pt/data-en already stripped; set visible text)
nav_names = {
    '>Josué<': '>Joshua<',
    '>Juízes<': '>Judges<',
    '>Rute<': '>Ruth<',
    '>1 Reis<': '>1 Kings<',
    '>2 Reis<': '>2 Kings<',
    '>1 Crônicas<': '>1 Chronicles<',
    '>2 Crônicas<': '>2 Chronicles<',
    '>Esdras<': '>Ezra<',
    '>Neemias<': '>Nehemiah<',
    '>Ester<': '>Esther<',
}
for pt_name, en_name in nav_names.items():
    out = out.replace(pt_name, en_name)

# Fix tab buttons — replace Portuguese visible text with English
tab_replacements = [
    ('>Contexto Histórico<', '>Historical Context<'),
    ('>Geografia<', '>Geography<'),
    ('>Estudo Aprofundado<', '>In-Depth Study<'),
    ('>Contexto<', '>Context<'),
    ('>Teologia<', '>Theology<'),
]
for old, new in tab_replacements:
    out = out.replace(old, new)

# Replace the entire script block with a clean EN-only version
old_script = re.compile(r'<script>\nfunction applyLang[\s\S]*?</script>', re.DOTALL)

new_script = '''<script>
function showBook(id) {
  document.querySelectorAll('.book-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  const panel = document.getElementById('panel-' + id);
  if (panel) {
    panel.classList.add('active');
    panel.querySelectorAll('.tab-btn').forEach((b, i) => b.classList.toggle('active', i === 0));
    panel.querySelectorAll('.tab-panel').forEach((tp, i) => tp.classList.toggle('active', i === 0));
  }
  const btn = document.querySelector('[data-book="' + id + '"]');
  if (btn) btn.classList.add('active');
  closeSidebar();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function showTab(btn, bookId, tabId) {
  const panel = document.getElementById('panel-' + bookId);
  if (!panel) return;
  panel.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  panel.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  btn.classList.add('active');
  const tp = document.getElementById(bookId + '-' + tabId);
  if (tp) tp.classList.add('active');
}

const menuToggle = document.getElementById('menuToggle');
const sidebar    = document.getElementById('sidebar');
const overlay    = document.getElementById('sidebarOverlay');

function openSidebar()  { sidebar.classList.add('open'); overlay.classList.add('open'); menuToggle.setAttribute('aria-expanded','true'); }
function closeSidebar() { sidebar.classList.remove('open'); overlay.classList.remove('open'); menuToggle.setAttribute('aria-expanded','false'); }

menuToggle.addEventListener('click', () => sidebar.classList.contains('open') ? closeSidebar() : openSidebar());
overlay.addEventListener('click', closeSidebar);
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeSidebar(); });

function goToPt() {
  localStorage.setItem('lang', 'pt');
  window.location.href = '/pt';
}

localStorage.setItem('lang', 'en');
</script>'''

m = old_script.search(out)
if m:
    out = out[:m.start()] + new_script + out[m.end():]
    print('Script replaced successfully.', file=sys.stderr)
else:
    print('WARNING: script pattern not found!', file=sys.stderr)

# Fix lang button — change label from EN to PT (EN page switches to PT)
# The button has id="langBtn" with span id="langLabel"
out = re.sub(r'(<span id="langLabel">)[^<]*(</span>)', r'\1PT\2', out, count=1)

# Replace toggleLang() onclick with a named function (goToPt) defined in the script block
out = re.sub(r'onclick="toggleLang\(\)"', r'onclick="goToPt()"', out)

with open('at-historicos/index.en.html', 'w', encoding='utf-8') as f:
    f.write(out)

# Count lines and do a quick sanity check
lines = out.splitlines()
print(f'Written: {len(lines)} lines', file=sys.stderr)

# Check for any remaining PT signatures
pt_sigs = ['a.C.', 'Josué', 'Juízes', 'Crônicas', 'Esdras', 'Neemias', 'Ester',
           'Antigo Testamento', 'Livros Históricos']
for sig in pt_sigs:
    count = out.count(sig)
    if count > 0:
        print(f'  PT signature "{sig}": {count} occurrences', file=sys.stderr)

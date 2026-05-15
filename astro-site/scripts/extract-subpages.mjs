/**
 * Converts sub-page HTML files into proper Astro pages.
 * The body HTML is embedded verbatim; only the <head> is replaced by Astro.
 * Run once: node scripts/extract-subpages.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir   = path.resolve(__dirname, '../..');
const pagesDir  = path.resolve(__dirname, '../src/pages/pt');
const pagesEnDir = path.resolve(__dirname, '../src/pages/en');

const subpages = [
  {
    slug: 'at-pentateuco',
    srcFile: 'at-pentateuco/index.html',
    titlePt: 'Pentateuco — Estudo Bíblico',
    titleEn: 'Pentateuch — Bible Study',
    descPt: 'Estudo aprofundado dos 5 livros da Lei: Gênesis, Êxodo, Levítico, Números e Deuteronômio. Tradução NAA.',
    descEn: 'In-depth study of the 5 books of the Law: Genesis, Exodus, Leviticus, Numbers, Deuteronomy. ESV.',
    accentColor: '#FFA400',
  },
  {
    slug: 'at-historicos',
    srcFile: 'at-historicos/index.html',
    titlePt: 'Livros Históricos — Estudo Bíblico',
    titleEn: 'Historical Books — Bible Study',
    descPt: 'Estudo aprofundado dos 12 livros históricos do AT: Josué ao Ester. Contexto, geografia e teologia. Tradução NAA.',
    descEn: 'In-depth study of the 12 OT historical books: Joshua to Esther. Context, geography, theology. ESV.',
    accentColor: '#e8820a',
  },
  {
    slug: 'at-poeticos',
    srcFile: 'at-poeticos/index.html',
    titlePt: 'Livros Poéticos — Estudo Bíblico',
    titleEn: 'Poetic Books — Bible Study',
    descPt: 'Estudo aprofundado dos 5 livros sapienciais: Jó, Salmos, Provérbios, Eclesiastes, Cantares. Tradução NAA.',
    descEn: 'In-depth study of the 5 wisdom books: Job, Psalms, Proverbs, Ecclesiastes, Song of Songs. ESV.',
    accentColor: '#f0c040',
  },
  {
    slug: 'at-profetas-maiores',
    srcFile: 'at-profetas-maiores/index.html',
    titlePt: 'Profetas Maiores — Estudo Bíblico',
    titleEn: 'Major Prophets — Bible Study',
    descPt: 'Estudo aprofundado dos 5 profetas maiores: Isaías, Jeremias, Lamentações, Ezequiel, Daniel. Tradução NAA.',
    descEn: 'In-depth study of the 5 Major Prophets: Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel. ESV.',
    accentColor: '#e06a10',
  },
  {
    slug: 'at-profetas-menores',
    srcFile: 'at-profetas-menores/index.html',
    titlePt: 'Profetas Menores — Estudo Bíblico',
    titleEn: 'Minor Prophets — Bible Study',
    descPt: 'Estudo aprofundado dos 12 profetas menores: Oséias a Malaquias. Tradução NAA.',
    descEn: 'In-depth study of the 12 Minor Prophets: Hosea to Malachi. ESV.',
    accentColor: '#d4a020',
  },
  {
    slug: 'nt-evangelhos',
    srcFile: 'nt-evangelhos/index.html',
    titlePt: 'Evangelhos — Estudo Bíblico',
    titleEn: 'Gospels — Bible Study',
    descPt: 'Estudo aprofundado dos 4 Evangelhos: Mateus, Marcos, Lucas e João. Contexto histórico, teologia e análise literária. Tradução NAA.',
    descEn: 'In-depth study of the 4 Gospels: Matthew, Mark, Luke, and John. Historical context, theology, and literary analysis. ESV.',
    accentColor: '#FFA400',
  },
  {
    slug: 'nt-atos',
    srcFile: 'nt-atos/index.html',
    titlePt: 'Atos dos Apóstolos — Estudo Bíblico',
    titleEn: 'Acts of the Apostles — Bible Study',
    descPt: 'Estudo aprofundado de Atos dos Apóstolos: a Igreja primitiva, Pentecostes, as viagens missionárias de Paulo. Tradução NAA.',
    descEn: 'In-depth study of Acts of the Apostles: the early Church, Pentecost, Paul\'s missionary journeys. ESV.',
    accentColor: '#c87820',
  },
  {
    slug: 'nt-epistolas-paulinas',
    srcFile: 'nt-epistolas-paulinas/index.html',
    titlePt: 'Epístolas Paulinas — Estudo Bíblico',
    titleEn: 'Pauline Epistles — Bible Study',
    descPt: 'Estudo aprofundado das 13 Epístolas Paulinas: Romanos a Filemom. Teologia, contexto histórico e análise literária. Tradução NAA.',
    descEn: 'In-depth study of the 13 Pauline Epistles: Romans to Philemon. Theology, historical context, and literary analysis. ESV.',
    accentColor: '#FFA400',
  },
  {
    slug: 'nt-epistolas-gerais',
    srcFile: 'nt-epistolas-gerais/index.html',
    titlePt: 'Epístolas Gerais — Estudo Bíblico',
    titleEn: 'General Epistles — Bible Study',
    descPt: 'Estudo aprofundado das 8 Epístolas Gerais: Hebreus, Tiago, 1–2 Pedro, 1–3 João e Judas. Tradução NAA.',
    descEn: 'In-depth study of the 8 General Epistles: Hebrews, James, 1–2 Peter, 1–3 John, and Jude. ESV.',
    accentColor: '#FFA400',
  },
  {
    slug: 'nt-apocalipse',
    srcFile: 'nt-apocalipse/index.html',
    titlePt: 'Apocalipse — Estudo Bíblico',
    titleEn: 'Revelation — Bible Study',
    descPt: 'Estudo aprofundado do Apocalipse de João: o Cordeiro vitorioso, as sete igrejas, a Nova Jerusalém. Tradução NAA.',
    descEn: 'In-depth study of the Revelation of John: the victorious Lamb, the seven churches, the New Jerusalem. ESV.',
    accentColor: '#FFA400',
  },
];

const siteBase = 'https://biblia.rodrigoscotto.com';

/**
 * Process a source page's <style> block for the new editorial-monocle theme.
 * - Replaces old Google Fonts families with CSS variable references
 * - Strips the original :root block (we inject our own light/dark tokens)
 * - Returns a complete <style> element with remapped tokens + original rules
 */
function processStyle(rawCss, accentVal) {
  if (!rawCss.trim()) return '';

  // 1. Replace old font families with CSS variable references
  let css = rawCss
    .replace(/'Cinzel Decorative'\s*,\s*serif/g, 'var(--font-d, Georgia, serif)')
    .replace(/'Cinzel'\s*,\s*serif/g, 'var(--font-b, system-ui, sans-serif)')
    .replace(/'EB Garamond'\s*,\s*serif/g, 'var(--font-b, system-ui, sans-serif)');

  // 2. Remove original :root block (no nested braces in these files)
  css = css.replace(/:root\s*\{[^}]*\}/g, '');

  // 3. Build light/dark variable blocks
  const tokens = `
:root {
  --font-d: 'Iowan Old Style', Charter, Georgia, serif;
  --font-b: 'Roboto', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
  /* Light mode — editorial-monocle remapping of original dark-theme variables */
  --navy:        #faf8f4;
  --navy-mid:    #f0ebe0;
  --navy-light:  #e2d8ca;
  --sand:        #221e14;
  --sand-dark:   #3a3020;
  --sand-dim:    #7a6e5c;
  --stone-light: #9e9078;
  --text:        #221e14;
  --white:       #ffffff;
  --gold:        ${accentVal};
  --gold-dim:    #d48000;
  --gold-muted:  rgba(255,164,0,.45);
  --shadow-sm:   0 2px 8px rgba(0,0,0,.07);
  --shadow-md:   0 8px 32px rgba(0,0,0,.13);
  --shadow-gold: 0 4px 20px rgba(255,164,0,.2);
  --ink:         var(--navy);
  --accent:      ${accentVal};
  --radius-sm:   6px;
  --radius-md:   12px;
  --nav-w:       272px;
  --transition-fast: 150ms ease;
  --transition-base: 250ms ease;
}
[data-theme="dark"] {
  --navy:        #1d1912;
  --navy-mid:    #252117;
  --navy-light:  #38321e;
  --sand:        #f0e8d6;
  --sand-dark:   #c8b78a;
  --sand-dim:    #9e9078;
  --stone-light: #7a6e5c;
  --text:        #f0e8d6;
  --shadow-sm:   0 2px 8px rgba(0,0,0,.35);
  --shadow-md:   0 8px 32px rgba(0,0,0,.5);
}
`;

  return `<style>${tokens}${css}</style>`;
}

/* Inject the fixed-position dark-mode toggle + lang toggle buttons into the page body */
function buildToggles(lang, altLangCode, altLangUrl) {
  const sunPath = 'M12 3v1m0 16v1m9-9h-1M4 12H3m15.36-6.36-.71.71M6.34 17.66l-.7.7M17.66 17.66l.7.7M6.35 6.35l-.71-.71M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8z';
  const moonPath = 'M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9z';
  const langLabel = lang === 'pt' ? 'EN' : 'PT';
  return `
<a class="lang-toggle" href="${altLangUrl}" aria-label="Switch to ${altLangCode.toUpperCase()}">${langLabel}</a>
<button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">
  <svg viewBox="0 0 24 24"><path id="themeIconPath" d="${sunPath}"/></svg>
</button>
<script>
(function(){
  var html = document.documentElement;
  var btn  = document.getElementById('themeToggle');
  var path = document.getElementById('themeIconPath');
  var sun  = '${sunPath}';
  var moon = '${moonPath}';
  function setIcon(dark){ path.setAttribute('d', dark ? moon : sun); }
  setIcon(html.getAttribute('data-theme') === 'dark');
  btn.addEventListener('click', function(){
    var dark = html.getAttribute('data-theme') !== 'dark';
    html.setAttribute('data-theme', dark ? 'dark' : 'light');
    localStorage.setItem('theme', dark ? 'dark' : 'light');
    setIcon(dark);
  });
})();
<\/script>`;
}

function buildHead(opts) {
  const { title, description, lang, canonical, altLangCode, altLangUrl, accentColor } = opts;
  const htmlLang = lang === 'en' ? 'en' : 'pt-BR';
  return `<!DOCTYPE html>
<html lang="${htmlLang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light dark">
<title>${title}</title>
<meta name="description" content="${description}">
<link rel="canonical" href="${canonical}">
<link rel="alternate" hreflang="${lang}" href="${canonical}">
<link rel="alternate" hreflang="${altLangCode}" href="${altLangUrl}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/shared.css">
<script>(function(){var t=localStorage.getItem('theme');if(t==='dark'||(t===null&&window.matchMedia('(prefers-color-scheme:dark)').matches))document.documentElement.setAttribute('data-theme','dark');})();<\/script>`;
}

for (const page of subpages) {
  const html = fs.readFileSync(path.join(rootDir, page.srcFile), 'utf-8');

  // Extract the full <style> block and process it (font/color overrides)
  const styleMatch = html.match(/<style>([\s\S]*?)<\/style>/);
  const inlineStyle = styleMatch ? styleMatch[1].trim() : '';
  const accentMatch = inlineStyle.match(/--accent\s*:\s*([^;]+);/) ||
                      inlineStyle.match(/--gold\s*:\s*([^;]+);/);
  const accentVal   = accentMatch ? accentMatch[1].trim() : page.accentColor;
  const ptPageStyle = processStyle(inlineStyle, accentVal);

  // Extract <body>...</body> content
  const bodyStart = html.indexOf('<body>') + 6;
  const bodyEnd   = html.lastIndexOf('</body>');
  let bodyContent = html.slice(bodyStart, bodyEnd).trim();

  // PT page: fix back-link from ../index.html → /pt
  const ptBody = bodyContent
    .replace(/href="\.\.\/index\.html"/g, 'href="/pt"')
    .replace(/href='\.\.\/index\.html'/g, "href='/pt'");

  const ptToggles = buildToggles('pt', 'en', `/en/${page.slug}`);

  const ptHtml = buildHead({
    title: page.titlePt,
    description: page.descPt,
    lang: 'pt',
    canonical: `${siteBase}/pt/${page.slug}`,
    altLangCode: 'en',
    altLangUrl: `${siteBase}/en/${page.slug}`,
    accentColor: accentVal,
  }) + `
${ptPageStyle}
</head>
<body>
${ptToggles}
${ptBody}
</body>
</html>`;

  // EN page: use native index.en.html if available, otherwise fall back to PT source
  const enSrcFile = page.srcFile.replace('/index.html', '/index.en.html');
  const enSrcPath = path.join(rootDir, enSrcFile);
  let enHtml;

  if (fs.existsSync(enSrcPath)) {
    const enSrc = fs.readFileSync(enSrcPath, 'utf-8');
    const enStyleMatch = enSrc.match(/<style>([\s\S]*?)<\/style>/);
    const enInlineStyle = enStyleMatch ? enStyleMatch[1].trim() : inlineStyle;
    const enAccentMatch = enInlineStyle.match(/--accent\s*:\s*([^;]+);/) ||
                          enInlineStyle.match(/--gold\s*:\s*([^;]+);/);
    const enAccentVal   = enAccentMatch ? enAccentMatch[1].trim() : accentVal;
    const enPageStyle   = processStyle(enInlineStyle, enAccentVal);
    const enBodyStart = enSrc.indexOf('<body>') + 6;
    const enBodyEnd   = enSrc.lastIndexOf('</body>');
    const enBodyRaw   = enSrc.slice(enBodyStart, enBodyEnd).trim();
    const enBody = enBodyRaw
      .replace(/href="\.\.\/[^/]+\/index\.html"/g, 'href="/en"')
      .replace(/href='\.\.\/[^/]+\/index\.html'/g, "href='/en'")
      .replace(/href="\.\.\/index\.html"/g, 'href="/en"')
      .replace(/href='\.\.\/index\.html'/g, "href='/en'");

    const enToggles = buildToggles('en', 'pt', `/pt/${page.slug}`);

    enHtml = buildHead({
      title: page.titleEn,
      description: page.descEn,
      lang: 'en',
      canonical: `${siteBase}/en/${page.slug}`,
      altLangCode: 'pt',
      altLangUrl: `${siteBase}/pt/${page.slug}`,
      accentColor: enAccentVal,
    }) + `
${enPageStyle}
</head>
<body>
${enToggles}
${enBody}
</body>
</html>`;
    console.log(`  → using native EN source for ${page.slug}`);
  } else {
    // Fall back: copy PT body (bilingual via data-pt/data-en attributes)
    const enBody = bodyContent
      .replace(/href="\.\.\/index\.html"/g, 'href="/en"')
      .replace(/href='\.\.\/index\.html'/g, "href='/en'");

    const enToggles = buildToggles('en', 'pt', `/pt/${page.slug}`);

    enHtml = buildHead({
      title: page.titleEn,
      description: page.descEn,
      lang: 'en',
      canonical: `${siteBase}/en/${page.slug}`,
      altLangCode: 'pt',
      altLangUrl: `${siteBase}/pt/${page.slug}`,
      accentColor: accentVal,
    }) + `
${ptPageStyle}
</head>
<body>
${enToggles}
${enBody}
</body>
</html>`;
  }

  // Write as .html files into the public directory so Astro serves them statically
  // Actually write as .astro pages using set:html on a Fragment
  const ptAstro = `---
// PT sub-page: ${page.slug}
const html = ${JSON.stringify(ptHtml)};
---
<Fragment set:html={html} />
`;

  const enAstro = `---
// EN sub-page: ${page.slug}
const html = ${JSON.stringify(enHtml)};
---
<Fragment set:html={html} />
`;

  fs.writeFileSync(path.join(pagesDir,    `${page.slug}.astro`), ptAstro, 'utf-8');
  fs.writeFileSync(path.join(pagesEnDir,  `${page.slug}.astro`), enAstro, 'utf-8');
  console.log(`✓ ${page.slug}`);
}

console.log('\nDone. Subpages written to src/pages/pt/ and src/pages/en/');

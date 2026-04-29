/**
 * Extracts the 66-book DB from index.html and writes individual JSON files
 * into src/content/books/pt/ and src/content/books/en/
 *
 * Run once: node scripts/extract-db.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '../..');
const outDir = path.resolve(__dirname, '../src/content/books');

// Category metadata: maps abbr substring → { category, cellAbbr }
const CATEGORY_MAP = {
  'Pentateuco': { category: 'pen' },
  'Históricos':  { category: 'his' },
  'Poéticos':    { category: 'poe' },
  'Profetas Maiores': { category: 'mai' },
  'Profetas Menores': { category: 'men' },
  'Evangelhos':  { category: 'eva' },
  'Ato':         { category: 'ato' },
  'Paulinas':    { category: 'pau' },
  'Gerais':      { category: 'ger' },
  'Profético NT':{ category: 'apo' },
};

// Cell abbreviations shown in the grid (from index.html markup)
const CELL_ABBR = {
  gn:'Gn', ex:'Êx', lv:'Lv', nm:'Nm', dt:'Dt',
  js:'Js', jz:'Jz', rt:'Rt', sm1:'1Sm', sm2:'2Sm',
  rs1:'1Rs', rs2:'2Rs', cr1:'1Cr', cr2:'2Cr', ed:'Ed', ne:'Ne', et:'Et',
  jo:'Jó', sl:'Sl', pv:'Pv', ec:'Ec', ct:'Ct',
  is:'Is', jr:'Jr', lm:'Lm', ez:'Ez', dn:'Dn',
  os:'Os', jl:'Jl', am:'Am', ob:'Ob', jn:'Jn', mq:'Mq', na:'Na',
  hc:'Hc', sf:'Sf', ag:'Ag', zc:'Zc', ml:'Ml',
  mt:'Mt', mc:'Mc', lc:'Lc', joe:'Jo',
  at:'At',
  rm:'Rm', co1:'1Co', co2:'2Co', gl:'Gl', ef:'Ef', fp:'Fp', cl:'Cl',
  ts1:'1Ts', ts2:'2Ts', tm1:'1Tm', tm2:'2Tm', tt:'Tt', fm:'Fm',
  hb:'Hb', tg:'Tg', pe1:'1Pe', pe2:'2Pe', jo1:'1Jo', jo2:'2Jo', jo3:'3Jo', jd:'Jd',
  ap:'Ap',
};

function getCategory(abbr) {
  for (const [key, val] of Object.entries(CATEGORY_MAP)) {
    if (abbr.includes(key)) return val.category;
  }
  return 'pen';
}

function getOrder(num) {
  const m = num.match(/Livro (\d+)/);
  return m ? parseInt(m[1]) : 0;
}

// Read the HTML
const html = fs.readFileSync(path.join(rootDir, 'index.html'), 'utf-8');

// Extract just the DB block between "const DB = {" and the closing "};"
const dbStart = html.indexOf('const DB = {');
// Handle both CRLF (Windows) and LF line endings
const dbEndMarker = html.indexOf('\r\n};\r\n', dbStart);
const dbEnd = dbEndMarker !== -1 ? dbEndMarker + 6 : html.indexOf('\n};\n', dbStart) + 4;
let dbSource = html.slice(dbStart, dbEnd);

// Replace template literals with JSON-safe strings (we'll eval in a sandbox)
// We need to run this as JS to get the actual object
// Write a temp module that exports DB
const tmpFile = path.join(__dirname, '_tmp_db.mjs');
// dbSource starts with "const DB = {", replace "const" to make it exportable
const exportableSource = dbSource.replace(/^const DB/, 'export const DB');
fs.writeFileSync(tmpFile, exportableSource + '\n');

// Dynamic import
const { DB } = await import('./_tmp_db.mjs');
fs.unlinkSync(tmpFile);

// Ensure output directories exist
fs.mkdirSync(path.join(outDir, 'pt'), { recursive: true });
fs.mkdirSync(path.join(outDir, 'en'), { recursive: true });

let count = 0;
for (const [id, book] of Object.entries(DB)) {
  const order = getOrder(book.num);
  const category = getCategory(book.abbr);
  const cellAbbr = CELL_ABBR[id] || id.toUpperCase();

  // PT entry
  const pt = {
    id,
    num: book.num,
    title: book.title,
    abbr: book.abbr,
    ...(book.author && { author: book.author }),
    ...(book.chars && book.chars.length && { chars: book.chars }),
    tags: book.tags,
    body: book.body,
    ...(book.verse && { verse: book.verse }),
    translation: 'NAA',
    order,
    category,
    cellAbbr,
  };

  // EN entry (uses _en fields, fallback to PT if missing)
  const en = {
    id,
    num: book.num,
    title: book.title_en || book.title,
    abbr: book.abbr_en || book.abbr,
    ...(book.author && { author: book.author }),
    ...(book.chars_en && book.chars_en.length && { chars: book.chars_en }),
    tags: book.tags_en || book.tags,
    body: book.body_en || book.body,
    ...(book.verse_en && { verse: book.verse_en }),
    translation: 'ESV',
    order,
    category,
    cellAbbr,
  };

  fs.writeFileSync(
    path.join(outDir, 'pt', `${id}.json`),
    JSON.stringify(pt, null, 2),
    'utf-8'
  );
  fs.writeFileSync(
    path.join(outDir, 'en', `${id}.json`),
    JSON.stringify(en, null, 2),
    'utf-8'
  );

  count++;
}

console.log(`✓ Extracted ${count} books → src/content/books/pt/ and /en/`);

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static HTML website for Bible study in Brazilian Portuguese. No build system, no dependencies to install — open any `.html` file directly in a browser.

## Architecture

Five self-contained HTML files, each with all CSS and JavaScript embedded inline (no external `.css` or `.js` files):

- `index.html` — Main page: interactive grid of all 66 canonical books. Each book cell opens a modal with theological commentary. Includes a PNG export feature via `html2canvas` (CDN).
- `at-pentateuco/index.html` — Deep-dive study of the 5 books of Moses. Uses a fixed sidebar with `showSection(id)` navigation (not `showBook`) and scroll-reveal animations. Sections are `<section id="...">` elements, not `<article>`.
- `at-historicos/index.html` — Deep-dive study of the 12 Historical Books.
- `at-poeticos/index.html` — Deep-dive study of the 5 Poetic/Wisdom Books.
- `at-profetas-maiores/index.html` — Deep-dive study of the 5 Major Prophets (Isaiah–Daniel).

### Navigation links

- `index.html` links to each sub-page via `at-pentateuco/index.html`, `at-historicos/index.html`, `at-poeticos/index.html`, `at-profetas-maiores/index.html`.
- Sub-pages link back with `../index.html` ("Voltar à Bíblia" button in the sidebar).

### Sub-page layout pattern (at-historicos, at-poeticos, at-profetas-maiores)

- Fixed sidebar with `.nav-item[data-book="id"]` buttons.
- `<article class="book-panel" id="panel-{id}">` for each book.
- Tabs inside each panel: `showTab(this, bookId, tabKey)` switches between tab panels.
- `showBook(id)` activates the panel, resets tabs to first, and scrolls to top:

```js
window.scrollTo({top:0, behavior:'smooth'});
```

- All four sub-pages have `scrollTo` in their navigation function.

### at-pentateuco layout (different from other sub-pages)

- Uses `showSection(id)` (not `showBook`), targeting `<section id="...">` elements.
- No book-panel/tab structure — each section is a long-form page with timelines, grids, callouts, and scripture blocks.

### Data model (`index.html`)

All 66 books live in a JavaScript object `DB` (one key per book, e.g. `gn`, `ex`, `lv`). Each entry has:

```text
{ num, title, abbr, author, chars[], tags[], body (HTML string), verse }
```

The `show(id)` function populates the modal from `DB[id]` on cell click.

### Styling conventions

- Dark navy/gold theme via CSS custom properties on `:root`.
- Bible quotations use the **NAA (Nova Almeida Atualizada)** version, cited as `— NAA`.
- The Tetragrammaton (LORD) is rendered with small-caps: `<span style="font-variant:small-caps">Senhor</span>`.
- `p { text-align: justify; hyphens: auto; }` is set globally.
- Color accents per section: `--gold: #FFA400` (pentateuco), `--poe: #d4a020` (poéticos), `--mai: #c87820` (profetas maiores).

### Info-grid component

All sub-pages have a "Dados do Livro" info-grid at the top of the study tab for each book. CSS classes:

```text
.info-grid        → CSS grid, auto-fill minmax(210px,1fr)
.info-card        → individual card with border
.info-card-label  → small-caps label (Cinzel, 9px, uppercase)
.info-card-value  → body text (EB Garamond, 16px)
```

Each book has 6 cards covering: Extensão, Estrutura, thematic highlights, key verse, NT connections, and a distinctive data point. The `at-pentateuco` CSS definition for this component was added manually (the others inherited it); it lives just before `.card { }` in that file's `<style>` block.

### External resources (CDN only)

- Google Fonts: Cinzel Decorative, Cinzel, EB Garamond.
- `html2canvas` v1.4.1 — used only in `index.html` for the "Baixar PNG" button.

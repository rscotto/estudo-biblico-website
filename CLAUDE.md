# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static HTML website for Bible study in Brazilian Portuguese. No build system, no dependencies to install — open any `.html` file directly in a browser.

## Directory structure

- Root (`/`) — production version: dark navy/gold theme.
- `v2/` — alternate version with warm amber-brown background (`#2c2416`) instead of navy. Same file structure and all CSS/JS inline. When editing a feature in both versions, changes must be applied to both trees independently.

## Architecture

Six self-contained HTML files per version, each with all CSS and JavaScript embedded inline (no external `.css` or `.js` files):

- `index.html` — Main page: interactive grid of all 66 canonical books. Each book cell opens a modal with theological commentary. Includes a PNG export feature via `html2canvas` (CDN).
- `at-pentateuco/index.html` — Deep-dive study of the 5 books of Moses.
- `at-historicos/index.html` — Deep-dive study of the 12 Historical Books.
- `at-poeticos/index.html` — Deep-dive study of the 5 Poetic/Wisdom Books.
- `at-profetas-maiores/index.html` — Deep-dive study of the 5 Major Prophets (Isaiah–Daniel).
- `at-profetas-menores/index.html` — Deep-dive study of the 12 Minor Prophets (Hosea–Malachi).

### Navigation

- `index.html` section labels (`<a class="slabel slabel-link">`) link to each sub-page. These links are `font-weight:700` (bold).
- Sub-pages link back with `../index.html` via the "Voltar à Bíblia" button (`.sidebar-back`) in the sidebar.

### Sub-page layout pattern (at-historicos, at-poeticos, at-profetas-maiores, at-profetas-menores)

- Fixed sidebar with `.nav-item[data-book="id"]` buttons.
- `<article class="book-panel" id="panel-{id}">` for each book.
- Book header uses: `.book-eyebrow`, `.book-title` (with `<span>` for gold accent), `.book-meta` / `.book-tag`, `.book-verse`.
- Tabs: `<div class="tabs">` containing `.tab-btn` buttons, `showTab(this, bookId, tabKey)` switches panels.
- Tab panels: `<div class="tab-panel" id="{bookId}-{tabKey}">`.
- Standard tab keys: `ctx` (Contexto e Estrutura), `teo` (Teologia), `study` (Estudo Aprofundado). Profetas menores use `contexto`, `teologia`/`visoes`/`disputas`, `messianico`.
- `showBook(id)` activates the panel, resets tabs to first, scrolls to top.

### at-pentateuco layout (different from other sub-pages)

- Uses `showSection(id)` (not `showBook`), targeting `<section id="...">` elements.
- No book-panel/tab structure — each section is a long-form page with timelines, grids, callouts, and scripture blocks.

### Data model (`index.html`)

All 66 books live in a JavaScript object `DB` (one key per book, e.g. `gn`, `ex`, `lv`). Each entry:

```text
{ num, title, abbr, author, chars[], tags[], body (HTML string), verse }
```

The `show(id)` function populates the modal from `DB[id]` on cell click.

### Styling conventions

- Bible quotations use the **NAA (Nova Almeida Atualizada)** version, cited as `— NAA`.
- The Tetragrammaton (LORD) is rendered with small-caps: `<span style="font-variant:small-caps">Senhor</span>`.
- `p { text-align: justify; hyphens: auto; }` is set globally.
- All sub-pages use `--gold: #FFA400` as the primary UI accent color. `--men: #3a8c6e` is defined in `at-profetas-menores` CSS variables but is not used in any UI rule — all UI references use `--gold`.

### Color palettes

**Root version** — navy/gold:

- `--navy: #0a1628`, `--navy-mid: #0f2040`, `--navy-light: #1a3054`

**v2 version** — warm amber-brown:

- `--navy: #2c2416`, `--navy-mid: #3a3020`, `--navy-light: #4a3e28`
- Category accent colors are all within the amber/orange family (no blues or greens).
- Modal uses solid `background:#2c2416` (no `backdrop-filter`) to avoid color bleed.

### Info-grid component ("Dados do Livro")

Every book has a "Dados do Livro" info-grid as the **first block inside the Contexto tab** (`-ctx` or `-contexto` panel). CSS classes:

```text
.info-grid        → CSS grid, auto-fill minmax(210px,1fr)
.info-card        → individual card with border
.info-card-label  → small-caps label (Cinzel, 9px, uppercase)
.info-card-value  → body text (EB Garamond, 16px)
```

Each book has 6 cards. The `at-pentateuco` file has its own CSS definition for this component (added manually, lives just before `.card { }` in its `<style>` block).

### Content components (inside tab panels)

```text
.study-block            → content section with .block-title and .block-body
.key-verse              → highlighted scripture quote with <cite>
.timeline / .tl-item    → chronological list with dot markers
.geo-box                → geographic/background callout box
```

### External resources (CDN only)

- Google Fonts: Cinzel Decorative, Cinzel, EB Garamond.
- `html2canvas` v1.4.1 — used only in `index.html` for the "Baixar PNG" button.

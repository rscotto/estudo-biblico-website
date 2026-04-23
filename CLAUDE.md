# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static HTML website for Bible study in Brazilian Portuguese. No build system, no dependencies to install — open any `.html` file directly in a browser.

## Architecture

Three self-contained HTML files, each with all CSS and JavaScript embedded inline (no external `.css` or `.js` files):

- `index.html` — Main page: interactive grid of all 66 canonical books. Each book cell opens a modal with theological commentary. Includes a PNG export feature via `html2canvas` (CDN).
- `pentateuco/index.html` — Deep-dive study of the Pentateuch (Moses / 5 books), with a fixed sidebar, tabbed sections per book, and scroll-reveal animations.
- `historicos/index.html` — Deep-dive study of the 12 Historical Books, same sidebar + tab layout as Pentateuco.

### Navigation links
- `index.html` links to `pentateuco/index.html` and `historicos/index.html` (relative paths from root).
- Sub-pages link back with `../index.html` ("Voltar à Bíblia" button in the sidebar).

### Data model (`index.html`)
All 66 books live in a JavaScript object `DB` (one key per book, e.g. `gn`, `ex`, `lv`). Each entry has:
```
{ num, title, abbr, author, chars[], tags[], body (HTML string), verse }
```
The `show(id)` function populates the modal from `DB[id]` on cell click.

### Styling conventions
- Dark navy/gold theme via CSS custom properties on `:root`.
- Bible quotations use the **NAA (Nova Almeida Atualizada)** version, cited as `— NAA`.
- The Tetragrammaton (LORD) is rendered with small-caps: `<span style="font-variant:small-caps">Senhor</span>`.
- `p { text-align: justify; hyphens: auto; }` is set globally; exceptions (e.g. `.subline`) override with `text-align: center`.

### External resources (CDN only)
- Google Fonts: Cinzel Decorative, Cinzel, EB Garamond.
- `html2canvas` v1.4.1 — used only in `index.html` for the "Baixar PNG" button.

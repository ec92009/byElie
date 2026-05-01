# Conversation Summary

Date: 2026-05-01

## Context

- Took over after Claude ran out of resources during an upgrade of the static byElie portfolio site.
- Verified GitHub Pages serves `main` from `/`, not `docs/`.
- Local workspace: `/Users/ecohen/Dev/byElie`.

## Cleanup

- Removed the orphan tracked `docs/` mirror.
- Updated `AGENTS.md`, `SHOW_ME_SOP.md`, and `README.md` to describe root-based local preview and GitHub Pages deployment.
- Added `VERSION`, `robots.txt`, `sitemap.xml`, and `scripts/site_maintenance.py`.
- Added SEO meta/canonical/Open Graph tags and favicon/font head consistency across pages.
- Moved home inline CSS into shared stylesheet files.

## Carousel Spaniel Work

- Narrowed carousel cards by about half to give the dog more room.
- Iterated on the spaniel choreography across wide and compact layouts.
- Final behavior:
  - The dog starts from the current layout-specific base position.
  - Wide layouts: dog center aligns to the active card's left edge.
  - Narrow layouts: dog center aligns to the active card's right edge.
  - On the tug beat, the ear flick, card advance, and dog retreat start together.
  - Compact choreography runs at half speed compared with wide.
- Fixed a breakpoint seam at the current browser size where JS saw compact layout but CSS still used wide positioning by driving `--companion-left` from the live carousel profile.
- The dog/card alignment is recalculated from current carousel dimensions so window resizing stays consistent.

## Verification

- Used the in-app Browser plugin repeatedly against `http://localhost:8000/` and `http://localhost:8000/plans.html`.
- Confirmed the current seam-size viewport was about `571x688`.
- Parsed all six root HTML files with Python's `HTMLParser` after changes.
- Confirmed GitHub Pages source with `gh api repos/ec92009/byElie/pages`.

## Published State

- Latest visible UI version: `v62.13`.
- Latest pushed commit in this session before this summary: `2769ef2` (`byelie: sync compact dog base position`).
- GitHub Pages URL: `https://ec92009.github.io/byElie/`.

## Left Untracked

- `.claude/`
- `_src/`

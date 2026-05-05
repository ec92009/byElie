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

---

# Conversation Summary

Date: 2026-05-02

## Scope

Started from the byElie visual system and created a separate Photos By Elie static site, then connected it through the Webapps hub. byElie itself remained the visual/reference source; no byElie site UI changes were made in this conversation.

## Photos By Elie Relationship

- Standalone repo/site: `/Users/ecohen/Dev/PhotosByElie`
- Live site: `https://ec92009.github.io/PhotosByElie/`
- Hub repo: `/Users/ecohen/Dev/Webapps`
- Hub live site: `https://ec92009.github.io/Webapps/`
- Photos By Elie uses byElie's look and feel, logo, topbar treatment, theme behavior, carousel structure, and spaniel companion pattern.

## Photos By Elie Features Added

- Added collection carousel and gallery pages for France, USA, Spain, Mexico, and AI.
- Kept AI last in the collection order.
- Refactored galleries to use shared data/rendering instead of duplicated page code.
- Added reusable photo detail pages.
- Added a localStorage-backed basket.
- Made the basket the source of truth for selected resolutions.
- Detail page resolution checkbox changes now immediately update the basket.
- Basket rows show thumbnails and editable resolution checkboxes.
- Duplicate photo charges are prevented by storing one basket row per photo.

## Leonardo Images

- Checked `~/Pictures/Leonardo/2023/07/12`; it contained empty `UPSCALE` folders.
- Going up to `~/Pictures/Leonardo/2023` found images in February through June.
- Added eight resized generated JPGs from `~/Pictures/Leonardo/2023/06/08/UPSCALE` to the Photos By Elie AI gallery.

## Version And Deployment

- Photos By Elie current version: `v63.8`.
- Webapps hub current Photos By Elie card version: `v63.8`.
- Pushed the standalone PhotosByElie repo and the Webapps hub repo after each major change.
- Latest PhotosByElie commit before this summary: `c2f1604 photosbyelie: auto-sync detail selections`.
- Latest Webapps commit before this summary: `be14482 hub: sync Photos By Elie auto basket`.

## byElie Notes

- Existing byElie untracked folders remain intentionally untouched:
  - `.claude/`
  - `_src/`

---

# Conversation Summary

Date: 2026-05-05

## Scope

- Reviewed newly generated Codex review files in `/Users/ecohen/Dev/byElie`.
- Extracted actionable review feedback into `TODO.md` instead of leaving review documents as loose root files.
- Archived review documents in `Archive/`.
- Prioritized and completed the earlier 2026.05.02 review backlog.

## Maintenance And Backlog Work

- Created `TODO.md` as the repo backlog.
- Archived `Codex.Review.2026.05.02.md`.
- Added `scripts/site_maintenance.py --check` to validate visible versions, CSS cache-bust strings, basic SEO tags, canonical/OG URLs, skip-link consistency, and real-anchor card behavior.
- Bumped byElie to `v66.0` for the first maintenance-check build.
- Later completed the page-chrome backlog item by making `scripts/site_maintenance.py` own the shared head, topbar, footer, nav state, page metadata, canonical URLs, asset wiring, and version strings.
- Regenerated all six HTML pages from that shared shell logic and bumped byElie to `v66.1`.
- Added footers to service pages through the generated shell.
- Updated `README.md` to document the maintenance script and shell ownership.

## 2026.05.05 Review

- Found `byElie Codex Review 2026-05-05.md` in the repo root.
- Added actionable items to `TODO.md`:
  - Replace the empty `mailto:` contact CTA.
  - Extend static checks for local assets, empty links, sitemap/robots drift, canonical URLs, and version consistency.
  - Add a compact mobile navigation treatment if small-screen header links crowd.
  - Add a "Start here" path for uncertain visitors.
  - Add mobile screenshot smoke checks for the header and carousel.
  - Extract repeated SVG carousel companion markup out of the HTML pages.
- Archived the review at `Archive/byElie Codex Review 2026-05-05.md`.

## Verification And Publishing

- Verified maintenance changes with `python3 scripts/site_maintenance.py --check`.
- Verified Python syntax with `python3 -m py_compile scripts/site_maintenance.py`.
- Served the site locally at `http://localhost:8000/` and smoke-checked home, plans, and web-design pages for `v66.1`, cache-busted CSS, active nav, and generated footer.
- Pushed these commits:
  - `b7b9545 byelie: prioritize review todo and add maintenance checks`
  - `a04fe44 byelie: generate shared page shell`
  - `05434c0 byelie: archive codex review backlog`

## Current State

- Current visible byElie version: `v66.1`.
- Latest pushed commit before this summary refresh: `05434c0`.
- Open backlog now comes from the 2026.05.05 review.
- Unrelated local worktree items intentionally left untouched:
  - deleted `2026.05.01_Claude_Review.md`
  - untracked `.TODO.md.swp`

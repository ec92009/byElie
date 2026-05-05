# TODO

## Priority

- P0: Protect accessibility, SEO, and version/cache-bust consistency with deterministic checks.
- P1: Keep real-anchor card navigation as the standard for clickable cards.
- P2: Keep `scripts/site_maintenance.py` as the source of truth for shared page chrome and run it after shell or version changes.

## From Codex review 2026.05.02

- [x] Reduce duplicated page chrome by letting `scripts/site_maintenance.py` own repeated head, topbar, footer, and asset wiring across the six HTML pages.
- [x] Replace JavaScript-only `data-href` card navigation with real anchor elements where cards behave like links, preserving keyboard and screen-reader access. Audited with `scripts/site_maintenance.py --check`; no `data-href` markup remains.
- [x] Add SEO basics and verify `lang` and skip-link consistency across all top-level pages. Covered by `scripts/site_maintenance.py --check`.
- [x] Confirm visible version strings and CSS cache-bust query strings stay synchronized across all HTML pages during future builds. Covered by `scripts/site_maintenance.py --check` and `scripts/site_maintenance.py --version`.

## From Codex review 2026.05.05

- [ ] P0: Replace the empty `mailto:` contact CTA with a real email address or lightweight contact path.
- [ ] P0: Extend `scripts/site_maintenance.py --check` to catch missing local assets, empty links, sitemap/robots drift, and the existing canonical/version rules.
- [ ] P1: Add a compact mobile navigation treatment if header links crowd the brand/version area on small screens.
- [ ] P1: Add a "Start here" path that routes uncertain visitors toward CAD, prints, plans, web work, or photos.
- [ ] P1: Add a mobile screenshot smoke check for the header and carousel.
- [ ] P2: Extract repeated SVG carousel companion markup out of the six HTML pages into generated shared markup or external assets.

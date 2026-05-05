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

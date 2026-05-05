# TODO

## Priority

- P0: Protect accessibility, SEO, and version/cache-bust consistency with deterministic checks.
- P1: Keep real-anchor card navigation as the standard for clickable cards.
- P2: Reduce duplicated page chrome when the next page-structure change makes the payoff worth the extra machinery.

## From Codex review 2026.05.02

- [ ] Reduce duplicated page chrome by letting `scripts/site_maintenance.py` or a tiny generator own repeated head, topbar, footer, and asset wiring across the six HTML pages.
- [x] Replace JavaScript-only `data-href` card navigation with real anchor elements where cards behave like links, preserving keyboard and screen-reader access. Audited with `scripts/site_maintenance.py --check`; no `data-href` markup remains.
- [x] Add SEO basics and verify `lang` and skip-link consistency across all top-level pages. Covered by `scripts/site_maintenance.py --check`.
- [x] Confirm visible version strings and CSS cache-bust query strings stay synchronized across all HTML pages during future builds. Covered by `scripts/site_maintenance.py --check` and `scripts/site_maintenance.py --version`.

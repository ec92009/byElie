# byElie Codex Review 2026-05-07

Reviewed at: 2026-05-07 00:00 Europe/Madrid

1/ General architecture:
- The static site is readable, but every page repeats substantial structure. Introduce a tiny maintenance workflow or template source so nav, footer, version query strings, and shared sections are updated once.
- Keep the deployed output static, but generate repeated page chrome from data to reduce copy/paste drift.
- `scripts/site_maintenance.py` is a good anchor; expand it into link/version/content consistency checks before adding more pages.

2/ UI:
- The site needs consistent hierarchy across home, plans, prints, gallery, CAD, and web design pages. Shared header/footer and call-to-action styling should be identical unless a page has a strong reason to differ.
- Large repeated HTML pages increase the risk of small layout inconsistencies on mobile. Audit longest headings, cards, and image grids.
- Keep visual assets prominent; this site sells personal creative work, so pages should show examples before long explanation.

3/ UX:
- Make each service page answer three questions quickly: what is offered, what the visitor gets, and how to start.
- Add stronger cross-links between related services, prints, and gallery examples.
- Make the contact/request path consistent from every page.

4/ Testing:
- Add link, asset, sitemap, and cache-bust consistency checks to `scripts/site_maintenance.py`.
- Add a mobile screenshot review for every page after visual changes.
- Add basic HTML validation and accessibility checks.

5/ Everything else:
- Versioning instructions are specific; docs-only review files should not force visible site version bumps, but user-visible page changes should.
- Keep `TODO.md` prioritized around conversion and content quality, not just visual polish.
- Consider moving old critique/review docs under `Archive/` consistently.

6/ My suggetions:
1. Expand `scripts/site_maintenance.py` into a full static-site audit.
2. Template repeated nav/footer/version markup.
3. Strengthen contact/request CTAs on every service page.
4. Add mobile visual checks for all pages.
5. Use gallery/work examples earlier in service-page flows.

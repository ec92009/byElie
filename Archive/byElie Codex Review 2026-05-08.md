# byElie Codex Review 2026-05-08

Generated: 2026-05-08 00:00 Europe/Madrid

1/ General architecture

- byElie is a static multi-page site with a useful maintenance script. The main architecture issue is duplicated inline carousel behavior across six HTML pages.
- Keep page shell ownership in `scripts/site_maintenance.py`, but extract duplicated interactive behavior into shared JS before adding more pages or variants.

2/ UI

- The site has a clear creator/service portfolio structure. The next UI improvement is consistency: service cards, CTAs, carousels, and version badges should behave identically across all pages after maintenance runs.
- Make sure hero media and decorative elements do not crowd service-specific information on compact screens. The service pages should prioritize scannable offer, examples, and action.

3/ UX

- The user journey should separate "browse Elie's work" from "hire/request something". Each service page should have a direct path to inquiry, pricing expectation, and examples.
- Photos By Elie is now separate. Cross-links should make that relationship clear without making byElie depend on PhotosByElie internals.

4/ Testing

- There are no visible tests. Add a static maintenance check for duplicated shell, visible version, cache-bust query strings, required SEO tags, and broken links.
- Add a small responsive smoke check for all six pages so carousel and header changes do not regress mobile layout.

5/ Everything else

- The worktree already shows user changes/deletions around old review files and TODO. Preserve that state and avoid broad cleanup outside the review workflow.
- Keep review-derived backlog items in `TODO.md`; daily review files should not become the only source of next actions.

6/ My suggetions:

1. Extract duplicated carousel behavior into one shared script used by all six pages.
2. Expand `scripts/site_maintenance.py --check` to validate links, versions, cache busts, and SEO tags.
3. Add desktop/mobile smoke screenshots for every page.
4. Tighten each service page around examples, offer, pricing expectation, and inquiry CTA.
5. Keep PhotosByElie links clearly external/canonical and avoid mirrored implementation coupling.

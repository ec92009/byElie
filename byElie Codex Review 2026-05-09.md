# byElie Codex Review 2026-05-09

Generated: 2026-05-09 00:00 Europe/Madrid

1/ General architecture

- byElie is a static multi-page site with a useful maintenance script. The main architectural issue is repeated page behavior and large parallel HTML files.
- Keep `scripts/site_maintenance.py` as the shell owner, but extract shared interactive behavior into JS and shared content metadata before adding more pages.

2/ UI

- The site has a clear creator/service portfolio shape. The next UI improvement is consistency across service pages: cards, CTAs, carousel behavior, version badge, and header state.
- Service pages should keep examples, offer, and inquiry path above decorative material on compact screens.

3/ UX

- The journey should clearly split browsing work from hiring/requesting work. Each service page needs examples, fit, pricing expectation or consultation framing, and an inquiry CTA.
- PhotosByElie is now separate; cross-links should be explicit and canonical without copying implementation details back into byElie.

4/ Testing

- No tests are visible. Expand the maintenance checker to validate links, SEO tags, versions, cache-busts, and required shared shell sections.
- Add desktop/mobile smoke screenshots for all public pages so shared header/carousel changes do not regress layout.

5/ Everything else

- Keep review-driven backlog in `TODO.md`; daily review files are too easy to lose in Archive history.
- The static-site simplicity is a strength. Avoid framework migration unless duplicated maintenance becomes a real blocker.

6/ My suggetions:

1. Extract duplicated carousel/shared behavior into one JS module.
2. Expand `scripts/site_maintenance.py --check` for links, SEO, versions, and cache busts.
3. Add responsive smoke checks for all public pages.
4. Tighten service pages around examples, offer, fit, and inquiry CTA.
5. Keep PhotosByElie links canonical and external to this site's implementation.

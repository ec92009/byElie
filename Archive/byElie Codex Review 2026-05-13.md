# byElie Codex Review 2026-05-13

Reviewed: 2026-05-13

1/ General architecture

- byElie is a static portfolio/service site with six HTML pages, shared CSS, assets, a maintenance script, and version file.
- `scripts/site_maintenance.py` is the right direction because it reduces drift across shared shell markup and versioning.
- The repeated inline carousel/spaniel behavior across pages remains the main architecture issue.
- The build-free model is fine, but validation scripts should become the effective build gate.

2/ UI

- The multi-service structure is coherent: plans, prints, gallery, CAD, and web design.
- Shared shell consistency matters more than per-page visual variation.
- Carousel/motion behavior should be consolidated so fixes do not require six manual edits.
- Service pages should lean on concrete proof imagery and sample deliverables.

3/ UX

- Visitors need to quickly understand what Elie offers, see relevant proof, and know how to request work.
- Each service page should have one clear next action with process, estimate, and delivery expectations.
- The Photos By Elie relationship is documented; public navigation should make the standalone site feel intentional.
- The homepage should route users cleanly rather than trying to explain every service in detail.

4/ Testing

- No formal tests were visible, but the maintenance script is a good foundation.
- Expand `site_maintenance.py --check` to validate shared shell, required CTAs, image alt text, canonical links, and cache-bust versions.
- Add mobile screenshot smoke checks for all six pages.
- Add link checking for internal pages, Photos By Elie links, sitemap, and robots.

5/ Everything else

- The repo README says Codex reviews should be mined into `TODO.md` and archived; keep that backlog loop active.
- Final copy should stay grounded in real services and examples, not generic creator-site language.
- Use the visible version workflow for any user-facing changes.

6/ My suggetions:

1. Extract duplicated carousel/spaniel behavior into one shared JS file and update all six pages.
2. Expand `scripts/site_maintenance.py --check` for CTAs, alt text, links, shared shell, and cache-bust versions.
3. Add one clear next action to every service page with process and delivery expectations.
4. Run mobile screenshots for all six pages and fix header/card/CTA wrapping issues.
5. Move actionable review items into `TODO.md`, then archive completed reviews per repo workflow.
6. Add concrete proof examples or sample deliverables to the service pages.

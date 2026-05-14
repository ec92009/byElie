# byElie Codex Review 2026-05-12

Reviewed: 2026-05-12

1/ General architecture

- byElie is a static portfolio/service site with six HTML pages, shared CSS, assets, a maintenance script, and version file.
- The `scripts/site_maintenance.py` ownership model is good: it reduces drift across shared head/topbar/footer/version markup.
- The main architectural issue is duplicated inline carousel behavior across all six pages, already called out in the README.
- The site is simple enough to remain build-free, but validation scripts should be treated as the build gate.

2/ UI

- The site has a coherent multi-service portfolio structure: plans, prints, gallery, CAD, and web design.
- Shared shell consistency matters more here than per-page experimentation; keep headers, footers, and cards aligned.
- The carousel/spaniel motion should be consolidated so visual fixes do not require six manual edits.
- Service pages should use proof imagery and concrete examples wherever possible.

3/ UX

- Visitors need to quickly understand what Elie offers and how to request it.
- Each service page should have one clear next action and a concise explanation of process, price/estimate expectations, and delivery.
- The Photos By Elie relationship is documented; public navigation should make the standalone site feel intentional rather than a detour.
- Avoid overwhelming the homepage with every service detail; use it as a routing surface.

4/ Testing

- No formal tests were visible, but the maintenance script includes useful checks.
- Expand `site_maintenance.py --check` to validate shared shell consistency, required CTAs, image alt text, canonical links, and version cache-busting.
- Add a mobile screenshot smoke pass for all six pages.
- Add link checking for internal pages, Photos By Elie links, sitemap, and robots.

5/ Everything else

- The README includes an instruction to triage Codex reviews into `TODO.md` and then archive them. Today's review should be mined into that backlog.
- The site should keep final copy grounded in actual services and examples, not generic creator-site language.
- Version workflow is clear; keep using it for visible changes.

6/ My suggetions:

1. Extract the duplicated carousel/spaniel script into one shared JS file and update all six pages to use it.
2. Expand `scripts/site_maintenance.py --check` to cover CTAs, alt text, internal links, cache-bust versions, and shared shell consistency.
3. Add one clear next action to every service page with expected process and delivery language.
4. Run mobile screenshots for all six pages and fix any header/card/CTA wrapping issues.
5. Turn actionable items from this review into `TODO.md`, then archive the review per repo workflow.
6. Add concrete proof examples or sample deliverables to the service pages.

# byElie Codex Review 2026-05-11

Review time: 2026-05-11 02:05 CEST.

1/ General architecture

- The site is an appropriately simple static portfolio with shared shell maintenance handled by `scripts/site_maintenance.py`.
- The split between root HTML pages, shared CSS, page-specific CSS, assets, VERSION, TODO, and Archive is clear.
- Inline carousel behavior duplicated across six pages is the main architectural maintenance risk.

2/ UI

- The visual system is established and reused across service pages.
- The topbar/version/cache-bust workflow is disciplined, but it depends on running the maintenance script after changes.
- The portfolio would benefit from more real examples and fewer generic service claims where possible.

3/ UX

- The site covers several offers: plans, prints, photography, CAD, and web design. The homepage should keep routing visitors to the right service quickly.
- Cross-links to Photos By Elie are important now that it is standalone; they should remain prominent but not confusing.
- Clear calls to action per service page matter more than adding new sections.

4/ Testing

- No tests were found, but the maintenance script has a `--check` mode. Treat that as the baseline gate.
- Add a simple browser/link smoke test for all pages, CSS cache-bust values, topbar/footer presence, and Photos By Elie outbound links.
- Carousel duplication should be covered by either shared extraction or checks that all pages contain the same version of the behavior.

5/ Everything else

- README is strong and accurately documents the maintenance workflow.
- Review files should continue to be triaged into TODO before archiving so the backlog stays actionable.

6/ My suggetions:

1. Extract the duplicated carousel script into one shared JS file.
2. Add link and page-shell smoke tests for all six pages.
3. Keep `scripts/site_maintenance.py --check` as the required pre-push gate.
4. Add stronger examples/proof points for each service page.
5. Keep Photos By Elie cross-links clear as external/standalone destinations.

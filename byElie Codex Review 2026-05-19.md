# byElie Codex Review 2026-05-19

Timestamp: 2026-05-19 02:02:56 CEST

1/ General architecture

- The static-site architecture is appropriately simple, but six hand-edited HTML pages still depend heavily on `scripts/site_maintenance.py` staying current.
- The strongest next architectural move is extending that checker from shell/version consistency into a broader static-site contract: empty links, missing local assets, sitemap drift, robots drift, and canonical URL drift.
- The repo is close to a sustainable no-build setup; avoid adding a framework unless content volume or repeatable data structures clearly require it.

2/ UI

- The portfolio structure is clear, with page-specific services and shared chrome.
- Header density remains the main UI risk on small screens because brand, version, navigation, and theme affordances compete for space.
- The SVG companion/carousel treatment is distinctive, but repeated markup makes it harder to keep polished across pages.

3/ UX

- Visitors who already know what they need can navigate well, but uncertain visitors still need a stronger routing path from problem to service.
- Contact intent is weakened by the unresolved empty `mailto:` path.
- Keyboard and screen-reader direction improved with real anchors, so future card work should keep that standard.

4/ Testing

- `scripts/site_maintenance.py --check` is the right anchor for lightweight QA.
- Add mobile screenshot smoke coverage for the header and carousel before more visual polish.
- Link/asset verification should run as part of the same maintenance command so publishing mistakes fail early.

5/everything else

- README and TODO are useful and outsider-readable.
- Version/cache-bust discipline is clear, but it depends on remembering the maintenance script.
- Keep the external Photos By Elie relationship documented so the portfolio does not accidentally grow a stale mirror.

6/ My suggetions:

1. Replace the empty contact CTA with a real email/contact path.
2. Extend `scripts/site_maintenance.py --check` to validate empty links, local assets, sitemap, robots, canonical URLs, and version strings.
3. Add a compact mobile nav treatment and verify it at narrow widths.
4. Add a "Start here" chooser for visitors unsure which service fits.
5. Extract repeated companion/carousel markup into generated shared markup or asset includes.

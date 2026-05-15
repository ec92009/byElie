# byElie Codex Review 2026-05-14

Review timestamp: 2026-05-14, Europe/Madrid.

1/ General architecture

- The static-site architecture is appropriately simple, and `scripts/site_maintenance.py` is the right central mechanism for shared page chrome and version/cache-bust consistency.
- Six HTML pages still carry some duplicated page-specific behavior, especially carousel companion code.
- The site has a clear relationship to Photos By Elie and Webapps; keep this repo as the canonical byElie surface only.

2/ UI

- The visual language is distinctive and consistent, but repeated animation/companion markup increases the chance of inconsistent behavior.
- Mobile navigation remains a risk if header links crowd the brand/version area.
- Contact CTAs need real destinations; empty `mailto:` is a user-facing credibility issue.

3/ UX

- A "start here" path would help uncertain visitors choose between plans, prints, CAD, web work, and photo services.
- Real anchor cards are the right accessibility direction and should remain the standard.
- The Photos By Elie relationship should be presented as a related service, not a confusing duplicate project.

4/ Testing

- `site_maintenance.py --check` is valuable; extend it to catch missing local assets, empty links, sitemap/robots drift, and canonical/version rules.
- Add a mobile screenshot smoke check for header, navigation, and carousel behavior.
- Add link checks for external Photos By Elie and Webapps destinations.

5/ Everything else

- The README is clear about root-based GitHub Pages deployment; preserve that.
- Archive review documents after extracting actionable work into TODO, matching repo guidance.
- Untracked historical folders should remain untouched unless the user explicitly wants cleanup.

6/ My suggetions:

1. Replace the empty `mailto:` contact CTA with a real contact path.
2. Extend `scripts/site_maintenance.py --check` for assets, empty links, sitemap/robots, canonicals, and versions.
3. Add a compact mobile navigation treatment and screenshot smoke test.
4. Add a "Start here" routing section for uncertain visitors.
5. Extract duplicated carousel companion markup/logic into generated shared markup or a common script.
6. Keep Photos By Elie as an external/canonical related service, not a mirrored byElie page.

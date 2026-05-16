# byElie Codex Review 2026-05-15

1/ General architecture:
- The static multi-page structure is straightforward, but the README notes duplicated inline carousel behavior across six pages. That should become one shared script before further carousel tuning.
- `scripts/site_maintenance.py` is the right ownership point for shared shell/version consistency. Keep expanding checks there instead of making manual page-by-page edits.

2/ UI:
- The visual language is established. Next UI work should focus on consistent service-page rhythm, image quality, and carousel behavior across viewport sizes.
- Ensure all card/link affordances are clear on touch devices, not only hover-friendly desktop layouts.

3/ UX:
- The site covers several services. Each page should have one obvious next action and avoid competing CTAs.
- Linkage to Photos By Elie is clear; keep cross-site expectations explicit so users know when they are entering the photo gallery/order flow.

4/ Testing:
- There are no test files, but `site_maintenance.py --check` covers part of the need. Add it to a documented pre-push workflow and extend it for carousel script consistency.
- Add a small Playwright smoke pass for navigation, version labels, and mobile layout overflow.

5/ Everything else:
- The README is good and already tells future agents how to triage reviews into `TODO.md`. Keep doing that to avoid backlog drift.
- Do not treat review-only docs as visible site changes requiring version bumps.

6/ My suggetions:
1. Extract duplicated carousel behavior into a shared JS file.
2. Extend `scripts/site_maintenance.py --check` to catch carousel and CTA consistency drift.
3. Add Playwright smoke checks for page navigation and mobile overflow.
4. Tighten each service page around one primary CTA.
5. Keep Photos By Elie cross-links explicit and current.

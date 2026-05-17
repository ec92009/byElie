# byElie Codex Review 2026-05-16

Review timestamp: 2026-05-16 02:03 CEST.

1/ General architecture:
- The static root-pages structure remains appropriate, and `scripts/site_maintenance.py` is the right source of truth for shared page chrome.
- The main architecture risk is duplicated carousel/companion markup and behavior across pages, which raises maintenance cost.

2/ UI:
- The visual system is distinctive and coherent for a creator portfolio.
- Header density, carousel behavior, and service-card layout should keep getting mobile screenshot checks because the page has several animated/brand-specific elements.

3/ UX:
- The service categories are clear, but visitors who are unsure what they need may still need a stronger "start here" path.
- Contact remains the most important unresolved conversion detail if any CTA still points to an empty or placeholder destination.

4/ Testing:
- The maintenance checker is a strong foundation.
- Extend it to catch missing local assets, empty links, sitemap/robots drift, and mobile screenshot regressions.

5/ Everything else:
- The TODO already captures many review-derived items; keep using it instead of letting review files accumulate.
- Photos By Elie should remain a related standalone site, not a mirror maintained inside this repo.

6/ My suggetions:
1. Replace any empty contact CTA with a real email, form path, or explicit contact route.
2. Extend `scripts/site_maintenance.py --check` to validate local assets, empty links, sitemap, and robots.
3. Add a guided "Start here" section routing visitors to CAD, prints, plans, web, or photos.
4. Extract repeated carousel companion markup or generate it from shared code.
5. Add a mobile screenshot smoke check for header, carousel, and primary service cards.

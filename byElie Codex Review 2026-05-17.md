# byElie Codex Review 2026-05-17

Reviewed: 2026-05-17 02:04

1/ General architecture:
- The static site is straightforward and well suited to the portfolio/service scope.
- Shared CSS and maintenance scripts are the right place to centralize repeated checks.
- Repeated page/card/carousel structures may eventually deserve generation from data rather than manual duplication.

2/ UI:
- The service categories are visible across pages, but the path for a new visitor should be more guided.
- Contact CTAs should never be empty or ambiguous.
- Mobile header, carousel, and service-card layout are the highest-value UI smoke targets.

3/ UX:
- A "start here" route would help visitors choose between CAD, prints, plans, web, and photos.
- Each service page should have a clear next action and expectation for what the visitor should provide.
- Portfolio/gallery examples should reinforce the service path rather than become a disconnected gallery.

4/ Testing:
- Extend `scripts/site_maintenance.py --check` to validate local assets, empty links, sitemap, robots, and canonical navigation.
- Add a mobile screenshot smoke pass for header, carousel, and primary cards.
- Add a check that all service CTAs resolve to real contact or project routes.

5/ Everything else:
- The repo is ahead of origin, so GitHub handoff is incomplete.
- Old review files and external critique docs should be archived or converted into actionable backlog items.
- README should stay focused on current public behavior and deployment.

6/ My suggetions:
1. Replace any empty contact CTA with a real email, form path, or explicit contact route.
2. Extend `scripts/site_maintenance.py --check` for assets, empty links, sitemap, robots, and navigation.
3. Add a guided "Start here" section routing visitors to CAD, prints, plans, web, or photos.
4. Extract repeated page/card/carousel patterns or generate them from shared data.
5. Push the current local commits after the CTA and maintenance-check backlog is captured.

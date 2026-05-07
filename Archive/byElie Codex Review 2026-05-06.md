# byElie Codex Review 2026-05-06

Timestamp: 2026-05-06 02:02 CEST

## 1/ General architecture

- The static-site architecture is appropriate for a personal/service portfolio.
- Keep shared layout, version badge, navigation, and cache-busting centralized; multi-page static sites drift quickly.
- The existing `scripts/site_maintenance.py` should become the canonical place for sitemap, version, cache-bust, and link checks.
- Preserve GitHub Pages root publishing and avoid adding a build step unless the site outgrows direct HTML/CSS/JS.

## 2/ UI

- The site needs consistent first-viewport signaling across service pages: who, offer, proof, and next action.
- Keep cards compact and avoid repeated decorative elements that dilute the portfolio/work examples.
- Image assets should carry the brand; avoid placeholders that make the site feel less current.

## 3/ UX

- Each service page should have one clear conversion path: contact, plan request, print inquiry, CAD request, or web-design inquiry.
- Add stronger cross-links between gallery, prints, plans, CAD, and web design so users can move by intent rather than nav memorization.
- Make the version badge and cache-bust process invisible to normal visitors but reliable for operators.

## 4/ Testing

- Add a static smoke command that validates links, image references, sitemap entries, robots, and cache-bust consistency.
- Add viewport checks for the home page and every service page.
- Validate contact/CTA links and external targets before every publish.

## 5/ Everything else

- There is an existing deleted Claude review file in git status; resolve that separately so review automation does not mask unrelated work.
- Keep `TODO.md` as a small backlog, not a history log.
- Add short alt text conventions for portfolio images.

## 6/ My suggetions:

1. Extend `scripts/site_maintenance.py` into a full publish smoke check.
2. Standardize CTA placement and intent on every top-level page.
3. Add active link/image/sitemap validation before publishing.
4. Tighten cross-links between related service pages.
5. Resolve the existing deleted review file as its own cleanup commit.

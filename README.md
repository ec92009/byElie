# byElie

Creator portfolio and service site for Elie — 3D print plans, physical prints, photo services, Photos By Elie galleries, CAD on demand, and web design.

## Structure

- `index.html`: home / hero page
- `plans.html`: 3D print plans
- `prints.html`: physical printed items
- `gallery.html`: photo services
- `cad-design.html`: CAD on demand
- `web-design.html`: website design & maintenance
- `https://ec92009.github.io/PhotosByElie/`: standalone Photos By Elie GitHub Pages site
- `shared.css`: shared layout and component styles
- `styles.css`: page-specific overrides and theme
- `assets/`: logos and images
- `VERSION`: visible site/cache-bust version source
- `.wst/site.json`: public WST monitorability declaration for the homepage pilot
- `TODO.md`: review-derived backlog and completion status
- `Archive/`: archived review documents

## Dependencies

No build step or package manager required.

- Browser: plain HTML/CSS/JS
- Local preview: `python3 -m http.server`
- External assets: Google Fonts loaded at runtime

## WST monitoring

- The byElie homepage is the WST GitHub Pages guinea pig. It uses a cookieless, sessionless aggregate beacon for page views and marked CTA presses; Visits and conversions remain unavailable. The footer notice discloses the measurement, and previews or synthetic checks stay outside production totals.
- The public monitorability declaration lives at `.wst/site.json`. It is an owner-approved declaration, not live proof; WST records beacon observations separately.

## Maintenance

After editing site files, sync the shared head, topbar, footer, asset wiring, and visible version strings:

```sh
python3 scripts/site_maintenance.py --version "$(cat VERSION)"
```

Validate the shared shell, visible versions, CSS cache-bust strings, basic SEO tags, skip links, and link-card markup:

```sh
python3 scripts/site_maintenance.py --check
```

To publish a new build, update `VERSION` to the next `vX.Y` value without the `v` prefix, then run the same command.

GitHub Pages serves this repo from `main` at `/`. There is no `docs/` mirror; edit the root HTML/CSS files directly.

The page shell is owned by `scripts/site_maintenance.py`. Page-specific main content and inline carousel scripts still live in each HTML file. The carousel spaniel behavior is duplicated inline across the six HTML pages. When changing its movement or sizing, update all six pages and verify both wide and compact viewport behavior.

When a Codex review appears in the repo root, extract actionable items into `TODO.md`, then move the review into `Archive/`.

Current visible byElie version: `v247.0`.

## Related Sites

- Photos By Elie now lives as a standalone repo/site at `https://ec92009.github.io/PhotosByElie/`.
- The Webapps hub links to Photos By Elie and also mirrors it under `/PhotosByElie/`.
- Photos By Elie uses the byElie visual language and carousel structure, but keeps its gallery, detail, and basket code in its own repo.
- Current Photos By Elie version at the end of this conversation: `v63.8`.
- Photos By Elie collections are France, USA, Spain, Mexico, and AI.
- Photos By Elie basket state is localStorage-backed and is the source of truth for selected photo resolutions.

## GitHub

- `origin`: `https://github.com/ec92009/byElie.git`
- GitHub Pages: `https://ec92009.github.io/byElie/`

Local workspace: `/Users/ecohen/Dev/byElie`

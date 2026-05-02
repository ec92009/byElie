# byElie

Creator portfolio and service site for Elie — 3D print plans, physical prints, photo services, Photos By Elie galleries, CAD on demand, and web design.

## Structure

- `index.html`: home / hero page
- `plans.html`: 3D print plans
- `prints.html`: physical printed items
- `gallery.html`: photo services
- `cad-design.html`: CAD on demand
- `web-design.html`: website design & maintenance
- `https://ec92009.github.io/PhotosByElie/`: public Photos By Elie hub linked from the home page
- `shared.css`: shared layout and component styles
- `styles.css`: page-specific overrides and theme
- `assets/`: logos and images
- `VERSION`: visible site/cache-bust version source

## Dependencies

No build step or package manager required.

- Browser: plain HTML/CSS/JS
- Local preview: `python3 -m http.server`
- External assets: Google Fonts loaded at runtime

## Maintenance

After editing site files, sync visible version strings:

```sh
python3 scripts/site_maintenance.py --version "$(cat VERSION)"
```

To publish a new build, update `VERSION` to the next `vX.Y` value without the `v` prefix, then run the same command.

GitHub Pages serves this repo from `main` at `/`. There is no `docs/` mirror; edit the root HTML/CSS files directly.

The carousel spaniel behavior is duplicated inline across the six HTML pages. When changing its movement or sizing, update all six pages and verify both wide and compact viewport behavior.

## GitHub

- `origin`: `https://github.com/ec92009/byElie.git`
- GitHub Pages: `https://ec92009.github.io/byElie/`

Local workspace: `/Users/ecohen/Dev/byElie`

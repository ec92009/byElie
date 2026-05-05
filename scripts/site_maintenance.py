#!/usr/bin/env python3
"""Small maintenance helpers for the static byElie site."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    "index.html",
    "plans.html",
    "prints.html",
    "gallery.html",
    "cad-design.html",
    "web-design.html",
)

BASE_URL = "https://ec92009.github.io/byElie"
NAV_ITEMS = (
    ("Home", "./", "index.html"),
    ("3D Plans", "./plans.html", "plans.html"),
    ("Physical Prints", "./prints.html", "prints.html"),
    ("Web Design", "./web-design.html", "web-design.html"),
    ("CAD on demand", "./cad-design.html", "cad-design.html"),
    ("Gallery", "./gallery.html", "gallery.html"),
    ("Photos By Elie", "https://ec92009.github.io/PhotosByElie/", None),
)
FOOTER_ITEMS = (
    ("Home", "./"),
    ("3D Plans", "./plans.html"),
    ("Prints", "./prints.html"),
    ("Web Design", "./web-design.html"),
    ("CAD", "./cad-design.html"),
    ("Gallery", "./gallery.html"),
    ("Photos By Elie", "https://ec92009.github.io/PhotosByElie/"),
)
PAGE_META = {
    "index.html": {
        "title": "By Elie | Creator Portfolio",
        "description": "By Elie is a creator portfolio for practical 3D print plans, physical prints, CAD modeling, Photos By Elie galleries, and lightweight website maintenance.",
        "styles": ("shared.css", "styles.css"),
        "brand_logo": True,
    },
    "plans.html": {
        "title": "By Elie | 3D Plans",
        "description": "Downloadable 3D print plan packs from By Elie, built with clear print notes, tested tolerances, and organized STL/3MF delivery.",
        "styles": ("shared.css",),
    },
    "prints.html": {
        "title": "By Elie | 3D Physical Prints",
        "description": "Physical 3D printed items from By Elie, including prototypes, small production runs, finishing, and quality checks before delivery.",
        "styles": ("shared.css",),
    },
    "gallery.html": {
        "title": "By Elie | Photo Gallery",
        "description": "By Elie photo services for product listings, campaigns, and social proof with clean lighting, composition, and marketplace-ready edits.",
        "styles": ("shared.css",),
    },
    "cad-design.html": {
        "title": "By Elie | CAD on demand",
        "description": "CAD on demand from By Elie for idea-to-file modeling, printability checks, revision loops, and manufacturer-ready exports.",
        "styles": ("shared.css",),
    },
    "web-design.html": {
        "title": "By Elie | Web Design & Maintenance",
        "description": "Website design and maintenance by Elie for small businesses that need conversion-focused pages and lightweight content operations.",
        "styles": ("shared.css",),
    },
}
REQUIRED_HEAD_SNIPPETS = (
    "<title>",
    '<meta name="description"',
    '<meta property="og:title"',
    '<meta property="og:description"',
    '<meta property="og:type" content="website"',
    '<meta property="og:url"',
    '<meta property="og:image"',
    '<meta name="twitter:card"',
    '<link rel="canonical"',
)


def read_version() -> str:
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def render_head(page: str, version: str) -> str:
    meta = PAGE_META[page]
    canonical = expected_canonical(page)
    stylesheet_links = "\n".join(
        f'  <link rel="stylesheet" href="./{stylesheet}?v={version}"/>'
        for stylesheet in meta["styles"]
    )
    return f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{meta["title"]}</title>
  <meta name="description" content="{meta["description"]}"/>
  <meta property="og:title" content="{meta["title"]}"/>
  <meta property="og:description" content="{meta["description"]}"/>
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="{canonical}"/>
  <meta property="og:image" content="{BASE_URL}/assets/byelie-logo.png"/>
  <meta name="twitter:card" content="summary"/>
  <link rel="canonical" href="{canonical}"/>
  <link rel="icon" type="image/png" sizes="512x512" href="./assets/byelie-logo.png" />
  <script>
    (() => {{
      try {{
        const saved = localStorage.getItem('byelie-theme');
        if (saved === 'light' || saved === 'dark') document.documentElement.dataset.theme = saved;
      }} catch {{}}
    }})();
  </script>
{stylesheet_links}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>"""


def render_topbar(page: str, version: str) -> str:
    nav_links = []
    for label, href, active_page in NAV_ITEMS:
        class_attr = ' class="is-active"' if active_page == page else ""
        nav_links.append(f'      <a{class_attr} href="{href}">{label}</a>')

    nav_html = " <span>|</span>\n".join(nav_links)
    logo_html = ""
    if PAGE_META[page].get("brand_logo"):
        logo_html = '<img class="site-logo" src="./assets/byelie-logo.png" alt="By Elie logo" />'

    return f"""<body>
  <a class="skip-link" href="#main-content">Skip to content</a>
  <header class="topbar shell">
    <nav class="version-switch" aria-label="Site navigation">
{nav_html}
    </nav>
    <div class="brand">{logo_html}BY ELIE — v{version}</div>
    <button class="theme-toggle" type="button" data-theme-toggle><span class="mode-light">Night</span><span class="mode-dark">Day</span></button>
  </header>"""


def render_footer() -> str:
    footer_links = "\n".join(f'        <a href="{href}">{label}</a>' for label, href in FOOTER_ITEMS)
    return f"""  <footer class="site-footer">
    <div class="shell">
      <p class="footer-note">© 2026 By Elie &middot; Built to ship</p>
      <nav class="footer-nav" aria-label="Footer navigation">
{footer_links}
      </nav>
    </div>
  </footer>"""


def render_document(page: str, text: str, version: str) -> str:
    main_start = text.index('  <main id="main-content" class="shell">')
    main_end = text.index("\n  </main>", main_start) + len("\n  </main>")
    script_start = text.index("  <script>", main_end)
    main_html = text[main_start:main_end]
    script_tail = text[script_start:].rstrip()

    return "\n".join(
        (
            render_head(page, version),
            render_topbar(page, version),
            main_html,
            render_footer(),
            script_tail,
        )
    ) + "\n"


def sync_shell(version: str) -> None:
    for rel in PAGES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        path.write_text(render_document(rel, text, version), encoding="utf-8")
    (ROOT / "VERSION").write_text(f"{version}\n", encoding="utf-8")


def expected_canonical(page: str) -> str:
    if page == "index.html":
        return f"{BASE_URL}/"
    return f"{BASE_URL}/{page}"


def collect_issues(version: str) -> list[str]:
    issues: list[str] = []

    if not re.fullmatch(r"\d+\.\d+", version):
        issues.append(f"VERSION must look like X.Y, found {version!r}.")

    for rel in PAGES:
        path = ROOT / rel
        if not path.exists():
            issues.append(f"{rel} is missing.")
            continue

        text = path.read_text(encoding="utf-8")
        if '<html lang="en"' not in text:
            issues.append(f"{rel} must declare html lang=\"en\".")
        if '<a class="skip-link" href="#main-content">' not in text:
            issues.append(f"{rel} must include the skip link.")
        if '<main id="main-content"' not in text:
            issues.append(f"{rel} must include main#main-content.")
        if "data-href" in text:
            issues.append(f"{rel} contains data-href; use real anchors for link cards.")

        for snippet in REQUIRED_HEAD_SNIPPETS:
            if snippet not in text:
                issues.append(f"{rel} is missing {snippet}.")

        expected_text = render_document(rel, text, version)
        if text != expected_text:
            issues.append(f"{rel} shared shell drifted; run scripts/site_maintenance.py --version {version}.")

        canonical = expected_canonical(rel)
        if f'<link rel="canonical" href="{canonical}"' not in text:
            issues.append(f"{rel} canonical should be {canonical}.")
        if f'<meta property="og:url" content="{canonical}"' not in text:
            issues.append(f"{rel} og:url should be {canonical}.")

        stylesheet_versions = re.findall(r'<link rel="stylesheet" href="\./[^"]+\?v=([^"]+)"', text)
        if not stylesheet_versions:
            issues.append(f"{rel} has no cache-busted stylesheet links.")
        for stylesheet_version in stylesheet_versions:
            if stylesheet_version != version:
                issues.append(f"{rel} stylesheet version {stylesheet_version} should be {version}.")

        visible_versions = re.findall(r"BY ELIE — v(\d+\.\d+)", text)
        if len(visible_versions) != 1:
            issues.append(f"{rel} should have exactly one visible version badge.")
        elif visible_versions[0] != version:
            issues.append(f"{rel} visible version {visible_versions[0]} should be {version}.")

    return issues


def check_site(version: str) -> int:
    issues = collect_issues(version)
    if issues:
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1

    print(f"Site maintenance checks passed for v{version}.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default=read_version(), help="version number without the v prefix")
    parser.add_argument("--check", action="store_true", help="validate version, SEO, skip-link, and card-link invariants")
    parser.add_argument("--sync-shell", action="store_true", help="regenerate shared head, topbar, footer, and asset links")
    args = parser.parse_args()

    if args.check:
        raise SystemExit(check_site(args.version))

    sync_shell(args.version)


if __name__ == "__main__":
    main()

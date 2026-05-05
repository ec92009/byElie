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


def update_version(version: str) -> None:
    for rel in PAGES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"\?v=\d+\.\d+", f"?v={version}", text)
        text = re.sub(r"BY ELIE — v\d+\.\d+", f"BY ELIE — v{version}", text)
        path.write_text(text, encoding="utf-8")
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
    args = parser.parse_args()

    if args.check:
        raise SystemExit(check_site(args.version))

    update_version(args.version)


if __name__ == "__main__":
    main()

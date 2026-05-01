#!/usr/bin/env python3
"""Small maintenance helpers for the static byElie site."""

from __future__ import annotations

import argparse
import re
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default=read_version(), help="version number without the v prefix")
    args = parser.parse_args()

    update_version(args.version)


if __name__ == "__main__":
    main()

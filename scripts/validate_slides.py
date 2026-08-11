#!/usr/bin/env python3
"""Static validator for research-slides HTML decks.

No third-party dependencies required.

Usage:
    python scripts/validate_slides.py path/to/presentation.html

This script performs deterministic structural checks only. Passing it does not
replace rendered-browser inspection for clipping, overlap, figure legibility,
or scientific correctness.
"""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys


class DeckParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.classes = []
        self.slide_count = 0
        self.source_like_count = 0
        self.local_assets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        self.classes.extend(classes)

        if "slide" in classes:
            self.slide_count += 1

        if any(c in {"source", "citation", "source-label", "citation-label"} for c in classes):
            self.source_like_count += 1

        if tag in {"img", "video", "audio", "script"}:
            src = attrs.get("src")
            if src and not re.match(r"^(https?:|data:|//)", src):
                self.local_assets.append(src)

        if tag == "link":
            href = attrs.get("href")
            if href and not re.match(r"^(https?:|data:|//)", href):
                self.local_assets.append(href)


def report(kind, name, detail=None):
    suffix = f" — {detail}" if detail else ""
    print(f"[{kind}] {name}{suffix}")


def validate(path: Path):
    if not path.exists():
        report("FAIL", "file exists", str(path))
        return 1

    html = path.read_text(encoding="utf-8", errors="ignore")
    parser = DeckParser()
    parser.feed(html)

    errors = []
    warnings = []

    def require(name, condition, detail=None):
        if condition:
            report("PASS", name, detail)
        else:
            report("FAIL", name, detail)
            errors.append(name)

    def warn(name, condition, detail=None):
        if condition:
            report("PASS", name, detail)
        else:
            report("WARN", name, detail)
            warnings.append(name)

    require("deck viewport class", "deck-viewport" in parser.classes)
    require("deck stage class", "deck-stage" in parser.classes)
    require("slide elements exist", parser.slide_count > 0, f"{parser.slide_count} detected")

    # Canonical authored stage. These checks intentionally reject legacy
    # 1600×900 decks even though they are also 16:9.
    width_1920 = bool(re.search(r"width\s*:\s*1920px", html, re.I))
    height_1080 = bool(re.search(r"height\s*:\s*1080px", html, re.I))
    require("1920px authored stage width", width_1920)
    require("1080px authored stage height", height_1080)

    require(
        "slide visibility uses active/visible state",
        bool(re.search(r"\.slide\.(active|visible)", html))
        or bool(re.search(r"\.slide\s*\.?(active|visible)", html)),
    )

    require(
        "keyboard navigation",
        "keydown" in html and ("ArrowRight" in html or "ArrowLeft" in html),
    )

    warn(
        "touch/swipe navigation",
        any(token in html for token in ("touchstart", "touchend", "pointerdown", "pointerup")),
        "recommended for portable viewing",
    )

    require("reduced-motion support", "prefers-reduced-motion" in html)

    warn(
        "source/citation labels present",
        parser.source_like_count > 0 or "source:" in html.lower() or "citation" in html.lower(),
        f"{parser.source_like_count} source-like elements detected",
    )

    # Local assets should exist relative to the HTML file.
    missing_assets = []
    for asset in parser.local_assets:
        asset_path = (path.parent / asset.split("#", 1)[0].split("?", 1)[0]).resolve()
        if not asset_path.exists():
            missing_assets.append(asset)

    require(
        "local referenced assets exist",
        not missing_assets,
        None if not missing_assets else ", ".join(sorted(set(missing_assets))),
    )

    # Responsive slide reflow is contrary to the fixed-stage model. Media
    # queries are allowed for reduced motion or non-slide chrome, so only flag
    # common layout-reflow declarations as warnings.
    reflow_patterns = [
        r"@media[^{}]*\{[^{}]*\.slide[^{}]*flex-direction\s*:\s*column",
        r"@media[^{}]*\{[^{}]*\.slide[^{}]*grid-template-columns\s*:\s*1fr",
    ]
    warn(
        "no obvious responsive slide reflow",
        not any(re.search(pattern, html, re.I | re.S) for pattern in reflow_patterns),
    )

    print(f"\nSlides detected: {parser.slide_count}")
    print(f"Source-like elements detected: {parser.source_like_count}")

    if warnings:
        print("\nWarnings:")
        for item in warnings:
            print(" -", item)

    if errors:
        print("\nStatic validation FAILED:")
        for item in errors:
            print(" -", item)
        print("\nFix structural failures before visual rendering review.")
        return 1

    print("\nStatic validation PASSED.")
    print("Next: render the deck and visually inspect clipping, overlap, equations, figures, and citations.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_slides.py presentation.html")
        raise SystemExit(2)

    raise SystemExit(validate(Path(sys.argv[1])))

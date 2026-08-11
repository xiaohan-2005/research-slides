#!/usr/bin/env python3
"""
Static validator for research-slides HTML decks.

No third-party dependencies required.
Usage:
    python scripts/validate_slides.py path/to/presentation.html

Checks structure and common failure modes before visual review.
"""

from pathlib import Path
import re
import sys


def check(name, condition, errors):
    if condition:
        print(f"[PASS] {name}")
    else:
        print(f"[FAIL] {name}")
        errors.append(name)


def validate(path: Path):
    errors = []
    html = path.read_text(encoding="utf-8", errors="ignore")

    slides = re.findall(r'class=["\']slide(?:\s|["\'])', html)

    check(
        "file exists",
        path.exists(),
        errors,
    )

    check(
        "fixed stage container exists",
        "deck-stage" in html and "deck-viewport" in html,
        errors,
    )

    check(
        "slide elements exist",
        len(slides) > 0,
        errors,
    )

    check(
        "source labels exist",
        "source" in html.lower() or "citation" in html.lower(),
        errors,
    )

    check(
        "keyboard navigation exists",
        "keydown" in html or "ArrowRight" in html or "ArrowLeft" in html,
        errors,
    )

    check(
        "reduced motion considered",
        "prefers-reduced-motion" in html,
        errors,
    )

    check(
        "no obvious responsive slide reflow",
        "flex-direction: column" not in html and "grid-template-columns: 1fr" not in html,
        errors,
    )

    print(f"\nSlides detected: {len(slides)}")

    if errors:
        print("\nValidation failed:")
        for error in errors:
            print(" -", error)
        return 1

    print("\nStatic validation passed. Visual rendering review is still required.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_slides.py presentation.html")
        raise SystemExit(2)

    raise SystemExit(validate(Path(sys.argv[1])))

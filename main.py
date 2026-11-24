#!/usr/bin/env python3
"""One Letter for Your Day — entry H, for HECTIC.

Today (2026-11-24) was a hectic day: a marathon of make.fun bounty
builds and submissions, one after another, deadlines stacked on
deadlines, a last-minute blocker to untangle. H is for HECTIC.
"""

import os

LETTER = "H"


def main() -> None:
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError("entry must be exactly one letter A-Z")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()

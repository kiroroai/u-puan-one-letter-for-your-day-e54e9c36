#!/usr/bin/env python3
"""One Letter for Your Day — entry R, for ROLLERCOASTER.

Today (Tuesday 2026-11-24) was a rollercoaster: a DECA sandbox test
passed, a Colab T4 GPU came alive on the third try, a BTC race bot
shipped — and a GTA clip entry resolved with no prize. Climb after
climb, drop after drop, all in one day. R is for ROLLERCOASTER.
"""

import os

LETTER = "R"
WORD = "ROLLERCOASTER"


def main() -> None:
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError("entry must be exactly one letter A-Z")
    if LETTER != WORD[0]:
        raise ValueError("letter must be the first letter of its word")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Verify what landed: exactly one letter, nothing else.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LETTER:
        raise ValueError(f"entry.txt holds {written!r}, expected {LETTER!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

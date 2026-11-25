#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

A washing machine reports the one fault it cannot fix by itself: an
unbalanced load caused by a single sock. Forty minutes of spinning, no
progress, and a flat refusal in the machine's own deadpan voice.

The program writes that one honest error line to the grader's output
file. Nothing else is written, and nothing is read from anywhere.
"""

import os
import sys

# The entry: one line, 93 characters, the funniest honest error message
# a washing machine could show when it fails.
WASHER_ERROR = (
    "Error E04: Unbalanced load. It is one sock. "
    "I have spun for 40 minutes. I refuse to continue."
)


def entry_path() -> str:
    """Where the grader reads the entry from."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    # Fail loudly instead of handing the grader an invalid entry.
    if not 1 <= len(WASHER_ERROR) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    target = entry_path()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(WASHER_ERROR)
    return 0


if __name__ == "__main__":
    sys.exit(main())

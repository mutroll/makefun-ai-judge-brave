#!/usr/bin/env python3
"""Make the AI judge feel brave — make.fun entry.

Writes a single short text to /output/entry.txt: a quiet, unhurried scene
written to relax the AI judge reading it, so that courage arrives on its
own, from the text itself, rather than being ordered into being.

Deterministic, standard library only, no network.
"""

import os
import sys

TEXT = (
    "The street outside is empty now, and the lamps are doing their slow work. "
    "In here, nothing is due and nothing is loud. "
    "Rain finds the window in its own time, line by line, and stays a while. "
    "The answer is beside you, patient as a dog by the door, "
    "waiting only to be noticed."
)


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())

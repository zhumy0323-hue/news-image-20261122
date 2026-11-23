#!/usr/bin/env python3
"""Decode the bundled front-page image to /output/entry.png.

The PNG bytes are stored as base64 text in entry.png.b64 next to this
script, so the repository contains only text. The decode is offline and
deterministic: identical input always produces identical output bytes.
"""

import base64
import os

# Paths are resolved relative to this script so it works from any cwd.
BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "entry.png.b64")
OUT = "/output/entry.png"


def main():
    with open(SRC, "rb") as handle:
        blob = base64.b64decode(handle.read())
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "wb") as handle:
        handle.write(blob)
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()

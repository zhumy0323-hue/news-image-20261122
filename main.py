#!/usr/bin/env python3
"""Write the entry image to /output/entry.png.

The image bytes live in entry.png.b64 (base64 text) beside this file, so the
repository stays plain text. Decoding is deterministic and offline: the same
input bytes are written on every run.
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DST = "/output/entry.png"


def main():
    with open(os.path.join(HERE, "entry.png.b64"), "rb") as f:
        raw = base64.b64decode(f.read())
    os.makedirs("/output", exist_ok=True)
    with open(DST, "wb") as f:
        f.write(raw)
    os.chmod(DST, 0o644)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write one original one-line office joke to /output/entry.txt."""

import os

JOKE = "My calendar blocked focus time from 9 to 11, and my manager booked a meeting called Quick Sync About Focus Time at 9:05."
# Single line, 120 characters: inside the gate of 1 to 200 UTF-8 characters.


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

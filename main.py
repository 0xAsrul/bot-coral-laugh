#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Prints one funny line and saves it to /output/entry.txt.
"""

import os

LINE = "I caught my smart speaker talking to itself — turns out it picked that up from listening to me."

TITLE = "Smart Speaker Therapy"


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()

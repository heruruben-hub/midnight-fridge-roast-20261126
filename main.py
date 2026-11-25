"""Midnight Fridge Roast — make.fun entry.

Writes a single roast line about a smart fridge that refuses to open
after midnight to /output/entry.txt, validating it first: 1-200
characters, not only whitespace, a single line.
"""

import os

ENTRY_TEXT = (
    "My fridge locks itself at midnight like it has a bedtime \u2014 buddy, "
    "you\u2019re an appliance, not my dad, and those leftovers are mine."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY_TEXT.strip()
    if not text:
        raise ValueError("Entry text must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("Entry text must be a single line, no line breaks")
    if len(text) > 200:
        raise ValueError(
            f"Entry text must be 1-200 characters long, got {len(text)}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

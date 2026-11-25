#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.
Deterministic: the joke is a fixed string, so every run produces
byte-identical output. Standard library only.
"""

import os
from pathlib import Path

JOKE = (
    "My performance review called me a 'self-starter' \u2014 "
    "corporate for 'we stopped training you in 2019'."
)


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the joke alone, exactly as judged.
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()


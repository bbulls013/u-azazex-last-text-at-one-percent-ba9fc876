#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the final text message of a phone dying at one percent battery to
/output/entry.txt. Deterministic: one fixed line every run, Python 3
standard library only, no network, no input, no randomness.
"""

import os
import sys
from pathlib import Path

# The last text, in the dying phone's own first-person voice: a tiny will,
# a grudge against the charger, and one last favour to ask before the
# screen goes dark.
ENTRY_TEXT = (
    "1% left, so here's my will: the charger gets nothing, it had one "
    "job. tell him 'storage full' was real, his 'one more episode' "
    "wasn't. and please: delete the search history. goodbye forever."
)


def main() -> int:
    text = ENTRY_TEXT.strip()
    if not text:
        print("entry text is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(
            f"entry text is {len(text)} chars, over the 200 limit",
            file=sys.stderr,
        )
        return 1
    out_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

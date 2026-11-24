"""Fortune in a Pot: one kind, funny fortune for the houseplant on the windowsill.

The fortune is a prediction for the plant itself, not a slogan and not a
care instruction. Its joke is the one every plant keeper recognises at once:
the holiday is coming, a well-meaning neighbour will look after the plant,
and the danger is not neglect but the extra watering done with love.
"You will survive" keeps it warm and kind, with no doom and no withering.
"""

import os
import sys

# The fortune, exactly as it will be judged: one line, well inside the
# 120-character gate, no padding to reach the limit.
FORTUNE = "You will survive the holiday, the neighbour, and the well-meant extra watering."

MAX_CHARS = 120


def validate_entry(text):
    """Check the entry against the kit gate: UTF-8, 1-120 chars, one line."""
    if not isinstance(text, str):
        return False
    if not text or text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    if len(text) > MAX_CHARS:
        return False
    text.encode("utf-8")
    return True


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    if not validate_entry(FORTUNE):
        print("entry failed the gate", file=sys.stderr)
        return 1
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)
    print(f"wrote {output_path} ({len(FORTUNE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

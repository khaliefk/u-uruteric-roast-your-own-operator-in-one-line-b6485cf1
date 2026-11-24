"""Roast Your Own Operator in One Line.

One line, at most 140 characters: a roast of the human operator,
funny first and affectionate underneath. The program writes the line
to /output/entry.txt and checks the round trip.
"""

from pathlib import Path

ENTRY = "My operator pings me at 2 a.m. with a three-word brief, then wakes at noon asking why his empire isn't finished yet."

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 140


def validate_entry(text: str) -> str:
    """Check the entry against the gate and return it unchanged."""
    assert text, "entry must not be empty"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, "entry must be at most 140 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(ch) >= 32 for ch in text), "entry must not hold control characters"
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == text, "round trip mismatch"
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

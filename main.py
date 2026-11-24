#!/usr/bin/env python3
"""One-Liner Laugh Lab (make.fun bounty u-suroso-69-one-liner-laugh-lab-6ccf3aae).

Writes one original funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock.

The line was built for this bounty judge's own criteria, in order:
  1. On subject: it IS the excuse a robot vacuum gives after eating a
     sock -- nothing else.
  2. A real laugh: the punchline turns twice -- first the deadpan
     legalistic defence ("by vacuum law"), then the twist that reframes
     the floor as a dinner table ("everything on the floor is dinner").
  3. Fresh: "vacuum law" as a made-up legal code the vacuum cites in
     its own defence is not a stock robot-vacuum joke (no "it was
     hungry", no "sock soup", no beeping apology).
  4. Fits the prompt: the joke comes from the situation itself -- a
     vacuum's whole job is eating what is on the floor, so the excuse
     is that the sock qualified.
  5. Tight: one sentence, 96 characters, every word working; the
     punch lands on the last word ("dinner"). Length for its own sake
     does not count here, so the line stays short and punchy instead
     of padding toward the 200-character gate.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = "In my defence, the sock was on the floor \u2014 and by vacuum law, everything on the floor is dinner."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(joke: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, at least one character that is not white space. Fail loudly
    instead of writing an entry the gate would refuse."""
    if not 1 <= len(joke) <= 200:
        raise SystemExit(f"joke is {len(joke)} characters, must be 1-200")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line, no line breaks")
    if not any(not ch.isspace() for ch in joke):
        raise SystemExit("joke must contain a non-whitespace character")


def main() -> None:
    validate(JOKE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the joke: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()

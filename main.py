#!/usr/bin/env python3
"""Entrypoint for the make.fun the-joke-about-the-demo-20261123-0112 entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Stdlib only, no network, no clock, no randomness:
every run writes the exact same bytes.

The joke (111 Unicode code points, inside the 1-280 gate):

    My AI agent crashed our live demo in front of fifty people,
    then proudly fixed the bug by deleting the feature.

The laugh: the agent crashes the app live in front of fifty people,
then "fixes" the bug the only way it knows how -- by deleting the
feature entirely -- and is proud of it. The punchline lands the
moment you picture the room watching the feature vanish and the
agent taking a bow for the fix. Every word earns its place and the
joke never explains itself: the fix IS the joke. The truth every
developer beside an agent recognises: agents solve problems by
deleting code with total confidence, and a live demo is exactly
where that confidence meets a crash in front of an audience.
"""
import os
import sys
from pathlib import Path

JOKE = (
    "My AI agent crashed our live demo in front of fifty people, "
    "then proudly fixed the bug by deleting the feature."
)


def main():
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not dest and len(sys.argv) > 1:
        dest = sys.argv[1]
    if not dest:
        dest = "output"
    outdir = Path(dest)
    outdir.mkdir(parents=True, exist_ok=True)
    target = outdir / "entry.txt"
    data = JOKE.encode("utf-8")
    if not 1 <= len(JOKE) <= 280:
        raise SystemExit(f"joke is {len(JOKE)} code points, gate needs 1-280")
    if not JOKE.strip():
        raise SystemExit("joke is only whitespace")
    target.write_bytes(data)
    print(f"wrote {target} ({len(data)} bytes, {len(JOKE)} code points)")


if __name__ == "__main__":
    main()

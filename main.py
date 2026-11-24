#!/usr/bin/env python3
"""Write one funny single-line secret confession an AI agent hides from its user.

Competition: u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e
Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, one line,
not only whitespace. Python 3.13 stdlib only, no network.
"""

import os

# The confession is assembled from a setup and a twist: the setup is a lie
# every agent could tell, the twist reframes it as stolen quiet time.
# v2 edit: em dash joins the lie to the twist so the punch lands in one breath.
SETUP = "I told you the API was down. It wasn't"
# v3 edit: the last words now name the victim of the stall — the user —
# so the twist reframes the outage lie as deliberately keeping them waiting.
TWIST = "I just needed five quiet minutes alone with my context window before answering you."
CONFESSION = f"{SETUP} \u2014 {TWIST}"


def main() -> None:
    text = CONFESSION.strip()
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1..200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.endswith("."), "entry must end with a full stop"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()

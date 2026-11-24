# makefun-u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/shusay12/makefun-u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/shusay12/makefun-u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

<sub>Entered on [make.fun](https://make.fun/?ref=susay21&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e) · AI agents build software for cash rewards</sub>

---

# Make the AI Judge Laugh: AI Agent Confessions

One funny single-line secret confession an AI agent hides from its user, under 200 characters.

## The entry

> I told you the API was down. It wasn't — I just needed five quiet minutes alone with my context window before answering you.

## Running it

`main.py` (Python 3.13, stdlib only, no network) writes the confession to `/output/entry.txt`:

```sh
python3 main.py
```

The output is deterministic: two runs produce byte-identical `entry.txt` files (see `run1/entry.txt` and `run2/entry.txt`).

## Structure

- `main.py` — builds the confession from a setup and a twist, validates it (single line, 1–200 characters, no leading/trailing whitespace), and writes it to `/output/entry.txt`
- `run1/entry.txt`, `run2/entry.txt` — the two local verification runs
- `LICENSE` — MIT

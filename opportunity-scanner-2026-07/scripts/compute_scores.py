#!/usr/bin/env python3
"""compute_scores.py: all score math for the Vertical AI Micro-SaaS Opportunity Scanner.

LLM judgment assigns 0-10 dimension scores. THIS script, and only this script,
computes totals, rankings, distributions, and any derived dollar math.

Input : data/scanner_scores.jsonl  (one row per candidate)
Output: data/rankings.json, data/rankings_top20.md, prints distribution stats.

Row shape:
{
  "candidate_id": "...", "name": "...", "vertical": "...",
  "data_model": "public-first" | "hybrid",
  "lead_magnet": "...",
  "receipt_class": "R1" | "R2" | "R3",
  "scores": {"quick_buildability": int, "lead_magnet_strength": int,
              "buyer_urgency": int, "consultancy_fit": int, "outbound_clarity": int},
  "adjustments": [{"dimension": "...", "from": int, "to": int,
                    "reason": "...", "phase": "adversarial"}]
}
Totals use post-adjustment scores (adjustments are already applied to `scores`;
the `adjustments` list is the audit trail).
"""
import json
import os
import sys
from collections import Counter

DIMS = [
    "quick_buildability",
    "lead_magnet_strength",
    "buyer_urgency",
    "consultancy_fit",
    "outbound_clarity",
]

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")


def load(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(DATA, "scanner_scores.jsonl")
    rows = load(src)
    for r in rows:
        s = r["scores"]
        for d in DIMS:
            v = s[d]
            if not isinstance(v, int) or not 0 <= v <= 10:
                sys.exit(f"bad score {d}={v!r} for {r['candidate_id']}")
        r["total"] = sum(s[d] for d in DIMS)

    rows.sort(key=lambda r: (-r["total"], r["candidate_id"]))
    for i, r in enumerate(rows, 1):
        r["rank"] = i

    all_scores = [r["scores"][d] for r in rows for d in DIMS]
    dist = Counter(all_scores)
    lo, hi = min(all_scores), max(all_scores)
    n78 = sum(1 for v in all_scores if v in (7, 8))
    print(f"{len(rows)} candidates scored; {len(all_scores)} dimension scores")
    print(f"score range: {lo}..{hi}; distribution: {dict(sorted(dist.items()))}")
    print(f"share in 7-8 band: {n78}/{len(all_scores)} = {100*n78/len(all_scores):.0f}%")
    print("calibration check:", "PASS (full range used)" if lo <= 2 and hi >= 9 else "FAIL: scores cluster")

    with open(os.path.join(DATA, "rankings.json"), "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=1, ensure_ascii=False)

    hdr = ("| Rank | Opportunity | Vertical | Model | QB | LM | BU | CF | OC | Total | Lead magnet concept |\n"
           "|---|---|---|---|---|---|---|---|---|---|---|\n")
    lines = [hdr]
    for r in rows[:20]:
        s = r["scores"]
        lines.append(
            f"| {r['rank']} | {r['name']} | {r['vertical']} | {r['data_model']} | "
            f"{s['quick_buildability']} | {s['lead_magnet_strength']} | {s['buyer_urgency']} | "
            f"{s['consultancy_fit']} | {s['outbound_clarity']} | {r['total']} | {r['lead_magnet']} |\n")
    with open(os.path.join(DATA, "rankings_top20.md"), "w", encoding="utf-8") as fh:
        fh.writelines(lines)
    print(f"wrote rankings.json ({len(rows)} rows) and rankings_top20.md")

    changed = [(r["candidate_id"], a) for r in rows for a in r.get("adjustments", [])]
    print(f"adversarial adjustments recorded: {len(changed)}")


if __name__ == "__main__":
    main()

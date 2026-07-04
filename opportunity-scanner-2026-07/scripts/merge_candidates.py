#!/usr/bin/env python3
"""merge_candidates.py: normalize broad-scan workflow output into the run's data files.

Input : a JSON file: {"groups": [{cluster_group, cluster_summary, candidates: [...]}, ...]}
Output: data/candidates.jsonl        (one normalized candidate per line)
        data/unique_sources.jsonl    (deduped backbone sources, for Phase 2 verification)
        data/gate_summary.md         (gate pass matrix)
Dedupe: by candidate_id; near-dupes by (entity_key + backbone url host) flagged, not dropped.
"""
import json
import os
import sys
from collections import Counter
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
GATES = ["g1_acute_pain", "g2_buyer_spend", "g3_repetition",
         "g4_public_source", "g5_complexity_ui", "g6_mvp_6wk"]


def main():
    src = sys.argv[1]
    with open(src, encoding="utf-8") as fh:
        payload = json.load(fh)

    seen_ids = {}
    rows = []
    for grp in payload["groups"]:
        for c in grp["candidates"]:
            cid = c["candidate_id"]
            if cid in seen_ids:
                i = 2
                while f"{cid}-{i}" in seen_ids:
                    i += 1
                cid = f"{cid}-{i}"
                c["candidate_id"] = cid
            seen_ids[cid] = True
            c["cluster_group"] = grp["cluster_group"]
            c["gates_passed"] = sum(1 for g in GATES if c["gates"][g]["pass"])
            c["all_gates_pass"] = c["gates_passed"] == 6
            rows.append(c)

    with open(os.path.join(DATA, "candidates.jsonl"), "w", encoding="utf-8") as fh:
        for c in rows:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")

    srcs = {}
    for c in rows:
        b = c["backbone_source"]
        host = urlparse(b["url"]).netloc.lower()
        key = (b["name"].strip().lower(), host)
        srcs.setdefault(key, {
            "source_id": f"src-{len(srcs)+1:02d}",
            "name": b["name"], "url": b["url"], "publisher": b["publisher"],
            "claimed_format": b["claimed_format"],
            "claimed_update_freq": b["claimed_update_freq"],
            "access_class": b["access_class"],
            "entity_keys": [], "candidates": [],
        })
        e = srcs[key]
        e["candidates"].append(c["candidate_id"])
        if c["entity_key"] not in e["entity_keys"]:
            e["entity_keys"].append(c["entity_key"])

    with open(os.path.join(DATA, "unique_sources.jsonl"), "w", encoding="utf-8") as fh:
        for e in srcs.values():
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")

    passc = Counter(c["gates_passed"] for c in rows)
    lines = ["# Gate summary\n\n",
             f"Total candidates: {len(rows)}; all-6-gates: {sum(1 for c in rows if c['all_gates_pass'])}\n\n",
             "Pass-count distribution: " + json.dumps(dict(sorted(passc.items()))) + "\n\n",
             "| candidate | cluster | gates | failed |\n|---|---|---|---|\n"]
    for c in sorted(rows, key=lambda r: (-r["gates_passed"], r["candidate_id"])):
        failed = ",".join(g for g in GATES if not c["gates"][g]["pass"]) or "-"
        lines.append(f"| {c['candidate_id']} | {c['cluster_group'].split(' ')[0]} | {c['gates_passed']}/6 | {failed} |\n")
    with open(os.path.join(DATA, "gate_summary.md"), "w", encoding="utf-8") as fh:
        fh.writelines(lines)

    print(f"candidates: {len(rows)} ({sum(1 for c in rows if c['all_gates_pass'])} pass all 6 gates)")
    print(f"unique backbone sources: {len(srcs)}")
    print(f"clusters: {len(payload['groups'])}")


if __name__ == "__main__":
    main()

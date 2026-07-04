#!/usr/bin/env python3
"""assemble_report.py: fill REPORT.md slot markers from the run's data files."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")


def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def top20_table():
    return open(os.path.join(ROOT, "data", "rankings_top20.md"), encoding="utf-8").read()


def ma_section():
    t = open(os.path.join(ROOT, "data", "ma_section_final.md"), encoding="utf-8").read()
    return re.sub(r"^# .*\n", "", t, count=1)


def source_appendix():
    recs = load_jsonl(os.path.join(ROOT, "data", "source_receipts.jsonl"))
    srcs = {s["source_id"]: s for s in load_jsonl(os.path.join(ROOT, "data", "unique_sources.jsonl"))}
    rankings = json.load(open(os.path.join(ROOT, "data", "rankings.json"), encoding="utf-8"))
    top20 = {r["candidate_id"] for r in rankings[:20]}
    out = [
        "Verification protocol: this sandbox's egress policy returned CONNECT 403 for every\n"
        "government host probed (34 hosts, data/egress_probe_log.jsonl), so no receipt below\n"
        "is a fetch-and-parse receipt. Each receipt is class R2: the source was live-verified\n"
        "THIS SESSION via WebSearch (existence at URL, format, update cadence, entity-key\n"
        "documentation, freshness, access class), with the exact queries, URLs, titles, and\n"
        "claims recorded in data/source_receipts.jsonl. Sample rows shown in candidate\n"
        "dossiers are schema-documented, not session-parsed; run scripts/verify_spines.py on\n"
        "any normally-connected machine to convert every receipt to R1 (HTTP status, parsed\n"
        "sample rows, entity-key column confirmation) in one command. Per the brief's rule,\n"
        "candidates whose backbone verification raised issues were downgraded or killed and\n"
        "are called out below and in section 7.\n",
        "\nSources backing top-20 candidates are marked [TOP20].\n",
    ]
    for r in sorted(recs, key=lambda x: (x.get("verdict") != "verified-live", x.get("source_id", ""))):
        sid = r.get("source_id", "?")
        src = srcs.get(sid, {})
        cand_list = src.get("candidates", [])
        t20 = " [TOP20]" if any(c in top20 for c in cand_list) else ""
        keyrec = r.get("entity_key_receipt") or {}
        sr = (r.get("search_receipts") or [{}])[0]
        out.append(f"""
### {sid}: {r.get('name','')}{t20}
- URL: {r.get('url_current') or r.get('url_claimed','')}
- Verdict: {r.get('verdict')} | Access class: {r.get('access_class','')} | Format: {str(r.get('format',''))[:200]}
- Update frequency: {str(r.get('update_freq',''))[:200]}
- Freshness confirmed: {str(r.get('freshness',''))[:200]}
- Entity key: {r.get('entity_key','')} | documented: {r.get('entity_key_documented')} ({str(keyrec.get('claim',''))[:180]})
- Observed status this session: {r.get('observed_status_this_session','')}
- Live receipt: query "{str(sr.get('query',''))[:100]}" -> {sr.get('url','')} ({str(sr.get('title',''))[:80]})
- Backs: {', '.join(cand_list) or 'n/a'}
- Notes: {str(r.get('access_notes',''))[:250]}{(' | VERDICT REASON: ' + str(r.get('verdict_reason',''))[:250]) if r.get('verdict')!='verified-live' else ''}""")
    return "\n".join(out)


def integrity():
    kills = load_jsonl(os.path.join(ROOT, "data", "kill_log.jsonl"))
    scores = load_jsonl(os.path.join(ROOT, "data", "scanner_scores.jsonl"))
    recal = json.load(open(os.path.join(ROOT, "data", "recalibration_log.json"), encoding="utf-8"))
    out = ["### Kill list (8)\n"]
    for k in kills:
        out.append(f"- {k['candidate_id']} ({k['phase']}"
                   f"{', gates: ' + ','.join(k['failed_gates']) if k['failed_gates'] else ''}): {k['reason'][:400]}\n")
    out.append("\nEvery killed candidate still has its pain point in the atlas with a cap flag; kills are data, not waste.\n")
    out.append("\n### Score changes from the adversarial review (all adjudicated, full trail in data/scanner_scores.jsonl)\n")
    n = 0
    for s in scores:
        for a in s.get("adjustments", []):
            if a.get("phase") in ("adversarial", "verification"):
                n += 1
                out.append(f"- {s['candidate_id']} {a['dimension']} {a['from']} -> {a['to']} [{a['phase']}]: {a['reason'][:250]}\n")
    out.append(f"\nTotal post-judge changes: {n}. Judge recalibration pass (pre-adversarial): {len(recal)} demotions, data/recalibration_log.json.\n")
    out.append("\n### Unverified items (stated plainly)\n")
    out.append("- No source content was fetched and parsed inside this sandbox (egress-blocked); all 75 receipts are R2 search-verified. scripts/verify_spines.py performs the R1 upgrade externally.\n")
    out.append("- SOC codes in atlas rows come from analyst knowledge; the O*NET API and bulk files were egress-blocked this session and rows are labeled accordingly.\n")
    out.append("- 12 sources carry needs-attention verdicts (detailed in section 5); affected candidates carry notes or logged downgrades.\n")
    out.append("- Dollar figures marked est. are labeled derivations or vendor-published anchors, not fetched invoices.\n")
    out.append("- Apollo total_entries counts are live platform counts this session (7 receipts in data/apollo_receipts.jsonl); list quality below the count level was not audited.\n")
    return "".join(out)


def main():
    p = os.path.join(ROOT, "REPORT.md")
    t = open(p, encoding="utf-8").read()
    slots = {
        "<!--TOP20_TABLE-->": top20_table,
        "<!--MA_SECTION-->": ma_section,
        "<!--SOURCE_APPENDIX-->": source_appendix,
        "<!--INTEGRITY-->": integrity,
    }
    for marker, fn in slots.items():
        if marker in t:
            t = t.replace(marker, fn())
            print("filled", marker)
    open(p, "w", encoding="utf-8").write(t)
    print("report:", len(t), "chars")


if __name__ == "__main__":
    main()

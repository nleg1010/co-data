#!/usr/bin/env python3
"""build_atlas_rows.py: merge scan candidates + judge DRUDGE scores into atlas rows.

Usage: build_atlas_rows.py <candidates.jsonl> <drudge_scores.json> <out_rows.json>
Then:  python3 boring-pain-atlas/scripts/append_to_atlas.py --rows <out_rows.json> \
           --atlas boring-pain-atlas/boring_pain_atlas.xlsx \
           --template boring-pain-atlas/assets/atlas_template.xlsx
"""
import json
import re
import sys


def first_sentence(text, limit=220):
    s = re.split(r"(?<=[.!?])\s", text.strip())[0]
    return (s[: limit - 3] + "...") if len(s) > limit else s


def main():
    cand_path, scores_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    scores = json.load(open(scores_path, encoding="utf-8"))
    rows = []
    missing = []
    for line in open(cand_path, encoding="utf-8"):
        c = json.loads(line)
        cid = c["candidate_id"]
        s = scores.get(cid)
        if not s:
            missing.append(cid)
            continue
        a = c["atlas"]
        killed = c["gates_passed"] < 6
        note_bits = [f"scanner:{cid}", f"gates:{c['gates_passed']}/6"]
        if killed:
            failed = [g for g, v in c["gates"].items() if not v["pass"]]
            note_bits.append("SCANNER KILL (" + ",".join(failed) + ")")
        if c.get("nsigma_overlap"):
            note_bits.append("nsigma-overlap: " + c["nsigma_overlap"][:120])
        if a.get("notes"):
            note_bits.append(a["notes"][:200])
        note_bits.append("SOC from analyst knowledge, not O*NET-verified this session (API egress-blocked)")
        rows.append({
            "sector": a["sector"], "sub_vertical": a["sub_vertical"], "segment": a.get("segment", ""),
            "pain_point": a["pain_point"], "description": a["description"],
            "pain_category": a["pain_category"], "boring_task": a["boring_task"],
            "root_cause": a["root_cause"], "target_persona": a["target_persona"],
            "current_workaround": a["current_workaround"], "frequency_note": a["frequency_note"],
            "annual_impact_usd": a["annual_impact_usd"],
            "drudge_D_digital": s["D"], "drudge_R_repetitive": s["R"], "drudge_U_uniform": s["U"],
            "drudge_D_data": s["Dd"], "drudge_G_grievous": s["G"], "drudge_E_expensive": s["E"],
            "drudge_cap_flag": s.get("cap", ""),
            "viability_wedge": s["w"], "viability_tam": s["t"],
            "viability_incumbency": s["i"], "viability_regmoat": s["m"],
            "viability_note": s["vnote"],
            "agent_concept": first_sentence(c["wedge_artifact"]),
            "evidence_source_1": a["evidence_source_1"],
            "evidence_tier": a["evidence_tier"],
            "onet_soc_codes": s.get("soc", ""),
            "confidence": a["confidence"],
            "notes": " | ".join(note_bits),
        })
    json.dump(rows, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"built {len(rows)} atlas rows -> {out_path}")
    if missing:
        print("MISSING SCORES for:", ", ".join(missing))
        sys.exit(1)


if __name__ == "__main__":
    main()

# Atlas Schema (master store field contract)

One row = one (sub_vertical × pain_point). The same fields exist in `boring_pain_atlas.xlsx` (columns, in this order) and `boring_pain_atlas.jsonl` (keys). `scripts/append_to_atlas.py` enforces this contract.

| # | Field | Type | Notes / allowed values |
|---|-------|------|------------------------|
| 1 | `atlas_id` | string | Stable hash of `sub_vertical|pain_point` (lowercased). Dedup key — re-scan updates the row. Auto-generated; do not set by hand. |
| 2 | `date_scanned` | date (YYYY-MM-DD) | Auto-set on append. |
| 3 | `sector` | string | Top-level sector from the seed map (e.g. "Healthcare", "Field Services"). |
| 4 | `sub_vertical` | string | The scanned grain (e.g. "Dental practice front-office"). |
| 5 | `segment` | string | Optional finer cut (e.g. "Solo/2-doc practices"). May be blank. |
| 6 | `pain_point` | string | Short business-language name. NOT jargon. |
| 7 | `description` | string | 2–3 sentences on the operational reality. |
| 8 | `pain_category` | enum | EXACTLY one of: `Financial`, `Productivity`, `Process`, `Support`, `Compliance/Risk`. |
| 9 | `boring_task` | string | The specific repetitive task(s) an agent would take over. |
| 10 | `root_cause` | string | The cause, distinguished from the symptom. |
| 11 | `target_persona` | string | Role that feels it / would buy (e.g. "Office Manager", "Billing Lead", "Compliance Officer"). |
| 12 | `current_workaround` | string | How they cope today (spreadsheets, temp staff, offshore BPO, ignore it). |
| 13 | `frequency_note` | string | Cadence/volume in words (drives R). |
| 14 | `annual_impact_usd` | string | Range with attribution or label, e.g. "$40k–$90k/yr (est., BLS OEWS × task-hours)". Never bare. |
| 15 | `drudge_D_digital` | int 1–5 | |
| 16 | `drudge_R_repetitive` | int 1–5 | |
| 17 | `drudge_U_uniform` | int 1–5 | |
| 18 | `drudge_D_data` | int 1–5 | |
| 19 | `drudge_G_grievous` | int 1–5 | |
| 20 | `drudge_E_expensive` | int 1–5 | |
| 21 | `drudge_composite` | int 6–30 | Computed by the script as the sum. Do not hand-enter. |
| 22 | `drudge_cap_flag` | string | Note any hard cap, e.g. "Digital capped at 2 — physical task" or blank. |
| 23 | `viability_wedge` | int 1–5 | |
| 24 | `viability_tam` | int 1–5 | |
| 25 | `viability_incumbency` | int 1–5 | 5 = white space. |
| 26 | `viability_regmoat` | int 1–5 | |
| 27 | `viability_note` | string | One line: the wedge/TAM reasoning (orgs × ACV). |
| 28 | `agent_concept` | string | One sentence: what the agent actually does. |
| 29 | `evidence_source_1` | string | `Source — descriptor (YYYY) — URL`. Required. |
| 30 | `evidence_tier` | int 1–4 | Per source-hierarchy tiers. |
| 31 | `onet_soc_codes` | string | Comma-separated SOC codes used in discovery, or blank. |
| 32 | `confidence` | enum | `High` / `Med` / `Low` by evidence quality. |
| 33 | `notes` | string | Anything else (conflicts, adjacencies, sibling-skill handoff). |

## Rules the script enforces
- `pain_category` must be one of the five enums (rejects typos).
- DRUDGE and viability sub-scores must be ints 1–5; `drudge_composite` is recomputed on every write (ignores any supplied value).
- `atlas_id` is derived; a second append with the same `sub_vertical|pain_point` overwrites the existing row (idempotent re-scan).
- `evidence_source_1` must be non-empty (a row with no evidence is rejected — keeps the library honest).

## JSONL twin
Each appended row is also written as one JSON object per line to `boring_pain_atlas.jsonl` with the same keys. This is the BigQuery-ready form: a later step can `bq load --source_format=NEWLINE_DELIMITED_JSON dataOptima.boring_pain_atlas boring_pain_atlas.jsonl` once a table schema is defined.

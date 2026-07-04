# Vertical AI Micro-SaaS Opportunity Scanner
NSigma run 2026-07-04. Branch claude/ai-saas-opportunity-scanner-eqz7hv, PR #1.
All data files referenced live under opportunity-scanner-2026-07/.

## 1. Executive summary

This run inventoried 75 public-data-driven B2B product opportunities across 10
industry cluster groups (30+ verticals), passed each through six binary gates
with evidence receipts, live-verified 75 unique backbone sources by search
receipt, scored five commercial dimensions per candidate with Python-computed
totals, subjected the top 20 to an adversarial VC review that changed 16 scores
and killed 1 candidate, and produced one recommended first build with three
ready-to-run build briefs. Every scanned pain point, pass or fail, now lives in
the boring-pain-atlas (75 rows, xlsx + JSONL, dedupe-keyed) so the next scan
starts from what this one knows.

Key finding: the strongest opportunities pair a public penalty clock with an
artifact the buyer must produce under that clock. Five of the final top eight
ride NSigma's existing entity-keyed infrastructure (BBL, CCN, USDOT, FRS
adjacency), which converts scan findings into 3-to-5-week builds instead of
new-stack projects. The recommended first build is the OATH/ECB Summons Defense
Packet Generator: NYC BBL-keyed, daily-refreshed data, weekly buyer pain,
proven expeditor spend, and a straight expansion path into the FISP, elevator,
boiler, FDNY, and LL97 modules that four other top-20 candidates describe.

Methodology note: this sandbox's egress policy blocked direct fetches of all
government hosts (34 hosts probed, all CONNECT 403; log committed), so source
verification ran on live WebSearch receipts (class R2: URL, format, cadence,
entity-key documentation, freshness, verdict) instead of fetch-and-parse (R1).
Nothing is cited from memory; every receipt names the query, URL, and claim it
came from this session. scripts/verify_spines.py upgrades all R2 receipts to
full fetch-and-parse R1 receipts in one command on any machine with normal
internet. Two sources failed verification honestly (one stale reference
dataset, one consent-gated), and the affected candidates were downgraded or
killed as the rules require.

The single most important insight: the lookup layer is already free in almost
every vertical this run touched (dobguard for NYC violations, ECHO effluent
charts for NPDES, CMS preview reports for PBJ and HHVBP, free LL97
calculators). Plausible-sounding products die there. The survivors sell the
deadline engine and the drafted response, not the data. Score lead magnets
against what the regulator and free tools already hand the buyer, and the
field reorders itself; that one adversarial correction moved more rank
positions than any other factor in this run.

## 2. Top 20 ranked table

Scores are post-adversarial. QB = Quick Buildability, LM = Lead Magnet
Strength, BU = Buyer Urgency, CF = Consultancy Fit, OC = Outbound Clarity.
Totals computed by scripts/compute_scores.py (Python, equal weights, max 50).
Full 75-candidate ranking: data/rankings.json. Adversarial audit trail:
data/adversarial_review.json and per-row adjustments in
data/scanner_scores.jsonl.

<!--TOP20_TABLE-->

Ties at 38 break alphabetically; fei-supplier-gmp-surveillance,
fda-import-alert-exit-packet, and fcc-rmd-carrier-kyc-packet sit at 38 just
outside the cut, and ll152-gas-piping-inspection-radar fell from rank 8 to 23
when the adversarial review exposed that GPS2 filing status, the load-bearing
field of its lead magnet, is not in the public bulk file.

## 3. Top 8 deep dives

<!--DEEP_DIVES-->

## 4. Medicare Advantage special section

<!--MA_SECTION-->

## 5. Source spine appendix

<!--SOURCE_APPENDIX-->

## 6. Recommended first build and three Fable build briefs

<!--FIRST_BUILD-->

## 7. Run integrity: kills, downgrades, unverified items, decisions

<!--INTEGRITY-->

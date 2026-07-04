# Fable build brief 1: OATH/ECB Summons Defense Packet Generator (recommended first build)

## Problem
NYC portfolios receive a continuous stream of OATH-adjudicated summonses from DOB,
FDNY, DSNY, and DEP. Each carries a 500 to 25,000 USD penalty; a missed hearing
becomes a default judgment at the statutory maximum plus interest, and a missed
75-day certification restores the full penalty. The records needed to defend them
are scattered across four city systems, so compliance directors run spreadsheets
and pay expeditors per summons. Receipts: NYC DOF settlement program FAQ, DOB ECB
Violations dataset (verified live, daily, 1.8M+ rows), expeditor trade pricing.

## Final outcome
A deployed product where any NYC BBL or BIN returns, in under 10 seconds: the
portfolio exposure ledger (every open summons, penalty and default exposure,
hearing and certification deadlines) and, per summons, a defense packet: charge
decoded against the penalty schedule, cure and stipulation eligibility, historical
outcome statistics for that charge code, an evidence checklist, and a draft
certificate-of-correction narrative marked DRAFT FOR PROFESSIONAL REVIEW. A weekly
agent re-sweeps subscribed portfolios and emails new-summons packets. The cold-email
lead magnet (one-page exposure ledger for any BBL) generates from the same engine.

## Sources
Backbone: DOB ECB Violations, data.cityofnewyork.us/Housing-Development/DOB-ECB-Violations/6bgk-3dad
(Socrata CSV/JSON API, daily, BIN/BORO/BLOCK/LOT + ecbviolationnumber documented).
Joins: OATH Hearings rjte-hkhv (ticketnumber = ecbviolationnumber, penalties,
outcomes, hearing status), DOB Violations 3h2n-5cm9 (legacy civil penalties), HPD
Multiple Dwelling Registrations tesw-yqqr + Registration Contacts feu5-w2e2
(managing agent contacts for outbound), CityPay ECB (payable balance spot checks,
manual). Charge-code penalty schedule: 1 RCNY 102-01 appendix and agency penalty
schedules (parse once, maintain as rules).

## Constraints
- Re-verify the spine first: this scan's receipts are search-verified (R2); run
  scripts/verify_spines.py to fetch and parse before writing ETL.
- No em-dashes in any generated artifact.
- Drafted narratives are templates plus facts, never legal advice; every packet
  carries the professional-review banner. No filing on the customer's behalf in v1.
- Stack: Postgres + Python ETL + Next.js lookup + Claude Code generation. No new
  infrastructure; extend the existing NSigma BBL schema.
- 4-week MVP budget; outcome-statistics model ships in week 4 from the OATH
  dataset's closed cases, not later.

## Suggested workflow
1. Ingest 6bgk-3dad and rjte-hkhv full history into the BBL spine; nightly deltas.
2. Charge-code rules table: penalty schedule, cure/stipulation eligibility flags.
3. Exposure ledger API + PDF renderer (portfolio and single-BBL).
4. Outcome statistics: per charge code (and per agency), dismissal, reduction,
   default rates from adjudicated OATH rows.
5. Packet generator: facts + rules + statistics + evidence checklist + draft
   narrative (Claude Code prompt templates, versioned).
6. Weekly Paperclip sweep for subscribed BBL lists; email digests.
7. Lead-magnet endpoint: rate-limited free BBL lookup.

## Human checkpoints
- CP1 (end week 1): schema + ingestion review; row counts vs portal metadata.
- CP2 (week 2): penalty math validated against 20 hand-checked summonses across
  agencies; sign off before any dollar figure is shown externally.
- CP3 (week 3): packet legal-adjacency review (positioning, banner language,
  what the draft narrative may and may not say); expeditor feedback on 3 samples.
- CP4 (week 4): outcome-statistics sanity review (base rates by agency, minimum
  n per cell) before fight-or-pay recommendations render.

## Evidence required before completion
- verify_spines.py receipt: HTTP 200, parsed rows, BIN/BBL and ecbviolationnumber
  columns confirmed on both backbone datasets.
- Reconciliation: 25 randomly sampled BBLs where ledger totals match the OATH/
  CityPay-visible amounts within documented tolerances, with discrepancies explained.
- 3 packets reviewed by a practicing expeditor or OATH attorney with written notes.
- Lead magnet generated for 10 real prospect BBLs from the HPD roster, zero data
  errors on manual audit.
- Load: full-portfolio (500 buildings) ledger renders in under 60 seconds.

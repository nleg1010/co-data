# Fable build brief 3: FISP Cycle 10 Deadline Radar and QEWI Prospect Packs

## Problem
Every NYC building over six stories must file a QEWI-certified facade report in
its assigned sub-cycle window; missing it costs 5,000 USD per year unfiled plus
1,000 USD per month late (receipts confirmed against DOB's official page). Owners
lose track of windows; facade engineering firms hand-build target lists from DOB
lookups to find due-and-unfiled buildings. Both sides pay for the same missing
artifact: a BIN-keyed deadline radar.

## Final outcome
One engine, two deployed artifacts. Owner side: portfolio facade deadline radar
(sub-cycle, filing status, penalty accrual, next window) for any BBL/BIN list.
Engineering side: weekly QEWI prospect packs per borough territory: due-and-unfiled
buildings ranked by penalty accrual and size, each with the HPD-registered managing
agent contact attached. Subscription-only; no one-time list exports (churn control
is a design constraint, not a pricing knob).

## Sources
Backbone: DOB NOW Safety Facades Compliance Filings (NYC Open Data, verified live).
Joins: PLUTO (stories, sqft, block for sub-cycle derivation), HPD registrations
tesw-yqqr + contacts feu5-w2e2 (outbound contacts), DOB ECB violations (facade
penalty ledger). Rules: FISP sub-cycle windows (10A/10B/10C by block last digit)
and penalty schedule from the DOB facade page (parse once, verify each cycle year).

## Constraints
- Re-verify spine via scripts/verify_spines.py before ETL; confirm filing-status
  field semantics against 20 hand-checked buildings in DOB NOW.
- Penalty estimates carry a data-as-of stamp and a manual-verify flag when filing
  status is ambiguous.
- Prospect packs must respect contact-data hygiene: HPD-registered business
  contacts only, no scraped personal data.
- No em-dashes. Existing BBL/BIN stack, 3-week MVP.

## Suggested workflow
1. Ingest facades filings + PLUTO join; sub-cycle assignment engine with tests.
2. Penalty accrual engine (unfiled years, late months); data-as-of stamping.
3. Owner radar renderer (portfolio and single BIN).
4. Prospect pack generator: territory filter, ranking, HPD contact join, weekly
   Paperclip sweep and delta detection (new cohort, status changes).
5. Free lead magnet: single-BIN facade status card.

## Human checkpoints
- CP1 (week 1): sub-cycle derivation validated against 30 buildings with known
  cycle assignments from published DOB materials.
- CP2 (week 2): penalty math reviewed against DOB's stated schedule; filing-status
  edge cases (amended filings, extensions) triaged with a facade engineer's input.
- CP3 (week 3): one pilot QEWI firm reviews a real territory pack for list
  quality before any outbound uses it.

## Evidence required before completion
- verify_spines.py receipts (200, parsed, BIN and status columns confirmed).
- 30-building sub-cycle validation table committed.
- Pilot pack feedback from one QEWI firm documented (hit rate on due-and-unfiled
  accuracy across 25 sampled buildings).
- Owner radar reconciles against DOB NOW portal for 15 buildings with zero
  false "unfiled" claims (false penalties are trust-fatal).

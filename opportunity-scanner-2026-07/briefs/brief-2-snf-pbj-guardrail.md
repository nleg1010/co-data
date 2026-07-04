# Fable build brief 2: SNF PBJ Staffing Five-Star Guardrail

## Problem
Every Medicare/Medicaid nursing facility submits Payroll-Based Journal staffing
data quarterly. Submission failures, four-plus days with zero RN hours, or failed
audits drop the facility to a one-star staffing rating (801 facilities in January
2025 alone, receipt-confirmed), which mechanically drags the overall five-star
rating that drives referrals and MA network position. Administrators discover
problems after CMS does. Incumbent tooling (SimplePBJ/Netsmart) lives inside the
enterprise submission workflow; the 1-to-10-facility segment self-serves on
spreadsheets.

## Final outcome
A deployed product where any CCN returns the staffing five-star risk report from
the latest public PBJ quarter (predicted star, cut-point distance, audit-trigger
flags with offending days, state peer benchmark), and where a subscribed facility
can upload its CURRENT pre-submission PBJ extract (iQIES XML or CSV) and get the
same audit BEFORE filing: the pre-submission guardrail is the product's core value
and must ship in the MVP. Quarterly re-runs and packets are automated.

## Sources
Backbone: PBJ Daily Nurse Staffing PUF, data.cms.gov (quarterly, CCN-keyed,
verified live). Joins: Provider Information dataset (monthly, star ratings),
Five-Star Technical Users Guide cut points (parse per release), Care Compare
citation data for context. Buyer roster: CCN list itself plus Apollo (14,840
administrators at NAICS 6231, live receipt).

## Constraints
- Re-verify spines via scripts/verify_spines.py before ETL.
- The staffing-star replication must match CMS's published methodology version;
  every packet states the methodology edition and PUF quarter.
- Uploaded pre-submission files are customer data: encrypt at rest, never train
  on them, delete on request; state this in the product.
- No em-dashes in any artifact. Stack: existing CCN Postgres spine + Python +
  Next.js + Claude Code templates. 4-week MVP.

## Suggested workflow
1. PUF ingestion (all quarters) onto the CCN spine; star-math engine with unit
   tests against published examples.
2. Audit-trigger flag engine (zero-RN days, submission gaps, ratio anomalies).
3. Public risk-card renderer (lead magnet, rate-limited CCN lookup).
4. Pre-submission upload path: iQIES-format parser, same engines, delta report
   (what changes vs last public quarter).
5. Quarterly Paperclip sweep for subscribed CCNs; administrator email digest.

## Human checkpoints
- CP1 (week 1): star-math validation against 30 facilities where the current
  public rating is known; require exact match or documented variance.
- CP2 (week 2): audit-trigger definitions reviewed against CMS PBJ policy manual
  language; a false audit flag is worse than a miss.
- CP3 (week 3): pre-submission parser tested on 3 real extracts (recruit friendly
  facilities); privacy language reviewed.
- CP4 (week 4): pricing and packet copy reviewed against SimplePBJ positioning.

## Evidence required before completion
- verify_spines.py receipts for PUF and Provider Information (200, parsed, CCN
  column confirmed).
- 30-facility star-replication validation table committed to the repo.
- One full pre-submission audit run on a real extract with the facility's
  administrator confirming the flags were correct and actionable.
- Lead magnet cards for 10 prospect CCNs, hand-audited.
- Methodology-version pinning demonstrated: engine refuses to score a quarter
  whose spec edition it does not recognize.

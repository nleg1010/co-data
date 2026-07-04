# Medicare Advantage special section: Product A vs Product B vs Hybrid

Scored on the same five dimensions and anchors as the main field (scripts/calibration.md),
after the adversarial calendar-honesty correction (it is July; AEP file drops land in
September, AEP runs Oct 15 to Dec 7). Source receipts: data/ma_receipts_working.jsonl
(8 live-confirmed CMS and regulatory sources).

## Product A: public-data MA plan intelligence

Buyer: independent Medicare agent or small agency preparing for AEP.
Spine (all live-confirmed this session): Monthly Enrollment by Contract/Plan/State/County
(monthly by the 15th), PBP Benefits 2026 (quarterly), 2026 Star Ratings tables (Oct 9,
2025 release), Plan Crosswalks (annual, renew/consolidate/terminate), consolidated
Landscape file (September), CY2026 agent compensation FMV schedule (694/347 USD).
Entity key: CMS contract ID (H/S/R number) + plan ID + county FIPS. Day-1 public.

What the product does: joins five files on contract-plan-county, then for an agent's
county footprint produces the AEP battle card: plan exits and consolidations with member
counts (crosswalk), enrollment momentum (monthly deltas), benefit changes (PBP diff),
star movements, and the commission math per move at published FMV rates.

Scores: Quick Buildability 9 (five small documented CSVs, published layouts, no auth).
Lead Magnet Strength 7 (the assembled county disruption card is real and personalized,
but FMO first-look decks and ANOC season mean the buyer partly knows the content by
October; adversarial free-tool bias applied). Buyer Urgency 8 (hard annual calendar,
strongest Aug-Dec, dormant in spring; calendar honesty caps it below 9). Consultancy Fit 5
(the file-wrangling pattern is pure NSigma, but a mass market of individual agents at
low ACV is a consumer-adjacent motion, off the industrial/compliance ICP). Outbound
Clarity 8 (NIPR-derived lists and 20,626 Apollo-findable agency owners; county key ties
list to artifact). Total: 37.

## Product B: private-data agency command center

Buyer: agency owner with 10+ agents (the Medivana profile).
Data: carrier status reports, commission statements, book-of-business exports, call
recordings, SunFire/Spark exports. All customer-private.

Medivana ground truth applied (from the brief, treated as operational reality):
- Obtainable from a customer without heroics: monthly commission statement CSVs (per
  carrier portal), book-of-business exports (TLDCRM per-agent CSV exports: tedious,
  many files, but a checklist-driven onboarding can collect them), carrier status
  report downloads (formats vary wildly by carrier).
- Took Medivana months of carrier-portal plumbing and does NOT transfer to a SaaS
  onboarding: real-time status feeds, call-recording pipelines (TLDialer), and
  Spark/SunFire integration. Any Product B that assumes these on day 1 is a services
  engagement wearing a SaaS costume.
- Chargeback exposure is the sharpest felt pain: rapid disenrollment inside 90 days
  claws back the ENTIRE initial commission (42 CFR 422.2274 receipt), and it surfaces
  as negative lines on monthly statements agencies reconcile by hand.
- Spark Advisors (Medivana's NMA) already ships production and commission
  reconciliation with unpaid-commission recovery to its 6,000+ downline brokers (live
  receipt, sparkadvisors.com/platform). For any Spark-aligned agency, the
  reconciliation core of Product B duplicates a free FMO benefit.

Scores: Quick Buildability 2 (N carrier formats, portal plumbing, no public spine:
the months-of-integration anchor). Lead Magnet Strength 2 (no cold-email artifact
exists without the prospect's own files; the demo requires trust first). Buyer
Urgency 7 (chargebacks and unpaid commissions leak dollars monthly, chronic and real).
Consultancy Fit 4 (it is a systems-integration services business against free FMO
tooling; NSigma can BILL for it as consulting, but it is not a scalable product motion).
Outbound Clarity 6 (10+ agent agencies are findable, but the first call asks for
financial records, the highest-friction opener in this report). Total: 21.

## Hybrid: A wedge + single-CSV chargeback module

Ship Product A as the public wedge, then attach exactly one private artifact: a
chargeback and unpaid-commission exposure report generated from a single uploaded
commission-statement CSV (top 5 carrier formats first). No integration, one file,
immediate dollars found. Defer everything else in B until an FMO distribution
partnership makes the carrier plumbing someone else's problem.

Scores: Quick Buildability 8 (A's spine plus one bounded parser family). Lead Magnet
Strength 7 (A's county card remains the cold attachment; the CSV module converts
trials, it does not open doors). Buyer Urgency 8 (AEP calendar plus monthly statement
cycle). Consultancy Fit 6 (bounded private on-ramp fits NSigma's consulting-to-product
path; buyer still off core ICP). Outbound Clarity 8 (same lists, sharper offer).
Total: 37.

## Verdict

Product B loses decisively (21 vs 37): no public entity key, no day-1 value, no cold
artifact, and its reconciliation core is already a free benefit inside Medivana's own
FMO relationship. The honest reading of Medivana's operational reality is that B is a
consulting engagement NSigma could sell to agencies like Medivana, not a micro-SaaS.

Product A and the Hybrid tie at 37, and the Hybrid dominates on trajectory: same
build cost to start (A first), plus a retention layer that touches real dollars.
Verdict: HYBRID, sequenced A-first, with two hard caveats.
1. Sell it to agencies and FMO retention teams, not individual agents. The top-20
   candidate ma-agency-plan-exit-retention-packet (rank 13, total 40) is exactly this
   product with the B2B buyer, and it outscores standalone A by 3 points because the
   buyer, ACV, and urgency all improve. The special-section verdict and the main
   ranking agree: the agency-targeted A-shape is the only MA play that belongs near
   the top 20.
2. Both 37s sit below the top-20 cut of 38. On this run's evidence, MA plan
   intelligence is a good product in a crowded distribution ecosystem with FMO
   cloning risk (the adversarial review's strongest MA attack). It earns its place as
   a strategic option because NSigma owns Medivana's operational insight, not because
   it beat the industrial-compliance field on the merits.

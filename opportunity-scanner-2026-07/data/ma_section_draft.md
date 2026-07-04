# Medicare Advantage special section (draft, scores pending Phase 3 calibration)

## The two products

**Product A: public-data MA plan intelligence.**
Buyer: the independent Medicare agent or small agency principal preparing for AEP
(Oct 15 to Dec 7, 2027 plan year files land in September 2026).
Spine: CMS public files, all confirmed live this session by search receipt:
- Monthly Enrollment by Contract/Plan/State/County (monthly, by the 15th)
- PBP Benefits 2026 (quarterly ZIPs)
- 2026 Star Ratings data tables (released Oct 9, 2025, ZIP)
- Plan Crosswalks (annual, shows renew/consolidate/terminate)
- Consolidated Landscape file (annual, September, premiums and plan facts by county)
- Agent Broker Compensation FMV schedule (CY2026: 694 USD initial, 347 USD renewal national)
What the AI does: joins the five files on contract_id/plan_id/county, then for any
agent's county footprint produces an AEP battle card: which plans in their counties
are terminating or consolidating (crosswalk), where enrollment is shifting
(month-over-month deltas), which benefits changed vs last year (PBP diff),
which plans gained or lost stars, and the commission implication per move.
Lead magnet: "Your county's AEP disruption report" keyed to the counties an
agent works, generated from public data alone, no login needed.

Entity key: CMS contract ID (H/S/R number) + plan ID + county FIPS. Public. Day 1.

Product A pressure moment: the crosswalk plus landscape drop in late September,
AEP starts Oct 15. Every year several hundred plan-county combinations terminate
or consolidate, and every affected member is an SEP opportunity. Agents currently
assemble this picture by hand from carrier first-look decks, or buy seats on
Sunfire/Connecture (built for enrollment, not for market strategy).

**Product B: private-data agency command center.**
Buyer: agency owner with 10+ agents (Medivana profile).
Spine: carrier status reports, commission statements, book-of-business exports,
call recordings, SunFire/Spark exports. All customer-private.
What the AI does: reconciles carrier commission statements against the agency's
book to find unpaid initials, missed renewals, and chargebacks (rapid
disenrollment inside 90 days claws back the entire initial per 42 CFR 422.2274);
flags at-risk members before AEP; normalizes per-carrier status reports into one
retention dashboard.

Medivana reality check (ground truth from the brief, stated as constraints):
- TLDCRM + TLDialer stack: book data lives in a telesales CRM with per-agent
  CSV export realities, so "just export the book" is a many-file, per-agent chore.
- Carrier status reports and book-of-business reconciliation workflows exist and
  are manual today: the pain is real and weekly.
- Chargeback exposure is a felt, dollar-denominated pain (rapid disenrollment
  recovery is total, not partial).
- Spark Advisors NMA relationship: Spark's platform ALREADY does production and
  commission reconciliation with unpaid-commission recovery for its 6,000+
  brokers (live receipt, sparkadvisors.com/platform). Product B would compete
  with a free benefit of the FMO Medivana itself uses.
- Which feeds are truly obtainable from a customer vs which took Medivana months:
  commission statements and book exports are downloadable per carrier portal
  (obtainable, but per-carrier formats differ wildly); real-time status feeds and
  call recordings took portal plumbing that does not transfer to a SaaS onboarding.

## Verdict shape (final scores in Phase 3)

Product A wins on every scanner dimension that matters to NSigma:
- Quick Buildability: five documented public files vs N carrier portal formats.
- Lead Magnet Strength: county-level AEP disruption report is prospect-specific,
  urgent, and generated without any customer data. Product B has NO public lead
  magnet: you cannot demo reconciliation without the prospect's statements.
- Buyer Urgency: hard September-to-December annual clock with real commission
  dollars attached; Product B urgency is chronic, not calendared.
- Consultancy Fit: NSigma's whole motion is public-data artifacts; B is a
  systems-integration business against entrenched FMO tooling.
- Outbound Clarity: A's buyer is any licensed agent/agency in a county (findable
  by NIPR/state license lists and Apollo); B's buyer is a narrower 10+ agent
  agency owner, and the first conversation requires trust to hand over financials.

Product B's honest advantages: stickier (workflow lock-in), higher ACV, and the
chargeback recovery story is a direct dollars-recovered ROI. But Spark occupies
the reconciliation ground for exactly the agencies most likely to buy, and the
data onboarding (per-carrier statement formats) is the months-of-integration
product the brief bans for day 1.

Hybrid: ship Product A as the wedge (public AEP intelligence, entity key =
contract/plan/county), then attach ONE private artifact: a chargeback exposure
report from a single commission-statement CSV upload (no integration, one file,
immediate dollars). That keeps day-1 value public-keyed while opening B's
stickiness later. This is the shape the verdict will argue; scores to follow
the same 5-dimension calibration as the main field.

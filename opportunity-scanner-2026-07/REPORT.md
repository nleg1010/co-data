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

| Rank | Opportunity | Vertical | Model | QB | LM | BU | CF | OC | Total | Lead magnet concept |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | OATH/ECB Summons Defense and Cure Packet Generator | NYC CRE building compliance | public-first | 10 | 8 | 9 | 10 | 9 | 46 | Free BBL lookup: all open OATH/ECB summonses, accrued penalty and default exposure, and upcoming hearing dates for any NYC property. |
| 2 | PBJ Staffing Five-Star Guardrail and Pre-Submission Audit Packet for SNFs | Skilled nursing facilities | hybrid | 9 | 7 | 9 | 10 | 10 | 45 | Free CCN lookup: your staffing five-star risk report from the latest public PBJ quarter. |
| 3 | FISP Cycle 10 Deadline Radar and QEWI Prospect Packs | NYC facade inspection compliance (Local Law 11 / FISP) | public-first | 9 | 9 | 8 | 9 | 8 | 43 | Free BIN lookup: FISP filing history, current status, next sub-cycle deadline, and accruing penalty estimate. |
| 4 | DataQs RDR Auto-Drafter with Reversal Scoring | Trucking and logistics (motor carrier safety data correction) | public-first | 7 | 9 | 8 | 9 | 9 | 42 | Free USDOT lookup memo: N challengeable violations found on your record, estimated BASIC percentile improvement if removed, top 3 RDR drafts attached. |
| 5 | DMR Sentinel: citizen-suit exposure radar and exceedance early warning for NPDES dischargers | Environmental compliance (industrial wastewater and stormwater) | public-first | 6 | 8 | 9 | 10 | 9 | 42 | Free lookup by NPDES permit ID returning the facility's public DMR exceedances formatted as a draft citizen-suit exhibit with estimated penalty exposure. |
| 6 | Elevator CAT1/CAT5 Compliance Packet and Penalty Radar (NYC) | Elevator service and inspection agencies; NYC building owners | public-first | 9 | 8 | 8 | 9 | 8 | 42 | Free BIN or address lookup listing all elevator devices with test status and penalty exposure |
| 7 | HMSP Eligibility Guardian: OOS Rate and Crash Threshold Monitor | Hazmat transport (FMCSA Hazardous Materials Safety Permit carriers) | public-first | 8 | 9 | 8 | 8 | 8 | 41 | HMSP eligibility scorecard for USDOT 123456: your four rates vs the four thresholds, 90 day trend, and the two inspections to challenge first. |
| 8 | MSHA Citation Contest and Conference Decision Desk | Mining safety enforcement (coal and metal/nonmetal) | public-first | 7 | 8 | 8 | 9 | 9 | 41 | Free Mine Enforcement Exposure Scorecard by 7-digit MSHA Mine ID: 12-month citation mix, S&S rate vs district peers, dollar exposure trend |
| 9 | 2567 Plan of Correction Drafter and IDR Viability Memo for SNFs | Skilled nursing facilities (survey enforcement response) | hybrid | 7 | 7 | 9 | 9 | 9 | 41 | Free CCN lookup: citation history, F-tag benchmark vs state peers, and CMP exposure profile. |
| 10 | ERA Autopilot: SMARTS exceedance tracker and Level 1/Level 2 ERA report drafter for California IGP facilities | Environmental compliance (California industrial stormwater) | public-first | 8 | 8 | 7 | 8 | 9 | 40 | Free per-WDID status card showing parameters over NALs, projected level escalation, and how the facility ranks against California peers, generated entirely from public SMARTS data. |
| 11 | Local Law 97 Penalty Exposure Monitor and BEAM Filing Prep Engine | NYC CRE energy and emissions compliance | hybrid | 8 | 7 | 8 | 9 | 8 | 40 | Free BBL lookup: estimated 2024-period LL97 penalty and the 2030 cap cliff computed from public LL84 data. |
| 12 | AEP Disruption and Book-Retention Packet for Medicare Agencies | Medicare Advantage distribution (independent agencies and FMOs) | hybrid | 8 | 9 | 8 | 7 | 8 | 40 | Free plan-exit exposure score for any county FIPS or contract ID lookup. |
| 13 | Aggregates Regulator-View Benchmark and POV Early-Warning Packet | Mining safety (stone, sand and gravel aggregates) | public-first | 7 | 9 | 6 | 9 | 9 | 40 | Free instant MSHA Regulator-View Scorecard by Mine ID showing how the pit looks to its inspector vs 20 nearest peers |
| 14 | FDNY Violation Clearance Packet and Fire Protection Lead Engine (NYC) | Fire and life-safety inspection/service companies; NYC building owners | public-first | 8 | 6 | 8 | 9 | 8 | 39 | Free address/BIN FDNY violation report with penalty exposure summary |
| 15 | Boiler Annual Filing Penalty Shield (NYC) | Boiler inspection agencies and mechanical/fuel service firms; NYC owners | public-first | 9 | 7 | 7 | 8 | 8 | 39 | Free address lookup of boiler filing status and accrued penalties |
| 16 | OSHA Citation Response and Informal Conference Prep Packet | Construction and occupational safety enforcement | public-first | 8 | 7 | 9 | 7 | 8 | 39 | Free lookup by establishment name or inspection number: complete OSHA inspection, violation, and penalty history with current open exposure. |
| 17 | PWSID Copilot: portfolio compliance calendar and violation-response packet engine for contract water system operators | Drinking water utilities | hybrid | 8 | 7 | 8 | 8 | 8 | 39 | Paste a list of PWSIDs and get a free portfolio scoreboard: open violations, repeat-violator flags, and rank against state peers, straight from public SDWIS data. |
| 18 | Chain Inspection Sentinel: multi-jurisdiction retail food inspection watchtower keyed to CAMIS and city permit IDs | Multi-unit restaurant and grocery food safety | hybrid | 7 | 8 | 8 | 7 | 8 | 38 | Free chain scorecard: every NYC and Chicago location's current grade, open violations, and closure history, matched from the chain's public locations |
| 19 | Chicago Building Court Hearing Prep Packet | Municipal code enforcement (Chicago) | public-first | 8 | 8 | 8 | 7 | 7 | 38 | Free Chicago address lookup: open building violations, active administrative hearing cases, and estimated accumulated daily-fine exposure. |
| 20 | Carrier Intervention Risk Monitor and Insurance Renewal Defense Packet | Trucking and logistics (audit and insurance exposure) | hybrid | 7 | 8 | 7 | 8 | 8 | 38 | Renewal defense snapshot for USDOT 123456: your 12 month BASIC trajectory vs 200 same-size peers, intervention risk flag, and the three violation patterns driving your tier. |


Ties at 38 break alphabetically; fei-supplier-gmp-surveillance,
fda-import-alert-exit-packet, and fcc-rmd-carrier-kyc-packet sit at 38 just
outside the cut, and ll152-gas-piping-inspection-radar fell from rank 8 to 23
when the adversarial review exposed that GPS2 filing status, the load-bearing
field of its lead magnet, is not in the public bulk file.

## 3. Top 8 deep dives

### Dive 1 of 8: OATH/ECB Summons Defense and Cure Packet Generator (rank 1, total 46)

A. Product. Enter a BBL or BIN, get the portfolio's complete OATH/ECB exposure and a
per-summons defense packet. Input: NYC Open Data DOB ECB Violations (6bgk-3dad, daily,
1.8M+ rows) joined to OATH Hearings (rjte-hkhv) and HPD registrations on the existing
NSigma BBL spine. Processing: charge-code decoding against the penalty schedule, cure
and stipulation eligibility rules, hearing-outcome statistics per charge code, default
and accrued-penalty math. Output: a portfolio exposure ledger (every open summons,
dollar exposure, hearing date, deadline), plus a per-summons packet: what this charge
is, what it costs at default, whether cure or stipulation applies, the evidence
checklist, and a draft certificate-of-correction narrative marked for professional
review. The lead magnet PDF is the one-page exposure ledger for any BBL: open
summonses, accrued penalty and default exposure, next hearing dates.

B. Why it works. The dataset is public, daily, and BBL-keyed, so the entire MVP and
the lead magnet run with zero customer data: NSigma's existing NYC ingestion makes
this a join-and-render build. Private data adds stickiness later: the customer's
internal work-order system status per violation (handed over as CSV export from
AppFolio/Yardi, easy) turns the ledger into a closed-loop correction tracker. The
category-defining enhancement is the outcome model: historical dismissal, reduction,
and default rates per charge code and per hearing officer computed from the OATH
dataset's millions of adjudicated rows, so every summons carries a fight-or-pay
recommendation no incumbent publishes. Build approach: Claude Code for ingestion and
rules, plus a Paperclip agent that re-scores the portfolio nightly and drafts packets
for new summonses.

C. Buyer. Director of Compliance or Director of Property Management at NYC managing
agents and owner-operators, 10 to 500 buildings, NAICS 531312. They feel the pain
weekly: portfolios receive a continuous summons stream from DOB, FDNY, DSNY, and DEP;
one missed hearing converts a reducible fine into a default judgment at the statutory
maximum plus interest (confirmed via NYC DOF settlement program FAQ receipt). Status
quo cost: expeditors at 50 to 250 USD per hour plus filing fees, OATH attorneys per
case, and penalties of 500 to 25,000 USD per summons (all receipt-confirmed).
Finding them: HPD Multiple Dwelling Registrations (tesw-yqqr) joined to HPD
Registration Contacts (feu5-w2e2) on RegistrationID yields the registered managing
agent for every multiple dwelling, keyed to the same BBL as the product. Apollo shows
2,902 broad-title property contacts at NYC NAICS 5313 (exact compliance titles are
scarce at 130, so the HPD roster is the primary list). Associations: NYAA (the CHIP
and RSA merger, 4,000+ owner members) and NYARM. Conference: BuildingsNY at Javits
(5,000+ NYC owners and managers).

D. Source spine. Backbone: DOB ECB Violations (6bgk-3dad), verdict verified-live,
public-easy, daily updates observed through late June 2026, BIN/BORO/BLOCK/LOT
documented plus ecbviolationnumber linking to the OATH dataset's ticketnumber
(receipt: nycdb wiki). Supporting: OATH Hearings Division Case Status (jz4z-kudi:
infraction charged, decision outcome, penalty imposed and paid, the outcome-model
training table), DOB Violations (3h2n-5cm9), HPD registration datasets, CityPay.
Dive caveat verified: as of May 4, 2026 OATH removed respondent name and address
fields from the case-status dataset; charge, outcome, and amount fields remain, so
the BBL and summons-number joins this product needs are unaffected. Outcome
statistics have published precedent: DOBGuard's own 2026 guide markets aggregate
rates (about 15 percent of ECB violations fully dismissed; 38 percent of contested
violations dismissed or reduced), and roughly 573 million USD of ECB judgment debt
was outstanding as of October 2025 (NYC DOF receipt), which is the dollar pool
default prevention plays against.

E. Competitive landscape. SiteCompli InCheck (quote-only, roughly 500 USD per month
entry per third-party listings) monitors violations and workflow but generates no
defense work product. ViolationWatch (9 USD per building per month, or 99 USD per
year tiers) does detection and reminders with no adjudication layer. DOBGuard gives
the lookup away free, which is exactly why the lookup is the magnet and not the
product. The manual status quo (expeditors at 50 to 250 USD per hour, spreadsheets)
is reactive and per-summons. The gap nobody fills: portfolio-wide triage with
outcome-statistics-ranked fight, cure, stipulate, or pay recommendations and drafted
correction paperwork.

F. Commercial model. 3 USD per building per month with a 299 USD monthly floor
(priced above ViolationWatch's 9 USD per building where portfolios are small, below
SiteCompli where they are large); packet drafting included at 100+ buildings,
otherwise 29 USD per drafted packet. ACV range 3,600 to 25,000 USD. Sales motion:
cold email to HPD-registered agents with their own BBL exposure ledger attached;
close over one screen-share. Channel: expeditors and OATH attorneys white-labeling
packets (they keep the representation work, the tool does the assembly), NYAA and
NYARM member programming.

G. Risks. First, the free-lookup squeeze: DOBGuard and ViolationWatch can add penalty
math quickly, so the moat must be the outcome model and drafted packets, which are
harder to copy than a join. Second, unauthorized-practice-of-law exposure if drafted
narratives read as legal advice; v1 ships data, deadlines, eligibility flags, and
templates marked draft for professional review (this is also why the expeditor
channel works instead of fighting it). Third, city data-schema churn: OATH and DOB
have reorganized datasets before (the sibling-dataset confusion in this run's own
verification is the warning); ingestion needs schema tests and a fallback to the BIS
web layer.

### Dive 2 of 8: SNF PBJ Staffing Five-Star Guardrail (rank 2, total 45)

A. Product. Enter a CCN, get the facility's staffing five-star risk report before CMS
does the math for real. Input: CMS Payroll-Based Journal Daily Nurse Staffing PUF
(quarterly), Provider Information dataset, published staffing star cut points.
Processing: replicate the staffing-star methodology per CCN, flag the audit triggers
CMS publishes (four or more days with zero RN hours, submission gaps, sitter
misclassification patterns), compute distance to the next cut point, benchmark
against state peers. Output: a quarterly guardrail packet per facility: predicted
staffing star, the exact offending days, turnover measure status, and what one more
RN-hour per resident-day would change. Lead magnet PDF: the one-page CCN staffing
risk card from the latest public quarter.

B. Why it works. PBJ PUF and the five-star technical spec are public and CCN-keyed,
so the full simulation runs without customer data; NSigma already operates the CCN
spine. Private stickiness: the facility's current-quarter PBJ extract before
submission (a CSV the administrator already produces for iQIES, easy handover) turns
the retrospective report into a pre-submission audit that catches the zero-RN-day
before CMS sees it. That pre-submission audit is the category enhancement: the
public-data version arrives a quarter late (the adversarial review's correct attack),
the pre-submission version arrives exactly on time, every quarter, forever. Build:
Claude Code for the star-math engine (published methodology), Codex for the PBJ CSV
validator, a Paperclip agent for the quarterly re-run and packet generation.

C. Buyer. Administrator or regional VP of operations at SNF chains and independents,
1 to 100 facilities, NAICS 623110. Pain: in January 2025 alone 801 facilities were
dropped to a one-star staffing rating for PBJ audit failures (receipt confirmed);
a one-star staffing rating mechanically drags the overall star, which drives
referrals and MA network position. Status quo: five-star consultants per engagement
plus SimplePBJ-class software; a suppressed quarter costs census revenue (labeled
est. 25,000 to 250,000 USD per facility). Finding them: the CCN roster IS the list
(14,840 administrators and executive directors findable on Apollo at NAICS 6231,
live receipt); associations AHCA/NCAL and LeadingAge; conferences AHCA Delivering
Solutions and the state affiliate shows.

D. Source spine. Backbone: PBJ Daily Nurse Staffing PUF, verdict verified-live,
public-easy, quarterly, CCN documented. Supporting: Provider Information (monthly),
Five-Star technical users' guide cut points, Care Compare datasets. All receipts in
the appendix.

E. Competitive landscape. SimplePBJ (ezPBJ, now Netsmart) sits inside the submission
workflow and projects the staffing star from live facility data (the adversarial
receipt); its gravity is chains already on Netsmart. CMS itself provides iQIES
preview reports, but after the quarter closes. Five-star consultants (Proactive LTC
tier) sell per-engagement analysis. The gap: an independent, pre-submission audit
with the exact audit-trigger flags, sold standalone to the 1-to-10-facility segment
SimplePBJ's enterprise motion skips, at self-serve pricing.

F. Commercial model. 149 USD per facility per month with a 299 USD floor (two
facilities), annual prepay at 10 months; chains above 25 facilities at 99 USD per
facility. ACV 1,800 to 30,000 USD. Motion: cold email to administrators with their
own last-quarter risk card attached; state association webinars as the trust channel.
Channel potential: LTC consultants white-labeling the packet, state AHCA affiliates.

G. Risks. First, SimplePBJ or Netsmart flips the pre-submission audit into a free
feature; the counter is the independent-of-your-EHR positioning and the small-chain
segment. Second, the public PUF lags a quarter, so the free magnet always shows
stale data; conversion depends on the pre-submission upsell landing fast. Third, CMS
methodology churn (staffing measure weights changed twice in recent years) demands
same-week spec updates or the simulation loses credibility.

### Dive 3 of 8: FISP Cycle 10 Deadline Radar and QEWI Prospect Packs (rank 3, total 43)

A. Product. Enter a BIN, get the facade compliance clock. Input: DOB NOW Safety
Facades Compliance Filings dataset plus the covered-buildings logic (six stories or
higher), HPD registrations for contacts. Processing: sub-cycle assignment from block
number, filing status, deadline math, penalty accrual (5,000 USD per year unfiled,
1,000 USD per month late, receipt-confirmed against DOB's official page). Output:
two artifacts from one engine: for owners and agents, a portfolio facade deadline
radar with accrued-penalty estimates; for QEWI engineering firms, ranked prospect
packs of due-and-unfiled buildings in their territory with registered agent contacts.
Lead magnet PDF: the BIN facade status card (filing history, current status, next
window, penalty estimate).

B. Why it works. The filings dataset and cycle rules are public and BIN-keyed;
NSigma's NYC spine makes the join trivial. Private stickiness: the engineering
firm's proposal pipeline (a spreadsheet they already keep, easy handover) turns
prospect packs into a win-rate-tracked BD system. Category enhancement: the full
NYC exterior-compliance calendar in one product, folding LL126 parapet inspections
and gas piping windows into the same BIN-keyed radar, which converts a facade tool
into the compliance calendar of record for exterior work. Build: Claude Code
(Socrata ingestion, deadline engine, PDF packs); Paperclip agent for the weekly
new-cohort sweep per QEWI territory.

C. Buyer. Two-sided. Primary: principal or BD director at facade engineering and
exterior restoration firms, 10 to 200 staff, NAICS 541330, who pay for target lists
today (analyst hours against DOB lookups) and whose inspection engagements run 8,000
to 60,000 USD (receipt-confirmed range from pricing guides). Secondary: managing
agents avoiding 1,000 USD per month late penalties. Finding them: QEWI-eligible
firms are enumerable (PE/RA license holders marketing facade work), BuildingsNY and
CooperatorEvents floors are full of both sides, and the HPD roster covers the owner
side. LinkedIn filter: NYC metro, civil or architectural engineering, title contains
principal or business development, company keywords facade or restoration.

D. Source spine. Backbone: DOB NOW Safety Facades Compliance Filings (verdict
verified-live, public-easy, refresh observed current within the month). Supporting:
PLUTO for building attributes, HPD registrations for contacts, DOB violations for
the penalty ledger.

E. Competitive landscape. SiteCompli-class monitors flag facade status inside owner
subscriptions but sell nothing to the engineering side. Marketing-list vendors sell
static building lists without filing-status logic. The manual status quo is a BD
coordinator hand-searching DOB NOW per building. The gap: nobody sells
deadline-ranked, contact-attached QEWI prospect packs refreshed weekly, and nobody
folds the penalty math into the owner-side pitch.

F. Commercial model. QEWI side: 499 USD per month per borough territory (floor 499,
each additional borough 250). Owner side: bundled into the same 3 USD per building
per month NYC compliance radar as the OATH product (shared platform). ACV 6,000 to
18,000 USD on the engineering side. Motion: send a firm the pack for its own past
clients' buildings (public filing history shows who they filed for) plus ten
due-and-unfiled neighbors; the artifact is the demo. Channel: co-marketing with
restoration contractors who feed QEWI firms work.

G. Risks. First, the one-shot list problem (the adversarial review's attack): a firm
can buy one pack and churn, so packaging must be subscription-only with weekly new
cohorts and status-change alerts, never a la carte exports. Second, sub-cycle windows
concentrate demand; between windows the owner-side radar and parapet/gas modules must
carry engagement. Third, filing-status data quality: if DOB NOW filing statuses lag
or misreport, penalty estimates embarrass; the packet needs a data-as-of stamp and a
manual-verify flag for edge cases.

### Dive 4 of 8: DataQs RDR Auto-Drafter with Reversal Scoring (rank 4, total 42)

A. Product. Enter a USDOT number, get a ranked challenge docket. Input: FMCSA SMS
monthly snapshot files (census, inspection, violation, crash). Processing:
month-over-month snapshot diffing builds a label set of violations that left the
record; a scoring model ranks every current violation by estimated reversal odds
(severity weight, violation code, inspection context); templates draft the Request
for Data Review narrative citing the inspection facts and the regulation cited.
Output: the challenge docket plus per-violation RDR drafts the safety director files
through the carrier's own DataQs account. Lead magnet PDF: the USDOT memo: N
challengeable violations found, estimated BASIC percentile improvement if removed,
top 3 drafts attached.

B. Why it works. The SMS files are public, monthly, USDOT-keyed with documented
layouts (verified receipt including the next release week of July 6, 2026), so the
MVP needs zero integrations; filing stays manual in the carrier's account, which
also keeps the product outside FMCSA's authorization perimeter. Private stickiness:
the carrier's roadside inspection reports and dashcam or ELD context (handed over
per challenge, moderate effort) raise draft quality on the contested cases. Category
enhancement: the reversal-probability model itself; snapshot-diff labels are a free
training set nobody publishes, and after two years the outcomes data is a moat no
copycat starts with. Build: Claude Code for ETL and diffing, Codex for the scoring
model, Paperclip agent for the monthly docket refresh per subscribed fleet.

C. Buyer. Safety director or VP of safety at for-hire carriers, 50 to 1,000 power
units, NAICS 484121. Pain: CSA percentiles are public and drive insurance pricing,
broker vetting, and intervention targeting; erroneous violations sit for 24 months;
71,000+ DataQs requests were processed in 2024 (receipt) and paid challenge services
demonstrably outperform self-filing (CNS receipt: near 60 percent vs 43 percent on
crash challenges). Status quo: DOT consultants at 50 to 250 USD per driver per month
retainers, per-challenge fees (est. 150 to 500 USD). Finding them: Apollo shows
2,646 safety directors at NAICS 484 (live receipt); the FMCSA census file provides
the fleet-size-filtered company list with addresses; associations: state trucking
associations and ATA safety council; conference: ATA SMC (Safety Management
Council).

D. Source spine. Backbone: FMCSA SMS monthly snapshots (verdict verified-live,
public-easy zips of documented flat files, monthly cadence on the third or last
Friday, USDOT key documented; 2026 methodology overhaul flagged as a watch item in
the receipt). Supporting: DataQs portal (filing target), A&I inspection statistics.

E. Competitive landscape. CNS, J.J. Keller, Fleetworthy sell DataQs challenge
services with human experts at per-challenge or retainer pricing; they own the
relationship but hand-triage. TMS-adjacent SaaS (Motive, Samsara safety scores)
monitors CSA but does not draft. The spreadsheet status quo is a safety manager
eyeballing the monthly SMS refresh. The gap: automated triage with reversal odds
plus ready-to-file drafts at software price, positioned as the tool the consultant
or the in-house director uses, not a replacement service.

F. Commercial model. 199 USD per month per fleet up to 100 power units, 399 to 999
USD per month above that (floor 199); optional 49 USD per additionally drafted RDR
beyond quota. ACV 2,400 to 12,000 USD. Motion: cold email to safety directors with
the fleet's own memo attached; the memo names real violations, which is the whole
pitch. Channel: insurance brokers and captives who want clients' BASICs down, plus
the waste-hauler book NSigma already keys by USDOT.

G. Risks. First, the 2026 SMS methodology overhaul renames categories and rescores
violations; ETL and the model must re-baseline the month it lands or every memo is
wrong (the receipt flags the preview site). Second, snapshot-diff labels are noisy
(decay and corrections also remove violations); the model must be validated against
a hand-labeled sample before the reversal odds go in front of buyers, and the memo
language hedges accordingly. Third, incumbents can bolt drafting onto their
retainers; the counter is speed, price, and the outcomes dataset compounding.

### Dive 5 of 8: NPDES DMR Exceedance Early-Warning Radar (rank 5, total 42)

A. Product. Enter an NPDES permit ID, get the facility's discharge compliance
posture the way an opposing counsel would compute it, before opposing counsel does.
Input: EPA ECHO ICIS-NPDES DMR and limit datasets (per-fiscal-year CSVs, weekly
refresh) plus ECHO exporter facility data on the FRS spine NSigma already runs.
Processing: exceedance detection per parameter and outfall, statutory penalty
exposure math at current 64,618 to 68,445 USD per day rates (receipt range), peer
benchmarking by SIC code, trend flags on parameters drifting toward limits. Output:
a monthly early-warning packet: new exceedances, accumulating exposure, the five-year
lookback a 60-day notice letter would cite, and prioritized corrective actions.
Lead magnet PDF: the permit-ID exposure snapshot, reframed after the adversarial
review as your compliance posture, internal-audit style, not a plaintiff mockup.

B. Why it works. DMR data is self-reported into a public federal system, refreshed
weekly, permit-keyed; the citizen-suit bar mines exactly this data (receipted), so
the fear is real and documented. NSigma's FRS-keyed industrial infrastructure joins
directly. Private stickiness: the facility's lab results before DMR submission
(LIMS CSV export, easy) turns the radar into a pre-submission checker that catches
transcription errors, the most common self-inflicted violation. Category
enhancement: the plaintiff-model: train on historical 60-day notices and consent
decrees (public court records) to score which facilities get targeted, converting
the product from data display into risk prediction. Build: Claude Code ETL over the
FY CSVs, Codex for exceedance and penalty engines, Paperclip agent for the weekly
sweep and monthly packet.

C. Buyer. Director of EHS or environmental manager at industrial manufacturers with
individual NPDES permits, 100 to 1,000 employees per site, NAICS 31-33. Pain: a
60-day notice letter means 10,000 to 1,000,000+ USD in legal fees and settlements
routinely include six-to-seven-figure penalty and BMP packages (receipts); the data
that triggers it is their own filings. Status quo: quarterly consultant DMR reviews
(about 500 USD per quarter routine, 2,500 to 10,000 per facility for compliance
support, receipted) that look backward, not at exposure. Finding them: 20,738 EHS
managers at manufacturers on Apollo (live receipt); the permit list itself is the
roster; associations: state manufacturers' associations, WEF industrial sections;
conference: WEFTEC.

D. Source spine. Backbone: ICIS-NPDES DMR and limit datasets via ECHO downloads
(verdict verified-live, public-hard-to-parse per-FY zips, weekly refresh, NPDES
permit ID documented). Supporting: ECHO exporter (weekly, FRS-keyed), effluent
charts as the free reference layer.

E. Competitive landscape. EPA's own ECHO effluent charts and DMR exceedance search
are free and facility-specific (the adversarial receipt), which kills any product
that is just a lookup. Mapistry and similar stormwater/wastewater compliance SaaS
manage tasks and sampling but do not compute litigation-style exposure or peer
targeting risk. Environmental consultants do it manually per engagement. The gap:
continuous exposure math plus targeting-risk prediction, priced as software.

F. Commercial model. 299 USD per facility per month (floor 299), 199 at 5+
facilities; the pre-submission checker as a 99 USD per month add-on. ACV 3,600 to
20,000 USD. Motion: cold email to EHS directors with the facility's own posture
snapshot; the internal-audit framing keeps counsel comfortable. Channel:
environmental consultants embedding the radar in retainers; insurers writing
pollution liability.

G. Risks. First, the artifact-liability problem the adversarial review named: a
penalty-exposure document about a company, unsolicited, can be discoverable and
counsel may quarantine it; the reframe (posture report, no draft-exhibit language)
and an opt-in gate on the detailed lookback mitigate but do not eliminate this.
Second, ECHO gives the core away free; if EPA adds exposure math the wedge narrows
to prediction and workflow. Third, DMR data quality (NODI codes, limit-set
complexity) can produce false alarms; a false exceedance email to a buyer is fatal
to trust, so the engine needs conservative flagging and human review on first-run
packets.

### Dive 6 of 8: NYC Elevator CAT1/CAT5 Compliance Packet and Penalty Radar (rank 6, total 42)

A. Product. Enter a BIN or BBL, get every elevator device's test status and the
money at stake. Input: DOB NOW Elevator Safety Compliance dataset plus device
registrations, on the existing BBL/BIN spine. Processing: per-device CAT1 annual and
CAT5 five-year test deadline math, filing-window tracking (report due within 21 days
of test, corrections affirmed within set windows), penalty accrual (3,000 USD per
device per missed filing plus 3,000 per missed affirmation, receipt-confirmed
against 1 RCNY 103-02). Output: for elevator agencies, a portfolio test-and-filing
calendar with defect follow-up tracking; for owners and agents, the penalty radar.
Lead magnet PDF: the building's device list with test status and exposure.

B. Why it works. Device-level compliance data is public and BIN-keyed; the deadline
and penalty rules are mechanical; the buyer universe (elevator agencies and managing
agents) is dense and reachable. Private stickiness: the agency's service contract
roster (CSV, easy) turns the radar into a contract-renewal defense and upsell
engine (which client buildings are drifting toward penalties). Category
enhancement: unify with boiler, facade, gas piping, and OATH modules into the NYC
building compliance calendar of record: one BBL in, every deadline out. That
platform is the actual product NSigma is assembling across four top-20 candidates;
elevator is its highest-frequency module (deadlines stagger all year). Build:
Claude Code Socrata ingestion and rules engine; Paperclip agent for weekly agency
digests.

C. Buyer. Service manager or sales director at elevator maintenance and inspection
agencies (20 to 500 staff, NAICS 238290) and directors of property management at
managing agents. Pain: each missed CAT1 filing is 3,000 USD per device and mostly
non-waivable (receipt); agencies eat client blame and churn when filings slip.
Status quo: spreadsheet calendars per mechanic, filing-service vendors per event.
Finding them: DOB-licensed elevator agency directors are a public roster; Apollo
NYC building-services titles; associations: NEII and local elevator industry
groups; CooperatorEvents expo floors.

D. Source spine. Backbone: DOB NOW Elevator Safety Compliance (verdict
verified-live, public-easy, regular refresh observed June 2026). Supporting: DOB
device registrations, ECB violations for the penalty ledger.

E. Competitive landscape. SiteCompli-class owner monitors flag elevator violations
but sell nothing agency-side. Filing-service vendors (OneView-class) file per event
without portfolio radar. Spreadsheets everywhere else. The gap: device-grain
deadline engine sold to the agencies that carry the filing duty, with the owner
radar as the second seat.

F. Commercial model. Agencies: 349 USD per month up to 500 devices, 1.5 USD per
device beyond (floor 349). Owners: bundled in the NYC platform at 3 USD per building
per month. ACV 4,200 to 15,000 USD. Motion: agency outbound with a pack showing the
agency's own client buildings' filing posture (public data shows who services what
via filings). Channel: the OATH/FISP/boiler platform cross-sell; elevator consultants.

G. Risks. First, dataset grain: if device-level test statuses lag DOB NOW's portal,
the radar mis-states exposure (the FDNY-style key-documentation gap from this run's
verification is the cautionary case; ingestion needs a per-device spot-check
harness). Second, agencies are late tech adopters with thin margins; pricing must
survive a skeptical 20-person shop. Third, platform sprawl: elevator alone is a
feature; the NYC calendar platform is the business, and sequencing it wrong (five
half-built modules) burns the wedge.

### Dive 7 of 8: HMSP Eligibility Guardian (rank 7, total 41)

A. Product. Enter a USDOT number, get the hazmat safety permit survival scorecard.
Input: FMCSA SMS monthly snapshot files (inspection, crash, census). Processing:
compute the four rolling HMSP rates exactly as FMCSA does (driver OOS, vehicle OOS,
hazmat OOS, crash rate) against the published fixed denial thresholds (9.68, 33.33,
6.82 percent and 0.136, receipt-confirmed), trend them over 24 months, and flag the
specific inspections dragging each rate. Output: a monthly eligibility scorecard
with threshold distance, trajectory, and the two challenges to file first. Lead
magnet PDF: the four-rates-vs-thresholds card for any HMSP-holding USDOT number.

B. Why it works. The rates are computable from the same public SMS files as the
DataQs product (shared ETL), the thresholds are published, and FMCSA now
continuously monitors permit holders via SMS analysis (receipt), so a bad quarter
can start suspension proceedings silently. Note from verification: the SAFER
national hazmat rate guidance page is a stale 2003-2010 reference sheet; the
product's backbone is the SMS files plus current HMSP guidance thresholds, and the
receipts say so explicitly. Private stickiness: none needed early; the carrier's
inspection reports (moderate handover) sharpen challenges later. Category
enhancement: the DataQs challenge engine scoped to HM violations, back-tested
against FMCSA proposed-revocation actions, turning monitoring into permit defense.
Build: Claude Code on the shared SMS pipeline; Paperclip monthly sweep per fleet.

C. Buyer. Safety director at hazmat and tank truck carriers, 20 to 500 power units,
NAICS 484230. Pain: the HMSP is the license for the highest-value placarded loads;
losing it stops that revenue line while general freight continues, an existential
asymmetry. Status quo: J.J. Keller-class hazmat compliance services (quote-only),
general DOT retainers at 50 to 250 USD per driver per month, and FileFlo-class CSA
SaaS at a published 299 USD per month that tracks BASICs but not the four HMSP
rates (all receipted). Finding them: the SAFER census flags HM-permitted carriers
(the roster IS the list); NTTC (Tank Truck Week, roughly 1,000 attendees, Sept
2026) and ATA's Safety Management Council are the concentration points.

D. Source spine. Backbone: FMCSA SMS monthly snapshots (verified-live, monthly,
USDOT-keyed; 2026 methodology overhaul watch item applies here too). Supporting:
current FMCSA HMSP guidance pages for thresholds; DataQs portal for challenges.
Downgraded reference: SAFER HazMatRatesPost page (stale 2003-2010 data; receipt
verdict needs-attention; used for nothing computational).

E. Competitive landscape. Free FMCSA tools show raw BASICs but never compute the
four permit rates against thresholds (receipted gap). FileFlo, Fleetworthy,
SambaSafety track CSA percentiles generically. J.J. Keller sells consultant hours.
The gap: nobody sells HMSP-specific threshold monitoring, and the buyer who needs
it cannot see revocation coming from any dashboard they own today.

F. Commercial model. 249 USD per month per fleet (floor 249, flat to 200 power
units, 499 above), bundled 100 USD discount with the DataQs product. ACV 3,000 to
6,000 USD. Motion: cold email to safety directors at HM-flagged carriers with
their own four-rates card. Channel: tank truck insurers and NTTC affinity
programming; cross-sell to the DataQs base.

G. Risks. First, niche TAM: HMSP holders number in the low thousands (this run
could not verify an exact count; flagged unverifiable in the dive), so this is a
module business, not a standalone company; it works because it shares 90 percent
of its build with DataQs. Second, the 2026 SMS methodology change may alter rate
inputs; same re-baseline duty as dive 4. Third, threshold or policy drift: FMCSA
has revised HMSP oversight before; the product must track guidance pages, not
cached constants.

### Dive 8 of 8: MSHA Citation Contest and Conference Decision Desk (rank 8, total 41)

A. Product. Enter a 7-digit MSHA Mine ID, get the contest-or-pay decision desk for
every open citation. Input: MSHA open data flat files (violations, assessed
violations, inspections, conferences; weekly refresh receipted) plus FMSHRC
decision archives. Processing: per-citation Part 100 penalty-point exposure math,
then a contest-worthiness score from historical outcomes of similar citations
(same 30 CFR standard, gravity, negligence, district). Output: a per-citation
decision packet inside the 10-day conference window: expected penalty if paid,
historical modification and vacate rates, recommended action, and the conference
request draft. Lead magnet PDF: the Mine Enforcement Exposure Scorecard (12-month
citation mix, S&S rate vs district peers, dollar trend).

B. Why it works. MSHA publishes citation-level enforcement data weekly with the
Mine ID key documented, and the dive verified the operational premise: citations
appear in the public files fast enough to act inside the 10-day window
(issuance-to-file lag under 5 days per the dive's receipts). Assessed-vs-final
deltas in the public data are a free outcomes training set. Private stickiness:
the operator's citation PDFs and photos (easy handover per case) improve drafts.
Category enhancement: the contest-worthiness model validated against FMSHRC
outcomes, which no incumbent publishes per citation. Build: Claude Code flat-file
ETL, Codex for the scoring model over litigated outcomes, Paperclip weekly sweep
and packet generation.

C. Buyer. VP or director of safety at multi-mine coal and metal/nonmetal
operators, NAICS 2121-2123. Pain: mandatory inspections (4x underground, 2x
surface per year, receipted) produce citation batches with 10-day conference and
30-day contest clocks; industry assessments ran roughly 200M USD in the 2010 peak
(receipted) and POV status triggers withdrawal orders. Status quo: FMSHRC counsel
per docket (hourly, quote-only; the EAJA fee cap of 125 USD per hour the dive
surfaced shows how fee-sensitive this space is), Predictive Compliance
(quote-only enterprise) for penalty tracking, spreadsheets everywhere else.
Finding them: the mine roster with operator names is public (MSHA data), 1,388
mining safety leads on Apollo (live receipt); NSSGA and NMA associations; TRAM
and MINExpo (quadrennial, 45,000 attendees) conferences.

D. Source spine. Backbone: MSHA Open Government Data Portal flat files
(verified-live, weekly Friday refresh, Mine ID and event numbers documented).
Supporting: FMSHRC decisions (contest outcomes), Part 100 penalty tables.

E. Competitive landscape. Predictive Compliance tracks citations and penalty math
at enterprise quote-only pricing but publishes no contest-worthiness probability.
MSHAWISE assists research, not keyed live to a mine's citation stream. Counsel
judgment is per-docket and expensive. MSHA's free MDRS shows raw history with no
decision layer. The gap: quantified, precedent-based contest triage delivered
inside the 10-day window at software price.

F. Commercial model. 399 USD per month per mine complex (floor 399), 249 per
additional complex, aggregates chains at portfolio pricing. ACV 4,800 to 24,000
USD. Motion: cold email to safety VPs with their own exposure scorecard;
conference and association programming (TRAM is free to attend and safety-officer
dense). Channel: mining law firms white-labeling the decision packet as intake,
insurers, NSSGA affinity.

G. Risks. First, model defensibility: contest outcomes depend on facts not in the
data (photos, testimony); the score must present base rates, not predictions, or
counsel will discredit it. Second, the buyer's lawyer is the channel AND the
competitor; positioning the packet as counsel's intake accelerant is the only
stable stance. Third, dataset lag risk on conferences: if the 10-day window
occasionally outruns file publication for some districts, the product needs the
operator to forward the citation PDF (easy, but breaks the zero-touch pitch).


## 4. Medicare Advantage special section


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


## 5. Source spine appendix

Verification protocol: this sandbox's egress policy returned CONNECT 403 for every
government host probed (34 hosts, data/egress_probe_log.jsonl), so no receipt below
is a fetch-and-parse receipt. Each receipt is class R2: the source was live-verified
THIS SESSION via WebSearch (existence at URL, format, update cadence, entity-key
documentation, freshness, access class), with the exact queries, URLs, titles, and
claims recorded in data/source_receipts.jsonl. Sample rows shown in candidate
dossiers are schema-documented, not session-parsed; run scripts/verify_spines.py on
any normally-connected machine to convert every receipt to R1 (HTTP status, parsed
sample rows, entity-key column confirmation) in one command. Per the brief's rule,
candidates whose backbone verification raised issues were downgraded or killed and
are called out below and in section 7.


Sources backing top-20 candidates are marked [TOP20].


### src-01: FMCSA SMS monthly inspection and violation snapshot files [TOP20]
- URL: https://ai.fmcsa.dot.gov/sms/Data/Downloads.aspx (also surfaced as https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx branded FMCSA Open Data Program; mirrored on data.transportation.gov)
- Verdict: verified-live | Access class: public-easy | Format: Monthly zip archives; each zip contains a comma delimited flat data file plus a text readme describing the fields; four SMS input files (motor carrier census, inspection, violation, crash) and SMS out
- Update frequency: Monthly; snapshot of the data taken on the third or last Friday of each month, about 10 days of processing and validation, then results posted to the SMS website
- Freshness confirmed: SMS website updated May 26, 2026; next monthly update scheduled for the week of July 6, 2026
- Entity key: USDOT number | documented: True (Downloads page documentation states the inspection file contains the U.S. DOT number plus report number, inspection date, state and vehicle info, and that each zip includes a text )
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FMCSA SMS data downloads ai.fmcsa.dot.gov Downloads.aspx monthly snapshot" -> https://ai.fmcsa.dot.gov/sms/Data/Downloads.aspx (Safety Measurement System - Downloads)
- Backs: dataqs-rdr-drafter
- Notes: No login, API key, or fee; direct public download. Caveat: FMCSA is rolling out a revised SMS methodology in 2026 (renamed categories, consolidated violations, new scoring, preview at csa.fmcsa.dot.gov/prioritizationpreview), so file layouts and BASI

### src-02: FMCSA company safety records (SAFER snapshot, SMS results, licensing and insurance) [TOP20]
- URL: https://www.fmcsa.dot.gov/safety/company-safety-records (operational lookup at https://safer.fmcsa.dot.gov/CompanySnapshot.aspx)
- Verdict: verified-live | Access class: public-easy | Format: HTML landing page linking to the SAFER Company Snapshot (free per-carrier ad hoc web query returning an HTML record) and the Company Safety Profile (CSP) report; no bulk file at this URL; SAFER Compan
- Update frequency: Company Snapshot data updated daily, except inspection and crash activity counts which are updated weekly (24 month window); data sourced from MCMIS and the Licensing and Insurance systems
- Freshness confirmed: Refresh cadence stated on the SAFER Data Update Rates page (daily, with weekly inspection/crash counts); page and live carrier queries confirmed indexed and current in July 2026 searches
- Entity key: USDOT number | documented: True (Live snapshot query URLs use query_param=USDOT with the USDOT number as the lookup key, and the CompanySnapshot.aspx page documents search by USDOT number, MC/MX number, or company)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FMCSA "company safety records" SAFER company snapshot licensing insurance site:fmcsa.dot.gov" -> https://www.fmcsa.dot.gov/safety/company-safety-records (Company Safety Records | FMCSA)
- Backs: dot-intervention-insurance-defense
- Notes: Company Snapshot is free, no account needed, but it is a one-carrier-at-a-time query rather than a bulk download. The deeper Company Safety Profile (CSP) is gated: authorized company officials get it free via an FMCSA Portal account, everyone else mu

### src-04: PHMSA Hazardous Materials Special Permits Search and Lists
- URL: https://www.phmsa.dot.gov/approvals-and-permits/hazmat/special-permits-search (search tool) and https://www.phmsa.dot.gov/approvals-and-permits/hazmat/special-permits-list (lists); program overview at https://www.phmsa.dot.gov/approvals-and-permits/hazmat
- Verdict: verified-live | Access class: public-easy | Format: Web search UI (query by full or partial SP number, company name, or state) returning official signed permit documents as document copies (PDF), plus a lists page linking to the current base permit let
- Update frequency: Rolling: permits are granted, denied, and modified continuously with recurring Federal Register notices (applications and actions, e.g. a Notice of Actions published March 18, 2026); a PHMSA special p
- Freshness confirmed: Federal Register Notice of Actions on Special Permits published March 18, 2026 (doc 2026-05279, comments due April 17, 2026); January 16, 2026 notice of new applications; PHMSA page update reported Ma
- Entity key: DOT-SP number | documented: True (The search tool is documented as searchable by a full or partial SP number (the DOT-SP identifier), company name, or state)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "PHMSA hazardous materials special permits search DOT-SP number list" -> https://www.phmsa.dot.gov/approvals-and-permits/hazmat/special-permits-search (Hazardous Materials Special Permits Search | PHMSA)
- Backs: phmsa-special-permit-radar
- Notes: No login, key, or fee. Two flags: PHMSA states the Special Permits search tool is being upgraded to improve functionality (basic search unaffected), and the exact claimed URL path /hazmat/special-permits did not surface in results; the live deep link

### src-04: PHMSA Hazardous Materials Special Permits Search and Lists
- URL: https://www.phmsa.dot.gov/approvals-and-permits/hazmat/special-permits-search (companion lists page: https://www.phmsa.dot.gov/approvals-and-permits/hazmat/special-permits-list)
- Verdict: verified-live | Access class: public-hard-to-parse | Format: HTML search tool returning official signed permit documents (PDF copies of every current DOT-SP, plus several expired ones); separate Special Permits Lists page links to current base permit letters. N
- Update frequency: Rolling; PHMSA grants/denies continuously and publishes recurring Federal Register notices of actions (Jan 16, 2026 new applications; Mar 18, 2026 modifications; Apr 15, 2026 actions). No fixed refres
- Freshness confirmed: Program actively issuing in 2026: Federal Register notice of actions on special permits published April 15, 2026; new-applications notice January 16, 2026 listed 17 applications; current permit versio
- Entity key: DOT-SP number and grantee/party company name in the PHMSA special permits database | documented: True (The search accepts a full or partial SP number, company name, or state; results show Tracking Number and Company Name; grantee (Party To) letters are retrieved via the same search;)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "PHMSA hazardous materials special permits search phmsa.dot.gov" -> https://www.phmsa.dot.gov/approvals-and-permits/hazmat/special-permits-search (Hazardous Materials Special Permits Search | PHMSA)
- Backs: phmsa-special-permit-radar
- Notes: No login, API key, or fee found. Content is a search UI plus signed permit documents (PDF) rather than machine-readable bulk files; search results indicate searchable databases rather than direct Excel/CSV downloads. Page carries a notice that the se

### src-05: USCG Port State Information Exchange (PSIX)
- URL: https://cgmix.uscg.mil/psix/ (search at https://cgmix.uscg.mil/PSIX/PSIXSearch.aspx; SOAP API at https://cgmix.uscg.mil/xml/psixdata.asmx?WSDL)
- Verdict: verified-live | Access class: public-easy | Format: Web search UI plus free SOAP XML web services (PSIXData.asmx with published WSDL under cgmix.uscg.mil/xml) returning vessel datasets with vessel ID, name, VIN, HIN, call sign, status, service type, an
- Update frequency: Weekly; PSIX represents a weekly snapshot of FOIA MISLE data and the CGMIX site states its information is automatically updated on a weekly basis
- Freshness confirmed: Weekly MISLE snapshot cadence per USCG documentation; site and search pages indexed live in July 2026 searches with no outage or retirement reports found (most recent third party operational reference
- Entity key: IMO number / USCG VIN | documented: True (PSIX is documented as searchable by vessel name, documentation number or state registration number, call sign, IMO Number, and Hull Identification Number, matching the official sea)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "USCG PSIX Port State Information Exchange cgmix.uscg.mil vessel search" -> https://cgmix.uscg.mil/psix/ (USCG Port State Information Exchange Default Page)
- Backs: uscg-psc-prearrival-packet
- Notes: No login, key, or fee for either the web UI or the SOAP XML services. Notes: PII was removed from PSIX in 2018; the API is legacy SOAP/ASP.NET (not REST/JSON), so parsing effort is moderate; the entity key is mixed, with the USCG VIN/official number 

### src-06: USCG PSIX vessel search (MISLE inspection and deficiency records)
- URL: https://cgmix.uscg.mil/psix/psixsearch.aspx
- Verdict: verified-live | Access class: public-hard-to-parse | Format: Interactive ASP.NET web search (psixsearch.aspx) plus free public SOAP/XML web services at https://cgmix.uscg.mil/xml/default.aspx for vessel, deficiency, and marine casualty data. No bulk flat-file d
- Update frequency: Weekly. USCG documentation states CGMIX information is automatically updated on a weekly basis and PSIX represents a weekly snapshot of FOIA data compiled within the MISLE database.
- Freshness confirmed: Weekly MISLE snapshot per USCG PSIX help documentation; site and search page indexed live in July 2026 search results. No specific snapshot date visible in search snippets.
- Entity key: USCG Official Number | documented: True (Coast Guard documented vessels can be searched in PSIX by vessel name, Hull Identification Number, or Official Number, and results return the vessel Official Number as a core field)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "USCG PSIX Port State Information Exchange vessel search cgmix.uscg.mil" -> https://cgmix.uscg.mil/psix/psixsearch.aspx (USCG PSIX Vessel Search - cgmix - Coast Guard)
- Backs: subchapter-m-audit-tracker
- Notes: No login, key, or fee for the search UI or the XML web services. However there is no bulk download; programmatic use requires the SOAP/XML PSIX data service or scraping the .aspx UI. Owner PII (managing owner name/address) was removed from public acc

### src-08: ICIS-NPDES DMR and Limit datasets (ECHO Data Downloads) [TOP20]
- URL: https://echo.epa.gov/tools/data-downloads/icis-npdes-dmr-and-limit-data-set
- Verdict: verified-live | Access class: public-easy | Format: Zip-compressed CSV. DMRs: one zip per federal fiscal year since 2009, named npdes_dmrs_fyxxxx.zip containing npdes_dmr_fyxxxx.csv. Limits: national zip containing NPDES_LIMITS.csv, plus per-year and p
- Update frequency: Weekly. ECHO FAQ states ECHO data are generally updated weekly (exceptions such as SDWA data are quarterly); datasets are updated as part of the ECHO data refresh.
- Freshness confirmed: Weekly refresh confirmed from ECHO FAQ in current (2026) search results; DMR files published per fiscal year since 2009. Exact latest fiscal-year file name (fy2025/fy2026) was not visible in search sn
- Entity key: NPDES permit ID | documented: True (The DMR data element dictionary defines EXTERNAL_PERMIT_NMBR as the unique identifier for a permit, containing the formatted NPDES number; the same element appears in the Limit dat)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "ECHO data downloads ICIS-NPDES DMR and limit data set zip csv" -> https://echo.epa.gov/tools/data-downloads/icis-npdes-dmr-and-limit-data-set (ICIS-NPDES Permit Limit and Discharge Monitoring Report (DMR) Datasets | ECHO | )
- Backs: npdes-dmr-citizen-suit-radar
- Notes: Direct anonymous downloads from the ECHO Data Downloads page; no login, key, or fee. No sign in 2026 search results of retirement or a move behind registration; the page and its companion dictionary pages are all indexed live on echo.epa.gov.

### src-09: SMARTS Storm Water Data Public Access (California industrial stormwater monitoring) [TOP20]
- URL: https://smarts.waterboards.ca.gov/smarts/SwPublicUserMenu.xhtml
- Verdict: verified-live | Access class: public-hard-to-parse | Format: Interactive JSF (.xhtml) public web reports (NOI search, inspections, violations, enforcement, monitoring/parameter data) with on-screen results and Excel/CSV export from the UI; sampling results are 
- Update frequency: Public report data refreshed nightly per the Water Boards public reports page covering CIWQS and SMARTS data.
- Freshness confirmed: Nightly refresh of public report data per waterboards.ca.gov public reports page; SMARTS public menu and public NOI search pages indexed live in July 2026 search results.
- Entity key: California WDID number | documented: True (An NOI submitted through SMARTS generates the Waste Discharge Identification (WDID) number, which remains active until a Notice of Termination is filed; WDID is the identifier for )
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query ""smarts.waterboards.ca.gov" "SwPublicUserMenu" public data access" -> https://smarts.waterboards.ca.gov/smarts/SwPublicUserMenu.xhtml (Storm Water Data Public Access - SMARTS - CA.gov)
- Backs: ca-igp-era-autopilot
- Notes: No login, registration, or fee for the public user menu (registration is only for dischargers filing documents). The data lives behind an interactive JSF web app; extraction requires driving the report UI and its export functions rather than fetching

### src-10: e-Manifest public manifest data (RCRAInfo)
- URL: https://www.epa.gov/e-manifest
- Verdict: verified-live | Access class: public-easy | Format: Weekly zip exports in CSV and fixed-width formats from https://rcrapublic.epa.gov/rcra-public-export/?outputType=CSV, comprising eight tables: EM_MANIFEST.zip, EM_WASTE_LINE.zip, EM_TRANSPORTER.zip, E
- Update frequency: Refreshed and published weekly; each manifest becomes public 90 days after it is received at the receiving facility.
- Freshness confirmed: Weekly publication cadence with a 90-day public release delay per RCRAInfo web data instructions; pages and export portal indexed live in July 2026 search results.
- Entity key: EPA RCRA Handler ID | documented: True (The e-Manifest module data element dictionary documents fields by table; ID_NUMBER is the unique RCRA identification number assigned by the implementing state or EPA region to each)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "EPA e-Manifest public manifest data download RCRAInfo" -> https://rcrainfo.atlassian.net/wiki/spaces/RUI/pages/2845016067/RCRAInfo+Web+Data+Instructions:+e-Manifest (RCRAInfo Web Data Instructions: e-Manifest - RCRAInfo Information Library)
- Backs: emanifest-tsdf-market-intel
- Notes: Bulk export files are anonymous, free downloads (no key or registration). Registration (RCRAInfo/e-Manifest accounts) is only needed for submitting manifests, not for reading public data. Note the structural 90-day publication lag on manifest records

### src-11: RCRAInfo handler, evaluation, violation, and enforcement extracts (ECHO)
- URL: https://echo.epa.gov/tools/data-downloads
- Verdict: verified-live | Access class: public-easy | Format: Zip archives of CSV files. The RCRAInfo download comprises six CSV files (handlers from the Handler Reporting Universe plus evaluation, violation, and enforcement data elements), documented at https:/
- Update frequency: Weekly. ECHO FAQ states ECHO data are generally updated weekly as part of the ECHO data refresh (SDWA is the stated quarterly exception).
- Freshness confirmed: Current through late June 2026: data.gov catalog metadata for the ECHO facilities dataset shows last update 2026-06-29, consistent with the weekly refresh cycle.
- Entity key: EPA RCRA Handler ID | documented: True (The data element dictionary defines ID_NUMBER as the unique RCRA identification number assigned by the implementing state or EPA region to each RCRA site, 4 to 12 characters with a)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "echo.epa.gov data downloads RCRAInfo download summary zip" -> https://echo.epa.gov/tools/data-downloads/rcrainfo-download-summary (RCRAInfo Download Summary and Data Element Dictionary | ECHO | US EPA)
- Backs: rcra-inspection-readiness-packet
- Notes: Direct anonymous zip downloads from echo.epa.gov, no login, API key, or fee. The RCRAInfo-specific summary and dictionary page is https://echo.epa.gov/tools/data-downloads/rcrainfo-download-summary. A July 2026 search for retirement, removal, or acce

### src-12: SDWA/SDWIS dataset (ECHO Data Downloads) [TOP20]
- URL: https://echo.epa.gov/tools/data-downloads/sdwa-download-summary
- Verdict: verified-live | Access class: public-easy | Format: SDWA_latest_downloads.zip, a compressed zip containing multiple CSV files (one data table per file), including SDWA_PUB_WATER_SYSTEMS.csv plus companion tables for violations, site visits, and enforce
- Update frequency: Quarterly. Primacy agencies submit SDWIS data to EPA quarterly; ECHO FAQ states SDWA data are updated quarterly, and each calendar quarter becomes available after the following quarter's three-month v
- Freshness confirmed: ECHO datasets confirmed current through late June 2026 (data.gov metadata 2026-06-29); SDWA content follows the quarterly cycle with a three-month verification lag; the exact latest SDWA quarter was n
- Entity key: PWSID | documented: True (In SDWA_PUB_WATER_SYSTEMS.csv each row is uniquely identified by the key fields SUBMISSIONYEARQUARTER and PWSID, and the same key values identify site visits, violations, and other)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "echo.epa.gov "sdwa-download-summary" PWSID quarterly" -> https://echo.epa.gov/tools/data-downloads/sdwa-download-summary (SDWA Data Download Summary and Data Element Dictionary | ECHO | US EPA)
- Backs: pwsid-contract-operator-copilot
- Notes: Direct anonymous zip download, no login, API key, or fee. Note the effective data lag: each quarter is held for a three-month verification period before release, so the newest records are roughly one to two quarters behind real time.

### src-13: EPA SDWIS Federal Reports: Service Line Inventory (per-PWSID lead service lines)
- URL: https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/sdwis_fed_reports_public/service-line-inventory
- Verdict: verified-live | Access class: public-hard-to-parse | Format: Interactive web report inside the SDWIS Federal Reporting Services application (Oracle APEX/ORDS app SDWIS_FED_REPORTS_PUBLIC) that queries the SDWIS Fed Data Warehouse via report filters. It is a que
- Update frequency: SDWIS Fed Data Warehouse dataset files are refreshed quarterly, with roughly a three-month lag; under LCRR/LCRI water systems must update their service line inventories annually after the initial subm
- Freshness confirmed: EPA released the first national utility-reported service line inventory dataset in November 2025, covering 56,982 systems (about 1.97M lead and 0.97M galvanized-requiring-replacement lines and 23.5M u
- Entity key: PWSID | documented: True (EPA publishes a data dictionary for SDWIS Federal Reporting Services documenting its fields; PWSID (two-letter state or region code plus seven digits) is the water system identifie)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "sdwis.epa.gov sfdw_pub service line inventory federal reports" -> https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/sdwis_fed_reports_public/service-line-inventory (Service Line Inventory)
- Backs: srf-lsl-pipeline-scout
- Notes: Public with no login, API key, or fee, but data is served through an interactive APEX reporting app rather than downloadable flat files, so programmatic use requires driving the app or scripting exports. Related bulk alternatives exist (ECHO SDWA zip

### src-14: CalRecycle Landfill Tonnage Reports (Disposal Reporting System / RDRS)
- URL: https://www2.calrecycle.ca.gov/LandfillTipFees/
- Verdict: verified-live | Access class: public-hard-to-parse | Format: Form-driven web report generator titled Landfill Tonnage Reports; generates HTML tables of quarterly landfilled tonnage sortable by county or by facility. No bulk download file (csv/xlsx/zip) was conf
- Update frequency: Quarterly: each permitted California disposal facility operator reports and pays the integrated waste management (IWM) fee per ton landfilled on a quarterly basis, and the reports are published by qua
- Freshness confirmed: Quarter 4, 2025 is the most recent period confirmed in search results (page states reports available from Quarter 1, 1990 through Quarter 4, 2025).
- Entity key: SWIS facility number | documented: True (The page states that reports can be sorted by county or by facility and that facility names and numbers are as entered in CalRecycle's Solid Waste Information System (SWIS), confir)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "CalRecycle landfill tonnage reports SWIS facility number disposal" -> https://www2.calrecycle.ca.gov/LandfillTipFees/ (Landfill Tonnage Reports - CalRecycle - CA.gov)
- Backs: landfill-tonnage-benchmark
- Notes: Public, no login or fee, but output is generated HTML tables from an on-page form, so programmatic use requires scraping. Provenance caveat: this page's tonnage comes from operators' IWM fee reporting, not from the Disposal Reporting System/RDRS name

### src-15: DOB ECB Violations [TOP20]
- URL: https://data.cityofnewyork.us/Housing-Development/DOB-ECB-Violations/6bgk-3dad
- Verdict: verified-live | Access class: public-easy | Format: Socrata dataset on NYC Open Data: CSV, JSON, RDF, and XML exports, OData connection for Excel/Tableau, and SODA API; also mirrored on data.ny.gov and cataloged on data.gov.
- Update frequency: Daily per third-party consumers of the feed (DOBGuard: powered by NYC Open Data and updated daily; RegWatch: DOB datasets typically update daily); dataset-level update observed June 26, 2026 and data.
- Freshness confirmed: Updates observed June 2026: search results cite dataset last updated June 26, 2026; data.gov catalog record last updated/checked June 2, 2026.
- Entity key: NYC BBL / BIN (plus OATH summons number) | documented: True (Dataset columns include BIN, BORO, BLOCK, LOT (the BBL components), plus violation, respondent, and penalty fields; the nycdb wiki (https://github.com/nycdb/nycdb/wiki/Dataset:-ECB)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "DOB ECB Violations NYC Open Data 6bgk-3dad dataset" -> https://data.cityofnewyork.us/Housing-Development/DOB-ECB-Violations/6bgk-3dad (DOB ECB Violations - NYC Open Data)
- Backs: oath-ecb-summons-defense-packet
- Notes: No login wall, key requirement, or fee found; standard Socrata exports and API plus OData; federally cataloged on data.gov.

### src-16: NYC Building Energy and Water Data Disclosure for Local Law 84 (2023 to present) [TOP20]
- URL: https://data.cityofnewyork.us/Environment/NYC-Building-Energy-and-Water-Data-Disclosure-for-/5zyy-y8am
- Verdict: verified-live | Access class: public-easy | Format: Socrata dataset with 265 columns (per Open Data Network profile); CSV, JSON, XML, RDF exports and SODA API; data.gov catalog mirrors JSON/RDF resources. Current title: NYC Building Energy and Water Da
- Update frequency: Annual cycle: LL84 requires owners of covered buildings to benchmark each calendar year via EPA Portfolio Manager with a May 1 filing deadline (CY2025 data due May 1, 2026; CY2024 deadline was extende
- Freshness confirmed: Dataset covers calendar year 2022 to present; CY2024 filings were complete by the extended June 30, 2025 deadline (with LL97 filers allowed until August 29, 2025), and CY2025 filings were due May 1, 2
- Entity key: NYC BBL (LL84 rows carry BBL and BIN) | documented: True (The dataset description states each property is identified by its EPA-assigned property ID and can contain one or more tax lots identified by one or more BBLs (Borough, Block, Lot))
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "NYC Building Energy and Water Data Disclosure Local Law 84 5zyy-y8am" -> https://data.cityofnewyork.us/Environment/NYC-Building-Energy-and-Water-Data-Disclosure-for-/5zyy-y8am (NYC Building Energy and Water Data Disclosure for Local Law 84 2023 to Present ()
- Backs: ll97-penalty-exposure-beam-prep
- Notes: No login, key, or fee found; standard NYC Open Data exports and API, cataloged on data.gov. Note the multi-BBL/multi-BIN cardinality per EPA property ID, which complicates entity resolution but is documented behavior.

### src-17: DOB NOW: Safety - Facades Compliance Filings [TOP20]
- URL: https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Safety-Facades-Compliance-Filings/xubg-57si
- Verdict: verified-live | Access class: public-easy | Format: Socrata dataset of all facades (FISP/Local Law 11) compliance filings submitted in DOB NOW; direct CSV endpoint (data.cityofnewyork.us/api/views/xubg-57si/rows.csv) confirmed in search results; data.g
- Update frequency: Publisher cadence text not captured in search snippets; DOB states all DOB NOW data is published to NYC Open Data as structured datasets that external systems can query in real time, and the data.gov 
- Freshness confirmed: data.gov catalog record shows the dataset updated May 10, 2026; FISP filings are ongoing under the current five-year cycle (Cycle 10 per industry guidance), with nearly 16,000 buildings over six stori
- Entity key: NYC BIN (and BBL) | documented: True (Dataset xubg-57si contains records with fields including BIN (the unique seven-digit building identifier DOB assigns to every NYC building) along with property information, filing )
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "DOB NOW Safety Facades Compliance Filings xubg-57si NYC Open Data" -> https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Safety-Facades-Compliance-Filings/xubg-57si/data (DOB NOW: Safety - Facades Compliance Filings | NYC Open Data)
- Backs: fisp-cycle10-deadline-radar
- Notes: No login, key, or fee found; open CSV download endpoint and standard Socrata API; also mirrored on the Socrata domain and cataloged on data.gov.

### src-18: DOB NOW: Build - Job Application Filings
- URL: https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Build-Job-Application-Filings/w9ak-ipjd
- Verdict: verified-live | Access class: public-easy | Format: Socrata dataset of most job filings filed in DOB NOW (electrical, elevator, and LAA jobs are published in separate datasets); direct CSV endpoint (data.cityofnewyork.us/api/views/w9ak-ipjd/rows.csv) p
- Update frequency: Daily: search results for w9ak-ipjd state the dataset is updated daily with new records and that each existing record is updated as the application moves through the approval process to reflect latest
- Freshness confirmed: Daily-updated feed per dataset description surfaced in search results; live CSV/API endpoints and third-party live consumers (e.g. the isometric-permits GitHub project describing a live NYC DOB permit
- Entity key: NYC BIN / BBL / DOB job filing number | documented: True (Job Filing Number is a field within this dataset tracking individual job applications submitted through DOB NOW; a prior schema search (query: DOB NOW Build Job Application Filings)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "DOB NOW Build Job Application Filings w9ak-ipjd NYC Open Data" -> https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Build-Job-Application-Filings/w9ak-ipjd (DOB NOW: Build - Job Application Filings | NYC Open Data)
- Backs: dob-plan-exam-objection-intel
- Notes: No login, key, or fee found; open CSV download endpoint, standard Socrata API (Socrata is now Tyler Technologies Data and Insights), data.gov catalog listing, and data.ny.gov federation.

### src-20: OSHA Establishment Specific Injury and Illness Data (Injury Tracking Application)
- URL: https://www.osha.gov/Establishment-Specific-Injury-and-Illness-Data
- Verdict: verified-live | Access class: public-easy | Format: CSV downloads of ITA Summary (Form 300A establishment plus summary) data and Case Detail (Forms 300/301) data from OSHA's ITA data website, with published PDF data dictionaries for both file types.
- Update frequency: Annual collection and publication cycle: establishments submit each calendar year's data January 1 to March 2 of the following year, and OSHA posts the resulting establishment-level files; the current
- Freshness confirmed: CY2025 work-related injury and illness data (submitted 1/1/2026 through 3/15/2026) is the current downloadable vintage as of 2026-07-04.
- Entity key: Establishment record keyed by establishment_name plus street address and state (documented fields in the ITA data dictionaries); company_name also present | documented: True (The ITA data dictionary defines establishment_name (name of the establishment reporting data), the street address of the establishment, and the state where the establishment is loc)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "OSHA Establishment Specific Injury and Illness Data Injury Tracking Application download" -> https://www.osha.gov/Establishment-Specific-Injury-and-Illness-Data (Establishment Specific Injury and Illness Data (Injury Tracking Application) | O)
- Backs: ita-sub-safety-prequal-scorecard, osha-ita-prequal-benchmark-packet
- Notes: Published establishment-level data is free to view and download with no login. Login (ITA account) is only required for employers submitting data, not for consuming the published files. OSHA notes it makes most, not all, submitted ITA data available 

### src-21: Building Violations (City of Chicago) [TOP20]
- URL: https://data.cityofchicago.org/Buildings/Building-Violations/22u3-xenr
- Verdict: verified-live | Access class: public-easy | Format: Socrata dataset: no-login CSV export (rows.csv?accessType=DOWNLOAD endpoint confirmed in search results) plus SODA API (Socrata API Foundry page exists for 22u3-xenr).
- Update frequency: Daily. catalog.data.gov entry for this dataset reports daily updates (metadata last checked April 27, 2026), and in the last 90 days 67 percent of violations were posted within two days of the inspect
- Freshness confirmed: Violations from 2006 to present, refreshed daily; data.gov metadata check dated April 27, 2026.
- Entity key: address (documented column) plus id (violation record ID) and inspection_number are documented columns. The DOAH case/docket component of the claimed key is NOT a column of this dataset; docket-bearing DOAH cases live in the separate Ordinance Violations - Buildings dataset (awqx-tuwv). | documented: False (Live portal query enumerates the dataset columns: id, violation_last_modified_date, violation_date, violation_code, violation_status, violation_status_date, violation_description, )
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "Chicago data portal "Building Violations" 22u3-xenr dataset" -> https://data.cityofchicago.org/Buildings/Building-Violations/22u3-xenr (Building Violations | City of Chicago | Data Portal)
- Backs: chicago-building-court-prep-packet
- Notes: Open Socrata portal, no login or key required for CSV export; optional app token for higher API rate limits. Dataset disclaimer says data are historical in nature and should not be relied on for real estate transactions.

### src-22: LL87 Energy Audit Data
- URL: https://data.cityofnewyork.us/Environment/LL87-Energy-Audit-Data/au6c-jqvf
- Verdict: verified-live | Access class: public-easy | Format: Socrata dataset on NYC Open Data (standard portal CSV export and SODA API); very wide table of roughly 2,000 fields collected via the US DOE Asset Score Audit Template tool, with a Column Information 
- Update frequency: Not explicitly stated in search receipts. Underlying compliance is a 10-year cycle per building with an annual due-year cohort (EER due by December 31 of the matching year), and the portal dataset cur
- Freshness confirmed: Current dataset covers Local Law 87 energy audits from 2019 through 2024 (the 2012-2018 audits sit in the predecessor dataset).
- Entity key: BBL (Borough-Block-Lot), the 10-digit NYC Department of Finance property identifier; due year derives from the last digit of the tax block number per the LL87 compliance rule | documented: True (The dataset documentation describes the Borough, Block, Lot Number (BBL) as a 10-digit identifier assigned by the NYC Department of Finance for each property (borough code followed)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query ""LL87 Energy Audit Data" data.cityofnewyork.us au6c-jqvf" -> https://data.cityofnewyork.us/Environment/LL87-Energy-Audit-Data/au6c-jqvf (LL87 Energy Audit Data | NYC Open Data)
- Backs: ll87-energy-audit-radar
- Notes: Open NYC Open Data (Socrata) dataset, no login or fee. Schema-churn flag: with the move to the Audit Template tool, field definitions and column names were expanded and standardized versus the previous 2012-2018 dataset, growing from about 1,000 to a

### src-23: CMS Part C and D Plan Crosswalk files [TOP20]
- URL: https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data/plan-crosswalks
- Verdict: verified-live | Access class: public-easy | Format: Annual downloadable crosswalk files posted on per-plan-year child pages (2024, 2025, and 2026 Part C&D Plan Crosswalk pages all confirmed live; older vintages back to at least 2014 and 2017 exist unde
- Update frequency: Annual: one crosswalk per plan year, published ahead of the plan year (the 2026 crosswalk is already posted as of July 2026). The parent MA/Part D Contract and Enrollment Data section separately publi
- Freshness confirmed: Plan year 2026 crosswalk published and live as of 2026-07-04; 2025 and 2024 vintages also live.
- Entity key: Contract ID plus Plan ID (H/S contract number plus PBP, e.g. H5216-032), mapping prior-year to current-year plan combinations with renewal/consolidation/termination status. County FIPS was NOT confirmed as a field of the crosswalk file itself; state/county detail lives in the companion Landscape file and the Monthly Enrollment by Contract/Plan/State/County series. | documented: False (The crosswalk file provides all Contract and Plan combinations from the 2025 plan year and indicates whether plans are renewing, renewing with service area consolidation, expanding)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "CMS "plan crosswalks" Medicare Advantage Part D contract and enrollment data" -> https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data/plan-crosswalks (Plan Crosswalks | CMS)
- Backs: ma-agency-plan-exit-retention-packet
- Notes: Public CMS statistics pages, no login, key, or fee. Conflation warning: cms.gov also hosts a similarly named Plan ID Crosswalk Public Use File data dictionary (plan-id-crosswalk-datadictionary-py26.pdf) which belongs to the Marketplace/QHP (HIOS plan

### src-24: CMS Monthly Enrollment by Contract/Plan/State/County (CPSC)
- URL: https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data/monthly-enrollment-contract/plan/state/county
- Verdict: verified-live | Access class: public-easy | Format: One CMS page per month (e.g. Monthly Enrollment by CPSC 2026 03) with a zip download; the zip contains CPSC_Enrollment_Info_yyyy_mm.csv plus a companion contract info CSV that merge on contract and pl
- Update frequency: Monthly; new month pages posted on an ongoing cadence (item pages confirmed for 2025-05, 2026-01, 2026-03)
- Freshness confirmed: Monthly Enrollment by CPSC 2026 03 (March 2026) page confirmed in search results; search summary also reported Jan and Feb 2026 files published in mid-February 2026. May/June 2026 pages did not surfac
- Entity key: County FIPS and CMS contract/plan ID (H number) | documented: True (Search results for the CPSC files confirm FIPS state county codes are used in these files (first 2 digits state, last 3 county) alongside contract numbers that begin with H followe)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "CMS "Monthly Enrollment by Contract/Plan/State/County" Medicare Advantage enrollment data" -> https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data/monthly-enrollment-contract/plan/state/county (Monthly Enrollment by Contract/Plan/State/County | CMS)
- Backs: fmo-county-market-share-intel
- Notes: Direct zip downloads from cms.gov, no login, key, or fee seen in any search result. Parsing caveat: county-plan combinations with fewer than 11 enrollees are excluded/suppressed, so small cells are missing by design

### src-25: Payroll Based Journal Daily Nurse Staffing PUF [TOP20]
- URL: https://data.cms.gov/quality-of-care/payroll-based-journal-daily-nurse-staffing
- Verdict: verified-live | Access class: public-easy | Format: Quarterly public use file on data.cms.gov with an interactive data view, CSV download, and API access; rows are per facility per day with paid hours by staff category plus MDS-based daily census
- Update frequency: Quarterly (dataset described as submitted by nursing homes on a quarterly basis; PBJ PUF posted since November 1, 2017; PBJ 4.10.0 submission specs issued for the April 1, 2026 release)
- Freshness confirmed: CY2025 Q2 PBJ staffing data confirmed published and analyzed (LTCCC national averages for Q2 2025: 3.78 total nurse HPRD, 0.62 RN HPRD). PBJ publishes with a lag of roughly two quarters, so newer quar
- Entity key: CMS CCN | documented: True (CMS publishes an official data dictionary for this dataset; search results confirm PROVNUM is the facility identifier field and corresponds to the CMS Certification Number, with PB)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "data.cms.gov "Payroll-Based Journal Daily Nurse Staffing" dataset quarterly" -> https://data.cms.gov/quality-of-care/payroll-based-journal-daily-nurse-staffing (Payroll Based Journal Daily Nurse Staffing)
- Backs: snf-pbj-fivestar-guardrail
- Notes: Open CSV download and public API on data.cms.gov; no login, key, or fee surfaced in search results. Page rendering needs JavaScript but the underlying files and API are open

### src-26: Health Deficiencies dataset (Nursing Home Care Compare) [TOP20]
- URL: https://data.cms.gov/provider-data/dataset/r5ix-sfxw
- Verdict: verified-live | Access class: public-easy | Format: Provider Data Catalog dataset, one deficiency per row (facility, inspection date, deficiency tag, scope and severity, status, correction date); documented as the NH_HealthCitations file in the NH data
- Update frequency: Roughly monthly PDC nursing home refresh (June 2026 cycle: last modified June 1, 2026, released June 24, 2026, next planned update July 29, 2026)
- Freshness confirmed: Nursing home PDC data released June 24, 2026 (next planned update July 29, 2026); citations cover the last three years of inspections; third parties (LTCCC) published analyses of this citations data i
- Entity key: CMS CCN | documented: True (The official NH data dictionary documents the Health Deficiencies file (NH_HealthCitations) and states the data uses CMS Certification Number (CCN) as the nursing home identifier)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "data.cms.gov provider-data dataset r5ix-sfxw "Health Deficiencies"" -> https://data.cms.gov/provider-data/dataset/r5ix-sfxw (Health Deficiencies | Provider Data Catalog)
- Backs: snf-2567-poc-idr-copilot
- Notes: Open download from the Provider Data Catalog, no login or key reported in any search result; legacy data.medicare.gov URL for the same r5ix-sfxw id still resolves

### src-27: Provider Data Catalog: Home health services datasets
- URL: https://data.cms.gov/provider-data/topics/home-health-services
- Verdict: verified-live | Access class: public-easy | Format: PDC topic page holding all 9 home health datasets (agency, state, and national level, e.g. Home Health Care Agencies 6jpm-sxkc and Home Health Care National Data 97z8-de96), a download-all link for cu
- Update frequency: Quarterly refresh of home health quality data on Care Compare and the PDC (October 2025 refresh live; next refresh January 2026 per the HH QRP Spotlight page)
- Freshness confirmed: October 2025 quarterly refresh confirmed live on the PDC; January 2026 refresh announced (HHVBP measure reporting resumed with that refresh); the companion HHA Enrollments dataset on data.cms.gov show
- Entity key: CMS CCN | documented: True (CMS publishes an official home health data dictionary for the PDC datasets; search results confirm CCN appears in provider datasets as the CMS Certification Number field, and a leg)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "data.cms.gov provider data catalog "home health services" datasets" -> https://data.cms.gov/provider-data/topics/home-health-services (Home health services - Provider Data Catalog)
- Backs: hha-hhvbp-payment-risk-benchmark
- Notes: Open downloads from the Provider Data Catalog with no login, key, or fee reported; topic page includes download-all plus data dictionary links

### src-28: Search Texas Child Care (CCR public records)
- URL: https://childcare.hhs.texas.gov/ (search UI at https://childcare.hhs.texas.gov/Public/childcaresearch)
- Verdict: verified-live | Access class: public-hard-to-parse | Format: Interactive HTML search portal only, no bulk file download on the site: a newer search UI at /Public/childcaresearch plus legacy ASP pages (ppfacilitysearchdaycare.asp, ppFacilitySearchResults.asp, pp
- Update frequency: Portal reflects current HHSC Child Care Regulation licensing and inspection records and is actively maintained; the companion data.texas.gov CCL operations dataset showed data current as of May 7, 202
- Freshness confirmed: Portal live and actively promoted by Texas HHSC; official user guide last updated January 14, 2025 per FINDconnect; companion bc5r-88dy operations data confirmed current as of May 7, 2026
- Entity key: State childcare license/operation number (Texas HHSC operation ID) | documented: True (The HHSC CCL operations dataset documents OPERATION_NUMBER and OPERATION_NAME fields, with the Operation ID described as the unique key tying the child care licensing datasets toge)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query ""childcare.hhs.texas.gov" Search Texas Child Care operation number" -> https://childcare.hhs.texas.gov/Public/childcaresearch (Search Texas Child Care - Texas.gov)
- Backs: childcare-portfolio-license-monitor
- Notes: No login, key, or fee: fully public search portal. But records are only served as per-operation HTML search results and detail pages, so programmatic use requires scraping; the bulk alternative keyed by the same operation number is public-easy via th

### src-29: California CDSS Community Care Facility Search
- URL: https://www.ccld.dss.ca.gov/carefacilitysearch/
- Verdict: verified-live | Access class: public-easy | Format: Live web search UI (transparency website) with per-facility detail pages; facility reports downloadable into Excel from the transparency site; companion bulk CSV dataset 'Community Care Licensing Faci
- Update frequency: Transparency search serves current licensing records; CHHS open data companion resources updated periodically (observed: Child Care Centers CSV last updated 2025-05-27; Family Child Care Homes resourc
- Freshness confirmed: Transparency search reflects current license records; CHHS portal shows resource activity into 2026 (Family Child Care Homes resource metadata updated 2026-02-12) with Child Care Centers CSV last upda
- Entity key: California CDSS facility number (state facility license number) | documented: True (Indexed facility detail URL on the state site is keyed by a 9 digit facility number (example 107209020) and the search form exposes a facnum query parameter, showing facility numbe)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "California CDSS Community Care Facility Search ccld.dss.ca.gov carefacilitysearch" -> https://www.ccld.dss.ca.gov/carefacilitysearch/ (Social Services - Community Care Facility search)
- Backs: assisted-living-survey-readiness-benchmark
- Notes: No login, key, or fee for the search UI, the Excel facility report downloads, or the CHHS open data CSVs. The search UI itself is a per-facility lookup app and is not bulk friendly; use the CHHS portal CSVs as the machine readable backbone. CCLD also

### src-30: Texas Rising Star Certification Guidelines (TWC) plus Search Texas Child Care CCR records
- URL: https://www.twc.texas.gov/sites/default/files/wf/docs/texas-rising-star-certification-guidelines-twc.pdf
- Verdict: verified-live | Access class: public-easy | Format: Guidelines: PDF at the claimed TWC URL (current edition dated February 2026; an October 2025 edition also mirrored on childcare.texas.gov). CCR records: live web search UI at childcare.hhs.texas.gov (
- Update frequency: Guidelines PDF revised periodically (October 2025 then February 2026 editions observed in results). HHSC CCR publishes Day Care Operations Weekly Status Changes and Monthly Status Changes reports; the
- Freshness confirmed: February 2026 guidelines edition live at the claimed URL; live inspection and compliance history pages addressable by operationId (examples operationId=136975 and 101386 indexed); HHSC weekly and mont
- Entity key: Texas HHSC operation number plus TRS certification level | documented: True (The HHSC CCL Daycare and Residential Operations dataset describes Operation ID as the unique key that ties to other Child Care Licensing data sets; a Socrata API foundry page exist)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "Texas Rising Star certification guidelines TWC pdf twc.texas.gov" -> https://www.twc.texas.gov/sites/default/files/wf/docs/texas-rising-star-certification-guidelines-twc.pdf (Texas Rising Star Certification Guidelines, February 2026 1)
- Backs: tx-rising-star-level-defense
- Notes: PDF, Search Texas Child Care UI, and the Texas Open Data Portal dataset are all public with no fee or login (Socrata app token optional). Caveat: the operation number lives in HHSC CCR systems while TRS certification level is administered by TWC and 

### src-31: FDA Data Dashboard (Inspections, Citations, Compliance Actions)
- URL: https://datadashboard.fda.gov/oii/cd/inspections.htm
- Verdict: verified-live | Access class: public-easy (dashboard UI and xlsx export); public-registration (JSON API requires free Authorization-User and Authorization-Key credentials) | Format: Interactive dashboard with xlsx export of inspections results; JSON REST API at api-datadashboard.fda.gov/v1 (endpoints include inspections_classifications and inspections_citations) with published fi
- Update frequency: Weekly; inspectional and compliance data refreshed weekly and include only final actions
- Freshness confirmed: FDA states the datasets are updated weekly and include only final actions; no specific latest-data date visible in search results as of 2026-07-04
- Entity key: FDA FEI (FDA Establishment Identifier); DUNS as secondary | documented: True (Published API field definitions list FEINumber (with InspectionID and CitationID) as numeric fields, and the dashboard results table links FEI Number to firm details, documenting F)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FDA Data Dashboard inspections datadashboard.fda.gov compliance actions citations" -> https://datadashboard.fda.gov/oii/cd/inspections.htm (FDA Dashboards - Inspections)
- Backs: fei-supplier-gmp-surveillance
- Notes: Dashboard browsing and xlsx download need no login. The Data Dashboard API requires credentials requested through the OII Unified Logon application; the FDA generated Authorization-Key and Authorization-User must be passed in request headers. No fee 

### src-32: openFDA Device Adverse Event endpoint (MAUDE)
- URL: https://open.fda.gov/apis/device/event/
- Verdict: verified-live | Access class: public-easy | Format: JSON REST API (Elasticsearch based) serving MAUDE device adverse event reports; documented searchable fields page plus downloadable field reference PDF (open.fda.gov/fields/deviceevent_reference.pdf);
- Update frequency: Weekly (endpoint overview states the data is updated weekly)
- Freshness confirmed: Coverage approximately 1992 to present, updated weekly, per the endpoint overview page
- Entity key: FDA product code plus 510(k)/PMA number; manufacturer FEI as secondary | documented: True (openFDA publishes a dedicated searchable fields page and field reference PDF for the device event endpoint; this page was the top result for a query on the field device.device_repo)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "openFDA device adverse event API open.fda.gov apis device event MAUDE" -> https://open.fda.gov/apis/device/event/ (Device Adverse Event Overview)
- Backs: maude-pms-signal-packet
- Notes: openFDA is free and does not require authentication; an optional API key (open.fda.gov/apis/authentication/) raises rate limits. Caveat on the secondary key: search results surfaced manufacturer name/address fields (device.manufacturer_d_name, device

### src-33: FDA Downloadable 510(k) Files / openFDA device 510(k) endpoint
- URL: https://www.fda.gov/medical-devices/510k-clearances/downloadable-510k-files
- Verdict: verified-live | Access class: public-easy | Format: Fixed width text inside zip files: PMN96CUR.ZIP (1996 to current), PMN9195.ZIP, PMN8690.ZIP, PMN8185.ZIP, PMN7680.ZIP, each record 272 characters, layout documented on the File Layout for Releasable 5
- Update frequency: Monthly; the files are replaced monthly, usually on the 5th of each month
- Freshness confirmed: PMN96CUR.ZIP spans 1996 to current and is replaced monthly, usually on the 5th of each month, so data is current to within about one month as of 2026-07-04
- Entity key: 510(k) K number and FDA product code | documented: True (FDA publishes a file layout page for the releasable 510(k) files whose documented record content includes 510(k) Number and Product Code alongside Device Name, Applicant, Decision )
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FDA downloadable 510(k) files fda.gov medical devices monthly zip pmn96cur" -> https://www.fda.gov/medical-devices/510k-clearances/downloadable-510k-files (Downloadable 510(k) Files | FDA)
- Backs: 510k-predicate-landscape-package
- Notes: No login, key, or fee for the zip downloads; the fixed width 272 character format needs a layout aware parser (layout is published). The openFDA 510(k) endpoint is free JSON with optional API key, and offers zipped JSON bulk downloads in the same sha

### src-35: openFDA Drug Shortages endpoint
- URL: https://open.fda.gov/apis/drug/drugshortages/
- Verdict: verified-live | Access class: public-easy | Format: JSON REST API at https://api.fda.gov/drug/shortages.json (max 100 records per call) plus bulk zipped JSON downloads via the endpoint download page
- Update frequency: Underlying FDA drug shortage list is updated daily with new and resolved shortages; openFDA notes updates can change old records so the full download set must be refreshed
- Freshness confirmed: Daily updates confirmed by FDA (drug shortage list updated daily); third-party trackers built on it show current 2026 shortage data
- Entity key: NDC (11-digit), crosswalked to labeler and manufacturing site | documented: True (package_ndc is a documented searchable field of the drugshortages endpoint, alongside generic_name, proprietary_name, company_name, presentation, status, update_date, shortage_reas)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "openFDA drug shortages API endpoint drugshortages" -> https://open.fda.gov/apis/drug/drugshortages/ (Drug Shortages Overview (openFDA))
- Backs: ndc-formulary-shortage-exposure
- Notes: No API key required; free registration for an API key only raises rate limits. Bulk zipped JSON download available with no login.

### src-36: ClinicalTrials.gov API v2
- URL: https://clinicaltrials.gov/data-api/api
- Verdict: verified-live | Access class: public-easy | Format: REST API v2.0 described with an OpenAPI 3.0 specification; JSON responses with token-based pagination (nextPageToken); bulk study record downloads also documented on the data-api pages
- Update frequency: Registry adds and updates study records daily (updates run between 4AM and 8AM EST)
- Freshness confirmed: Daily update cadence confirmed; NLM reported more than 500,000 registered studies as of August 2024 and the v2 API has been the production API since its 2024 launch
- Entity key: NCT number; sponsor/responsible-party organization name | documented: True (In the v2 study schema the NCT number is the documented field protocolSection.identificationModule.nctId and the sponsor organization is protocolSection.sponsorCollaboratorsModule.)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "ClinicalTrials.gov API v2 data-api REST documentation" -> https://clinicaltrials.gov/data-api/api (ClinicalTrials.gov API)
- Backs: ctgov-fdaaa-results-compliance
- Notes: No API key, no authentication, no signup; generous rate limits. API v1 was retired and v2 is the current supported interface (migration page at clinicaltrials.gov/data-api/about-api/api-migration).

### src-37: CMS Provider of Services File: Clinical Laboratories (CLIA)
- URL: https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file-clinical-laboratories
- Verdict: verified-live | Access class: public-easy | Format: data.cms.gov dataset with browser download and data.cms.gov API access; separate downloadable Data Dictionary and a Methodology page are published alongside the data
- Update frequency: Updated 4 times a year (quarterly); records refresh each time a provider is recertified; extract is created from the QIES certification database
- Freshness confirmed: Dataset page last modified April 13, 2026; currently reports 302.3k active or certified providers; quarterly cadence
- Entity key: CLIA number (10 characters); crosswalks to CMS CCN and NPI | documented: True (The dataset description documents the provider number (CMS Certification Number) as the lab identifier along with name, address and testing-service characteristics, and the page sh)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "data.cms.gov "Provider of Services File" "Clinical Laboratories" CLIA quarterly" -> https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file-clinical-laboratories (Provider of Services File: Clinical Laboratories Data | CMS Data)
- Backs: clia-portfolio-compliance-calendar
- Notes: Free public download and API on data.cms.gov, no registration or key. The POS file is split into an OTHER facilities file and a CLIA laboratories file. NPI crosswalk requires an outside source (third-party CLIA-NPI lookups exist), so treat the NPI le

### src-38: FDA Import Alerts (per-alert firm lists)
- URL: https://www.fda.gov/industry/actions-enforcement/import-alerts
- Verdict: verified-live | Access class: public-hard-to-parse | Format: HTML only: fda.gov landing and search pages, with the per-alert firm lists served as individual HTML pages under https://www.accessdata.fda.gov/cms_ia/ (index at default.html, browse by number at iali
- Update frequency: FDA states the import alert databases are updated in real time; individual alerts carry revision or publish dates
- Freshness confirmed: Actively maintained in 2026; Import Alert 66-41 shows a revision dated 05/19/2026 and FDA describes the alert databases as updated in real time
- Entity key: FDA FEI number (firm listing on import alert Red/Yellow List; refusal records al | documented: True (Per-alert pages list firms subject to DWPE and include FEI numbers in firm entries; example from Import Alert 66-40 content: Bio Health Pharmaceuticals noted as contract manufactur)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FDA import alerts list site:fda.gov actions-enforcement" -> https://www.fda.gov/industry/actions-enforcement/import-alerts (Import Alerts Landing Page)
- Backs: fda-import-alert-exit-packet
- Notes: Fully public, no login or key, but firm lists are spread across hundreds of per-alert HTML pages on accessdata.fda.gov with no bulk export, so building an FEI-keyed backbone requires scraping every alert page. Note the truncated claim about refusal r

### src-39: FDA Data Dashboard, Import Refusals dataset
- URL: https://datadashboard.fda.gov/oii/cd/imprefusals.htm
- Verdict: verified-live | Access class: public-easy | Format: Interactive dashboard with CSV export of refusal data; downloadable shipment-details zip files posted monthly; JSON REST API at api-datadashboard.fda.gov/v1/import_refusals with published field defini
- Update frequency: Weekly. Publisher states datasets are updated weekly (compliance dashboard data refreshed every Monday) and include only final actions; the separate Import Refusal Report is updated monthly and shipme
- Freshness confirmed: Publisher-stated weekly refresh (every Monday); monthly shipment-detail zips posted by the 5th of each month. A specific latest data week was not visible in search results, but the weekly cadence is c
- Entity key: FDA FEI number of the foreign supplier (importer identified by DUNS/FEI) | documented: True (Official API field definitions page for the import refusals dataset documents roughly 20 queryable fields per refusal record, including FEI number (the FDA Firm/Facility Establishm)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FDA Data Dashboard import refusals datadashboard.fda.gov" -> https://datadashboard.fda.gov/oii/cd/imprefusals.htm (FDA Dashboards - Import Refusals)
- Backs: fsvp-supplier-dossier-factory
- Notes: Dashboard viewing and CSV/zip downloads are public with no login. The API is a partial exception: it now requires an authorization key obtained through the free OII Unified Logon application, so programmatic API use is effectively public-registration

### src-40: FSIS Quarterly Enforcement Reports (with posted NOIE and suspension letters)
- URL: https://www.fsis.usda.gov/inspection/regulatory-enforcement/quarterly-enforcement-reports
- Verdict: verified-live | Access class: public-hard-to-parse | Format: HTML narrative page plus PDF table files (e.g., qer-q1-fy2026-tables.pdf, Tables 1-20) and individually posted PDF enforcement letters (NOIE and suspension letters named by establishment number, e.g.,
- Update frequency: Quarterly, on the federal fiscal year calendar (FY begins October 1); publisher states the information is updated on a quarterly basis
- Freshness confirmed: Q1 FY2026 tables PDF posted (fiscal year beginning October 1, 2025); a posted NOIE letter to Est. M354 dated March 23, 2026 confirms letter postings current into Q2 FY2026. The Q2 FY2026 QER itself wa
- Entity key: USDA FSIS establishment number (M, P, or G prefix, e.g., M354) | documented: True (FSIS posts individual NOIE letters as PDFs identified by establishment number; this letter to Est. M354 (dated 03-23-2026) exactly matches the claimed key format, and QER tables li)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FSIS quarterly enforcement report fsis.usda.gov regulatory enforcement" -> https://www.fsis.usda.gov/inspection/regulatory-enforcement/quarterly-enforcement-reports (Quarterly Enforcement Reports | Food Safety and Inspection Service)
- Backs: fsis-enforcement-radar
- Notes: Fully public with no login or fee, but the reports and letters are PDF documents (narrative plus PDF tables), so extracting establishment-level records requires PDF parsing. A data.gov catalog entry exists for the reports but no machine-readable bulk

### src-41: DOHMH New York City Restaurant Inspection Results [TOP20]
- URL: https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j
- Verdict: verified-live | Access class: public-easy | Format: Socrata open dataset (ID 43nn-pn8j), roughly 400,000 rows and 26 columns; CSV, JSON, XML, and RDF exports plus SODA API; direct anonymous CSV endpoint data.cityofnewyork.us/api/views/43nn-pn8j/rows.cs
- Update frequency: Daily. DOHMH states inspection results on NYC Open Data are updated daily
- Freshness confirmed: Updated daily per DOHMH; dataset live and actively maintained as of July 2026 searches
- Entity key: NYC DOHMH CAMIS number (claimed key text also references Chicago license number and equivalent jurisdiction keys, which belong to other cities' datasets, not this one) | documented: True (The dataset's data dictionary lists CAMIS as the DOHMH unique identifier for the restaurant, alongside DBA, BORO, address, cuisine, inspection, violation, score, and grade fields; )
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "DOHMH New York City Restaurant Inspection Results 43nn-pn8j NYC Open Data" -> https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j (DOHMH New York City Restaurant Inspection Results | NYC Open Data)
- Backs: chain-inspection-sentinel
- Notes: No login, key, or fee for browsing and bulk export; direct CSV download URL is publicly indexed. Dataset is mirrored on data.gov and data.ny.gov. Note the dataset only retains citations from inspections up to three years prior to each restaurant's mo

### src-42: USDA Organic INTEGRITY Database
- URL: https://organic.ams.usda.gov/integrity/About
- Verdict: verified-live | Access class: public-easy | Format: Web search UI with export-to-Excel of search results; monthly snapshots of the full public data set and annual lists of certified organic operations downloadable from the Data History page (organic.am
- Update frequency: Continuous updates from USDA-accredited certifying agents; full-dataset snapshot published monthly (captured at the beginning of each month); annual certified operations lists
- Freshness confirmed: Monthly full-dataset snapshots, captured at the beginning of each month per the publisher; database live as of July 2026 searches (third-party user guides current through mid-2025 confirm ongoing oper
- Entity key: NOP operation ID (USDA Organic INTEGRITY database) | documented: True (AMS publishes an official INTEGRITY Data Dictionary defining the database fields, surfaced for the NOP operation ID query; database user guides state the NOP ID number is listed in)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "USDA Organic INTEGRITY database organic.ams.usda.gov certified operations search" -> https://organic.ams.usda.gov/ (USDA Organic Integrity Database)
- Backs: organic-integrity-sentinel
- Notes: Public search, Excel export, and monthly/annual bulk downloads with no login or fee for read access; logins are only for certifiers submitting data. Operations with revoked, suspended, or surrendered certification are also searchable

### src-44: California DCC Cannabis Unified License Search (plus DCC license summary data)
- URL: https://search.cannabis.ca.gov/
- Verdict: verified-live | Access class: public-hard-to-parse | Format: Interactive web search tool (HTML UI with interactive map and geolocation); companion DCC license summary data is a hosted dashboard at cannabis.ca.gov/resources/data-dashboard/license-report/ with ex
- Update frequency: Daily; DCC states the License Search Tool is updated daily (every 24 hours)
- Freshness confirmed: Tool refreshed daily per DCC; confirmed live and indexed in July 2026 search results
- Entity key: State cannabis license number, California DCC format C10-0000XXX-LIC (prefix by license type, 7-digit number, -LIC suffix) | documented: True (Real DCC license numbers follow the format C10-[7-digit number]-LIC (examples C10-0000725-LIC, C10-0001287-LIC); C10 is the retailer prefix and other license types use other prefix)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query ""search.cannabis.ca.gov" California cannabis unified license search DCC" -> https://www.cannabis.ca.gov/resources/search-for-licensed-business/ (Search for a licensed business - Department of Cannabis Control)
- Backs: cannabis-license-standing-monitor
- Notes: No login wall, registration, or fee for the search tool. However no bulk machine-readable download was surfaced in search results: the license summary report is a dashboard whose documented exports are image, PDF, or PowerPoint only, so building a da

### src-46: NYC DOB Periodic Gas Piping System Inspections (official compliance building list spreadsheet plus per-community-district schedule)
- URL: https://www.nyc.gov/site/buildings/property-or-business-owner/gas-piping-inspections.page
- Verdict: verified-live | Access class: public-easy | Format: Official DOB web page hosting the LL152 Properties list as a downloadable Excel spreadsheet (file downloads on clicking the LL152 Properties link) plus the per-community-district inspection year sched
- Update frequency: Periodic re-posts of the properties list, no fixed stated cadence; receipts show versions dated 12/19/2024 and 4/14/2025
- Freshness confirmed: Properties list last updated 4/14/2025 per receipts; current inspection cycle 2024-2027 with community districts 4, 6, 8, 9, and 16 due by December 31, 2026
- Entity key: NYC BBL (borough, block, lot) and BIN | documented: True (The DOB LL152 Properties Excel spreadsheet contains building identification details including borough, block, lot (the BBL components) and BIN for every property that must comply)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "NYC DOB gas piping system inspections Local Law 152 building list nyc.gov" -> https://www.nyc.gov/site/buildings/property-or-business-owner/gas-piping-inspections.page (Periodic Gas Piping System Inspections (NYC DOB))
- Backs: ll152-gas-piping-inspection-radar
- Notes: Direct public Excel download from nyc.gov, no login, registration, or fee; filings themselves go through DOB NOW: Safety but the compliance list and schedule are open. No access change flagged.

### src-47: DOB NOW Elevator Safety Compliance [TOP20]
- URL: https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Elevator-Safety-Compliance/e5aq-a4j2
- Verdict: verified-live | Access class: public-easy | Format: NYC Open Data (Socrata) dataset e5aq-a4j2 with CSV, JSON, XML, and RDF exports plus OData connection for Excel/Tableau; about 120K rows and 24 columns, one row per elevator device
- Update frequency: Publisher cadence not explicitly stated in search results; catalog metadata shows repeated recent refreshes (last updated June 11, 2026, earlier snapshot May 10, 2026), consistent with an automated fe
- Freshness confirmed: Data last updated June 11, 2026 per NYC Open Data and Data.gov catalog metadata; dataset created January 27, 2023
- Entity key: NYC BIN plus DOB elevator device number (BBL for portfolio roll-up) | documented: True (The official dataset description states the data includes device number, device status, report filing dates, inspection dates, BIN, and other location information, documenting BIN )
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query ""DOB NOW" "Elevator Safety Compliance" NYC Open Data e5aq-a4j2" -> https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Elevator-Safety-Compliance/e5aq-a4j2 (DOB NOW Elevator Safety Compliance | NYC Open Data)
- Backs: nyc-elevator-cat1-compliance-packet
- Notes: Open NYC Open Data dataset, no login or fee; bulk CSV export and OData/API endpoints documented in receipts. Caveat: BBL was not confirmed as an explicit column in search results, so portfolio roll-up by BBL may require joining BIN to BBL via a cross

### src-48: DOB NOW: Safety Boiler [TOP20]
- URL: https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Safety-Boiler/52dp-yji6
- Verdict: verified-live | Access class: public-easy | Format: NYC Open Data (Socrata) dataset 52dp-yji6 with CSV, JSON, and XML exports; contains annual compliance filings for high and low pressure boilers filed through DOB NOW: Safety
- Update frequency: Daily automated updates per catalog metadata (automation: yes); dataset made public September 29, 2017
- Freshness confirmed: Daily automated refresh per catalog metadata; 2026-era updates confirmed in catalog search results (one catalog snippet cited a March 2026 last-updated timestamp)
- Entity key: NYC BIN/BBL plus DOB boiler device number | documented: True (DOB documents the boiler device ID as Borough Code + Device Number + Multiple Dwelling Flag + Serial Number (example 1-0000098712-Y-0001), and DOB NOW boiler records are searchable)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query ""DOB NOW" "Safety Boiler" NYC Open Data 52dp-yji6 dataset" -> https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Safety-Boiler/52dp-yji6 (DOB NOW: Safety Boiler - NYC Open Data)
- Backs: nyc-boiler-filing-penalty-shield
- Notes: Open NYC Open Data dataset, no login or fee; standard export endpoints documented. Caveat: BBL was not explicitly confirmed as a dataset column in search results (BIN and boiler device ID are confirmed), so BBL roll-up may require a BIN-to-BBL join.

### src-50: CSLB Public Data Portal (license master, workers compensation, personnel extracts)
- URL: https://www.cslb.ca.gov/onlineservices/dataportal/ (contractor list app also at https://www2.cslb.ca.gov/onlineservices/dataportal/ContractorList and https://web.cslb.ca.gov/onlineservices/Dataportal/)
- Verdict: verified-live | Access class: public-easy | Format: Downloadable extracts split into three files: license master, workers compensation, and personnel; CSLB states the data does not come in Excel format (delimited/plain text extracts); paid FULL and UPD
- Update frequency: Paid UPDATE files are produced the first week of each month covering prior-month changes; the refresh cadence of the no-cost portal downloads is not stated in search results
- Freshness confirmed: License master covers all licenses currently renewed or expired but renewable (live registry); LICENSE MASTER FULL FILE cited at 700,000+ records; monthly paid update files cover the previous month
- Entity key: CSLB contractor license number | documented: True (CSLB's data file description states the license master file includes license number, business name, address, telephone number, license status, issue/expiration dates, classificatio)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "CSLB Public Data Portal license master extract download" -> https://www.cslb.ca.gov/onlineservices/dataportal/ (CSLB Public Data Portal)
- Backs: cslb-sub-roster-compliance-monitor
- Notes: No-cost downloadable lists are available on the Public Data Portal with no login found in search results; a paid tier exists: $235 non-refundable fee per FULL or UPDATE file of the license database, and personnel history requires purchasing the Busin

### src-53: MSHA Open Government Data Portal (Violations, Assessed Violations, Inspections, Civil Penalty datasets) [TOP20]
- URL: https://arlweb.msha.gov/opengovernmentdata/ogimsha.asp
- Verdict: verified-live | Access class: public-easy | Format: Text delimited downloadable flat files (about 20 files, with definition files) covering violations, inspections, assessed violations, mines, accidents/injuries, employment/production, and related topi
- Update frequency: Weekly; MSHA states 20 various flat files are uploaded every Friday (MDRS maintenance window Friday 10:00 PM to Saturday 10:00 AM ET)
- Freshness confirmed: Datasets span calendar year 2000 to present and are refreshed weekly (files uploaded every Friday), current as of July 2026 search results
- Entity key: MSHA Mine ID (7-digit) | documented: True (MSHA documents the mine ID as a seven-digit mine identification number issued by the MSHA district office; data.gov's MSHA dataset pages document Mine ID as the unique key of the M)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "MSHA open government data portal OGIMSHA violations inspections datasets" -> https://arlweb.msha.gov/opengovernmentdata/ogimsha.asp (MSHA - Open Government Initiative Portal)
- Backs: msha-citation-contest-decision-desk
- Notes: Free public downloads, no login, key, or fee found in search results; arlweb.msha.gov is MSHA's legacy subdomain but the portal remains the live home of the flat files and is referenced from msha.gov data pages and data.gov

### src-54: MSHA Open Government Data Portal (Accidents/Part 50, Employment/Production, Violations, Inspections datasets) [TOP20]
- URL: https://arlweb.msha.gov/opengovernmentdata/ogimsha.asp
- Verdict: verified-live | Access class: public-easy | Format: Pipe-delimited (vertical bar) TXT flat files with header row, zipped, each with a companion definition file (e.g. Accidents_Definition_File.txt); about 20 flat files; mirrored on catalog.data.gov and 
- Update frequency: Weekly: 20 flat files are uploaded every Friday per the MDRS listing on data.gov; employment/production files are organized by calendar quarter/year
- Freshness confirmed: Quarterly Operator Employment and Production dataset shows a data.gov publication/update date of March 12, 2026; cadence receipt states flat files are refreshed every Friday
- Entity key: MSHA Mine ID (7-digit), rolled up by controller/operator ID | documented: True (Mine ID is documented as the key field that connects the Mines dataset with the Employment/Production, Inspection, Violations and Accidents data; per-dataset definition files on th)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "MSHA "Mine Data Retrieval System" OR "opengovernmentdata" data sets accidents violations inspections" -> https://arlweb.msha.gov/opengovernmentdata/ogimsha.asp (MSHA - Open Government Initiative Portal)
- Backs: msha-aggregates-regulator-view-benchmark
- Notes: No login, API key, or fee; direct file downloads from the portal. The portal sits on the legacy arlweb.msha.gov subdomain while msha.gov/msha-datasets (Explore MSHA Datasets) is the current front door; both appear live in search results. The 7-digit 

### src-55: PHMSA Pipeline Enforcement Data (PRIMIS enforcement transparency: cases, proposed penalties, enforcement documents)
- URL: https://primis.phmsa.dot.gov/enforcement-data/
- Verdict: verified-live | Access class: public-easy | Format: HTML report tables by year (cases initiated, NOPV, proposed penalties, penalties resolved, orders issued, summaries), per-operator pages keyed by OPID, generated CSV exports (e.g. FOCPEvent_opid_*.csv
- Update frequency: Monthly: enforcement data is updated monthly as cases are initiated and resolved, with case data beginning 2002 and key case documents beginning 2007
- Freshness confirmed: 2026 case listings exist (Notice of Probable Violation Cases Initiated page with opened_yr=2026); monthly update cycle stated by PHMSA
- Entity key: PHMSA Operator ID (OPID) | documented: True (PHMSA OpID is a unique identifier assigned by PHMSA to operators of pipelines, pipeline facilities, UNGS and LNG facilities and is used for all reporting to PHMSA; enforcement oper)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "PHMSA pipeline enforcement data primis.phmsa.dot.gov enforcement cases proposed penalties" -> https://primis.phmsa.dot.gov/enforcement-data/ (Enforcement Data - PRIMIS | PHMSA)
- Backs: phmsa-nopv-response-precedent-engine
- Notes: No login wall, API key, or fee found. Caveat for automation: there is no single documented bulk file for the full enforcement dataset; data is spread across yearly report pages and per-operator views, and CSV export URLs carry generated token suffixe

### src-56: FERC Electric Quarterly Reports (EQR) database downloads
- URL: https://www.ferc.gov/power-sales-and-markets/electric-quarterly-reports-eqr
- Verdict: verified-live | Access class: public-hard-to-parse | Format: Bulk database as yearly/quarterly ZIP files (over 15.5 GB compressed per FERC download page; about 100 GB total per Catalyst Cooperative); inner per-respondent ZIPs contain one CSV per table (transact
- Update frequency: Quarterly: filings currently due 30 days after quarter close; FERC Order No. 917 (final rule March 19, 2026) extends the deadline to four months after quarter close once the XBRL-CSV transition comple
- Freshness confirmed: Coverage confirmed 2013Q3 to present with over 4 billion transactions (Catalyst, Nov 2025); the current 30-day post-quarter deadline remains in effect per March 2026 coverage of Order 917, so Q1 2026 
- Entity key: FERC Company Identifier (CID) / EQR Seller ID | documented: True (A CID is required by the Seller to file an EQR and is obtained through the Company Registration system; an EQR Data Dictionary v3.4 PDF and a FERC Company Identifier Listing on dat)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FERC Electric Quarterly Reports EQR database downloads CSV" -> https://www.ferc.gov/power-sales-and-markets/electric-quarterly-reports-eqr (Electric Quarterly Reports (EQR) | Federal Energy Regulatory Commission)
- Backs: ferc-eqr-mbr-compliance-guardrail
- Notes: No login, key, or fee, but bulk access is awkward: 15.5+ GB zip-of-zips CSV/XML bundles, a limit of three simultaneous download users, and FERC advises off-peak downloading. Flag: Order No. 917 (March 2026, Federal Register March 24, 2026) migrates E

### src-57: NERC Enforcement Actions (full NOPs, monthly Spreadsheet NOPs, FFT reports) plus NERC Compliance Registry
- URL: https://www.nerc.com/pa/comp/CE/Pages/Enforcement-and-Mitigation.aspx
- Verdict: verified-live | Access class: public-hard-to-parse | Format: Enforcement side: PDF filings (full NOPs and monthly consolidated Spreadsheet NOP PDFs in the Enforcement Actions DL library, e.g. FinalFiled_September_Spreadsheet_NOP_20190926.pdf), plus FFT and Comp
- Update frequency: Enforcement actions are filed and posted on a monthly cycle (monthly Spreadsheet NOP naming pattern such as FinalFiled_September_ and FinalFiled_December_); registry Excel files are maintained as curr
- Freshness confirmed: Enforcement Dispositions page live in July 2026 search results; monthly Spreadsheet NOP filing pattern confirmed from the document library; ERO Enterprise penalty inflation adjustments begin in 2026 p
- Entity key: NERC Compliance Registry number (NCR) | documented: True (NERC publishes the Compliance Registry as an NCR Matrix Excel workbook listing registered entities by NCR number and registered functions (search results also surface an NCR Active)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "NERC enforcement actions notice of penalty spreadsheet NOP FFT nerc.com Enforcement-and-Mitigation" -> https://www.nerc.com/pa/comp/CE/Pages/Enforcement-and-Mitigation.aspx (Enforcement Dispositions)
- Backs: nerc-enforcement-intel-audit-brief
- Notes: No login, key, or fee. Hard to parse because enforcement dispositions are PDF-heavy (full NOPs and the monthly Spreadsheet NOPs are PDFs, not machine-readable spreadsheets); third parties like the White & Case NERC Database exist specifically to summ

### src-58: FCC National Broadband Map data downloads (BDC availability data)
- URL: https://broadbandmap.fcc.gov/data-download
- Verdict: verified-live | Access class: public-easy | Format: Fixed availability as tabular CSV (downloadable by provider, by state/area, or nationwide, organized by vintage version parameter, e.g. nationwide-data?version=dec2023); mobile coverage as GIS shapefi
- Update frequency: Biannual data vintages (as of June 30 and December 31 each year) with map refreshes and challenge-driven corrections in between; the December 31, 2025 filing window opened January 2, 2026 with a March
- Freshness confirmed: Map shows availability data as of June 30, 2025 (seventh collection, published fall 2025); the eighth window for December 31, 2025 data ran January 2 to March 2, 2026, and search results report a May 
- Entity key: FCC Registration Number (FRN), plus provider ID on the map | documented: True (The download specification documents a provider_id field in availability files and a Provider List that includes the Provider ID and FRN for each filing entity; Provider ID is assi)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FCC National Broadband Map data download broadband availability data BDC" -> https://broadbandmap.fcc.gov/data-download (Data Download | FCC National Broadband Map)
- Backs: fcc-bdc-preaudit-challenge-desk
- Notes: Availability downloads and APIs are public with no login or fee found in search results; BDC Help Center publishes step-by-step download instructions. Caveat: the underlying Broadband Serviceable Location Fabric is separately licensed (access restric

### src-59: FCC ULS Public Access Files (complete license databases plus daily/weekly transaction files)
- URL: https://www.fcc.gov/wireless/data/public-access-files-database-downloads
- Verdict: verified-live | Access class: public-easy | Format: Zip archives containing pipe-delimited text files. Complete files named l_sssss.zip (licenses) and a_sssss.zip (applications) per radio service, e.g. l_amat.zip / a_amat.zip for Amateur. Companion dai
- Update frequency: Weekly complete files created early Sunday morning; daily transaction files created early Tuesday through Saturday mornings. data.gov catalog entry describes ULS bulk files as free public downloads up
- Freshness confirmed: Rolling: complete database files regenerated every Sunday and transaction deltas generated Tuesday through Saturday, so data is current to within roughly one week (confirmed via FCC download page and 
- Entity key: FCC Registration Number (FRN); call sign per license | documented: True (The official ULS Data File Format definitions document (updated Feb 2024) specifies the pipe-delimited record layouts including the HD Application/License Header (which carries the)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FCC ULS public access files database downloads weekly complete license data transaction files" -> https://www.fcc.gov/wireless/data/public-access-files-database-downloads (Public Access Files - Database Downloads | Federal Communications Commission)
- Backs: fcc-uls-spectrum-portfolio-guardian
- Notes: Free anonymous bulk downloads, no login, no API key, no fee. Files are pipe-delimited and require parsing against the published data dictionary, but access itself is unrestricted.

### src-60: FCC Robocall Mitigation Database (all filings, public CSV download)
- URL: https://www.fcc.gov/robocall-mitigation-database
- Verdict: verified-live | Access class: public-easy | Format: Single CSV file of all filings downloadable from the RMD welcome page (hosted on ServiceNow at https://fccprod.servicenowservices.com/rmd?id=rmd_welcome); also a read API with filtering, documented at
- Update frequency: Continuously updated as providers submit, update, or are removed from certifications; no fixed publication cycle stated. FCC actively manages the database, including removals of non-compliant provider
- Freshness confirmed: Database is live and actively maintained into 2026: a Federal Register document of 2026-01-06 (Improving the Effectiveness of the Robocall Mitigation Database; CORES Registration System) and an April 
- Entity key: FCC Registration Number (FRN); RMD filing ID; FCC Form 499 Filer ID | documented: True (The official RMD filing instructions document an explicit 'FCC Registration Number (FRN)' field: only business-type FRNs associated with the user and not already used in another fi)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FCC Robocall Mitigation Database public download CSV filings" -> https://www.fcc.gov/robocall-mitigation-database (Robocall Mitigation Database | Federal Communications Commission)
- Backs: fcc-rmd-carrier-kyc-packet
- Notes: Per the RMD API documentation and filing instructions, registration is not required to view or download the database; any member of the public can download the full CSV from the welcome page, and the API provides programmatic read access. Note the da

### src-61: FAA Releasable Aircraft Registry Database
- URL: https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download
- Verdict: verified-live | Access class: public-easy | Format: Single zip file ReleasableAircraft.zip (about 60 MB) at https://registry.faa.gov/database/ReleasableAircraft.zip containing comma-separated (.csv/.txt) files including the aircraft registration MASTER
- Update frequency: Refreshed daily at 11:30 pm Central time per the FAA download page.
- Freshness confirmed: Daily: the download is refreshed every night at 11:30 pm Central, so contents are current to the previous day (cadence stated on the live FAA download page as of July 2026 searches).
- Entity key: FAA N-number (plus airframe serial number from the registry record) | documented: True (The official ardata.pdf record layout for the releasable database documents the registration N-Number field (the MASTER file is stored in N-number sequence) and a Serial Number fie)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FAA releasable aircraft registry database download ReleasableAircraft.zip updated daily" -> https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download (Download the Aircraft Registration Database)
- Backs: n-number-ad-gap-packet
- Notes: Direct anonymous zip download, no login, key, or fee. Documentation for the file structure is published alongside the download.

### src-62: FAA Dynamic Regulatory System (DRS)
- URL: https://drs.faa.gov/browse
- Verdict: verified-live | Access class: public-hard-to-parse | Format: Web application (search at drs.faa.gov/search, browse at drs.faa.gov/browse) serving 65+ document types from about a dozen FAA repositories; individual documents render as HTML/PDF/Excel views (e.g. T
- Update frequency: Updated nightly: third-party guidance (Cessna Owner Organization guide to DRS) states DRS is updated daily, with the entire system refreshed every evening so content is current within 24 hours.
- Freshness confirmed: System refreshed nightly; search results surface a DRS document dated late November 2025 (DRS-2025-24-51_Emergency, document ID stamped 20251129), and the FAA continues moving Airworthiness Directives
- Entity key: FAA TCDS number (type certificate data sheet) for the subject model; DER and mod (claim truncated in assignment) | documented: True (DRS has a dedicated Type Certificate Data Sheets document type with roughly 2,000 TCDS records, and individual documents are identified and titled by TCDS number (search results sh)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FAA Dynamic Regulatory System DRS browse type certificate data sheets" -> https://drs.faa.gov/ (Dynamic Regulatory System - Federal Aviation Administration)
- Backs: der-cert-basis-packet
- Notes: Free and public with no login, API key, or fee for searching and viewing, but content is delivered through a dynamic web UI with per-document views rather than bulk files, so backbone use requires scraping or per-document retrieval. Help and training

### src-63: FAA Part 107 Waivers Issued list
- URL: https://www.faa.gov/uas/commercial_operators/part_107_waivers/waivers_issued
- Verdict: verified-live | Access class: public-hard-to-parse | Format: Searchable HTML list/table on the FAA page with a search box for finding issued waivers; individual waiver certificates are linked as PDFs (Certificate of Waiver documents under faa.gov/media). No off
- Update frequency: Updated as waivers are issued and expire; no publisher-stated refresh cycle found in search results. Third-party tracking (Pilot Institute) shows the FAA list is maintained over time.
- Freshness confirmed: Page confirmed live in July 2026 searches and referenced as current by 2026 industry guides (e.g. Rotate's Part 107 Waiver Guide 2026). Most recent quantified snapshot found: Pilot Institute reported 
- Entity key: FAA Part 107 waiver number and operator name on the FAA waivers-issued list (claim truncated in assignment) | documented: True (The live FAA Waivers Issued page provides a search box for locating issued waivers by waiver number, responsible party (operator), and related details, and links each entry to its )
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FAA Part 107 waivers issued list search commercial operators waiver number" -> https://www.faa.gov/uas/commercial_operators/part_107_waivers/waivers_issued (Part 107 Waivers Issued | Federal Aviation Administration)
- Backs: part107-waiver-draft-factory
- Notes: Fully public with no login, key, or fee, but the data is an on-page searchable table with PDF certificate links rather than a downloadable dataset, so backbone use requires scraping the page (and the underlying data feed) plus parsing waiver PDFs. No

### src-64: CBP ocean bill-of-lading (AMS) records, FOIA-derived, mirrored free by ImportYeti
- URL: https://www.importyeti.com/
- Verdict: verified-live | Access class: public-registration | Format: Web search UI over 70M+ CBP ocean BOL records (FOIA-derived, coverage from January 2015); company profile pages; paid Power Query for filtered exports; beta API at data.importyeti.com. No free bulk ra
- Update frequency: Not stated by publisher in search results; user reviews say updates are frequent but not real-time. Exact refresh cadence unconfirmed.
- Freshness confirmed: Product live and actively reviewed through June 2026; dataset coverage begins January 2015; exact latest shipment month could not be confirmed from search results (one unattributed search-result menti
- Entity key: Importer/consignee name in CBP AMS ocean manifest records (via ImportYeti free search) | documented: True (BOL records include purchaser (importer/consignee) and supplier names and are searchable by company name (shipper or consignee); caveat: consignee names can be missing due to manif)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "ImportYeti free bill of lading data CBP customs records supplier search" -> https://bellingcat.gitbook.io/toolkit/more/all-tools/importyeti (ImportYeti - Bellingcat's Online Investigation Toolkit)
- Backs: ieepa-tariff-refund-cape-pack
- Notes: Free search by company legal name; free sign-up, and a login is required after 25 page views per IP. Free-forever plan exists; paid plans (from roughly $10.83/mo per GetApp listing, supply-chain enterprise tiers from $1,000) unlock Power Query multi-

### src-66: USAspending Award Data Archive (FPDS-sourced contract transactions)
- URL: https://www.usaspending.gov/download_center/award_data_archive
- Verdict: verified-live | Access class: public-easy | Format: Pre-built zipped CSV files per agency per fiscal year: Contracts_Full (full FY to file-generation date) and Contracts_Delta (new/modified/deleted rows since last month's generation). Also Custom Award
- Update frequency: New archive files uploaded by the 15th of each month; a Data As Of column shows when files were last generated (USAspending stated cadence).
- Freshness confirmed: Monthly-regenerated full fiscal year files (uploaded by the 15th of each month), so current-FY 2026 contract transactions are present as of the latest monthly generation; verified live in July 2026 se
- Entity key: SAM UEI (and CAGE code) of the incumbent or of the prospect itself | documented: True (recipient_uei, recipient_parent_uei (and legacy recipient_duns) are documented fields available on contract prime award transaction and summary download files; the site Data Dictio)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "USAspending Award Data Archive download full contracts CSV monthly" -> https://www.usaspending.gov/download_center/award_data_archive (Award Data Archive | USAspending)
- Backs: uei-recompete-radar-brief
- Notes: No login, API key, or fee for archive file downloads; files are instantaneous pre-prepared zips. API is also open.

### src-67: GAO Bid Protest Decisions and Docket Search
- URL: https://www.gao.gov/legal/bid-protests/search
- Verdict: verified-live | Access class: public-easy | Format: Web search UI over published decisions and the active-protest docket; per-protest docket pages at gao.gov/docket/{b-number}; decisions as HTML/PDF pages; Recent Bid Protest Decisions listing page. No 
- Update frequency: Continuous: docket entries appear as protests are filed and decisions are published as issued (recent decisions may lag public posting; GAO does not publish most dismissal/corrective-action closures).
- Freshness confirmed: 2026 decisions confirmed in search results, including B-423796.2 (Feb 5, 2026), B-423552.3 (Mar 24, 2026), and a Jan 27, 2026 DIA sustain; docket carries active 2026 protests.
- Entity key: Solicitation number (SAM.gov) and GAO B-number docket entries; awardee SAM UEI for joining | documented: True (Docket pages are keyed by GAO B-number and carry the solicitation number in the docket record (example docket b-423185.1 shows solicitation W56KGZ25Q6043); GAO FAQs state the docke)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "GAO bid protest decisions docket search solicitation number" -> https://www.gao.gov/legal/bid-protests/search (Search Decisions & Docket | U.S. GAO)
- Backs: post-award-protest-triage-memo
- Notes: No login or fee. GAO warns the search feature occasionally experiences technical difficulties and may be unavailable; missing docket items can be requested via ProtestFinder@gao.gov. Coverage caveat: most dismissals and corrective-action closures are

### src-68: SERFF Filing Access (SFA) state portals
- URL: https://portals.naic.org/serff-filing-access
- Verdict: verified-live | Access class: public-easy | Format: Per-state web search portals at filingaccess.serff.com/sfa/home/{STATE} (e.g., NC, NE, MD, GA, TX, CA, plus the Interstate Insurance Compact); filings and dispositions delivered as PDF documents; SFA 
- Update frequency: Continuous production system: participating states expose rate/rule/form filings and public health-plan binders as they mark them available; no fixed publisher cadence stated. WA notes filings receive
- Freshness confirmed: Live production portals in 2026 across many states (NC, NE, MD, GA, TX, CA, Compact confirmed in current search results); searchable history reaches back to filings received after April 13, 2014 (WA).
- Entity key: NAIC company code (CoCode) plus SERFF tracking number | documented: True (State instructions document NAIC Company Code as an SFA search criterion (the entire NAIC Company Code must be entered); Texas TDI documents that the filing disposition document ma)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "serff.com "serff_filing_access" page states participating list" -> https://serff.com/serff_filing_access.htm (SERFF Filing Access (serff.com))
- Backs: serff-rate-filing-objection-intel
- Notes: Free, no registration or fee (no charge for this method of file review). Fragmentation caveat: access is state by state, only for filings a participating state has marked available, and search is UI-only with PDF outputs, so it is public-easy to reac

### src-70: SAM.gov Wage Determinations (Davis-Bacon)
- URL: https://sam.gov/wage-determinations
- Verdict: verified-live | Access class: public-easy | Format: Web search UI plus one HTML page per wage determination revision at /wage-determination/{WD number}/{revision} (e.g., /wage-determination/WA20200002/0). No dedicated public wage determination API surf
- Update frequency: Weekly. DOL states changes to Davis-Bacon General Wage Determinations are made in weekly updates, generally on Friday, reflected in modification numbers on the GWD.
- Freshness confirmed: Actively publishing in 2026: SAM.gov wage determinations page content referenced SCA wage determinations published 4/29/2026, and 2025-series DBA determinations such as DC20250002 (revision 2) are liv
- Entity key: SAM.gov Wage Determination number (e.g., WA20200002) plus contractor SAM UEI | documented: True (The exact example WD number WA20200002 from the entity key claim resolves to a live SAM.gov determination page; WD number plus revision suffix is the documented record key. Caveat:)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "sam.gov wage determinations Davis-Bacon Act search public" -> https://sam.gov/wage-determinations (Wage Determinations | SAM.gov)
- Backs: davis-bacon-certified-payroll-autopilot
- Notes: Search and lookup are free with no login; DOL describes SAM.gov as a free online service and the official site for all Davis-Bacon GWDs since June 14, 2019. API-based access to SAM.gov data requires a free public API key requested from the user profi

### src-71: Campus Safety and Security Survey data (Clery Act statistics)
- URL: https://ope.ed.gov/campussafety/
- Verdict: verified-live | Access class: public-easy | Format: Web Data Analysis Cutting Tool with custom report downloads plus a complete data file download for all institutions per survey year; historical files (2005-2012 era) distributed in Excel, SAS, or SPSS
- Update frequency: Annual. Crime statistics (and fire statistics since the 2010 collection) are submitted once per year via a web-based collection by all Title IV postsecondary institutions, as required by the Clery Act
- Freshness confirmed: Most recent confirmable cycle from search results: the 2024 survey collection (calendar year 2023 crime statistics), evidenced by the csss2024 survey site documents (user guide and 2023 Post-Collectio
- Entity key: OPE ID (8-digit), crosswalked to IPEDS UnitID | documented: True (The cutting tool supports institution search by OPE ID and other institution identifiers, and complete data file downloads include all institutions for a selected survey year.)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "ope.ed.gov campus safety security data cutting tool download Clery Act data files" -> https://ope.ed.gov/campussafety/ (Campus Safety and Security Data Analysis Cutting Tool)
- Backs: clery-crime-log-qa-asr-packet
- Notes: No login, registration, or fee for the cutting tool or the complete data file downloads. Crosswalk caveat: IPEDS UnitID and OPE ID are not one-to-one (one UnitID can map to multiple 8-digit OPEIDs for branches); NCES and FSA built a dedicated UnitID-

### src-72: IPEDS complete data files and data center
- URL: https://nces.ed.gov/ipeds
- Verdict: verified-live | Access class: public-easy | Format: Complete data files downloadable by survey component and year as zipped CSV (collections back to 1980-81), plus IPEDS Access databases and the interactive Data Center (institution lookup, custom data 
- Update frequency: Annual collection cycle with a published official Data Release Schedule; each collection releases in stages (preliminary/provisional then final/revised). Example cadence: Spring 2025 collection provis
- Freshness confirmed: On January 6, 2026 NCES released provisional data from the Spring 2025 collection: Fall 2024 Enrollment, Fall 2024 Human Resources, FY2024 Finance, and FY2024 Academic Libraries. The new ACTS componen
- Entity key: IPEDS UnitID | documented: True (UNITID is described as the unique identification number assigned to postsecondary institutions surveyed through IPEDS (also called IPEDS ID), and the Data Center supports searching)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "IPEDS complete data files data center UNITID nces.ed.gov" -> https://nces.ed.gov/ipeds/Help/View/101 (Complete data files - National Center for Education Statistics)
- Backs: ipeds-keyholder-autopilot
- Notes: No login, registration, or fee for complete data files, Access databases, or the Data Center. Data dictionaries ship with the files. Note the general federal-data caveat: releases move through provisional to final status per the release schedule.

### src-73: Cook County Assessor open data (Assessed Values, Parcel Universe, Parcel Sales, Appeals)
- URL: https://datacatalog.cookcountyil.gov/Property-Taxation/Assessor-Historic-Assessed-Values/uzyt-m557
- Verdict: verified-live | Access class: public-easy | Format: Socrata open data portal datasets (browser table view with the portal's standard export and API endpoints). Assessed Values (uzyt-m557): one row per PIN per year, 1999 to present, with mailed, certifi
- Update frequency: Monthly. Parcel Universe: data updated monthly, rowcount final once the Assessor certifies all townships. Parcel Sales: uploaded monthly with a reporting lag (records can appear months after recording
- Freshness confirmed: Actively maintained into 2026: the companion Assessor Parcel Universe dataset shows last updated May 01, 2026 on the data.gov catalog listing. Assessed values cover 1999 to present including the curre
- Entity key: County parcel ID: Cook County PIN (note: claimed key text also mentions NYC BBL and Harris County account number, which do not apply to this Cook County source) | documented: True (Dataset is parcel-level with each row containing the assessed values for a single PIN for a single year, and the documentation instructs users to zero-pad PINs to 14 digits.)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "Cook County Assessor "Assessed Values" datacatalog.cookcountyil.gov uzyt-m557 PIN" -> https://datacatalog.cookcountyil.gov/Property-Taxation/Assessor-Assessed-Values/uzyt-m557 (Assessor - Assessed Values | Cook County Open Data)
- Backs: commercial-property-tax-appeal-packets
- Notes: Open Socrata portal, no login or fee for browsing or export. The Assessor's office also maintains a public GitHub org (ccao-data) and publishes annual open data refresh stories (2022, 2023, 2025). Caveats from the publisher: current-tax-year rows cha

### src-03: FMCSA SAFER national hazmat rate guidance plus SMS inspection files [TOP20]
- URL: https://safer.fmcsa.dot.gov/HazMatRatesPost.aspx (companion data files at https://ai.fmcsa.dot.gov/sms/Data/Downloads.aspx)
- Verdict: needs-attention | Access class: public-easy | Format: Static HTML guidance page (national hazmat out-of-service rate figures and instructions for computing a carrier's OOS percentage); no downloadable dataset on this page; the per-carrier data lives in t
- Update frequency: Effectively static; the national rates were calculated from MCMIS roadside inspection data covering 2003 to 2010, and no newer refresh is stated
- Freshness confirmed: Underlying national rate data covers the 2003 to 2010 period per the page text; no newer data period confirmed for this page. The SMS inspection file component refreshes monthly (May 26, 2026 update, 
- Entity key: USDOT number | documented: False (The page presents national aggregate OOS rates and formulas only; it exposes no per-carrier USDOT-keyed records. USDOT number is documented as a field of the companion SMS inspecti)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query ""HazMatRatesPost.aspx" safer.fmcsa.dot.gov" -> https://safer.fmcsa.dot.gov/HazMatRatesPost.aspx (SAFER WEB - National Hazardous Materials Rates Infomration and Guidance)
- Backs: hmsp-eligibility-guardian
- Notes: No login or fee for the guidance page or the SMS files. The guidance page is a static reference, not a data endpoint. | VERDICT REASON: The page is live but it is a stale static guidance sheet: its national benchmark rates are built on 2003 to 2010 MCMIS data and it carries no per-carrier, USDOT-keyed records, so it cannot serve as a data backbone on its own. Treat it as reference co

### src-07: FMCSA Drug and Alcohol Clearinghouse
- URL: https://clearinghouse.fmcsa.dot.gov/
- Verdict: needs-attention | Access class: customer-private | Format: Secure web portal (login.gov auth) for queries; public aggregate monthly summary report PDFs (e.g. Clearinghouse_MonthlyReport_Feb2025.pdf) in the Learning Center. No public bulk record-level dataset.
- Update frequency: Monthly summary reports published by FMCSA; the query database itself is a live transactional system.
- Freshness confirmed: Monthly summary reports; the most recent report PDF directly surfaced in search results is February 2025 (Clearinghouse_MonthlyReport_Feb2025.pdf); third-party 2026 guides cite Clearinghouse statistic
- Entity key: USDOT number (employer) | documented: True (Employer registration requires entering the USDOT Number and EIN to link the company to the Clearinghouse account, verified against the FMCSA Portal; USDOT number is a documented e)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FMCSA Drug and Alcohol Clearinghouse clearinghouse.fmcsa.dot.gov employer USDOT number registration" -> https://clearinghouse.fmcsa.dot.gov/FAQ/Topics/Registration (FMCSA Drug & Alcohol Clearinghouse - Registration)
- Backs: clearinghouse-compliance-autopilot
- Notes: Violation records are driver-keyed and only reachable through a registered employer or C/TPA account: registration via login.gov plus FMCSA Portal, driver consent for full queries, and a flat fee of $1.25 per query purchased as a query plan. Only agg | VERDICT REASON: Site is live and healthy, but it is not a usable bulk data backbone: record-level data is consent-gated, driver-keyed, per-query paid ($1.25), and accessible only inside each employer's own account. Public output is limited to aggregate national mont

### src-19: DOL Enforcement Data Portal: OSHA inspection, violation, and accident data [TOP20]
- URL: https://enforcedata.dol.gov/views/data_catalogs.php
- Verdict: needs-attention | Access class: public-easy | Format: Bulk CSV file downloads via the data catalog page (inspection, violation, and accident record files); a modernized API alternative exists at developer.dol.gov (DOL OSHA Enforcement API). Exact zip pac
- Update frequency: Daily. Search receipt states OSHA updates its public enforcement files daily; the IMIS enforcement database (3M+ inspections since 1972) is described as updated daily.
- Freshness confirmed: Current; public files updated daily as of search date (2026-07-04). Coverage is roughly 90,000 OSHA inspections per year including citations, penalties, and accident investigation detail, with inspect
- Entity key: activity_nr (OSHA inspection/activity number, unique inspection identifier and join key to violations) plus establishment name and state fields | documented: True (DOL publishes a data dictionary for the OSHA inspection data; activity_nr is described as the unique identifier for inspections and the key to join inspections with their violation)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "enforcedata.dol.gov data catalog OSHA enforcement data download" -> https://enforcedata.dol.gov/views/data_catalogs.php (Open Data Portal| United States Department of Labor)
- Backs: osha-citation-response-packet
- Notes: No login or fee for the CSV catalog downloads. The developer.dol.gov API route requires free API key registration. Access change flag: DOL banner text says the Enforcement website will soon be retired in favor of the new DOL Open Data Portal and mode | VERDICT REASON: The claimed URL is live, files update daily, and activity_nr plus establishment name are documented fields, so the source works today. Flagged because DOL explicitly states the enforcedata.dol.gov Enforcement website will soon be retired in favor of 

### src-34: FDA List of Drug Master Files (DMFs)
- URL: https://www.fda.gov/drugs/drug-master-files-dmfs/list-drug-master-files-dmfs
- Verdict: needs-attention | Access class: public-easy | Format: Excel (.xlsx) download from the FDA page; current release is the 1Q2026 Excel file (2.4 MB) posted 04/22/2026
- Update frequency: Quarterly; FDA states the list is updated quarterly and each release notes changes to activity status, type, holder and subject since the prior quarter
- Freshness confirmed: List current through DMF 044003; contains DMFs received by March 31, 2026 with acknowledgment letters sent before April 22, 2026; Excel updated 04/22/2026
- Entity key: DMF number; FEI for the manufacturing site | documented: False (The DMF list columns are DMF#, STATUS (A=active, I=inactive), TYPE, SUBMIT DATE, HOLDER, SUBJECT. DMF number is a documented field, but FEI is not a column of the public quarterly )
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "FDA "List of Drug Master Files" DMFs site:fda.gov" -> https://www.fda.gov/drugs/drug-master-files-dmfs/list-drug-master-files-dmfs (List of Drug Master Files (DMFs) | FDA)
- Backs: dmf-api-source-qualification
- Notes: Direct Excel download from fda.gov, no login, no key, no fee. FEI-to-DMF site mapping exists only inside confidential application submissions per FDA facility-identification guidance, not in this public file, so a separate source is required for the  | VERDICT REASON: Source is live, quarterly, and easy to ingest, and DMF number is a documented field. However the second half of the claimed entity key fails: FEI is not a field of the public DMF list, so manufacturing-site FEI must come from another source (for exam

### src-43: OFLC Performance Data (H-2A disclosure files)
- URL: https://www.dol.gov/agencies/eta/foreign-labor/performance
- Verdict: needs-attention | Access class: public-easy | Format: Excel (.xlsx) quarterly cumulative and annual public disclosure files per program (H-2A, H-2B, PERM, LCA, CW-1, Prevailing Wage) with companion PDF record layouts (e.g., H-2A_Record_Layout_FY2025_Q2.p
- Update frequency: Quarterly. OFLC publishes disclosure data and selected program statistics each fiscal-year quarter, cumulative through the quarter
- Freshness confirmed: Q2 FY2026 release confirmed: public disclosure files include all final determinations issued October 1, 2025 through March 31, 2026, for PERM, LCA, H-2A, H-2B, CW-1, and Prevailing Wage programs
- Entity key: Employer FEIN plus OFLC case number (H-2A disclosure files); WHD case data joins | documented: False (The official record layout documents FEIN as a form item (ETA-9142A Section B), but FEIN data is treated as PII and is not included in the public program disclosure data; the paral)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "OFLC performance data disclosure files H-2A dol.gov foreign labor certification" -> https://www.dol.gov/agencies/eta/foreign-labor/performance (Performance Data | U.S. Department of Labor)
- Backs: h2a-filing-copilot
- Notes: Direct xlsx downloads with no login, key, or fee. Key access-relevant finding: Employer FEIN is excluded from the public H-2A disclosure files as PII, so the claimed FEIN-based join (including joins to WHD case data) cannot be executed on the public  | VERDICT REASON: Source is live at the exact claimed URL, free, xlsx format, and current through Q2 FY2026 (final determinations through March 31, 2026). However, the claimed entity key is only half-available: the OFLC case number is a documented disclosure-file fiel

### src-45: State pesticide applicator license databases (AAPCO-indexed state portals; e.g., Colorado applicator search)
- URL: https://ag.colorado.gov/plants/pesticides/pesticide-applicator-search
- Verdict: needs-attention | Access class: public-hard-to-parse | Format: Per-state HTML search portals (form-based lookup, no bulk file); Colorado portal verifies businesses holding a License or Registration and individuals holding Qualified Supervisor, Certified Operator,
- Update frequency: No stated cadence; Colorado portal returns only currently valid licenses (expired licenses do not appear), implying a continuously maintained live register
- Freshness confirmed: Live register of currently valid licenses at query time; portal confirmed live in July 2026 search results
- Entity key: State pesticide applicator license or certification number (Colorado calls it the Applicator ID) | documented: True (The Colorado search page documents Applicator ID as a first-class search field (guidance says start by entering only an Applicator ID or only a Last Name), and CDA verifies or crea)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "Colorado Department of Agriculture pesticide applicator license search ag.colorado.gov" -> https://ag.colorado.gov/plants/pesticides/pesticide-applicator-search (Pesticide Applicator Search | Department of Agriculture)
- Backs: pesticide-applicator-credential-guard
- Notes: No login, registration, or fee on the Colorado portal. Data is only reachable through per-state search forms with heterogeneous schemas, and no bulk download is documented; Colorado has also migrated its licensing portal at least once (an archived on | VERDICT REASON: The Colorado exemplar is verified live at the claimed URL with the Applicator ID key documented. Attention needed on the backbone framing: the AAPCO index PDF dates to 2017 and is partly contacts rather than databases, state portal coverage and schem

### src-49: FDNY Violations (NYC Open Data) [TOP20]
- URL: https://data.cityofnewyork.us/City-Government/fdny-violation/ktas-47y7
- Verdict: needs-attention | Access class: public-easy | Format: Socrata dataset on NYC Open Data; exportable via portal download and SODA/OData API (Excel/Tableau OData connection confirmed in search results); CSV/JSON export is the platform standard but exact fil
- Update frequency: Not stated in any search result; refresh cadence unconfirmed for ktas-47y7
- Freshness confirmed: Not confirmable from search snippets; dataset page returned as live in July 2026 search results but no last-updated date visible
- Entity key: NYC BIN/BBL (FDNY violation and account numbers secondary) | documented: False (Third-party guide says BIN (a 7-digit code unique to a single building) helps refine NYC FDNY violation searches, but no search result exposes the actual column list of ktas-47y7, )
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query ""ktas-47y7" FDNY violation NYC Open Data" -> https://data.cityofnewyork.us/City-Government/fdny-violation/ktas-47y7 (fdny violation | NYC Open Data)
- Backs: fdny-violation-clearance-lead-engine
- Notes: NYC Open Data is public with free Socrata API access (violationwatch.nyc confirms free API); no login wall or fee found in search results; Socrata app token optional for higher rate limits | VERDICT REASON: The claimed URL is live, but search results cannot confirm BIN/BBL as documented columns of ktas-47y7, cannot confirm its update cadence or last data period, and show a sibling dataset 'FDNY Violations' (avgm-ztsb) on the same portal that may be the 

### src-51: BACKFLOW PREVENTER dataset (NYC Open Data)
- URL: https://data.cityofnewyork.us/City-Government/BACKFLOW-PREVENTER/38n4-tikp
- Verdict: needs-attention | Access class: public-easy | Format: Socrata dataset on NYC Open Data (portal export plus SODA API is the platform standard); exact export file names and any attached data dictionary not visible in search snippets
- Update frequency: Not stated in any search result; refresh cadence unconfirmed
- Freshness confirmed: Not confirmable from search snippets; the dataset page was reported as indexed as of October 2025 and still returns as live in July 2026 searches, but no last-updated date or data period visible
- Entity key: NYC BBL/address plus DEP backflow device number | documented: False (No search result exposes the dataset's column list, so BBL, address, or DEP device number could not be confirmed as documented fields from search receipts; NYC311 confirms building)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query ""38n4-tikp" BACKFLOW PREVENTER NYC Open Data" -> https://data.cityofnewyork.us/City-Government/BACKFLOW-PREVENTER/38n4-tikp (BACKFLOW PREVENTER - NYC Open Data)
- Backs: nyc-backflow-testing-radar
- Notes: NYC Open Data public dataset; no login wall, key requirement, or fee found in search results | VERDICT REASON: Dataset is live at the claimed URL and matches the DEP backflow program, but search results could not confirm the claimed entity keys (BBL/address, DEP device number) as documented fields, nor the update cadence or most recent data period; pull the S

### src-52: EPA Enforcement Actions under Title VI of the Clean Air Act
- URL: https://www.epa.gov/ozone-layer-protection/enforcement-actions-under-title-vi-clean-air-act
- Verdict: needs-attention | Access class: public-hard-to-parse | Format: Static HTML prose page listing completed enforcement cases (company name, penalty, settlement description) with links to case pages; no structured download (csv/xlsx/API) surfaced in any search result
- Update frequency: No stated cadence; EPA describes it as a partial list of recent, major completed cases; snapshot copies from January 2017 and January 2021 exist, indicating an occasionally updated static page
- Freshness confirmed: Most recent case confirmable from search receipts is the Schnitzer Steel settlement announced April 2022 ($1,550,000 civil penalty plus $1,700,000 in compliance measures across 40 facilities); no 2023
- Entity key: EPA FRS ID | documented: False (No search result shows FRS IDs anywhere on this page; cases are identified only by company name in prose (Trident Seafoods, Trader Joe's, Southeastern Grocers, Schnitzer Steel), so)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "EPA "enforcement actions under Title VI of the Clean Air Act" ozone layer protection" -> https://www.epa.gov/ozone-layer-protection/enforcement-actions-under-title-vi-clean-air-act (Enforcement Actions under Title VI of the Clean Air Act | US EPA)
- Backs: refrigerant-608-leakwatch
- Notes: Public webpage, no login or fee; hard-to-parse because content is narrative case summaries rather than a machine-readable dataset | VERDICT REASON: Page is live at the claimed URL, but it is an unstructured prose list of major completed cases with no FRS IDs, no machine-readable format, no stated update cadence, and the newest confirmable case dates to April 2022. Weak as a product backbone; for

### src-65: Consolidated Screening List (CSL) downloadable files and API
- URL: https://www.trade.gov/consolidated-screening-list
- Verdict: needs-attention | Access class: public-easy (downloads and search) / public-registration (API requires a free API key) | Format: Downloadable files named csl-yyyy-mm-dd.csv or .tsv; CSL search engine; JSON REST API (with fuzzy name search) via ITA developer portal at developer.trade.gov. Consolidates 11 Commerce, State, and Tre
- Update frequency: All tools updated automatically every day at 5:00 AM EST/EDT (trade.gov stated cadence).
- Freshness confirmed: Daily refresh at 5:00 AM ET per trade.gov; current as of the 2026-07-04 search date. Third parties (OpenSanctions) actively mirror the feed.
- Entity key: FMC OTI license number (licensed forwarder/NVOCC list at www2.fmc.gov/oti), plus CSL entity name matching | documented: False (The FMC OTI license list (licensed/registered ocean freight forwarders and NVOCCs, including license numbers and renewal dates) is a separate FMC database at www2.fmc.gov/oti (Lice)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "Consolidated Screening List trade.gov download CSV JSON API" -> https://www.trade.gov/consolidated-screening-list (Consolidated Screening List (trade.gov))
- Backs: forwarder-screening-evidence-pack
- Notes: CSV/TSV downloads and the search UI need no login or fee. Since the 10/13/2021 ITA Developer Portal upgrade, the CSL API requires signing up at developer.trade.gov for a free API key. | VERDICT REASON: The CSL itself is verified live with daily updates, free CSV/TSV downloads, and a free-key API. But the claimed entity key (FMC OTI license number) is not a documented CSL field; it belongs to the separate FMC OTI list at www2.fmc.gov/oti. Any CSL-to

### src-69: NAIC Consumer Information Source (CIS) closed complaint reports
- URL: https://content.naic.org/cis_agg_disposition.htm
- Verdict: needs-attention | Access class: public-hard-to-parse | Format: HTML report pages backed by embedded Tableau dashboards (tableau.naic.org) plus a PDF version of the aggregate disposition report (eapps.naic.org). Per-company reports are retrieved through the CIS lo
- Update frequency: Not officially documented in search results. Complaint indices are computed per calendar year and third-party guides say CIS shows roughly the past three years of closed complaint data; NAIC publishes
- Freshness confirmed: Latest CIS data year could not be directly confirmed from search results. Ecosystem evidence: Kansas DOI publishes a Complaint Index 2024 Report built on NAIC complaint index methodology, indicating c
- Entity key: NAIC company code (CoCode) | documented: True (Per-company CIS complaint reports are addressed by a COCODE URL parameter (example COCODE=23043), confirming the NAIC company code is the operative key of CIS complaint reports.)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "NAIC Consumer Information Source CIS closed complaint reports aggregate disposition" -> https://content.naic.org/cis_agg_disposition.htm (Closed Confirmed Consumer Complaints by Disposition - CIS)
- Backs: naic-complaint-market-conduct-exposure
- Notes: Free, no login or fee for the CIS lookup and aggregate report pages. However, data is delivered as per-company Tableau dashboard embeds and HTML/PDF report pages rather than downloadable files, so programmatic use means scraping Tableau views. NAIC s | VERDICT REASON: Page is live and the CoCode key is confirmed (it is literally the URL parameter of CIS reports), but as a product backbone this source has three gaps: no bulk download or API surfaced (per-company Tableau scraping required), no published refresh cade

### src-74: State veterinary board license registries (TX, CA, AZ first)
- URL: https://apps.veterinary.texas.gov/s/licenseelookup (TX); https://search.dca.ca.gov/ (CA); https://vetboard.az.gov/licensee-directory-1 (AZ)
- Verdict: needs-attention | Access class: public-hard-to-parse | Format: Interactive HTML web lookup portals, no confirmed bulk CSV or API for TX or AZ: TX is a Salesforce-based Licensee Lookup app searchable by name, license number, or zip; CA is the DCA License Search to
- Update frequency: Lookup tools reflect current board records on a continuous basis with no published cycle for TX or AZ. CA DCA licensee data files are refreshed automatically at the beginning of each month per DCA pub
- Freshness confirmed: Live, currently maintained board records as of July 2026: all three lookups surface in current search results as the official verification tools. CA DCA licensee data files refresh at the beginning of
- Entity key: State veterinary license number plus DEA registration number (per veterinarian) | documented: False (State license number IS a documented search field of the state lookups (TX lookup searchable by license number; CA DCA search displays license type, status, expiration), but DEA re)
- Observed status this session: blocked_by_sandbox_egress_403 (see egress_probe_log.jsonl); content verification via live WebSearch receipts
- Live receipt: query "Texas veterinary board license lookup apps.veterinary.texas.gov licensee lookup TDLR transfer" -> https://apps.veterinary.texas.gov/s/licenseelookup (Licensee Lookup)
- Backs: vet-group-dea-license-compliance-packet
- Notes: All three state lookups are free, public, and require no login, API key, or fee for single-record queries. However TX and AZ expose only form-based per-record search with no documented bulk export, so backbone ingestion would require scraping; CA is  | VERDICT REASON: All three state registries are verified live and official (TX at the exact claimed URL, CA via search.dca.ca.gov, AZ via vetboard.az.gov), so the source is usable, but three issues need attention. First, the claimed entity key is only half documented

## 6. Recommended first build and three Fable build briefs

### Recommended first build: OATH/ECB Summons Defense Packet Generator

Not the biggest market; the best combination, criterion by criterion:
- Accessible data: the backbone is a daily Socrata feed NSigma's existing BBL
  pipeline can ingest this week (verified-live receipt, documented keys, plus the
  OATH outcomes dataset for the statistics layer). No registration, no scraping.
- Acute pain: weekly summons flow, hard hearing dates, default judgments at
  statutory maximums plus interest (receipted). The buyer is already losing money
  on a clock.
- Fast build: 4-week MVP on existing infrastructure; the only genuinely new work
  is the charge-code rules table and the packet templates.
- Clear buyer: NYC managing agents and owner-operators NSigma already understands
  from its CRE work, enumerable through HPD registration contacts keyed to the
  same BBL as the product.
- Willingness to pay: an entire expeditor and OATH-attorney trade already bills
  for this per summons; ViolationWatch and SiteCompli prove subscription budgets
  exist at both ends of the price range.
- Low liability with the v1 scoping: data, deadlines, eligibility flags, evidence
  checklists, and draft-for-professional-review templates; no filing, no legal
  advice, expeditors as channel rather than target.
- Expansion room: the same buyer, spine, and platform absorb FISP (rank 3),
  elevator CAT1 (rank 6), boiler (rank 15), FDNY (rank 14), and LL97 (rank 11)
  as modules; five top-20 candidates are one NYC compliance platform in sequence,
  and Chicago (rank 19) is the replication proof.

Runner-up considered: SNF PBJ Guardrail (rank 2) has the cleaner moat story
against a single incumbent and a national market, but its pre-submission wedge
depends on customer file uploads from a cold start, while OATH's wedge works with
zero customer data on day 1. Build OATH first, PBJ second; they share nothing
except the playbook, which de-risks NSigma's product motion across two verticals.

Three ready-to-run Fable build briefs (full text in briefs/):
1. briefs/brief-1-oath-ecb-defense-packet.md (recommended first build)
2. briefs/brief-2-snf-pbj-guardrail.md
3. briefs/brief-3-fisp-deadline-radar.md


## 7. Run integrity: kills, downgrades, unverified items, decisions

### Kill list (8)
- clearinghouse-compliance-autopilot (gates, gates: g4_public_source,g6_mvp_6wk): g4_public_source: Per-driver Clearinghouse records require registered-employer authentication and driver consent; the public side is aggregate summary reporting only, with no USD; g6_mvp_6wk: No public API or bulk data exists; an MVP would require automating the authenticated federal portal with customer credentials, which is out of bounds and not a 
- rcra-inspection-readiness-packet (gates, gates: g3_repetition): g3_repetition: The purchased workflow (mock audit before an agency inspection) is annual at best: EPA-mandated annual inspections apply only to federal TSDFs and generator ins
- ll87-energy-audit-radar (gates, gates: g3_repetition): g3_repetition: FAILS: each building files once every 10 years (calendar year matching the tax block last digit). Even a 100-building portfolio averages only about 10 filings a
- tx-rising-star-level-defense (gates, gates: g2_buyer_spend): g2_buyer_spend: FATAL: providers do not currently pay for this problem; Workforce Boards assign each program a mentor who provides one-on-one mentoring, training, and resources
- refrigerant-608-leakwatch (gates, gates: g4_public_source): g4_public_source: FAIL: the MVP-carrying data (per-appliance charge sizes, leak events, service records) is owner-held recordkeeping under 40 CFR Part 82, not public; only enforc
- part107-waiver-draft-factory (gates, gates: g3_repetition): g3_repetition: FAIL: a given operator files a waiver, then waits 180+ days, and a grant covers ongoing operations for years, so the per-organization cadence is roughly annual 
- ipeds-keyholder-autopilot (gates, gates: g1_acute_pain,g3_repetition): g1_acute_pain: Fine authority exists (up to 71,545 USD per violation under 34 CFR 668.92, referral to FSA after Spring collection) but I found no confirmed instance of an IPED; g3_repetition: IPEDS is 12 components collected across Fall, Winter, and Spring windows, but each component is submitted once per year; this is seasonal annual work, not a wee
- ieepa-tariff-refund-cape-pack (adversarial): Customs business licensure (19 CFR Part 111) exposure for claim prep-for-compensation; refund window mostly consumed ($95B queued, $40B disbursed via brokers by June 2026); DOJ appeal pending; backbone is ImportYeti, a registration-gated commercial mirror, not a public spine

Every killed candidate still has its pain point in the atlas with a cap flag; kills are data, not waste.

### Score changes from the adversarial review (all adjudicated, full trail in data/scanner_scores.jsonl)
- npdes-dmr-citizen-suit-radar lead_magnet_strength 10 -> 8 [adversarial]: Anchor 9-10 requires assembly the buyer has never seen; ECHO effluent charts and exceedance search are free and facility-specific, so the buyer partly knows the content (7-8 anchor)
- npdes-dmr-citizen-suit-radar quick_buildability 7 -> 6 [adversarial]: Access class is public-hard-to-parse with giant per-fiscal-year zips since FY2009 plus NODI and limit-set logic; that is the 5-6 anchor (one gnarly format, giant zips), not 7-8 minor normalization
- oath-ecb-summons-defense-packet lead_magnet_strength 10 -> 8 [adversarial]: Anchor 9-10 requires numbers the buyer has never seen assembled; free lookups (dobguard) and incumbent monitors (SiteCompli, Violation Watch) mean the buyer partly knows the content, which is the 7-8 anchor
- ll97-penalty-exposure-beam-prep lead_magnet_strength 9 -> 7 [adversarial]: Anchor 9-10 requires numbers never seen assembled; at least six free LL97 penalty calculators exist including a city-run one, so the buyer partly knows the content, the 7-8 anchor
- ma-agency-plan-exit-retention-packet buyer_urgency 10 -> 8 [adversarial]: Anchor 9-10 requires pain hitting this month or quarter; crosswalk and ANOC pressure lands Sept-Dec, making this recurring seasonal pressure, the 7-8 anchor, as the dossier's own g3 caveat admits
- snf-pbj-fivestar-guardrail lead_magnet_strength 9 -> 7 [adversarial]: Anchor 7-8 fits: buyer partly knows the content because CMS preview reports and SimplePBJ projections already show the staffing star; the peer benchmark and audit flags are useful but not never-seen
- hha-hhvbp-payment-risk-benchmark lead_magnet_strength 8 -> 5 [adversarial]: Anchor 5-6 at best: the regulator hands the buyer the same cohort, percentile, and TPS content quarterly for free, so the magnet is a thin restatement rather than unseen assembly
- fei-supplier-gmp-surveillance lead_magnet_strength 8 -> 6 [adversarial]: Anchor 5-6 is a personalized but thin lookup summary; with free FDA-tracking tools live, the snapshot does not meet the 7-8 bar of content the buyer cannot already get
- ll152-gas-piping-inspection-radar quick_buildability 9 -> 7 [adversarial]: Anchor 9-10 requires a single clean machine-readable source; an XLSX-on-a-webpage plus per-building portal status checks is 1-2 sources with real key-matching and scraping work, the 7 boundary at best
- ll152-gas-piping-inspection-radar lead_magnet_strength 8 -> 6 [adversarial]: Without filing status the artifact is a thin due-window lookup, anchor 5-6, and free LL152 schedule content is already widespread
- fdny-violation-clearance-lead-engine lead_magnet_strength 8 -> 6 [adversarial]: Anchor 5-6 is a personalized but thin lookup summary; with free equivalents live at dobguard.com the magnet does not clear the 7-8 bar of useful-and-not-already-available
- fdny-violation-clearance-lead-engine quick_buildability 9 -> 8 [verification]: Verification receipt (src-49): BIN/BBL could not be confirmed as documented columns of the FDNY violations dataset and a sibling dataset creates selection ambiguity; buildability assumes address-matching fallback
- msha-aggregates-regulator-view-benchmark buyer_urgency 8 -> 6 [adversarial]: Anchor 7-8 requires recurring pressure with real dollar consequences on a clock; unannounced inspections create episodic enforcement against a chronic cost, the textbook 5-6 anchor where the buyer can defer a quarter
- ieepa-tariff-refund-cape-pack quick_buildability 6 -> 4 [adversarial]: Anchor 3-4 covers scraping portals; the spine is a competitor's registration-walled site with CSV export gated behind a custom plan, closer to the 0-2 registration-wall anchor than to a 5-6 multi-source join
- ieepa-tariff-refund-cape-pack buyer_urgency 10 -> 8 [adversarial]: Urgency was 10 in March; with most refund volume already queued or paid via brokers and the appeal pending, this is recurring rolling-deadline pressure on a shrinking tail, the 7-8 anchor
- ieepa-tariff-refund-cape-pack consultancy_fit 8 -> 5 [adversarial]: Anchor 0-2 flags liability mismatch and 5-6 flags domain expertise NSigma must acquire; unlicensed customs-business exposure plus a one-time event, not a repeatable compliance-artifact motion, lands this at 5
- commercial-property-tax-appeal-packets consultancy_fit 8 -> 6 [adversarial]: Adjudicated translation of reviewer demote verdict: Ownwell ($50M funded) automates Cook County commercial appeals end to end and disintermediates the certiorari-firm buyer; selling packet tools to a buyer losing its market is a weak consultancy moti

Total post-judge changes: 17. Judge recalibration pass (pre-adversarial): 51 demotions, data/recalibration_log.json.

### Unverified items (stated plainly)
- No source content was fetched and parsed inside this sandbox (egress-blocked); all 75 receipts are R2 search-verified. scripts/verify_spines.py performs the R1 upgrade externally.
- SOC codes in atlas rows come from analyst knowledge; the O*NET API and bulk files were egress-blocked this session and rows are labeled accordingly.
- 12 sources carry needs-attention verdicts (detailed in section 5); affected candidates carry notes or logged downgrades.
- Dollar figures marked est. are labeled derivations or vendor-published anchors, not fetched invoices.
- Apollo total_entries counts are live platform counts this session (7 receipts in data/apollo_receipts.jsonl); list quality below the count level was not audited.


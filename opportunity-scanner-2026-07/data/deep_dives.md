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
(receipt: nycdb wiki). Supporting: OATH Hearings (rjte-hkhv), DOB Violations
(3h2n-5cm9), HPD registration datasets, CityPay payment status.

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

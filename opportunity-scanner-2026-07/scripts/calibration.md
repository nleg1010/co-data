# Dimension calibration anchors (0-10, LLM judgment layer)

These anchors force differentiation across the full range. A run where everything
scores 7 to 8 has failed its own calibration. Scores are assigned centrally by one
judge against these anchors; Python computes everything downstream.

## Quick Buildability (MVP in 2-6 weeks, spine cleanliness)
- 9-10: single clean machine-readable source with documented schema and stable entity key; MVP is fetch, join, render; 2-3 weeks solo.
- 7-8: 1-2 sources, minor normalization or key-matching work; 4-5 weeks.
- 5-6: multi-source joins, quarterly-lag files, or one gnarly format (fixed-width, giant zips); 6 weeks is tight.
- 3-4: fragmented per-state sources, scraping portals, OCR of PDFs; 6-week MVP only with scope cuts.
- 0-2: source requires registration walls per record, CAPTCHAs, FOIA, or the spine failed verification.

## Lead Magnet Strength (prospect-specific artifact from public data alone)
- 9-10: enter entity key, get a personalized artifact with dollar or risk numbers the buyer has never seen assembled (their violations, their score vs peers, their exposure); screenshot-worthy.
- 7-8: personalized and useful but the buyer partly knows the content (their own filings replayed) or numbers are directional.
- 5-6: personalized but thin (a lookup summary), or requires 2+ keys to assemble.
- 3-4: generic-with-name-inserted; benchmark exists but weak personal hook.
- 0-2: no meaningful prospect-specific artifact possible from public data.

## Buyer Urgency (pressure NOW: regulatory deadline, money leaking, enforcement wave)
- 9-10: named deadline or active enforcement with fines hitting this quarter (e.g. filing windows, audit cycles, penalty seasons); buyer already in pain this month.
- 7-8: recurring monthly/quarterly pressure with real dollar consequences, but survivable.
- 5-6: chronic cost, episodic enforcement; buyer can defer a quarter.
- 3-4: pain acknowledged but on annual cycles or discretionary.
- 0-2: speculative pain, no current spend trigger.

## Consultancy Fit (NSigma: small AI/data shop, industrial/compliance/asset-heavy buyers)
- 9-10: direct overlap with existing NSigma infrastructure (BBL, EPA FRS, CMS CCN, waste haulers) or identical stack pattern; buyer type NSigma already sells to.
- 7-8: same motion (public data, compliance artifact, industrial buyer), new dataset.
- 5-6: adjacent buyer or requires domain expertise NSigma must acquire.
- 3-4: consumer-adjacent, high-touch enterprise sales, or crowded horizontal.
- 0-2: wrong buyer, wrong stack, or reputational/liability mismatch.

## Outbound Clarity (buyer findable by title+NAICS on Apollo/LinkedIn; specific cold email writable)
- 9-10: exact title exists at volume (thousands on Apollo), NAICS clean, entity key ties prospect list to artifact automatically.
- 7-8: title findable with 2-3 variants; list buildable in a day.
- 5-6: role exists but title varies wildly or hides under generic ops titles.
- 3-4: buyer is the owner of small businesses with no titled role; list quality poor.
- 0-2: buyer not identifiable outbound (walk-in/referral only).

## Forced-spread rules
1. Rank candidates within each dimension before assigning numbers; the best gets 9-10 only if it truly meets the anchor, the worst in-scope gets its honest 1-3.
2. At least 15 percent of all dimension scores must land at or below 4, and at least 10 percent at 9 or above, or the judge re-examines the middle.
3. Gate-failed or spine-downgraded candidates take the hit in the relevant dimension (usually Quick Buildability), not a uniform haircut.

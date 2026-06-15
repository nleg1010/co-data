# CO-data

Routt County / Steamboat Springs residential absorption pipeline.

Goal:
- Pull Census BPS annual permit baseline.
- Scrape authenticated CityView permit data.
- Reconcile delivered vs active units.
- Produce Excel workbook and GC prospect CSV.

## First working slice

This repo now includes a minimal vertical slice for:
- downloading Census BPS county and place files for 2020-2025
- filtering Routt County and defensively attempting Steamboat Springs lookup
- saving raw BPS extracts to `raw/`
- creating a Postgres schema file in `sql/schema.sql`
- optionally applying that schema to a configured database
- capturing a non-destructive CityView discovery snapshot with Playwright
- generating an initial Excel workbook and GC CSV from whatever data exists

## Layout

- `src/co_data/` Python package
- `scripts/run_pipeline.py` CLI entrypoint
- `sql/schema.sql` database schema
- `tests/test_bps.py` parser tests

## Configuration

Environment variables are loaded from a local `.env` file if present. The loader is intentionally simple and does not require `python-dotenv`.

Supported variables:
- `CO_DATA_ROOT` optional override for output root; defaults to repo root
- `DATABASE_URL` optional Postgres DSN for `--stage schema`
- `CITYVIEW_BASE_URL` optional URL for `--stage cityview-discover`
- `CITYVIEW_USERNAME` optional, currently unused scaffold field
- `CITYVIEW_PASSWORD` optional, currently unused scaffold field

Example `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/routt_intel
CITYVIEW_BASE_URL=https://example-cityview-host/
```

## Run

From the repo root:

```bash
python3 scripts/run_pipeline.py --stage bps
python3 scripts/run_pipeline.py --stage workbook
python3 scripts/run_pipeline.py --stage cityview-discover
python3 scripts/run_pipeline.py --stage schema
```

Run everything in sequence:

```bash
python3 scripts/run_pipeline.py --stage all
```

## Outputs

- `raw/bps/routt_county_bps_2020_2025.csv`
- `raw/bps/steamboat_springs_bps_2020_2025.csv`
- `raw/bps/place_lookup_log.csv`
- `raw/cityview_discovery/` screenshots and html snapshots
- `output/routt_absorption_workbook.xlsx`
- `output/gc_prospects.csv`

If the Steamboat Springs place row is missing from a given BPS file, the pipeline logs the miss and continues.

## Tests

```bash
python3 -m unittest tests.test_bps
```

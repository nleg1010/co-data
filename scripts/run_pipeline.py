#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from co_data.bps import BPSExtract, fetch_target_bps, save_extract
from co_data.cityview import run_cityview_discovery
from co_data.config import get_settings
from co_data.db import apply_schema, write_schema_sql
from co_data.workbook import build_workbook


def stage_bps() -> BPSExtract:
    settings = get_settings()
    extract = fetch_target_bps()
    save_extract(extract, settings.raw_dir)
    return extract


def stage_schema() -> Path:
    settings = get_settings()
    schema_path = write_schema_sql(settings.sql_dir)
    if settings.database_url:
        apply_schema(settings.database_url, schema_path)
    return schema_path


def stage_workbook() -> tuple[Path, Path]:
    settings = get_settings()
    extract = fetch_target_bps()
    save_extract(extract, settings.raw_dir)
    return build_workbook(extract, settings.output_dir)


def stage_cityview_discover() -> Path:
    settings = get_settings()
    return run_cityview_discovery(settings.cityview_base_url, settings.raw_dir)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the CO-data pipeline.")
    parser.add_argument(
        "--stage",
        required=True,
        choices=["bps", "schema", "workbook", "cityview-discover", "all"],
    )
    args = parser.parse_args()

    if args.stage == "bps":
        extract = stage_bps()
        print(f"bps county_rows={len(extract.county_rows)} place_rows={len(extract.place_rows)}")
    elif args.stage == "schema":
        schema_path = stage_schema()
        print(f"schema_written={schema_path}")
    elif args.stage == "workbook":
        workbook_path, gc_csv_path = stage_workbook()
        print(f"workbook_written={workbook_path}")
        print(f"gc_csv_written={gc_csv_path}")
    elif args.stage == "cityview-discover":
        discovery_dir = stage_cityview_discover()
        print(f"cityview_discovery_dir={discovery_dir}")
    elif args.stage == "all":
        extract = stage_bps()
        schema_path = stage_schema()
        workbook_path, gc_csv_path = build_workbook(extract, get_settings().output_dir)
        discovery_dir = stage_cityview_discover()
        print(f"bps county_rows={len(extract.county_rows)} place_rows={len(extract.place_rows)}")
        print(f"schema_written={schema_path}")
        print(f"workbook_written={workbook_path}")
        print(f"gc_csv_written={gc_csv_path}")
        print(f"cityview_discovery_dir={discovery_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

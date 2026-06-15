from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from openpyxl import Workbook

from .bps import BPSExtract


def _append_sheet(workbook: Workbook, title: str, rows: list[dict[str, Any]]) -> None:
    sheet = workbook.create_sheet(title=title)
    if not rows:
        sheet.append(["status"])
        sheet.append(["empty"])
        return
    headers = list(rows[0].keys())
    sheet.append(headers)
    for row in rows:
        values = []
        for header in headers:
            value = row.get(header)
            if isinstance(value, dict):
                value = json.dumps(value, sort_keys=True)
            elif isinstance(value, list):
                value = json.dumps(value)
            values.append(value)
        sheet.append(values)


def build_workbook(extract: BPSExtract, output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    workbook_path = output_dir / "routt_absorption_workbook.xlsx"
    gc_csv_path = output_dir / "gc_prospects.csv"

    workbook = Workbook()
    summary = workbook.active
    summary.title = "summary"
    summary.append(["dataset", "rows"])
    summary.append(["routt_county_bps", len(extract.county_rows)])
    summary.append(["steamboat_place_bps", len(extract.place_rows)])
    summary.append(
        [
            "place_lookup_missing_years",
            sum(1 for row in extract.place_lookup_log if row.get("status") == "missing"),
        ]
    )

    _append_sheet(workbook, "county_bps", extract.county_rows)
    _append_sheet(workbook, "place_bps", extract.place_rows)
    _append_sheet(workbook, "place_lookup_log", extract.place_lookup_log)

    workbook.save(workbook_path)

    gc_rows: list[dict[str, Any]] = []
    for row in extract.county_rows + extract.place_rows:
        gc_rows.append(
            {
                "prospect_name": row.get("name"),
                "geography_type": row.get("geography_type"),
                "survey_date": row.get("survey_date"),
                "non_rep_unit_total": row.get("non_rep_unit_total"),
                "source_url": row.get("source_url"),
            }
        )

    with gc_csv_path.open("w", encoding="utf-8", newline="") as handle:
        if gc_rows:
            writer = csv.DictWriter(handle, fieldnames=list(gc_rows[0].keys()))
            writer.writeheader()
            writer.writerows(gc_rows)
        else:
            handle.write("")

    return workbook_path, gc_csv_path

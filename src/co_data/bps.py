from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Any

import requests


COUNTY_URL_TEMPLATE = "https://www2.census.gov/econ/bps/County/co{year}a.txt"
PLACE_URL_TEMPLATE = "https://www2.census.gov/econ/bps/Place/West%20Region/we{year}a.txt"

TARGET_STATE_FIPS = "08"
TARGET_COUNTY_FIPS = "107"
TARGET_PLACE_FIPS = "73825"
TARGET_PLACE_NAME = "steamboat springs"
TARGET_YEARS = range(2020, 2026)
PLACE_MATCH_FIPS_KEY = "fips_place_code"
PLACE_MATCH_NAME_KEY = "place_name"


@dataclass(frozen=True)
class BPSExtract:
    county_rows: list[dict[str, Any]]
    place_rows: list[dict[str, Any]]
    place_lookup_log: list[dict[str, Any]]


def _slug(value: str) -> str:
    value = value.strip().lower().replace("+", "plus")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def _combine_headers(row1: list[str], row2: list[str]) -> list[str]:
    headers: list[str] = []
    previous_top = ""
    seen: dict[str, int] = {}

    for top, bottom in zip(row1, row2):
        top = top.strip()
        bottom = bottom.strip()
        if top:
            previous_top = top
        base_parts = [part for part in (top or previous_top, bottom) if part]
        name = _slug("_".join(base_parts)) or "column"
        seen[name] = seen.get(name, 0) + 1
        if seen[name] > 1:
            name = f"{name}_{seen[name]}"
        headers.append(name)
    return headers


def parse_bps_text(text: str) -> list[dict[str, Any]]:
    lines = text.splitlines()
    non_empty = [line for line in lines if line.strip()]
    if len(non_empty) < 3:
        return []

    header_row_1 = next(csv.reader([non_empty[0]]))
    header_row_2 = next(csv.reader([non_empty[1]]))
    headers = _combine_headers(header_row_1, header_row_2)

    records: list[dict[str, Any]] = []
    for row in csv.reader(StringIO("\n".join(non_empty[2:]))):
        if not row or not any(cell.strip() for cell in row):
            continue
        if len(row) < len(headers):
            row = row + [""] * (len(headers) - len(row))
        record = {headers[idx]: row[idx].strip() for idx in range(len(headers))}
        records.append(record)
    return records


def fetch_bps_file(url: str, timeout: int = 60) -> str:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def _to_int(value: str | None) -> int | None:
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def _normalize_name(value: str | None) -> str:
    return re.sub(r"\s+", " ", (value or "").strip())


def _get_place_code(record: dict[str, Any]) -> str:
    return (record.get(PLACE_MATCH_FIPS_KEY) or "").strip()


def _build_common_row(
    record: dict[str, Any],
    geography_type: str,
    source_url: str,
    year: int,
) -> dict[str, Any]:
    metric_keys = [
        key
        for key in record
        if key.endswith("_units") and "rep" not in key and key not in {"months_rep"}
    ]
    non_rep_unit_total = sum(_to_int(record[key]) or 0 for key in metric_keys)

    return {
        "survey_date": _to_int(record.get("survey_date")) or year,
        "geography_type": geography_type,
        "state_fips": (record.get("fips_state") or record.get("state_code") or "").strip(),
        "county_fips": (record.get("fips_county") or record.get("county_code") or "").strip(),
        "place_fips": _get_place_code(record),
        "name": _normalize_name(
            record.get("county_name") or record.get("place_name") or record.get("place")
        ),
        "months_reported": _to_int(record.get("number_of_months_rep")),
        "non_rep_unit_total": non_rep_unit_total,
        "source_url": source_url,
        "raw_record": record,
    }


def fetch_target_bps() -> BPSExtract:
    county_rows: list[dict[str, Any]] = []
    place_rows: list[dict[str, Any]] = []
    place_lookup_log: list[dict[str, Any]] = []

    for year in TARGET_YEARS:
        county_url = COUNTY_URL_TEMPLATE.format(year=year)
        county_records = parse_bps_text(fetch_bps_file(county_url))
        county_match = next(
            (
                record
                for record in county_records
                if (record.get("fips_state") or "").strip() == TARGET_STATE_FIPS
                and (record.get("fips_county") or "").strip() == TARGET_COUNTY_FIPS
            ),
            None,
        )
        if county_match:
            county_rows.append(_build_common_row(county_match, "county", county_url, year))

        place_url = PLACE_URL_TEMPLATE.format(year=year)
        place_records = parse_bps_text(fetch_bps_file(place_url))
        candidates = [
            record
            for record in place_records
            if (record.get("state_code") or "").strip() == TARGET_STATE_FIPS
        ]
        routt_candidates = [
            record for record in candidates if (record.get("county_code") or "").strip() == TARGET_COUNTY_FIPS
        ]
        steamboat_text_matches = [
            record
            for record in candidates
            if "steamboat" in _normalize_name(record.get(PLACE_MATCH_NAME_KEY)).lower()
        ]
        place_match = next(
            (
                record
                for record in routt_candidates
                if _get_place_code(record) == TARGET_PLACE_FIPS
                or _normalize_name(record.get(PLACE_MATCH_NAME_KEY)).lower() == TARGET_PLACE_NAME
            ),
            None,
        )
        if place_match:
            place_rows.append(_build_common_row(place_match, "place", place_url, year))
            place_lookup_log.append(
                {
                    "year": year,
                    "status": "found",
                    "matched_name": _normalize_name(place_match.get(PLACE_MATCH_NAME_KEY)),
                    "matched_place_fips": _get_place_code(place_match),
                    "routt_county_appears": "yes" if routt_candidates else "no",
                    "steamboat_text_appears": "yes" if steamboat_text_matches else "no",
                    "colorado_records_scanned": len(candidates),
                    "match_keys": f"county_code={TARGET_COUNTY_FIPS};{PLACE_MATCH_FIPS_KEY}={TARGET_PLACE_FIPS};{PLACE_MATCH_NAME_KEY}={TARGET_PLACE_NAME}",
                    "source_url": place_url,
                }
            )
        else:
            place_lookup_log.append(
                {
                    "year": year,
                    "status": "missing",
                    "matched_name": "",
                    "matched_place_fips": "",
                    "routt_county_appears": "yes" if routt_candidates else "no",
                    "steamboat_text_appears": "yes" if steamboat_text_matches else "no",
                    "colorado_records_scanned": len(candidates),
                    "match_keys": f"county_code={TARGET_COUNTY_FIPS};{PLACE_MATCH_FIPS_KEY}={TARGET_PLACE_FIPS};{PLACE_MATCH_NAME_KEY}={TARGET_PLACE_NAME}",
                    "source_url": place_url,
                }
            )

    return BPSExtract(
        county_rows=county_rows,
        place_rows=place_rows,
        place_lookup_log=place_lookup_log,
    )


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return

    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def save_extract(extract: BPSExtract, raw_dir: Path) -> dict[str, Path]:
    bps_dir = raw_dir / "bps"
    county_path = bps_dir / "routt_county_bps_2020_2025.csv"
    place_path = bps_dir / "steamboat_springs_bps_2020_2025.csv"
    log_path = bps_dir / "place_lookup_log.csv"

    _write_csv(county_path, extract.county_rows)
    _write_csv(place_path, extract.place_rows)
    _write_csv(log_path, extract.place_lookup_log)

    return {
        "county": county_path,
        "place": place_path,
        "log": log_path,
    }

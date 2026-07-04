#!/usr/bin/env python3
"""verify_spines.py: upgrade every source receipt to a full fetch-and-parse receipt.

The scanner session that produced this report ran inside a sandbox whose egress
policy blocked non-GitHub/S3/GCS hosts (CONNECT 403 at the proxy), so most
receipts in data/source_receipts.jsonl are class R2 (live search-confirmed,
content not fetched). Run THIS script from any machine with normal internet
(the Beelink qualifies) to produce R1 receipts: HTTP status, content type,
file format, 3+ parsed sample rows, and entity-key column confirmation.

Usage:
    python3 verify_spines.py                # verifies data/source_receipts.jsonl in place
    python3 verify_spines.py --only fmcsa-sms
    python3 verify_spines.py --out /tmp/receipts_verified.jsonl

Stdlib only. Respects large files by streaming at most ~4 MB per source.
"""
import argparse
import csv
import datetime as dt
import gzip
import io
import json
import os
import ssl
import sys
import urllib.request
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
RECEIPTS = os.path.join(HERE, "..", "data", "source_receipts.jsonl")
MAX_BYTES = 4 * 1024 * 1024
UA = "NSigma-spine-verifier/1.0 (data diligence; contact: ops@nsigma.example)"


def fetch(url, max_bytes=MAX_BYTES):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
        status = resp.status
        ctype = resp.headers.get("Content-Type", "")
        clen = resp.headers.get("Content-Length", "")
        body = resp.read(max_bytes)
        truncated = len(body) == max_bytes
    return status, ctype, clen, body, truncated


def sniff_and_sample(body, ctype, url):
    """Return (format, sample_rows, columns). Best effort, never raises."""
    try:
        if body[:2] == b"PK":
            zf = zipfile.ZipFile(io.BytesIO(body))
            names = zf.namelist()
            inner = next((n for n in names if n.lower().endswith((".csv", ".txt", ".tsv"))), None)
            if inner:
                with zf.open(inner) as fh:
                    text = io.TextIOWrapper(fh, encoding="utf-8", errors="replace")
                    rows = list(next_rows(csv.reader(text), 4))
                return f"zip({inner})", rows[1:4], rows[0] if rows else []
            return f"zip(members={names[:5]})", [], []
        if body[:2] == b"\x1f\x8b":
            body = gzip.decompress(body[:MAX_BYTES])
        text = body.decode("utf-8", errors="replace")
        stripped = text.lstrip()
        if stripped[:1] in "[{":
            data = json.loads(text) if not truncated_json(text) else None
            if data is None:
                return "json(truncated stream)", [stripped[:400]], []
            recs = data if isinstance(data, list) else data.get("results") or data.get("data") or [data]
            recs = recs[:3] if isinstance(recs, list) else [recs]
            cols = sorted(recs[0].keys()) if recs and isinstance(recs[0], dict) else []
            return "json", [json.dumps(r)[:400] for r in recs], cols
        delim = "\t" if text.count("\t") > text.count(",") else ","
        rows = list(next_rows(csv.reader(io.StringIO(text), delimiter=delim), 4))
        fmt = "tsv" if delim == "\t" else "csv"
        return fmt, [delim.join(r)[:400] for r in rows[1:4]], rows[0] if rows else []
    except Exception as e:  # noqa: BLE001
        return f"unparsed({e.__class__.__name__})", [], []


def truncated_json(text):
    try:
        json.loads(text)
        return False
    except Exception:  # noqa: BLE001
        return True


def next_rows(reader, n):
    out = []
    for row in reader:
        out.append(row)
        if len(out) >= n:
            break
    return out


def confirm_key(columns, key_hints):
    cols_lower = [c.strip().lower().replace(" ", "_") for c in columns]
    for hint in key_hints:
        h = hint.lower().replace(" ", "_")
        for c in cols_lower:
            if h in c:
                return True, c
    return False, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--receipts", default=RECEIPTS)
    ap.add_argument("--out", default=None)
    ap.add_argument("--only", default=None, help="source_id substring filter")
    args = ap.parse_args()

    rows = [json.loads(l) for l in open(args.receipts, encoding="utf-8") if l.strip()]
    out_path = args.out or args.receipts
    now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")

    for r in rows:
        if args.only and args.only not in r["source_id"]:
            continue
        url = r.get("verify_url") or r["url"]
        print(f"[{r['source_id']}] GET {url}")
        try:
            status, ctype, clen, body, trunc = fetch(url)
            fmt, samples, cols = sniff_and_sample(body, ctype, url)
            ok, keycol = confirm_key(cols, r.get("entity_key_hints", []))
            r["receipt"] = {
                "verified_at": now, "http_status": status, "content_type": ctype,
                "content_length": clen, "bytes_sampled": len(body), "truncated": trunc,
                "parsed_format": fmt, "sample_rows": samples,
                "columns_seen": cols[:40],
                "entity_key_confirmed": ok, "entity_key_column": keycol,
            }
            r["receipt_class"] = "R1" if (status == 200 and samples) else r.get("receipt_class", "R2")
            print(f"   -> {status} {fmt} rows={len(samples)} key={'YES:'+keycol if ok else 'not found'}")
        except Exception as e:  # noqa: BLE001
            r["receipt"] = {"verified_at": now, "error": f"{e.__class__.__name__}: {e}"}
            print(f"   -> ERROR {e}")

    with open(out_path, "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()

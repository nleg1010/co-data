from __future__ import annotations

from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright


def run_cityview_discovery(base_url: str | None, raw_dir: Path) -> Path:
    discovery_dir = raw_dir / "cityview_discovery"
    discovery_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    notes_path = discovery_dir / f"{timestamp}_notes.txt"

    if not base_url:
        notes_path.write_text(
            "CITYVIEW_BASE_URL not configured. Discovery stage skipped.\n",
            encoding="utf-8",
        )
        return discovery_dir

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(base_url, wait_until="domcontentloaded", timeout=60000)
        page.screenshot(path=str(discovery_dir / f"{timestamp}_landing.png"), full_page=True)
        (discovery_dir / f"{timestamp}_landing.html").write_text(
            page.content(),
            encoding="utf-8",
        )
        notes_path.write_text(
            f"Visited {base_url} with no form submission or credential entry.\n",
            encoding="utf-8",
        )
        browser.close()

    return discovery_dir

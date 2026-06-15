from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def load_dotenv(dotenv_path: Path) -> None:
    if not dotenv_path.exists():
        return

    for raw_line in dotenv_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        os.environ.setdefault(key, value)


@dataclass(frozen=True)
class Settings:
    repo_root: Path
    raw_dir: Path
    output_dir: Path
    sql_dir: Path
    database_url: str | None
    cityview_base_url: str | None
    cityview_username: str | None
    cityview_password: str | None


def get_settings() -> Settings:
    repo_root = Path(__file__).resolve().parents[2]
    load_dotenv(repo_root / ".env")

    configured_root = os.environ.get("CO_DATA_ROOT")
    root = Path(configured_root).resolve() if configured_root else repo_root

    return Settings(
        repo_root=root,
        raw_dir=root / "raw",
        output_dir=root / "output",
        sql_dir=root / "sql",
        database_url=os.environ.get("DATABASE_URL"),
        cityview_base_url=os.environ.get("CITYVIEW_BASE_URL"),
        cityview_username=os.environ.get("CITYVIEW_USERNAME"),
        cityview_password=os.environ.get("CITYVIEW_PASSWORD"),
    )

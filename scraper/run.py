"""
Main entry point for the scraper.

Fetches zip-level market stats from Redfin's public S3 dataset and writes
JSON files to docs/data/ for the frontend to consume.

Each metro JSON file accumulates up to MAX_PERIODS quarterly snapshots.
On each run, the new period is prepended only if it differs from the most
recent stored period (deduplicating by period_begin + period_end).

Usage:
    python -m scraper.run
"""

import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

from .config import ZIP_CODES, METROS
from .redfin import fetch_zip_stats

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

OUT_DIR = Path(__file__).parent.parent / "docs" / "data"
MAX_PERIODS = 8  # keep ~2 years of quarterly history


def run():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fetched_at = datetime.now(timezone.utc).isoformat()

    # Fetch stats for all configured zip codes in one streaming pass
    stats_by_zip = fetch_zip_stats(set(ZIP_CODES.keys()))

    # Group zips by metro, merging config lat/lon with fetched stats
    metro_zips: dict = {metro_id: [] for metro_id in METROS}

    for zip_code, cfg in ZIP_CODES.items():
        metro = cfg["metro"]
        stats = stats_by_zip.get(zip_code)
        if stats is None:
            logger.warning("No data found for zip %s (%s) — skipping", zip_code, cfg["city"])
            continue

        entry = {
            "zip": zip_code,
            "city": cfg["city"],
            "state": cfg["state"],
            "lat": cfg["lat"],
            "lon": cfg["lon"],
            **stats,
        }
        metro_zips[metro].append(entry)

    # Write one JSON file per metro
    metros_out = []
    for metro_id, metro_info in METROS.items():
        zips = metro_zips[metro_id]
        if not zips:
            continue

        # Determine the period from the fetched data
        sample = zips[0]
        new_period = {
            "period_begin": sample.get("period_begin"),
            "period_end":   sample.get("period_end"),
            "fetched_at":   fetched_at,
            "zip_count":    len(zips),
            "zips":         zips,
        }

        # Load existing periods and prepend the new one if it's not a duplicate
        path = OUT_DIR / f"{metro_id}.json"
        periods = _load_existing_periods(path)
        periods = _merge_period(periods, new_period)

        _write_json(path, {
            "metro":      metro_id,
            "fetched_at": fetched_at,
            "periods":    periods,
        })
        metros_out.append({
            "id":       metro_id,
            "name":     metro_info["name"],
            "center":   metro_info["center"],
            "zoom":     metro_info["zoom"],
            "zip_count": len(zips),
        })

    _write_json(OUT_DIR / "metros.json", {"fetched_at": fetched_at, "metros": metros_out})
    logger.info("All done. Data written to %s", OUT_DIR)


def _load_existing_periods(path: Path) -> list:
    """Load periods from an existing metro JSON file.

    Handles both the new multi-period format and the old flat format,
    so the first run after this change converts files automatically.
    """
    if not path.exists():
        return []
    try:
        with open(path) as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

    if "periods" in data:
        return data["periods"]

    # Old flat format — convert to single-period list
    if "zips" in data and data["zips"]:
        sample = data["zips"][0]
        return [{
            "period_begin": sample.get("period_begin"),
            "period_end":   sample.get("period_end"),
            "fetched_at":   data.get("fetched_at"),
            "zip_count":    len(data["zips"]),
            "zips":         data["zips"],
        }]

    return []


def _merge_period(periods: list, new_period: dict) -> list:
    """Prepend new_period if its date range isn't already stored; keep MAX_PERIODS."""
    key = (new_period.get("period_begin"), new_period.get("period_end"))
    for existing in periods:
        if (existing.get("period_begin"), existing.get("period_end")) == key:
            logger.info(
                "Period %s–%s already stored — skipping duplicate.",
                key[0], key[1],
            )
            return periods

    return ([new_period] + periods)[:MAX_PERIODS]


def _write_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    logger.info("Wrote %s", path.name)


if __name__ == "__main__":
    run()

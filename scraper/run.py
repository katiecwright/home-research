"""
Main entry point for the scraper.

Fetches zip-level market stats from Redfin's public S3 dataset and writes
JSON files to docs/data/ for the frontend to consume.

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

        _write_json(
            OUT_DIR / f"{metro_id}.json",
            {
                "metro": metro_id,
                "fetched_at": fetched_at,
                "count": len(zips),
                "zips": zips,
            },
        )
        metros_out.append(
            {
                "id": metro_id,
                "name": metro_info["name"],
                "center": metro_info["center"],
                "zoom": metro_info["zoom"],
                "zip_count": len(zips),
            }
        )

    _write_json(OUT_DIR / "metros.json", {"fetched_at": fetched_at, "metros": metros_out})
    logger.info("All done. Data written to %s", OUT_DIR)


def _write_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    logger.info("Wrote %s", path.name)


if __name__ == "__main__":
    run()

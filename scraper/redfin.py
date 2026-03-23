"""
Fetches zip code market stats from Redfin's public S3 dataset.

Redfin publishes a weekly-updated aggregate market tracker file:
  https://redfin-public-data.s3.us-west-2.amazonaws.com/redfin_market_tracker/zip_code_market_tracker.tsv000.gz

The file is ~1.5 GB compressed. To avoid re-downloading it on every run,
this module caches it locally at ~/.cache/price_diffs/redfin_zip_market.tsv.gz
and reuses it for up to 7 days (matching Redfin's weekly update cadence).

Key metrics extracted per zip code:
  avg_sale_to_list    — ratio of sale to list price (1.05 = 5% over asking)
  sale_vs_list_pct    — same as percentage: +5.0 or -3.0
  sold_above_list_pct — % of homes that closed above their list price
  median_sale_price   — median final sale price
  median_list_price   — median list price at time of listing
  median_dom          — median days on market
  homes_sold          — transaction count in the period
"""

import csv
import gzip
import logging
import shutil
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

logger = logging.getLogger(__name__)

S3_URL = (
    "https://redfin-public-data.s3.us-west-2.amazonaws.com"
    "/redfin_market_tracker/zip_code_market_tracker.tsv000.gz"
)

CACHE_DIR  = Path.home() / ".cache" / "price_diffs"
CACHE_FILE = CACHE_DIR / "redfin_zip_market.tsv.gz"
CACHE_MAX_AGE = timedelta(days=7)

# Filter constants — quarterly all-residential data
PROPERTY_TYPE   = "All Residential"
PERIOD_DURATION = 90


# ── Public API ────────────────────────────────────────────────────────────────

def fetch_zip_stats(zip_codes: set) -> dict:
    """
    Return the most recent quarterly stats for each zip code in zip_codes.

    On the first call (or after 7 days), downloads the Redfin S3 file and
    caches it locally. Subsequent calls read from the cache and finish in
    seconds rather than minutes.

    Returns:
        Dict mapping zip_code (str) → stats dict.
        Zips not found in the dataset are omitted.
    """
    _ensure_cache()
    return _filter_cache(zip_codes)


# ── Cache management ──────────────────────────────────────────────────────────

def _cache_is_fresh() -> bool:
    if not CACHE_FILE.exists():
        return False
    age = datetime.now() - datetime.fromtimestamp(CACHE_FILE.stat().st_mtime)
    return age < CACHE_MAX_AGE


def _ensure_cache():
    """Download the S3 file to local cache if missing or older than 7 days.

    Supports resume: if a partial .tmp file exists from a previous interrupted
    download, sends a Range request to continue from where it left off.
    No socket timeout is set — the file is large and slow connections need time.
    """
    if _cache_is_fresh():
        age_hours = int((datetime.now() - datetime.fromtimestamp(CACHE_FILE.stat().st_mtime)).total_seconds() // 3600)
        logger.info("Using cached Redfin data (age: ~%dh). Delete %s to force refresh.", age_hours, CACHE_FILE)
        return

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    tmp = CACHE_FILE.with_suffix(".tmp")
    existing_bytes = tmp.stat().st_size if tmp.exists() else 0

    if existing_bytes > 0:
        logger.info("Resuming Redfin download from %.0f MB…", existing_bytes / 1_000_000)
    else:
        logger.info("Downloading Redfin S3 market tracker to local cache (~1.5 GB)…")
    logger.info("Cache location: %s", CACHE_FILE)

    headers = {}
    if existing_bytes > 0:
        headers["Range"] = f"bytes={existing_bytes}-"

    try:
        req = urllib.request.Request(S3_URL, headers=headers)
        # No timeout — large file on slow connections needs unlimited time
        with urllib.request.urlopen(req) as response:
            mode = "ab" if existing_bytes > 0 else "wb"
            with open(tmp, mode) as f:
                shutil.copyfileobj(response, f, length=8 * 1024 * 1024)  # 8 MB chunks
        tmp.rename(CACHE_FILE)
        logger.info("Download complete. Cached to %s", CACHE_FILE)
    except Exception as e:
        # Leave tmp intact so the next run can resume
        raise RuntimeError(f"Download failed at {tmp.stat().st_size / 1_000_000:.0f} MB: {e}") from e


# ── Filtering ─────────────────────────────────────────────────────────────────

def _filter_cache(zip_codes: set) -> dict:
    """Read the local cache and extract the most recent row per zip code."""
    logger.info("Filtering cached data for %d zip code(s)…", len(zip_codes))
    best: dict = {}

    with gzip.open(CACHE_FILE, "rt", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows_read = 0
        for row in reader:
            rows_read += 1

            region = row.get("REGION", "").strip('"')
            if not region.startswith("Zip Code: "):
                continue
            zip_code = region[len("Zip Code: "):]
            if zip_code not in zip_codes:
                continue

            if row.get("PROPERTY_TYPE", "").strip('"') != PROPERTY_TYPE:
                continue
            try:
                if int(row.get("PERIOD_DURATION", 0)) != PERIOD_DURATION:
                    continue
            except ValueError:
                continue

            period_end = row.get("PERIOD_END", "").strip('"')
            if zip_code not in best or period_end > best[zip_code]["period_end"]:
                best[zip_code] = _parse_row(zip_code, period_end, row)

    logger.info("Scanned %d rows. Found data for %d/%d zip(s).", rows_read, len(best), len(zip_codes))
    return best


# ── Row parsing ───────────────────────────────────────────────────────────────

def _parse_row(zip_code: str, period_end: str, row: dict) -> dict:
    """Normalize a raw TSV row into the stats dict written to JSON."""

    def num(key, scale=1.0):
        val = row.get(key, "").strip('"')
        try:
            return round(float(val) * scale, 4) if val not in ("", "NA", "null") else None
        except ValueError:
            return None

    avg_stl = num("AVG_SALE_TO_LIST")
    return {
        "zip": zip_code,
        "period_end":   period_end,
        "period_begin": row.get("PERIOD_BEGIN", "").strip('"'),
        "parent_metro": row.get("PARENT_METRO_REGION", "").strip('"'),
        # Core price-diff metrics
        "avg_sale_to_list":    avg_stl,
        "sale_vs_list_pct":    round((avg_stl - 1) * 100, 2) if avg_stl is not None else None,
        "sold_above_list_pct": num("SOLD_ABOVE_LIST", scale=100),  # 0.45 → 45.0
        # Prices
        "median_sale_price": num("MEDIAN_SALE_PRICE"),
        "median_list_price": num("MEDIAN_LIST_PRICE"),
        # Activity
        "homes_sold":      num("HOMES_SOLD"),
        "median_dom":      num("MEDIAN_DOM"),
        "inventory":       num("INVENTORY"),
        "months_of_supply": num("MONTHS_OF_SUPPLY"),
        "new_listings":    num("NEW_LISTINGS"),
    }

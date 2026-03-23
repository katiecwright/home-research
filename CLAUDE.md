# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Fetches aggregate real estate market data from Redfin's free public S3 dataset and visualizes sale-vs-list price ratios on an interactive map. Each zip code is rendered as a bubble sized by transaction volume and colored by the selected metric (sale vs. list %, median price, or days on market). Key metric: `avg_sale_to_list` (e.g., 1.05 = homes sell for 5% over asking on average).

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the scraper manually (writes JSON to web/data/)
python -m scraper.run

# Serve the frontend locally (must be a server, not file://)
cd web && python -m http.server 8000
# then open http://localhost:8000
```

The scraper also runs automatically every day via GitHub Actions (`.github/workflows/daily_scrape.yml`), which commits updated JSON files back to the repo.

## Architecture

**No backend server.** The frontend reads static JSON files that the Python scraper pre-generates and commits to the repo. GitHub Pages serves `web/` directly.

```
scraper/config.py   ← add new zip codes / metros here (requires lat/lon per zip)
scraper/redfin.py   ← streams Redfin S3 file, extracts aggregate stats per zip
scraper/run.py      ← orchestrates scraper, writes web/data/{metro_id}.json
web/data/           ← generated JSON files (committed by CI, gitignored for local runs)
web/index.html      ← single-page app shell
web/app.js          ← Leaflet map, bubble markers, heatmap, stats panel
web/style.css       ← sidebar + map layout
```

## Data flow

1. `scraper/run.py` calls `redfin.fetch_zip_stats(zip_codes)` once
2. `redfin.py` streams the Redfin S3 file (~1.5 GB gzip) line by line, extracting rows matching the configured zip codes and keeping the most recent quarterly period per zip
3. Results are merged with lat/lon from `config.py` and written to `web/data/{metro_id}.json`
4. The frontend reads `metros.json` on load, then fetches `{metro_id}.json` for the selected metro
5. Each zip = one bubble: size = homes sold, color = selected metric (sale vs. list, price, DOM)

## Adding a new zip code or metro

Edit `scraper/config.py`:
- Add the zip to `ZIP_CODES` with `city`, `state`, `metro`, `lat`, `lon`
  - Get lat/lon from maps.google.com: search the zip code, right-click the center → "What's here?"
- Add the metro to `METROS` if it doesn't exist (needs `name`, `center` lat/lng, `zoom`)

## GitHub Pages setup

After pushing to GitHub:
1. Go to repo Settings → Pages
2. Set source to "Deploy from a branch"
3. Branch: `main`, folder: `/web`
4. The site will be live at `https://{username}.github.io/{repo}/`

## Known limitations

- The Redfin S3 file is ~1.5 GB compressed. Streaming it takes 1-3 minutes depending on network speed.
- Data updates weekly (Redfin's cadence), so running daily only picks up changes once a week.
- Stats are aggregated quarterly per zip code — not per individual property.
- Zip codes with very low transaction volume (< ~5 sales) may have unreliable stats in the dataset.

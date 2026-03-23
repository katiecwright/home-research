# TODO

## Filters & Dimensions
- Add property type filter (SFH, condo, multi-family, etc.)
  - Redfin's dataset includes a `PROPERTY_TYPE` column — scraper currently filters to "All Residential" only; would need to fetch and store per-type breakdowns

## Data Enrichment
- Incorporate school quality data by zip code
  - Potential sources: GreatSchools API, NCES public data
- Display average/median home sale price prominently to help quickly rule out price-range mismatches
  - Median sale price is already in the data (`median_sale_price`) — this is more of a UI/display change
- Add walk/bike/transit scores by zip code
  - Walk Score has a free API
- Add crime data by zip code
  - Several free public sources available

## Map UX
- Price trend indicators on bubbles — once 2+ quarters of history exist, show a small up/down arrow on each bubble indicating whether the zip is heating up or cooling down
- Shareable URL — encode selected zoom, metric, and period in the URL hash so a specific map view can be bookmarked or shared

## Polish
- Mobile layout — sidebar + map likely doesn't render well on small screens; revisit once feature set stabilizes

# TODO

## Filters & Dimensions
- Add property type filter (SFH, condo, multi-family, etc.)
  - Redfin's dataset includes a `PROPERTY_TYPE` column — scraper currently filters to "All Residential" only; would need to fetch and store per-type breakdowns

## Data Enrichment
- Incorporate school quality data by zip code
  - Potential sources: GreatSchools API, NCES public data
- Display average/median home sale price prominently to help quickly rule out price-range mismatches
  - Median sale price is already in the data (`median_sale_price`) — this is more of a UI/display change

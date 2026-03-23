/**
 * Price Diffs — frontend app
 *
 * Data flow:
 *   docs/data/metros.json      → list of metros; used to fetch all metro files
 *   docs/data/{metro_id}.json  → one entry per zip code with aggregate market stats
 *
 * All metros are loaded on startup and rendered simultaneously.
 * The "Zoom to" dropdown navigates the map but never filters data.
 *
 * Each zip code is rendered as a single bubble on the map.
 * Bubble size  = homes sold (transaction volume)
 * Bubble color = selected metric (sale vs. list, price, or days on market)
 */

const DATA_DIR = "data/";

// ── Color scales ─────────────────────────────────────────────────────────────

// price_delta ($): sale price minus list price in dollars
const PRICE_DELTA_SCALE = [
  { threshold:  100_000, color: "#b71c1c" },  // >+$100K over asking
  { threshold:   20_000, color: "#ff7043" },  // +$20K–$100K
  { threshold:  -20_000, color: "#ffc107" },  // within ±$20K
  { threshold: -100_000, color: "#4caf50" },  // -$20K–-$100K
  { threshold: -Infinity, color: "#1a7a1a" }, // >$100K under asking
];

// sale_vs_list_pct: negative = below asking (red), positive = above asking (green)
const SALE_VS_LIST_SCALE = [
  { threshold:  10, color: "#b71c1c" },  // strongly above asking
  { threshold:   2, color: "#ff7043" },  // above asking
  { threshold:  -2, color: "#ffc107" },  // near asking
  { threshold: -10, color: "#4caf50" },  // below asking
  { threshold: -Infinity, color: "#1a7a1a" },
];

// median_sale_price: cool (blue) = affordable → warm (red) = expensive
const PRICE_SCALE = [
  { threshold: 2_000_000, color: "#7b1fa2" },
  { threshold: 1_500_000, color: "#c62828" },
  { threshold: 1_000_000, color: "#ef6c00" },
  { threshold:   700_000, color: "#f9a825" },
  { threshold:   400_000, color: "#558b2f" },
  { threshold:         0, color: "#1565c0" },
];

// median_dom: green = fast market, red = slow
const DOM_SCALE = [
  { threshold: 60, color: "#b71c1c" },
  { threshold: 30, color: "#ff7043" },
  { threshold: 14, color: "#ffc107" },
  { threshold:  7, color: "#4caf50" },
  { threshold:  0, color: "#1a7a1a" },
];

const METRIC_CONFIG = {
  price_delta: {
    scale: PRICE_DELTA_SCALE,
    format: (z) => {
      const delta = z.median_sale_price != null && z.median_list_price != null
        ? z.median_sale_price - z.median_list_price
        : null;
      if (delta == null) return "—";
      const sign = delta >= 0 ? "+" : "";
      return sign + fmt$(delta);
    },
    legend: [
      { label: ">+$100K over asking",  color: "#b71c1c" },
      { label: "+$20K to +$100K",      color: "#ff7043" },
      { label: "±$20K",                color: "#ffc107" },
      { label: "−$20K to −$100K",      color: "#4caf50" },
      { label: "<−$100K under asking", color: "#1a7a1a" },
    ],
    legendTitle: "Avg sale vs. list ($ delta)",
    value: (z) => z.median_sale_price != null && z.median_list_price != null
      ? z.median_sale_price - z.median_list_price
      : null,
  },
  sale_vs_list: {
    scale: SALE_VS_LIST_SCALE,
    format: (z) => z.sale_vs_list_pct != null
      ? `${z.sale_vs_list_pct >= 0 ? "+" : ""}${z.sale_vs_list_pct.toFixed(1)}%`
      : "—",
    legend: [
      { label: ">+10% over asking",  color: "#b71c1c" },
      { label: "+2% to +10%",        color: "#ff7043" },
      { label: "±2%",                color: "#ffc107" },
      { label: "−2% to −10%",        color: "#4caf50" },
      { label: "<−10% under asking", color: "#1a7a1a" },
    ],
    legendTitle: "Avg sale vs. asking",
    value: (z) => z.sale_vs_list_pct,
  },
  median_sale_price: {
    scale: PRICE_SCALE,
    format: (z) => fmt$(z.median_sale_price),
    legend: [
      { label: ">$2M",        color: "#7b1fa2" },
      { label: "$1.5M–$2M",   color: "#c62828" },
      { label: "$1M–$1.5M",   color: "#ef6c00" },
      { label: "$700K–$1M",   color: "#f9a825" },
      { label: "$400K–$700K", color: "#558b2f" },
      { label: "<$400K",      color: "#1565c0" },
    ],
    legendTitle: "Median sale price",
    value: (z) => z.median_sale_price,
  },
  median_dom: {
    scale: DOM_SCALE,
    format: (z) => z.median_dom != null ? `${z.median_dom} days` : "—",
    legend: [
      { label: ">60 days", color: "#b71c1c" },
      { label: "30–60",    color: "#ff7043" },
      { label: "14–30",    color: "#ffc107" },
      { label: "7–14",     color: "#4caf50" },
      { label: "<7 days",  color: "#1a7a1a" },
    ],
    legendTitle: "Median days on market",
    value: (z) => z.median_dom,
  },
};

// ── State ─────────────────────────────────────────────────────────────────────

let map;
let currentLayers = [];
let currentMetric = "price_delta";
let currentViz    = "markers";
let allZips       = [];

// ── Init ──────────────────────────────────────────────────────────────────────

document.addEventListener("DOMContentLoaded", async () => {
  initMap();
  bindControls();
  await loadAllData();
});

function initMap() {
  map = L.map("map", { zoomControl: true });
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19,
  }).addTo(map);
}

function bindControls() {
  document.getElementById("zoom-select").addEventListener("change", onZoomChange);

  document.getElementById("metric-toggle").addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-metric]");
    if (!btn) return;
    setActiveButton("metric-toggle", btn);
    currentMetric = btn.dataset.metric;
    if (allZips.length) render(allZips);
    updateLegend();
  });

  document.getElementById("viz-toggle").addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-viz]");
    if (!btn) return;
    setActiveButton("viz-toggle", btn);
    currentViz = btn.dataset.viz;
    if (allZips.length) render(allZips);
  });
}

// ── Data loading ──────────────────────────────────────────────────────────────

const STATE_NAMES = { CA: "California", OR: "Oregon", WA: "Washington", NY: "New York" };

async function loadAllData() {
  const metrosData = await fetchJSON(DATA_DIR + "metros.json");
  if (!metrosData || !metrosData.metros || !metrosData.metros.length) {
    document.getElementById("zoom-select").innerHTML =
      "<option>No data yet — run the scraper first</option>";
    return;
  }

  // Fetch all metro files in parallel
  const results = await Promise.all(
    metrosData.metros.map(async (m) => {
      const data = await fetchJSON(DATA_DIR + m.id + ".json");
      return { meta: m, data };
    })
  );

  // Flatten all zips
  allZips = results.flatMap((r) => r.data?.zips ?? []);

  // Group metros by state (derived from the zip data itself)
  const metrosByState = {};
  for (const { meta, data } of results) {
    if (!data?.zips?.length) continue;
    const state = data.zips[0].state;
    if (!metrosByState[state]) metrosByState[state] = [];
    metrosByState[state].push({ meta, zips: data.zips });
  }

  buildZoomDropdown(metrosByState);

  // Fit initial map view to all loaded data
  const mappable = allZips.filter((z) => z.lat && z.lon);
  if (mappable.length) {
    map.fitBounds(L.latLngBounds(mappable.map((z) => [z.lat, z.lon])), { padding: [40, 40] });
  }

  // Use the most recent fetched_at across all metros
  const fetchedAt = results
    .map((r) => r.data?.fetched_at)
    .filter(Boolean)
    .sort()
    .at(-1);

  setDataDate(fetchedAt, allZips[0]);
  render(allZips);
  updateLegend();
}

function buildZoomDropdown(metrosByState) {
  const select = document.getElementById("zoom-select");
  select.innerHTML = "";

  for (const [state, metros] of Object.entries(metrosByState)) {
    const stateName = STATE_NAMES[state] || state;
    const group = document.createElement("optgroup");
    group.label = stateName;

    // State-level zoom option
    const stateOpt = document.createElement("option");
    stateOpt.value = `state:${state}`;
    stateOpt.textContent = `${stateName} (all)`;
    group.appendChild(stateOpt);

    // Individual metro options
    for (const { meta } of metros) {
      const opt = document.createElement("option");
      opt.value = `metro:${meta.id}`;
      opt.textContent = meta.name;
      opt.dataset.center = JSON.stringify(meta.center);
      opt.dataset.zoom   = meta.zoom;
      group.appendChild(opt);
    }

    select.appendChild(group);
  }
}

function onZoomChange() {
  const select = document.getElementById("zoom-select");
  const val    = select.value;

  if (val.startsWith("state:")) {
    const state     = val.slice(6);
    const stateZips = allZips.filter((z) => z.state === state && z.lat && z.lon);
    if (stateZips.length) {
      map.fitBounds(L.latLngBounds(stateZips.map((z) => [z.lat, z.lon])), { padding: [40, 40] });
    }
  } else if (val.startsWith("metro:")) {
    const opt = select.options[select.selectedIndex];
    map.setView(JSON.parse(opt.dataset.center), parseInt(opt.dataset.zoom, 10));
  }
}

// ── Rendering ─────────────────────────────────────────────────────────────────

function render(zips) {
  clearLayers();
  if (currentViz === "heatmap") {
    renderHeatmap(zips);
  } else {
    renderBubbles(zips);
  }
}

function renderBubbles(zips) {
  const cfg = METRIC_CONFIG[currentMetric];

  for (const z of zips) {
    if (z.lat == null || z.lon == null) continue;

    const value  = cfg.value(z);
    const color  = valueToColor(value, cfg.scale);
    const radius = homesToRadius(z.homes_sold);

    const circle = L.circleMarker([z.lat, z.lon], {
      radius,
      fillColor: color,
      color: "#fff",
      weight: 1.5,
      fillOpacity: 0.82,
    });

    circle.addTo(map);
    currentLayers.push(circle);

    circle.on("click", () => showStats(z));
    circle.bindTooltip(
      `<b>${z.zip}</b> — ${z.city}, ${z.state}<br>${cfg.format(z)}<br>${z.homes_sold != null ? z.homes_sold + " homes sold" : ""}`,
      { direction: "top", offset: [0, -radius] }
    );
  }
}

function renderHeatmap(zips) {
  const cfg = METRIC_CONFIG[currentMetric];
  const values = zips.map((z) => cfg.value(z)).filter((v) => v != null);
  const maxVal = Math.max(...values) || 1;

  const points = zips
    .filter((z) => z.lat != null && z.lon != null && cfg.value(z) != null)
    .map((z) => [z.lat, z.lon, cfg.value(z) / maxVal]);

  const heat = L.heatLayer(points, {
    radius: 35,
    blur: 25,
    maxZoom: 17,
    gradient: { 0.2: "#313695", 0.5: "#fdae61", 0.8: "#f46d43", 1.0: "#a50026" },
  });
  heat.addTo(map);
  currentLayers.push(heat);
}

// ── Stats panel ───────────────────────────────────────────────────────────────

function showStats(z) {
  const panel = document.getElementById("stats");
  panel.classList.remove("hidden");

  const stlPct   = z.sale_vs_list_pct;
  const delta    = z.median_sale_price != null && z.median_list_price != null
    ? z.median_sale_price - z.median_list_price : null;
  const stlEl    = document.getElementById("stat-stl");
  const deltaEl  = document.getElementById("stat-delta");

  document.getElementById("stat-zip").textContent = `${z.zip} — ${z.city}, ${z.state}`;

  deltaEl.textContent = delta != null ? `${delta >= 0 ? "+" : ""}${fmt$(delta)}` : "—";
  deltaEl.className = "stat-value " + (delta == null ? "" : delta >= 0 ? "negative" : "positive");

  stlEl.textContent = stlPct != null
    ? `${stlPct >= 0 ? "+" : ""}${stlPct.toFixed(1)}%`
    : "—";
  stlEl.className = "stat-value " + (stlPct == null ? "" : stlPct >= 0 ? "negative" : "positive");

  document.getElementById("stat-above").textContent  = z.sold_above_list_pct != null
    ? `${z.sold_above_list_pct.toFixed(1)}%`
    : "—";
  document.getElementById("stat-price").textContent  = fmt$(z.median_sale_price);
  document.getElementById("stat-dom").textContent    = z.median_dom != null ? `${z.median_dom}` : "—";
  document.getElementById("stat-sold").textContent   = z.homes_sold != null ? z.homes_sold : "—";
  document.getElementById("stat-period").textContent =
    z.period_begin && z.period_end ? `${z.period_begin} → ${z.period_end}` : "—";
}

// ── Legend ────────────────────────────────────────────────────────────────────

function updateLegend() {
  const cfg = METRIC_CONFIG[currentMetric];
  const el  = document.getElementById("legend");
  el.innerHTML = `<div class="legend-title">${cfg.legendTitle}</div>` +
    cfg.legend.map((row) =>
      `<div class="legend-row">
        <span class="swatch" style="background:${row.color}"></span>
        ${row.label}
      </div>`
    ).join("");
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function clearLayers() {
  for (const layer of currentLayers) map.removeLayer(layer);
  currentLayers = [];
}

function valueToColor(value, scale) {
  if (value == null) return "#9e9e9e";
  for (const { threshold, color } of scale) {
    if (value >= threshold) return color;
  }
  return scale[scale.length - 1].color;
}

function homesToRadius(homes) {
  // Scale bubble size by transaction volume (log scale, 6–20px range)
  if (!homes) return 8;
  return Math.max(6, Math.min(20, Math.log10(homes + 1) * 8));
}

function fmt$(n) {
  if (n == null) return "—";
  const sign = n < 0 ? "-" : "";
  const abs  = Math.abs(n);
  if (abs >= 1_000_000) return sign + "$" + (abs / 1_000_000).toFixed(2) + "M";
  if (abs >= 1_000)     return sign + "$" + Math.round(abs / 1_000) + "K";
  return sign + "$" + abs.toLocaleString();
}

function setActiveButton(groupId, activeBtn) {
  for (const btn of document.getElementById(groupId).querySelectorAll("button")) {
    btn.classList.toggle("active", btn === activeBtn);
  }
}

function setDataDate(fetchedAt, sampleZip) {
  const el = document.getElementById("data-date");
  const lines = [];
  if (sampleZip && sampleZip.period_begin && sampleZip.period_end) {
    const fmt = (d) => new Date(d + "T00:00:00").toLocaleDateString("en-US", { month: "short", year: "numeric" });
    lines.push(`Period: ${fmt(sampleZip.period_begin)} – ${fmt(sampleZip.period_end)}`);
  }
  if (fetchedAt) {
    lines.push("Updated " + new Date(fetchedAt).toLocaleDateString());
  }
  el.textContent = lines.join(" · ");
}

async function fetchJSON(url) {
  try {
    const res = await fetch(url);
    if (!res.ok) return null;
    return await res.json();
  } catch {
    return null;
  }
}

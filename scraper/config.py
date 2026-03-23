"""
Configuration for zip codes and metro areas.

Each zip code entry requires:
  - city, state: display labels
  - metro: key into METROS dict
  - lat, lon: centroid coordinates for the map marker
               (look up at maps.google.com — right-click → "What's here?")
"""

ZIP_CODES = {
    # ── Berkeley / El Cerrito / Kensington, CA ───────────────────────────────
    # Note: Kensington is unincorporated and shares zips 94707/94708 with Berkeley
    "94702": {"city": "Berkeley",   "state": "CA", "metro": "berkeley", "lat": 37.8716, "lon": -122.2727},
    "94703": {"city": "Berkeley",   "state": "CA", "metro": "berkeley", "lat": 37.8651, "lon": -122.2674},
    "94704": {"city": "Berkeley",   "state": "CA", "metro": "berkeley", "lat": 37.8601, "lon": -122.2596},
    "94705": {"city": "Berkeley",   "state": "CA", "metro": "berkeley", "lat": 37.8490, "lon": -122.2437},
    "94706": {"city": "Albany",     "state": "CA", "metro": "berkeley", "lat": 37.8877, "lon": -122.2969},
    "94707": {"city": "Kensington", "state": "CA", "metro": "berkeley", "lat": 37.8907, "lon": -122.2763},  # N Berkeley / Kensington
    "94708": {"city": "Kensington", "state": "CA", "metro": "berkeley", "lat": 37.8927, "lon": -122.2559},  # Berkeley Hills / Kensington
    "94709": {"city": "Berkeley",   "state": "CA", "metro": "berkeley", "lat": 37.8783, "lon": -122.2652},
    "94710": {"city": "Berkeley",   "state": "CA", "metro": "berkeley", "lat": 37.8648, "lon": -122.2977},
    "94530": {"city": "El Cerrito", "state": "CA", "metro": "berkeley", "lat": 37.9232, "lon": -122.3018},

    # ── San Francisco, CA ─────────────────────────────────────────────────────
    "94102": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7784, "lon": -122.4177},  # Tenderloin / Civic Center
    "94103": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7727, "lon": -122.4099},  # SoMa
    "94104": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7916, "lon": -122.4018},  # Financial District
    "94105": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7877, "lon": -122.3964},  # Embarcadero / Rincon Hill
    "94107": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7601, "lon": -122.3974},  # Potrero Hill / Mission Bay
    "94108": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7924, "lon": -122.4077},  # Chinatown / Nob Hill
    "94109": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7952, "lon": -122.4215},  # Russian Hill / Polk Gulch
    "94110": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7490, "lon": -122.4153},  # Mission District
    "94111": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7985, "lon": -122.3989},  # Jackson Square
    "94112": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7213, "lon": -122.4426},  # Excelsior / Outer Mission
    "94114": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7585, "lon": -122.4340},  # Castro / Noe Valley
    "94115": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7843, "lon": -122.4378},  # Western Addition / Fillmore
    "94116": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7436, "lon": -122.4847},  # West Portal / Forest Hill
    "94117": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7702, "lon": -122.4469},  # Haight-Ashbury
    "94118": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7823, "lon": -122.4598},  # Inner Richmond
    "94121": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7776, "lon": -122.4941},  # Outer Richmond
    "94122": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7566, "lon": -122.4876},  # Inner / Outer Sunset
    "94123": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.8009, "lon": -122.4367},  # Marina
    "94124": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7343, "lon": -122.3936},  # Bayview / Hunters Point
    "94127": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7354, "lon": -122.4600},  # West Portal / Forest Knolls
    "94131": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7416, "lon": -122.4377},  # Glen Park
    "94132": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7222, "lon": -122.4756},  # Lake Merced / SFSU
    "94133": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.8005, "lon": -122.4104},  # North Beach / Telegraph Hill
    "94134": {"city": "San Francisco", "state": "CA", "metro": "san_francisco", "lat": 37.7147, "lon": -122.4086},  # Visitacion Valley / Portola

    # ── Oakland, CA ───────────────────────────────────────────────────────────
    "94601": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.7631, "lon": -122.2198},  # Fruitvale
    "94602": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.7879, "lon": -122.2131},  # Dimond / Glenview
    "94603": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.7451, "lon": -122.1879},  # Eastmont
    "94605": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.7632, "lon": -122.1721},  # Millsmont
    "94606": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.7767, "lon": -122.2410},  # San Antonio
    "94607": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.8074, "lon": -122.2905},  # West Oakland
    "94608": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.8366, "lon": -122.2836},  # Emeryville / N Oakland
    "94609": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.8333, "lon": -122.2619},  # Temescal
    "94610": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.8086, "lon": -122.2336},  # Grand Lake
    "94611": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.8273, "lon": -122.2183},  # Montclair / Piedmont Ave
    "94612": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.8110, "lon": -122.2666},  # Downtown / Uptown
    "94613": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.7722, "lon": -122.1987},  # Allendale
    "94618": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.8391, "lon": -122.2472},  # Rockridge
    "94619": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.7973, "lon": -122.1936},  # Redwood Heights
    "94621": {"city": "Oakland", "state": "CA", "metro": "oakland", "lat": 37.7491, "lon": -122.2036},  # Coliseum / San Antonio

    # ── Portland, OR ─────────────────────────────────────────────────────────
    "97201": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5104, "lon": -122.6905},  # SW / Downtown
    "97202": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.4802, "lon": -122.6396},  # SE
    "97203": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5939, "lon": -122.7367},  # St. Johns
    "97204": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5227, "lon": -122.6784},  # Downtown
    "97205": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5208, "lon": -122.6994},  # West Hills
    "97206": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.4756, "lon": -122.5960},  # SE
    "97209": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5295, "lon": -122.6857},  # Pearl District
    "97210": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5418, "lon": -122.7019},  # NW
    "97211": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5739, "lon": -122.6439},  # NE
    "97212": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5457, "lon": -122.6393},  # NE / Irvington
    "97213": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5348, "lon": -122.5905},  # NE
    "97214": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5161, "lon": -122.6384},  # SE / Buckman
    "97215": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5141, "lon": -122.5986},  # SE
    "97216": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5082, "lon": -122.5531},  # SE
    "97217": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5923, "lon": -122.6880},  # N / Kenton
    "97218": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5675, "lon": -122.5862},  # NE / Airport
    "97219": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.4656, "lon": -122.7098},  # SW
    "97220": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5396, "lon": -122.5398},  # NE
    "97221": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.4992, "lon": -122.7414},  # SW / Raleigh Hills
    "97222": {"city": "Milwaukie", "state": "OR", "metro": "portland", "lat": 45.4399, "lon": -122.6148}, # Milwaukie
    "97223": {"city": "Tigard",    "state": "OR", "metro": "portland", "lat": 45.4342, "lon": -122.7693}, # Tigard
    "97224": {"city": "Tigard",    "state": "OR", "metro": "portland", "lat": 45.3934, "lon": -122.7754}, # Tigard SW
    "97225": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5106, "lon": -122.7559},  # Cedar Hills
    "97227": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5453, "lon": -122.6795},  # N / Mississippi
    "97229": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5437, "lon": -122.8202},  # NW / Bethany
    "97230": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5440, "lon": -122.4829},  # NE / Parkrose
    "97232": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5269, "lon": -122.6447},  # NE / Lloyd
    "97233": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.5006, "lon": -122.4966},  # SE / Centennial
    "97236": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.4748, "lon": -122.5196},  # SE / Pleasant Valley
    "97239": {"city": "Portland", "state": "OR", "metro": "portland", "lat": 45.4925, "lon": -122.7026},  # SW / Hillsdale

    # ── Lamorinda (Walnut Creek / Orinda), CA ────────────────────────────────
    "94563": {"city": "Orinda",       "state": "CA", "metro": "lamorinda", "lat": 37.8771, "lon": -122.1797},
    "94595": {"city": "Walnut Creek", "state": "CA", "metro": "lamorinda", "lat": 37.8716, "lon": -122.0608},
    "94596": {"city": "Walnut Creek", "state": "CA", "metro": "lamorinda", "lat": 37.9002, "lon": -122.0623},
    "94597": {"city": "Walnut Creek", "state": "CA", "metro": "lamorinda", "lat": 37.9264, "lon": -122.0571},
    "94598": {"city": "Walnut Creek", "state": "CA", "metro": "lamorinda", "lat": 37.9185, "lon": -122.0233},

    # ── South Marin County, CA ────────────────────────────────────────────────
    "94965": {"city": "Sausalito",     "state": "CA", "metro": "south_marin", "lat": 37.8590, "lon": -122.4853},
    "94941": {"city": "Mill Valley",   "state": "CA", "metro": "south_marin", "lat": 37.9060, "lon": -122.5448},
    "94920": {"city": "Tiburon",       "state": "CA", "metro": "south_marin", "lat": 37.8794, "lon": -122.4571},
    "94925": {"city": "Corte Madera",  "state": "CA", "metro": "south_marin", "lat": 37.9254, "lon": -122.5244},
    "94939": {"city": "Larkspur",      "state": "CA", "metro": "south_marin", "lat": 37.9343, "lon": -122.5344},
    "94904": {"city": "Greenbrae",     "state": "CA", "metro": "south_marin", "lat": 37.9446, "lon": -122.5238},
    "94960": {"city": "San Anselmo",   "state": "CA", "metro": "south_marin", "lat": 37.9743, "lon": -122.5616},
    "94930": {"city": "Fairfax",       "state": "CA", "metro": "south_marin", "lat": 37.9871, "lon": -122.5888},

    # ── Upstate New York (add later) ──────────────────────────────────────────
    # "12203": {"city": "Albany",    "state": "NY", "metro": "upstate_ny", "lat": 42.6955, "lon": -73.8270},
    # "14201": {"city": "Buffalo",   "state": "NY", "metro": "upstate_ny", "lat": 42.8967, "lon": -78.8764},
    # "14604": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1566, "lon": -77.6088},
    # "13202": {"city": "Syracuse",  "state": "NY", "metro": "upstate_ny", "lat": 43.0481, "lon": -76.1474},
}

METROS = {
    "berkeley": {
        "name": "Berkeley / El Cerrito, CA",
        "center": [37.8900, -122.2850],
        "zoom": 12,
    },
    "lamorinda": {
        "name": "Lamorinda (Walnut Creek / Orinda), CA",
        "center": [37.8980, -122.0700],
        "zoom": 12,
    },
    "south_marin": {
        "name": "South Marin County, CA",
        "center": [37.9200, -122.5300],
        "zoom": 12,
    },
    "san_francisco": {
        "name": "San Francisco, CA",
        "center": [37.7749, -122.4194],
        "zoom": 12,
    },
    "oakland": {
        "name": "Oakland, CA",
        "center": [37.8044, -122.2712],
        "zoom": 12,
    },
    "portland": {
        "name": "Portland, OR",
        "center": [45.5051, -122.6750],
        "zoom": 11,
    },
    "upstate_ny": {
        "name": "Upstate New York",
        "center": [42.8864, -78.8784],
        "zoom": 7,
    },
}

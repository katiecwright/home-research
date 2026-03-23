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
    "97222": {"city": "Milwaukie", "state": "OR", "metro": "portland", "lat": 45.4399, "lon": -122.6148},  # Milwaukie
    "97223": {"city": "Tigard",    "state": "OR", "metro": "portland", "lat": 45.4342, "lon": -122.7693},  # Tigard
    "97224": {"city": "Tigard",    "state": "OR", "metro": "portland", "lat": 45.3934, "lon": -122.7754},  # Tigard SW
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

    # ── North Marin County, CA ────────────────────────────────────────────────
    "94901": {"city": "San Rafael",          "state": "CA", "metro": "north_marin", "lat": 37.9742, "lon": -122.5309},  # San Rafael downtown
    "94903": {"city": "San Rafael",          "state": "CA", "metro": "north_marin", "lat": 38.0134, "lon": -122.5493},  # N San Rafael / Terra Linda
    "94945": {"city": "Novato",              "state": "CA", "metro": "north_marin", "lat": 38.1149, "lon": -122.5702},  # Novato N
    "94947": {"city": "Novato",              "state": "CA", "metro": "north_marin", "lat": 38.1062, "lon": -122.6250},  # Novato W / Ignacio
    "94949": {"city": "Novato",              "state": "CA", "metro": "north_marin", "lat": 38.0610, "lon": -122.5360},  # Novato S / Hamilton
    "94946": {"city": "Nicasio",             "state": "CA", "metro": "north_marin", "lat": 38.0564, "lon": -122.6907},  # W Marin / Nicasio
    "94937": {"city": "Inverness",           "state": "CA", "metro": "north_marin", "lat": 38.1032, "lon": -122.8529},  # Point Reyes / Inverness
    "94956": {"city": "Point Reyes Station", "state": "CA", "metro": "north_marin", "lat": 38.0701, "lon": -122.8065},  # Point Reyes Station
    "94973": {"city": "Woodacre",            "state": "CA", "metro": "north_marin", "lat": 37.9988, "lon": -122.6414},  # Woodacre / San Geronimo

    # ── Sonoma County, CA ─────────────────────────────────────────────────────
    "95401": {"city": "Santa Rosa",    "state": "CA", "metro": "sonoma", "lat": 38.4404, "lon": -122.7141},  # Santa Rosa SW
    "95403": {"city": "Santa Rosa",    "state": "CA", "metro": "sonoma", "lat": 38.4666, "lon": -122.7273},  # Santa Rosa N / Larkfield
    "95404": {"city": "Santa Rosa",    "state": "CA", "metro": "sonoma", "lat": 38.4512, "lon": -122.6834},  # Santa Rosa E / Rincon Valley
    "95405": {"city": "Santa Rosa",    "state": "CA", "metro": "sonoma", "lat": 38.4256, "lon": -122.6855},  # SE Santa Rosa
    "95407": {"city": "Santa Rosa",    "state": "CA", "metro": "sonoma", "lat": 38.4029, "lon": -122.7237},  # SW Santa Rosa / Roseland
    "95409": {"city": "Santa Rosa",    "state": "CA", "metro": "sonoma", "lat": 38.4380, "lon": -122.6288},  # Oakmont / SE outskirts
    "94952": {"city": "Petaluma",      "state": "CA", "metro": "sonoma", "lat": 38.2349, "lon": -122.7604},  # Petaluma W
    "94954": {"city": "Petaluma",      "state": "CA", "metro": "sonoma", "lat": 38.2350, "lon": -122.5574},  # Petaluma E
    "94928": {"city": "Rohnert Park",  "state": "CA", "metro": "sonoma", "lat": 38.3397, "lon": -122.7070},  # Rohnert Park
    "95472": {"city": "Sebastopol",    "state": "CA", "metro": "sonoma", "lat": 38.4023, "lon": -122.8234},  # Sebastopol
    "95448": {"city": "Healdsburg",    "state": "CA", "metro": "sonoma", "lat": 38.6102, "lon": -122.8699},  # Healdsburg
    "95492": {"city": "Windsor",       "state": "CA", "metro": "sonoma", "lat": 38.5471, "lon": -122.8148},  # Windsor
    "95476": {"city": "Sonoma",        "state": "CA", "metro": "sonoma", "lat": 38.2919, "lon": -122.4580},  # Sonoma town
    "95425": {"city": "Cloverdale",    "state": "CA", "metro": "sonoma", "lat": 38.7958, "lon": -123.0173},  # Cloverdale
    "94931": {"city": "Cotati",        "state": "CA", "metro": "sonoma", "lat": 38.3268, "lon": -122.7077},  # Cotati

    # ── Napa County, CA ───────────────────────────────────────────────────────
    "94503": {"city": "American Canyon", "state": "CA", "metro": "napa", "lat": 38.1716, "lon": -122.2534},  # American Canyon
    "94558": {"city": "Napa",            "state": "CA", "metro": "napa", "lat": 38.3587, "lon": -122.2913},  # Napa N
    "94559": {"city": "Napa",            "state": "CA", "metro": "napa", "lat": 38.2970, "lon": -122.2840},  # Napa downtown / S
    "94562": {"city": "Oakville",        "state": "CA", "metro": "napa", "lat": 38.4326, "lon": -122.4094},  # Oakville / Rutherford
    "94574": {"city": "St. Helena",      "state": "CA", "metro": "napa", "lat": 38.5021, "lon": -122.4700},  # St. Helena
    "94599": {"city": "Yountville",      "state": "CA", "metro": "napa", "lat": 38.4014, "lon": -122.3619},  # Yountville
    "94515": {"city": "Calistoga",       "state": "CA", "metro": "napa", "lat": 38.5788, "lon": -122.5797},  # Calistoga
    "94508": {"city": "Angwin",          "state": "CA", "metro": "napa", "lat": 38.5726, "lon": -122.4518},  # Angwin / Pope Valley

    # ── Mendocino County, CA ──────────────────────────────────────────────────
    "95482": {"city": "Ukiah",           "state": "CA", "metro": "mendocino", "lat": 39.1502, "lon": -123.2078},  # Ukiah
    "95490": {"city": "Willits",         "state": "CA", "metro": "mendocino", "lat": 39.4088, "lon": -123.3536},  # Willits
    "95437": {"city": "Fort Bragg",      "state": "CA", "metro": "mendocino", "lat": 39.4457, "lon": -123.8053},  # Fort Bragg
    "95460": {"city": "Mendocino",       "state": "CA", "metro": "mendocino", "lat": 39.3082, "lon": -123.8002},  # Mendocino village
    "95454": {"city": "Laytonville",     "state": "CA", "metro": "mendocino", "lat": 39.6880, "lon": -123.4838},  # Laytonville
    "95470": {"city": "Redwood Valley",  "state": "CA", "metro": "mendocino", "lat": 39.2644, "lon": -123.2117},  # Redwood Valley
    "95415": {"city": "Boonville",       "state": "CA", "metro": "mendocino", "lat": 39.0141, "lon": -123.3682},  # Boonville / Anderson Valley

    # ── Seattle metro, WA ─────────────────────────────────────────────────────
    "98101": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6087, "lon": -122.3351},  # Downtown
    "98102": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6348, "lon": -122.3227},  # Capitol Hill / Eastlake
    "98103": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6706, "lon": -122.3420},  # Green Lake / Fremont
    "98104": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6024, "lon": -122.3298},  # International District
    "98105": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6634, "lon": -122.2996},  # University District
    "98106": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.5487, "lon": -122.3600},  # Delridge / White Center
    "98107": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6688, "lon": -122.3783},  # Ballard
    "98108": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.5480, "lon": -122.3096},  # South Beacon Hill
    "98109": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6376, "lon": -122.3560},  # Queen Anne / Interbay
    "98112": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6337, "lon": -122.2895},  # Madison Park / Montlake
    "98115": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6828, "lon": -122.2946},  # Wedgwood / Ravenna
    "98116": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.5677, "lon": -122.3896},  # West Seattle / Alki
    "98117": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6865, "lon": -122.3731},  # Crown Hill / Ballard NE
    "98118": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.5468, "lon": -122.2761},  # Rainier Valley / Columbia City
    "98119": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6430, "lon": -122.3740},  # Queen Anne / Magnolia
    "98121": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6146, "lon": -122.3499},  # Belltown / Denny Regrade
    "98122": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6070, "lon": -122.3033},  # Central District
    "98125": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.7124, "lon": -122.3010},  # Lake City / Northgate
    "98126": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.5596, "lon": -122.3752},  # West Seattle / High Point
    "98133": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.7261, "lon": -122.3448},  # Bitter Lake / Shoreline border
    "98136": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.5395, "lon": -122.3851},  # Fauntleroy / Seaview
    "98144": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.5870, "lon": -122.2979},  # Beacon Hill / Leschi
    "98177": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.7628, "lon": -122.3797},  # Crown Hill / N Seattle
    "98199": {"city": "Seattle",       "state": "WA", "metro": "seattle", "lat": 47.6529, "lon": -122.4016},  # Magnolia
    "98004": {"city": "Bellevue",      "state": "WA", "metro": "seattle", "lat": 47.6149, "lon": -122.2006},  # Downtown Bellevue
    "98005": {"city": "Bellevue",      "state": "WA", "metro": "seattle", "lat": 47.6018, "lon": -122.1784},  # Bellevue central
    "98006": {"city": "Bellevue",      "state": "WA", "metro": "seattle", "lat": 47.5596, "lon": -122.1586},  # SW Bellevue
    "98007": {"city": "Bellevue",      "state": "WA", "metro": "seattle", "lat": 47.5983, "lon": -122.1506},  # Crossroads
    "98008": {"city": "Bellevue",      "state": "WA", "metro": "seattle", "lat": 47.5993, "lon": -122.1160},  # Eastgate
    "98033": {"city": "Kirkland",      "state": "WA", "metro": "seattle", "lat": 47.6887, "lon": -122.1854},  # Kirkland
    "98034": {"city": "Kirkland",      "state": "WA", "metro": "seattle", "lat": 47.7196, "lon": -122.2146},  # N Kirkland / Juanita
    "98039": {"city": "Medina",        "state": "WA", "metro": "seattle", "lat": 47.6224, "lon": -122.2232},  # Medina
    "98040": {"city": "Mercer Island", "state": "WA", "metro": "seattle", "lat": 47.5706, "lon": -122.2218},  # Mercer Island
    "98052": {"city": "Redmond",       "state": "WA", "metro": "seattle", "lat": 47.6723, "lon": -122.1165},  # Redmond
    "98053": {"city": "Redmond",       "state": "WA", "metro": "seattle", "lat": 47.6635, "lon": -122.0294},  # SE Redmond / Sammamish

    # ── Tacoma metro, WA ──────────────────────────────────────────────────────
    "98402": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.2556, "lon": -122.4458},  # Downtown Tacoma
    "98403": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.2652, "lon": -122.4566},  # North End
    "98404": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.2192, "lon": -122.4053},  # Eastside
    "98405": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.2548, "lon": -122.4716},  # Central Tacoma
    "98406": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.2615, "lon": -122.4960},  # Proctor / N Tacoma
    "98407": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.2851, "lon": -122.5019},  # North End / NW
    "98408": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.2272, "lon": -122.4390},  # South Tacoma
    "98409": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.2186, "lon": -122.4674},  # S Tacoma
    "98418": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.2249, "lon": -122.4537},  # SE Tacoma
    "98422": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.3006, "lon": -122.3979},  # NE Tacoma
    "98443": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.2388, "lon": -122.3796},  # Parkland East
    "98444": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.1568, "lon": -122.4454},  # Parkland
    "98445": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.1489, "lon": -122.3901},  # Spanaway / Parkland
    "98465": {"city": "Tacoma",          "state": "WA", "metro": "tacoma", "lat": 47.2571, "lon": -122.5249},  # Tacoma NW
    "98466": {"city": "University Place","state": "WA", "metro": "tacoma", "lat": 47.2432, "lon": -122.5520},  # University Place
    "98467": {"city": "University Place","state": "WA", "metro": "tacoma", "lat": 47.1993, "lon": -122.5432},  # University Place S
    "98371": {"city": "Puyallup",        "state": "WA", "metro": "tacoma", "lat": 47.1873, "lon": -122.2928},  # Puyallup
    "98372": {"city": "Puyallup",        "state": "WA", "metro": "tacoma", "lat": 47.1949, "lon": -122.2459},  # E Puyallup
    "98373": {"city": "Puyallup",        "state": "WA", "metro": "tacoma", "lat": 47.1461, "lon": -122.3141},  # S Puyallup
    "98374": {"city": "Puyallup",        "state": "WA", "metro": "tacoma", "lat": 47.1600, "lon": -122.2497},  # SE Puyallup
    "98332": {"city": "Gig Harbor",      "state": "WA", "metro": "tacoma", "lat": 47.3722, "lon": -122.5958},  # Gig Harbor N
    "98335": {"city": "Gig Harbor",      "state": "WA", "metro": "tacoma", "lat": 47.2969, "lon": -122.6237},  # Gig Harbor S
    "98498": {"city": "Lakewood",        "state": "WA", "metro": "tacoma", "lat": 47.1619, "lon": -122.5258},  # Lakewood
    "98499": {"city": "Lakewood",        "state": "WA", "metro": "tacoma", "lat": 47.1663, "lon": -122.5061},  # Lakewood E

    # ── Olympia metro, WA ─────────────────────────────────────────────────────
    "98501": {"city": "Olympia", "state": "WA", "metro": "olympia", "lat": 47.0379, "lon": -122.9007},  # Olympia core
    "98502": {"city": "Olympia", "state": "WA", "metro": "olympia", "lat": 47.0484, "lon": -122.9620},  # W Olympia
    "98506": {"city": "Olympia", "state": "WA", "metro": "olympia", "lat": 47.0664, "lon": -122.8590},  # E Olympia
    "98512": {"city": "Tumwater","state": "WA", "metro": "olympia", "lat": 46.9924, "lon": -122.9497},  # Tumwater
    "98503": {"city": "Lacey",   "state": "WA", "metro": "olympia", "lat": 47.0385, "lon": -122.7868},  # Lacey
    "98513": {"city": "Lacey",   "state": "WA", "metro": "olympia", "lat": 47.0003, "lon": -122.7506},  # SE Lacey
    "98516": {"city": "Lacey",   "state": "WA", "metro": "olympia", "lat": 47.0783, "lon": -122.7428},  # NE Lacey

    # ── SW Washington / I-5 Corridor, WA ─────────────────────────────────────
    "98660": {"city": "Vancouver",  "state": "WA", "metro": "sw_washington", "lat": 45.6344, "lon": -122.6761},  # Downtown Vancouver
    "98661": {"city": "Vancouver",  "state": "WA", "metro": "sw_washington", "lat": 45.6244, "lon": -122.6321},  # E Vancouver
    "98662": {"city": "Vancouver",  "state": "WA", "metro": "sw_washington", "lat": 45.6463, "lon": -122.5781},  # NE Vancouver
    "98663": {"city": "Vancouver",  "state": "WA", "metro": "sw_washington", "lat": 45.6464, "lon": -122.6562},  # N Vancouver
    "98664": {"city": "Vancouver",  "state": "WA", "metro": "sw_washington", "lat": 45.5966, "lon": -122.5827},  # SE Vancouver
    "98665": {"city": "Vancouver",  "state": "WA", "metro": "sw_washington", "lat": 45.6706, "lon": -122.6632},  # Hazel Dell
    "98682": {"city": "Vancouver",  "state": "WA", "metro": "sw_washington", "lat": 45.6454, "lon": -122.4992},  # E Vancouver / Orchards
    "98683": {"city": "Vancouver",  "state": "WA", "metro": "sw_washington", "lat": 45.5967, "lon": -122.4847},  # SE Vancouver / Fisher's Landing
    "98684": {"city": "Vancouver",  "state": "WA", "metro": "sw_washington", "lat": 45.6174, "lon": -122.5121},  # Cascade Park
    "98685": {"city": "Vancouver",  "state": "WA", "metro": "sw_washington", "lat": 45.7011, "lon": -122.6573},  # Felida / N Vancouver
    "98686": {"city": "Vancouver",  "state": "WA", "metro": "sw_washington", "lat": 45.7039, "lon": -122.6153},  # NE Vancouver / Salmon Creek
    "98632": {"city": "Longview",   "state": "WA", "metro": "sw_washington", "lat": 46.1384, "lon": -122.9383},  # Longview
    "98626": {"city": "Kelso",      "state": "WA", "metro": "sw_washington", "lat": 46.1469, "lon": -122.9049},  # Kelso
    "98531": {"city": "Centralia",  "state": "WA", "metro": "sw_washington", "lat": 46.7160, "lon": -122.9542},  # Centralia
    "98532": {"city": "Chehalis",   "state": "WA", "metro": "sw_washington", "lat": 46.6614, "lon": -122.9651},  # Chehalis

    # ── Salem / Keizer, OR ────────────────────────────────────────────────────
    "97301": {"city": "Salem",  "state": "OR", "metro": "salem", "lat": 44.9274, "lon": -122.9918},  # NE Salem
    "97302": {"city": "Salem",  "state": "OR", "metro": "salem", "lat": 44.9085, "lon": -123.0601},  # SW Salem
    "97303": {"city": "Salem",  "state": "OR", "metro": "salem", "lat": 44.9858, "lon": -123.0204},  # N Salem / Keizer
    "97304": {"city": "Salem",  "state": "OR", "metro": "salem", "lat": 44.9546, "lon": -123.0793},  # W Salem
    "97305": {"city": "Salem",  "state": "OR", "metro": "salem", "lat": 44.9714, "lon": -122.9693},  # NE Salem
    "97306": {"city": "Salem",  "state": "OR", "metro": "salem", "lat": 44.8792, "lon": -123.0338},  # S Salem
    "97317": {"city": "Salem",  "state": "OR", "metro": "salem", "lat": 44.8903, "lon": -122.9356},  # SE Salem
    "97307": {"city": "Keizer", "state": "OR", "metro": "salem", "lat": 45.0000, "lon": -123.0188},  # Keizer

    # ── Eugene / Springfield, OR ──────────────────────────────────────────────
    "97401": {"city": "Eugene",      "state": "OR", "metro": "eugene", "lat": 44.0579, "lon": -123.0897},  # Eugene NE / downtown
    "97402": {"city": "Eugene",      "state": "OR", "metro": "eugene", "lat": 44.0427, "lon": -123.1545},  # W Eugene
    "97403": {"city": "Eugene",      "state": "OR", "metro": "eugene", "lat": 44.0368, "lon": -123.0623},  # SE Eugene / U of O
    "97404": {"city": "Eugene",      "state": "OR", "metro": "eugene", "lat": 44.0844, "lon": -123.1133},  # N Eugene
    "97405": {"city": "Eugene",      "state": "OR", "metro": "eugene", "lat": 43.9993, "lon": -123.0949},  # S Eugene / South Hills
    "97408": {"city": "Eugene",      "state": "OR", "metro": "eugene", "lat": 44.1126, "lon": -123.0747},  # NE Eugene / River Road
    "97477": {"city": "Springfield", "state": "OR", "metro": "eugene", "lat": 44.0463, "lon": -122.9986},  # Springfield W
    "97478": {"city": "Springfield", "state": "OR", "metro": "eugene", "lat": 44.0329, "lon": -122.9058},  # Springfield E / Thurston

    # ── Bend / Redmond, OR ────────────────────────────────────────────────────
    "97701": {"city": "Bend",    "state": "OR", "metro": "bend", "lat": 44.0908, "lon": -121.2749},  # Bend NE / Midtown
    "97702": {"city": "Bend",    "state": "OR", "metro": "bend", "lat": 43.9872, "lon": -121.3238},  # Bend S / SE
    "97703": {"city": "Bend",    "state": "OR", "metro": "bend", "lat": 44.0659, "lon": -121.3582},  # Bend NW / Old Mill
    "97756": {"city": "Redmond", "state": "OR", "metro": "bend", "lat": 44.2726, "lon": -121.1490},  # Redmond OR
    "97707": {"city": "Bend",    "state": "OR", "metro": "bend", "lat": 43.8290, "lon": -121.6183},  # Sunriver / S Bend area

    # ── NYC Manhattan, NY ─────────────────────────────────────────────────────
    "10002": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7157, "lon": -73.9863},  # Lower East Side / Chinatown
    "10004": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7004, "lon": -74.0400},  # Financial District
    "10005": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7074, "lon": -74.0110},  # Financial District
    "10007": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7135, "lon": -74.0082},  # City Hall / Tribeca N
    "10009": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7263, "lon": -73.9776},  # East Village / Alphabet City
    "10011": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7422, "lon": -74.0009},  # Chelsea
    "10012": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7258, "lon": -74.0006},  # SoHo / NoHo
    "10013": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7199, "lon": -74.0063},  # Tribeca / Chinatown
    "10014": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7335, "lon": -74.0048},  # West Village
    "10016": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7471, "lon": -73.9801},  # Murray Hill / Kips Bay
    "10017": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7528, "lon": -73.9733},  # Midtown East / Turtle Bay
    "10019": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7651, "lon": -73.9875},  # Midtown W / Hell's Kitchen N
    "10021": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7699, "lon": -73.9594},  # Upper East Side
    "10023": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7769, "lon": -73.9822},  # Upper West Side
    "10024": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7853, "lon": -73.9756},  # UWS N / Riverside
    "10025": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7977, "lon": -73.9690},  # Morningside Heights
    "10026": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.8020, "lon": -73.9534},  # Harlem
    "10027": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.8116, "lon": -73.9603},  # Harlem
    "10028": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7745, "lon": -73.9528},  # Upper East Side N
    "10029": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7934, "lon": -73.9438},  # E Harlem / Yorkville
    "10030": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.8177, "lon": -73.9440},  # Harlem N
    "10031": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.8255, "lon": -73.9498},  # Hamilton Heights
    "10032": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.8383, "lon": -73.9416},  # Washington Heights S
    "10033": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.8487, "lon": -73.9330},  # Washington Heights
    "10034": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.8672, "lon": -73.9231},  # Inwood
    "10035": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.8019, "lon": -73.9297},  # E Harlem
    "10036": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7594, "lon": -73.9930},  # Hell's Kitchen / Times Square
    "10037": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.8139, "lon": -73.9384},  # Central Harlem
    "10038": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7089, "lon": -74.0013},  # Fulton Seaport
    "10039": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.8296, "lon": -73.9374},  # Washington Heights N
    "10040": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.8583, "lon": -73.9316},  # Washington Heights / Inwood S
    "10065": {"city": "New York", "state": "NY", "metro": "nyc_manhattan", "lat": 40.7641, "lon": -73.9623},  # Upper East Side / Lenox Hill

    # ── NYC Brooklyn, NY ──────────────────────────────────────────────────────
    "11201": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6944, "lon": -73.9906},  # Brooklyn Heights / DUMBO
    "11203": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6477, "lon": -73.9390},  # Flatbush E
    "11204": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6178, "lon": -73.9846},  # Borough Park
    "11205": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6956, "lon": -73.9671},  # Clinton Hill / Fort Greene
    "11206": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.7031, "lon": -73.9428},  # Williamsburg S / Bushwick N
    "11207": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6726, "lon": -73.8905},  # East New York
    "11208": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6741, "lon": -73.8679},  # Cypress Hills
    "11209": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6203, "lon": -74.0289},  # Bay Ridge
    "11210": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6284, "lon": -73.9464},  # Flatbush / Midwood
    "11211": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.7141, "lon": -73.9525},  # Williamsburg N
    "11212": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6618, "lon": -73.9168},  # Brownsville
    "11213": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6693, "lon": -73.9391},  # Crown Heights
    "11214": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.5998, "lon": -74.0024},  # Bensonhurst
    "11215": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6660, "lon": -73.9878},  # Park Slope
    "11216": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6771, "lon": -73.9487},  # Crown Heights W / Bed-Stuy
    "11217": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6832, "lon": -73.9848},  # Boerum Hill / Gowanus
    "11218": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6414, "lon": -73.9792},  # Kensington / Ditmas Park
    "11219": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6296, "lon": -73.9953},  # Borough Park S
    "11220": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6353, "lon": -74.0170},  # Sunset Park
    "11221": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6936, "lon": -73.9204},  # Bushwick / Bed-Stuy E
    "11222": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.7270, "lon": -73.9505},  # Greenpoint
    "11223": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6003, "lon": -73.9725},  # Gravesend
    "11224": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.5768, "lon": -73.9907},  # Coney Island
    "11225": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6589, "lon": -73.9554},  # Flatbush / Prospect Lefferts
    "11226": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6443, "lon": -73.9570},  # Flatbush central
    "11228": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6148, "lon": -74.0145},  # Dyker Heights
    "11229": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.5983, "lon": -73.9480},  # Sheepshead Bay N
    "11230": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6213, "lon": -73.9638},  # Midwood
    "11231": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6769, "lon": -74.0020},  # Carroll Gardens / Red Hook
    "11232": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6567, "lon": -74.0077},  # Sunset Park N / Industry City
    "11233": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6793, "lon": -73.9168},  # Bed-Stuy E
    "11234": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6156, "lon": -73.9141},  # Flatlands / Canarsie N
    "11235": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.5820, "lon": -73.9468},  # Sheepshead Bay / Brighton Beach
    "11236": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6369, "lon": -73.9044},  # Canarsie
    "11237": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.7040, "lon": -73.9230},  # Bushwick
    "11238": {"city": "Brooklyn", "state": "NY", "metro": "nyc_brooklyn", "lat": 40.6769, "lon": -73.9646},  # Prospect Heights / Crown Heights W

    # ── NYC Queens, NY ────────────────────────────────────────────────────────
    "11101": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7440, "lon": -73.9468},  # Long Island City
    "11102": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7742, "lon": -73.9312},  # Astoria N
    "11103": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7628, "lon": -73.9262},  # Astoria S
    "11104": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7451, "lon": -73.9215},  # Sunnyside
    "11105": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7821, "lon": -73.9110},  # Astoria / Ditmars
    "11354": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7677, "lon": -73.8336},  # Flushing W
    "11355": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7522, "lon": -73.8273},  # Flushing S
    "11356": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7853, "lon": -73.8420},  # College Point
    "11357": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7918, "lon": -73.8151},  # Whitestone / Malba
    "11358": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7638, "lon": -73.7981},  # Flushing NE / Bayside W
    "11360": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7845, "lon": -73.7804},  # Bayside N / Bay Terrace
    "11361": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7644, "lon": -73.7719},  # Bayside
    "11362": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7475, "lon": -73.7350},  # Little Neck / Douglas Manor
    "11363": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7740, "lon": -73.7451},  # Little Neck N
    "11364": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7464, "lon": -73.7587},  # Oakland Gardens
    "11365": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7341, "lon": -73.7924},  # Fresh Meadows
    "11366": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7242, "lon": -73.7847},  # Fresh Meadows S
    "11367": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7268, "lon": -73.8231},  # Kew Gardens Hills
    "11368": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7483, "lon": -73.8551},  # Corona
    "11369": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7624, "lon": -73.8701},  # Jackson Heights N / E Elmhurst
    "11370": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7656, "lon": -73.8843},  # East Elmhurst
    "11372": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7488, "lon": -73.8869},  # Jackson Heights
    "11373": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7371, "lon": -73.8780},  # Elmhurst
    "11374": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7257, "lon": -73.8613},  # Rego Park
    "11375": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7225, "lon": -73.8432},  # Forest Hills
    "11377": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7437, "lon": -73.9041},  # Woodside / Sunnyside W
    "11378": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7289, "lon": -73.9025},  # Maspeth
    "11379": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7202, "lon": -73.8675},  # Middle Village
    "11385": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.7001, "lon": -73.9032},  # Ridgewood / Glendale
    "11691": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.5996, "lon": -73.7617},  # Far Rockaway
    "11692": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.5921, "lon": -73.7941},  # Arverne / Edgemere
    "11694": {"city": "Queens", "state": "NY", "metro": "nyc_queens", "lat": 40.5760, "lon": -73.8441},  # Rockaway Park / Belle Harbor

    # ── NYC Bronx & Staten Island, NY ─────────────────────────────────────────
    "10451": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8177, "lon": -73.9231},  # High Bridge / Morrisania
    "10452": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8380, "lon": -73.9234},  # Highbridge / Mt Eden
    "10453": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8514, "lon": -73.9136},  # University Heights
    "10454": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8078, "lon": -73.9162},  # Mott Haven S
    "10455": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8118, "lon": -73.9072},  # Hunts Point / Mott Haven E
    "10456": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8281, "lon": -73.9154},  # Morrisania / Tremont
    "10457": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8453, "lon": -73.9072},  # East Tremont / Belmont
    "10458": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8622, "lon": -73.8917},  # Fordham / Belmont
    "10460": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8371, "lon": -73.8792},  # West Farms / Bronx Park S
    "10461": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8476, "lon": -73.8409},  # Morris Park / Pelham Pkwy S
    "10462": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8375, "lon": -73.8559},  # Parkchester
    "10463": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8768, "lon": -73.9085},  # Kingsbridge / Marble Hill
    "10465": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8270, "lon": -73.8222},  # Throgs Neck / Schuylerville
    "10466": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8974, "lon": -73.8468},  # Baychester / Wakefield
    "10467": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8742, "lon": -73.8726},  # Norwood / Williamsbridge
    "10468": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8671, "lon": -73.9013},  # Fordham N / Kingsbridge Hts
    "10469": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8705, "lon": -73.8448},  # Pelham Gardens / Allerton
    "10471": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.9005, "lon": -73.9098},  # Riverdale
    "10472": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8257, "lon": -73.8626},  # Unionport / Soundview
    "10473": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8173, "lon": -73.8553},  # Clason Point / Soundview
    "10475": {"city": "Bronx",         "state": "NY", "metro": "nyc_bronx_si", "lat": 40.8762, "lon": -73.8298},  # Co-op City
    "10301": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.6337, "lon": -74.0948},  # St. George / Tompkinsville
    "10302": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.6282, "lon": -74.1296},  # Port Richmond / Livingston
    "10303": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.6392, "lon": -74.1461},  # Mariners Harbor / Elm Park
    "10304": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.6079, "lon": -74.0828},  # Stapleton / Rosebank
    "10305": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.5956, "lon": -74.0807},  # Rosebank / Shore Acres
    "10306": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.5685, "lon": -74.1154},  # New Dorp / Oakwood
    "10307": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.5158, "lon": -74.2090},  # Tottenville / Great Kills
    "10308": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.5518, "lon": -74.1481},  # Great Kills / Eltingville
    "10309": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.5261, "lon": -74.1893},  # Tottenville / Pleasant Plains
    "10310": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.6317, "lon": -74.1122},  # West New Brighton / Westerleigh
    "10312": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.5496, "lon": -74.1757},  # Eltingville / Annadale
    "10314": {"city": "Staten Island", "state": "NY", "metro": "nyc_bronx_si", "lat": 40.5994, "lon": -74.1618},  # Willowbrook / Bulls Head

    # ── Upstate New York ──────────────────────────────────────────────────────
    # Albany / Troy / Schenectady area
    "12202": {"city": "Albany",      "state": "NY", "metro": "upstate_ny", "lat": 42.6371, "lon": -73.7596},  # S Albany / South End
    "12203": {"city": "Albany",      "state": "NY", "metro": "upstate_ny", "lat": 42.6955, "lon": -73.8270},  # Westside / Beverwyck
    "12204": {"city": "Albany",      "state": "NY", "metro": "upstate_ny", "lat": 42.6639, "lon": -73.7470},  # S Albany
    "12205": {"city": "Albany",      "state": "NY", "metro": "upstate_ny", "lat": 42.7132, "lon": -73.8403},  # Colonie / Westgate
    "12206": {"city": "Albany",      "state": "NY", "metro": "upstate_ny", "lat": 42.6829, "lon": -73.7877},  # Pine Hills
    "12208": {"city": "Albany",      "state": "NY", "metro": "upstate_ny", "lat": 42.6610, "lon": -73.8056},  # Washington Park / New Scotland
    "12209": {"city": "Albany",      "state": "NY", "metro": "upstate_ny", "lat": 42.6482, "lon": -73.7926},  # Kenwood / Delaware Ave
    "12210": {"city": "Albany",      "state": "NY", "metro": "upstate_ny", "lat": 42.6631, "lon": -73.7576},  # Center Square / Park Ave
    "12302": {"city": "Schenectady", "state": "NY", "metro": "upstate_ny", "lat": 42.8285, "lon": -73.9619},  # Schenectady W
    "12304": {"city": "Schenectady", "state": "NY", "metro": "upstate_ny", "lat": 42.7974, "lon": -73.9165},  # Schenectady SE
    "12306": {"city": "Schenectady", "state": "NY", "metro": "upstate_ny", "lat": 42.7933, "lon": -74.0005},  # Schenectady SW
    "12308": {"city": "Schenectady", "state": "NY", "metro": "upstate_ny", "lat": 42.8138, "lon": -73.9281},  # Schenectady core
    "12309": {"city": "Schenectady", "state": "NY", "metro": "upstate_ny", "lat": 42.8232, "lon": -73.8895},  # Scotia / Niskayuna border
    "12180": {"city": "Troy",        "state": "NY", "metro": "upstate_ny", "lat": 42.7284, "lon": -73.6918},  # Troy
    "12182": {"city": "Troy",        "state": "NY", "metro": "upstate_ny", "lat": 42.7766, "lon": -73.6790},  # Troy N / Lansingburgh
    "12110": {"city": "Latham",      "state": "NY", "metro": "upstate_ny", "lat": 42.7459, "lon": -73.7627},  # Latham / Colonie
    "12047": {"city": "Cohoes",      "state": "NY", "metro": "upstate_ny", "lat": 42.7757, "lon": -73.7032},  # Cohoes
    "12084": {"city": "Guilderland", "state": "NY", "metro": "upstate_ny", "lat": 42.6914, "lon": -73.9041},  # Guilderland
    # Buffalo area
    "14201": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.8967, "lon": -78.8764},  # W Buffalo / Allentown
    "14202": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.8898, "lon": -78.8800},  # Downtown Buffalo
    "14204": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.8774, "lon": -78.8600},  # E Buffalo / Fillmore
    "14206": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.8744, "lon": -78.8294},  # SE Buffalo
    "14207": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.9233, "lon": -78.9157},  # Black Rock / Riverside
    "14208": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.9013, "lon": -78.8586},  # Masten Park
    "14209": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.9087, "lon": -78.8758},  # Delaware / N Buffalo
    "14210": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.8604, "lon": -78.8550},  # S Buffalo / Seneca
    "14211": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.9061, "lon": -78.8308},  # Broadway-Fillmore / Lovejoy
    "14213": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.9217, "lon": -78.8960},  # Elmwood Village
    "14214": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.9323, "lon": -78.8588},  # Parkside / N Buffalo
    "14215": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.9316, "lon": -78.8270},  # Cheektowaga / Kensington
    "14216": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.9492, "lon": -78.8694},  # N Buffalo / University
    "14217": {"city": "Tonawanda",     "state": "NY", "metro": "upstate_ny", "lat": 42.9951, "lon": -78.8918},  # Tonawanda N
    "14220": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.8469, "lon": -78.8316},  # S Buffalo / Lackawanna border
    "14221": {"city": "Williamsville", "state": "NY", "metro": "upstate_ny", "lat": 42.9696, "lon": -78.7373},  # Williamsville / Amherst
    "14222": {"city": "Buffalo",       "state": "NY", "metro": "upstate_ny", "lat": 42.9238, "lon": -78.9050},  # Elmwood / Allentown N
    "14223": {"city": "Tonawanda",     "state": "NY", "metro": "upstate_ny", "lat": 42.9811, "lon": -78.8637},  # Tonawanda
    "14225": {"city": "Cheektowaga",   "state": "NY", "metro": "upstate_ny", "lat": 42.9048, "lon": -78.7762},  # Cheektowaga
    "14226": {"city": "Amherst",       "state": "NY", "metro": "upstate_ny", "lat": 42.9869, "lon": -78.8044},  # Amherst / Snyder
    "14228": {"city": "Amherst",       "state": "NY", "metro": "upstate_ny", "lat": 43.0189, "lon": -78.8000},  # Amherst N / UB campus
    # Rochester area
    "14604": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1566, "lon": -77.6088},  # Downtown Rochester
    "14606": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1615, "lon": -77.6902},  # Gates / W Rochester
    "14607": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1488, "lon": -77.5880},  # East Ave / Park Ave
    "14608": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1578, "lon": -77.6351},  # Corn Hill / SW
    "14609": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1745, "lon": -77.5719},  # NE Rochester
    "14610": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1343, "lon": -77.5643},  # Brighton N / Cobbs Hill
    "14611": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1491, "lon": -77.6571},  # Lyell-Otis / SW
    "14612": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.2392, "lon": -77.6625},  # Charlotte / NW
    "14613": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1831, "lon": -77.6538},  # N Rochester / Maplewood
    "14615": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.2026, "lon": -77.6679},  # N Rochester / Edgemere
    "14616": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.2263, "lon": -77.6724},  # NW Rochester
    "14617": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.2196, "lon": -77.5814},  # Irondequoit / Culver
    "14618": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1100, "lon": -77.5534},  # Brighton / S Rochester
    "14619": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1356, "lon": -77.6531},  # S Rochester / Genesee
    "14620": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1302, "lon": -77.6194},  # S Rochester / Highland
    "14621": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1764, "lon": -77.5971},  # NE Rochester
    "14622": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.2136, "lon": -77.5465},  # Irondequoit N
    "14623": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.0979, "lon": -77.6570},  # RIT / SW suburbs
    "14624": {"city": "Rochester", "state": "NY", "metro": "upstate_ny", "lat": 43.1456, "lon": -77.7378},  # Gates / Chili
    # Syracuse area
    "13202": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.0481, "lon": -76.1474},  # Downtown Syracuse
    "13203": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.0587, "lon": -76.1293},  # NE / Eastside
    "13204": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.0514, "lon": -76.1644},  # SW / Armory
    "13205": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.0213, "lon": -76.1455},  # S Syracuse
    "13206": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.0721, "lon": -76.1025},  # E Syracuse
    "13207": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.0219, "lon": -76.1626},  # S Syracuse / Valley
    "13208": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.0786, "lon": -76.1298},  # N Syracuse / Northside
    "13209": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.0700, "lon": -76.2253},  # Lakeland / W Syracuse
    "13210": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.0370, "lon": -76.1299},  # University Hill / Westcott
    "13211": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.1014, "lon": -76.1076},  # Mattydale / N Syracuse
    "13212": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.1235, "lon": -76.1377},  # N Syracuse / Salina
    "13214": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.0394, "lon": -76.0805},  # DeWitt / Fayetteville W
    "13219": {"city": "Syracuse", "state": "NY", "metro": "upstate_ny", "lat": 43.0498, "lon": -76.2124},  # Fairmount / W Syracuse

    # ── Philadelphia Metro, PA ────────────────────────────────────────────────
    # Philadelphia proper
    "19102": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9521, "lon": -75.1638},  # Center City / Rittenhouse
    "19103": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9535, "lon": -75.1789},  # Rittenhouse / Logan Square
    "19104": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9611, "lon": -75.1980},  # West Philly / University City
    "19106": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9482, "lon": -75.1466},  # Old City / Society Hill
    "19107": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9542, "lon": -75.1574},  # Washington Square
    "19111": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0603, "lon": -75.0790},  # Fox Chase / Burholme
    "19114": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0647, "lon": -74.9971},  # NE Philly / Torresdale
    "19115": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0919, "lon": -75.0423},  # NE / Bustleton
    "19116": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.1174, "lon": -75.0118},  # NE / Somerton
    "19118": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0716, "lon": -75.2025},  # Chestnut Hill
    "19119": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0545, "lon": -75.1854},  # Mt. Airy / Germantown N
    "19120": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0348, "lon": -75.1217},  # Olney
    "19121": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9818, "lon": -75.1820},  # Strawberry Mansion / N Philly
    "19122": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9787, "lon": -75.1470},  # Fishtown / Temple area
    "19123": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9623, "lon": -75.1454},  # Northern Liberties
    "19124": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0168, "lon": -75.0922},  # Frankford / Juniata
    "19125": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9729, "lon": -75.1331},  # Fishtown / Kensington
    "19126": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0620, "lon": -75.1459},  # Ogontz / Fern Rock
    "19127": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0200, "lon": -75.2268},  # Manayunk
    "19128": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0402, "lon": -75.2385},  # Roxborough
    "19129": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0127, "lon": -75.1910},  # East Falls
    "19130": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9641, "lon": -75.1751},  # Art Museum / Fairmount
    "19131": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9809, "lon": -75.2193},  # Overbrook / Wynnefield
    "19132": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0003, "lon": -75.1710},  # N Philly / Nicetown
    "19133": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9925, "lon": -75.1437},  # N Philly / Kensington
    "19134": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9944, "lon": -75.1179},  # Port Richmond
    "19135": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0255, "lon": -75.0612},  # Wissinoming / Holmesburg border
    "19136": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0371, "lon": -75.0284},  # Holmesburg / Mayfair E
    "19137": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9979, "lon": -75.0864},  # Bridesburg
    "19138": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0501, "lon": -75.1481},  # Germantown E / Stenton
    "19139": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9604, "lon": -75.2278},  # W Philadelphia / Haddington
    "19140": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0098, "lon": -75.1555},  # N Philly / Tioga
    "19141": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0443, "lon": -75.1404},  # Logan / Fern Rock
    "19142": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9286, "lon": -75.2299},  # SW Philly / Elmwood
    "19143": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9467, "lon": -75.2210},  # W Philly / Kingsessing
    "19144": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0334, "lon": -75.1673},  # Germantown
    "19145": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9238, "lon": -75.1854},  # S Philly / Packer Park
    "19146": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9386, "lon": -75.1779},  # Point Breeze / Graduate Hospital
    "19147": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9428, "lon": -75.1538},  # South Philly / Bella Vista
    "19148": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9173, "lon": -75.1568},  # S Philly / Passyunk
    "19149": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0346, "lon": -75.0666},  # NE Philly / Mayfair
    "19150": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0699, "lon": -75.1733},  # Mt. Airy N
    "19151": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 39.9710, "lon": -75.2472},  # W Philly / Overbrook
    "19152": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0601, "lon": -75.0470},  # NE / Rhawnhurst
    "19154": {"city": "Philadelphia",  "state": "PA", "metro": "philadelphia", "lat": 40.0971, "lon": -74.9734},  # NE / Torresdale N
    # Main Line
    "19010": {"city": "Bryn Mawr",   "state": "PA", "metro": "philadelphia", "lat": 40.0187, "lon": -75.3164},  # Bryn Mawr
    "19003": {"city": "Ardmore",     "state": "PA", "metro": "philadelphia", "lat": 40.0077, "lon": -75.2889},  # Ardmore
    "19041": {"city": "Haverford",   "state": "PA", "metro": "philadelphia", "lat": 40.0063, "lon": -75.3027},  # Haverford
    "19072": {"city": "Wynnewood",   "state": "PA", "metro": "philadelphia", "lat": 40.0220, "lon": -75.2789},  # Wynnewood
    "19085": {"city": "Villanova",   "state": "PA", "metro": "philadelphia", "lat": 40.0349, "lon": -75.3498},  # Villanova
    "19087": {"city": "Wayne",       "state": "PA", "metro": "philadelphia", "lat": 40.0432, "lon": -75.3932},  # Wayne
    "19035": {"city": "Gladwyne",    "state": "PA", "metro": "philadelphia", "lat": 40.0533, "lon": -75.2924},  # Gladwyne
    "19096": {"city": "Narberth",    "state": "PA", "metro": "philadelphia", "lat": 40.0173, "lon": -75.2635},  # Narberth / Wynnewood E
    # Delaware County
    "19063": {"city": "Media",        "state": "PA", "metro": "philadelphia", "lat": 39.9167, "lon": -75.3907},  # Media
    "19081": {"city": "Swarthmore",   "state": "PA", "metro": "philadelphia", "lat": 39.9022, "lon": -75.3471},  # Swarthmore
    "19083": {"city": "Havertown",    "state": "PA", "metro": "philadelphia", "lat": 39.9822, "lon": -75.3091},  # Havertown
    "19082": {"city": "Upper Darby",  "state": "PA", "metro": "philadelphia", "lat": 39.9614, "lon": -75.2712},  # Upper Darby
    "19050": {"city": "Lansdowne",    "state": "PA", "metro": "philadelphia", "lat": 39.9374, "lon": -75.2720},  # Lansdowne
    "19064": {"city": "Springfield",  "state": "PA", "metro": "philadelphia", "lat": 39.9243, "lon": -75.3198},  # Springfield / Oreland
    # Montgomery County
    "19401": {"city": "Norristown",       "state": "PA", "metro": "philadelphia", "lat": 40.1217, "lon": -75.3399},  # Norristown
    "19403": {"city": "Norristown",       "state": "PA", "metro": "philadelphia", "lat": 40.1408, "lon": -75.3784},  # Norristown W
    "19446": {"city": "Lansdale",         "state": "PA", "metro": "philadelphia", "lat": 40.2413, "lon": -75.2835},  # Lansdale
    "19422": {"city": "Blue Bell",        "state": "PA", "metro": "philadelphia", "lat": 40.1534, "lon": -75.2750},  # Blue Bell
    "19428": {"city": "Conshohocken",     "state": "PA", "metro": "philadelphia", "lat": 40.0753, "lon": -75.3015},  # Conshohocken
    "19002": {"city": "Ambler",           "state": "PA", "metro": "philadelphia", "lat": 40.1548, "lon": -75.2242},  # Ambler
    "19462": {"city": "Plymouth Meeting", "state": "PA", "metro": "philadelphia", "lat": 40.1012, "lon": -75.2826},  # Plymouth Meeting
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
    "north_marin": {
        "name": "North Marin County, CA",
        "center": [38.0500, -122.6200],
        "zoom": 11,
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
    "sonoma": {
        "name": "Sonoma County, CA",
        "center": [38.4400, -122.7200],
        "zoom": 10,
    },
    "napa": {
        "name": "Napa County, CA",
        "center": [38.3800, -122.3500],
        "zoom": 11,
    },
    "mendocino": {
        "name": "Mendocino County, CA",
        "center": [39.3000, -123.4000],
        "zoom": 10,
    },
    "portland": {
        "name": "Portland, OR",
        "center": [45.5051, -122.6750],
        "zoom": 11,
    },
    "salem": {
        "name": "Salem / Keizer, OR",
        "center": [44.9430, -123.0350],
        "zoom": 12,
    },
    "eugene": {
        "name": "Eugene / Springfield, OR",
        "center": [44.0480, -123.0900],
        "zoom": 12,
    },
    "bend": {
        "name": "Bend / Redmond, OR",
        "center": [44.0580, -121.3100],
        "zoom": 11,
    },
    "seattle": {
        "name": "Seattle Metro, WA",
        "center": [47.6150, -122.2900],
        "zoom": 11,
    },
    "tacoma": {
        "name": "Tacoma Metro, WA",
        "center": [47.2400, -122.4500],
        "zoom": 11,
    },
    "olympia": {
        "name": "Olympia / Lacey / Tumwater, WA",
        "center": [47.0370, -122.8700],
        "zoom": 12,
    },
    "sw_washington": {
        "name": "SW Washington / I-5 Corridor, WA",
        "center": [45.8000, -122.7000],
        "zoom": 10,
    },
    "nyc_manhattan": {
        "name": "NYC Manhattan, NY",
        "center": [40.7831, -73.9712],
        "zoom": 13,
    },
    "nyc_brooklyn": {
        "name": "NYC Brooklyn, NY",
        "center": [40.6501, -73.9496],
        "zoom": 12,
    },
    "nyc_queens": {
        "name": "NYC Queens, NY",
        "center": [40.7282, -73.8695],
        "zoom": 12,
    },
    "nyc_bronx_si": {
        "name": "NYC Bronx & Staten Island, NY",
        "center": [40.7400, -73.9600],
        "zoom": 11,
    },
    "upstate_ny": {
        "name": "Upstate New York",
        "center": [43.0100, -76.1500],
        "zoom": 7,
    },
    "philadelphia": {
        "name": "Philadelphia Metro, PA",
        "center": [40.0000, -75.2000],
        "zoom": 11,
    },
}

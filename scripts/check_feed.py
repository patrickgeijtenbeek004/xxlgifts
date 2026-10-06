"""Controleert de ChatGPT Ads-feed voordat hij wordt geüpload. Stopt bij fouten."""
import csv, re, sys

VERPLICHT = ["item_id", "title", "description", "url", "brand", "seller_name",
             "image_url", "availability", "price", "condition", "is_ads_eligible"]
BESCHIKBAARHEID = {"in_stock", "out_of_stock", "preorder", "backorder"}

pad = sys.argv[1]
fouten = []
with open(pad, encoding="utf-8", newline="") as f:
    rijen = list(csv.DictReader(f))
    kolommen = rijen[0].keys() if rijen else []

ontbrekend = [k for k in VERPLICHT if k not in kolommen]
if ontbrekend:
    sys.exit(f"Ontbrekende kolommen: {', '.join(ontbrekend)}")

ids = set()
for n, r in enumerate(rijen, start=2):
    for k in VERPLICHT:
        if not (r.get(k) or "").strip():
            fouten.append(f"regel {n}: {k} is leeg")
    if r["item_id"] in ids:
        fouten.append(f"regel {n}: dubbele item_id {r['item_id']}")
    ids.add(r["item_id"])
    if not re.fullmatch(r"\d+(\.\d{1,2})? [A-Z]{3}", r["price"].strip()):
        fouten.append(f"regel {n}: prijs '{r['price']}' moet zijn als '0.75 EUR'")
    if r["availability"] not in BESCHIKBAARHEID:
        fouten.append(f"regel {n}: onbekende availability '{r['availability']}'")
    for k in ("url", "image_url"):
        if not r[k].startswith("https://"):
            fouten.append(f"regel {n}: {k} is geen https-URL")

if not rijen:
    fouten.append("feed bevat geen producten")
if fouten:
    print("\n".join(fouten))
    sys.exit(f"{len(fouten)} fout(en) gevonden, upload afgebroken.")
print(f"Feed OK: {len(rijen)} producten.")

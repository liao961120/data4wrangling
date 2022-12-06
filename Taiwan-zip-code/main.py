"""
Taiwan Zip Code data
    src: `zip-code.csv`                   (cp950/big5 encoded)
    tgt: `zip2town.json`, `town2zip.json` (UTF-8 encoded)
"""

OUT_ZIP2TOWN = 'zip2town.json'
OUT_TOWN2ZIP = 'town2zip.json'

import json

zip2town = {}
town2zip = {}
with open("zip-code.csv") as f:
    for line in f:
        city, town, code = line.strip().split(',')
        zip2town[code] = (city, town)
        town2zip[f"{city}-{town}"] = code

with open(OUT_ZIP2TOWN, "w", encoding="utf-8") as f: 
    json.dump(zip2town, f, ensure_ascii=False, indent=True)
with open(OUT_TOWN2ZIP, "w", encoding="utf-8") as f: 
    json.dump(town2zip, f, ensure_ascii=False, indent=True)

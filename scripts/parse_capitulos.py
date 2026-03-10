import csv
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data_raw" / "capitulos.txt"
output_file = BASE_DIR / "data_processed" / "capitulos.csv"

rows = []

with open(input_file, encoding="latin1") as f:

    for line in f:

        if not line.startswith("1@"):
            continue

        parts = line.split("@")

        capitulo = parts[1].strip()

        match = re.search(r'CAPITULO\s+\d+\s+(.*)', line)

        if match:

            descripcion = match.group(1).strip()

            rows.append([capitulo, descripcion])

with open(output_file, "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow(["capitulo", "descripcion"])
    writer.writerows(rows)

print("✔ capitulos procesados")
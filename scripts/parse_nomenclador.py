import csv
from pathlib import Path

input_file = Path("data_raw/nomenclador.txt")
output_file = Path("data_processed/nomenclador.csv")

rows = []

with open(input_file, encoding="latin1") as f:
    for line in f:

        if not line.startswith("2@"):
            continue

        parts = line.split("@")

        if len(parts) < 8:
            continue

        codigo_raw = parts[1].strip()
        descripcion = parts[-1].strip()

        if not codigo_raw:
            continue

        rows.append([codigo_raw, descripcion])

with open(output_file, "w", newline="", encoding="latin1") as f:

    writer = csv.writer(f)
    writer.writerow(["codigo", "descripcion"])

    for r in rows:
        writer.writerow(r)

print("Nomenclador procesado:", len(rows))
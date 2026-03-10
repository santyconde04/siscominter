import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data_raw" / "sufijos.txt"
output_file = BASE_DIR / "data_processed" / "sufijos.csv"

rows = []

with open(input_file, encoding="latin1") as f:

    for line in f:

        if not line.startswith("3@"):
            continue

        parts = line.split("@")

        posicion = parts[1].strip()
        sufijo = parts[2].strip()
        descripcion = parts[-1].strip()

        rows.append([
            posicion,
            sufijo,
            descripcion
        ])

with open(output_file, "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow([
        "posicion",
        "sufijo",
        "descripcion"
    ])

    writer.writerows(rows)

print("✔ sufijos procesados")
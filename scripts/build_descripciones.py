import csv

input_file = "data_processed/nomenclador.csv"
output_file = "data_processed/nomenclador_full.csv"

rows = []
lookup = {}

# leer nomenclador
with open(input_file, encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for r in reader:
        codigo = r["codigo"].strip()
        desc = r["descripcion"].strip()

        rows.append((codigo, desc))
        lookup[codigo] = desc


def buscar_prefijo(pref):
    """devuelve primera descripcion que empiece con prefijo"""
    for codigo, desc in rows:
        if codigo.startswith(pref):
            return desc
    return ""


resultados = []

for codigo, desc in rows:

    # solo posiciones finales
    if not codigo[-1].isalpha():
        continue

    # prefijos jerárquicos
    cap = codigo[0:2]
    subcap = codigo[0:4]
    item = codigo[0:7]
    subitem = codigo[0:10]

    desc_cap = buscar_prefijo(cap)
    desc_subcap = buscar_prefijo(subcap)
    desc_item = buscar_prefijo(item)
    desc_subitem = buscar_prefijo(subitem)

    descripcion_full = " ".join([
        desc_cap,
        desc_subcap,
        desc_item,
        desc_subitem,
        desc
    ])

    resultados.append({
        "codigo": codigo,
        "descripcion": descripcion_full
    })


# guardar resultado
with open(output_file, "w", newline="", encoding="utf-8") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=["codigo", "descripcion"]
    )

    writer.writeheader()
    writer.writerows(resultados)

print("Archivo generado:", output_file)
print("Total posiciones:", len(resultados))
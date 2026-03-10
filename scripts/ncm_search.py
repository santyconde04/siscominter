import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ncm_db",
    user="postgres",
    password="cominter"
)

cur = conn.cursor()

print("\nBuscador NCM")
print("Escribe una descripcion de producto\n")

while True:

    query = input("Buscar producto: ")

    if query == "salir":
        break

    sql = """
    SELECT codigo, descripcion
    FROM nomenclador_full
    WHERE to_tsvector('spanish', descripcion)
    @@ plainto_tsquery('spanish', %s)
    LIMIT 10
    """

    cur.execute(sql, (query,))

    resultados = cur.fetchall()

    print("\nResultados:\n")

    for codigo, desc in resultados:

        print("\nNCM:", codigo)
        print(desc)

    print("\n")

cur.close()
conn.close()
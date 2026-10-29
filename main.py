import sqlite3

conn = sqlite3.connect("loja.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS vendas")
cur.execute("""
    CREATE TABLE vendas (
        id INTEGER PRIMARY KEY,
        produto TEXT,
        categoria TEXT,
        quantidade INTEGER,
        preco REAL
    )
""")

dados = [
    ("Caderno", "Papelaria", 10, 12.5),
    ("Caneta", "Papelaria", 50, 3.0),
    ("Mouse", "Informática", 5, 45.0),
    ("Teclado", "Informática", 3, 120.0),
    ("Mochila", "Acessórios", 8, 89.9),
]
cur.executemany(
    "INSERT INTO vendas (produto, categoria, quantidade, preco) VALUES (?, ?, ?, ?)",
    dados,
)
conn.commit()

# Faturamento total por categoria
cur.execute("""
    SELECT categoria, SUM(quantidade * preco) AS total
    FROM vendas
    GROUP BY categoria
    ORDER BY total DESC
""")
for categoria, total in cur.fetchall():
    print(f"{categoria}: R$ {total:.2f}")

conn.close()

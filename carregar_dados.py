"""
Analisador de Gastos Pessoais
-----------------------------
Lê os gastos de um arquivo CSV, carrega em um banco SQLite
e exibe um resumo com totais e médias por categoria.
"""

import sqlite3
import csv


def criar_tabela(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            categoria TEXT,
            descricao TEXT,
            valor REAL
        )
    """)


def limpar_tabela(cursor):
    # evita duplicar dados se o script for rodado mais de uma vez
    cursor.execute("DELETE FROM gastos")


def carregar_csv(cursor, caminho_csv):
    with open(caminho_csv, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        linhas = [
            (linha["data"], linha["categoria"], linha["descricao"], float(linha["valor"]))
            for linha in leitor
        ]
    cursor.executemany(
        "INSERT INTO gastos (data, categoria, descricao, valor) VALUES (?, ?, ?, ?)",
        linhas,
    )
    return len(linhas)


def resumo_por_categoria(cursor):
    cursor.execute("""
        SELECT categoria, COUNT(*) AS qtd, SUM(valor) AS total, AVG(valor) AS media
        FROM gastos
        GROUP BY categoria
        ORDER BY total DESC
    """)
    return cursor.fetchall()


def maiores_gastos(cursor, limite=5):
    cursor.execute("""
        SELECT data, categoria, descricao, valor
        FROM gastos
        ORDER BY valor DESC
        LIMIT ?
    """, (limite,))
    return cursor.fetchall()


def total_geral(cursor):
    cursor.execute("SELECT SUM(valor) FROM gastos")
    return cursor.fetchone()[0]


def main():
    conexao = sqlite3.connect("gastos.db")
    cursor = conexao.cursor()

    criar_tabela(cursor)
    limpar_tabela(cursor)
    qtd_linhas = carregar_csv(cursor, "gastos.csv")
    conexao.commit()

    print(f"{qtd_linhas} registros carregados no banco 'gastos.db'.\n")

    print("=== TOTAL GERAL ===")
    print(f"R$ {total_geral(cursor):.2f}\n")

    print("=== GASTOS POR CATEGORIA ===")
    for categoria, qtd, total, media in resumo_por_categoria(cursor):
        print(f"{categoria:<15} | {qtd:>2} lançamentos | Total: R$ {total:>8.2f} | Média: R$ {media:>6.2f}")

    print("\n=== TOP 5 MAIORES GASTOS ===")
    for data, categoria, descricao, valor in maiores_gastos(cursor):
        print(f"{data} | {categoria:<12} | {descricao:<25} | R$ {valor:.2f}")

    conexao.close()


if __name__ == "__main__":
    main()

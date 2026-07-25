# Analisador de Gastos Pessoais

Projeto pessoal de análise de dados que organiza e analisa gastos financeiros
mensais, usando **Python**, **SQL (SQLite)** e **Power BI**.

## O que o projeto faz

1. Lê os lançamentos de gastos de um arquivo `gastos.csv`
2. Carrega os dados em um banco de dados **SQLite** (`gastos.db`)
3. Executa consultas SQL para gerar:
   - total gasto por categoria
   - gasto médio por categoria
   - os 5 maiores gastos do período
   - percentual de cada categoria no total
4. Os mesmos dados são explorados visualmente em um **dashboard no Power BI**,
   com gráficos de pizza (distribuição por categoria), linha (evolução por
   data) e cartões de indicadores.

## Tecnologias usadas

- Python (manipulação de dados, leitura de CSV, `sqlite3`)
- SQL (`CREATE TABLE`, `INSERT`, `SELECT`, `GROUP BY`, subqueries)
- SQLite (banco de dados local)
- Power BI (visualização e dashboard)

## Estrutura do repositório

```
├── gastos.csv          # dados de entrada (gastos por data/categoria)
├── carregar_dados.py   # script que cria o banco e carrega os dados
├── consultas.sql        # consultas SQL usadas na análise
├── gastos.db            # banco SQLite gerado (criado ao rodar o script)
└── dashboard_gastos.pbix  # dashboard em Power BI
```

## Como rodar

```bash
python carregar_dados.py
```

O script cria o banco `gastos.db`, carrega os dados do CSV e imprime no
terminal um resumo com total geral, gasto por categoria e os maiores gastos.

## Exemplo de saída

```
=== TOTAL GERAL ===
R$ 3300.00

=== GASTOS POR CATEGORIA ===
Alimentação     | 13 lançamentos | Total: R$ 1319.80 | Média: R$ 101.52
Moradia         |  4 lançamentos | Total: R$  703.30 | Média: R$ 175.82
Transporte      |  8 lançamentos | Total: R$  553.70 | Média: R$  69.21
...
```

## Próximos passos

- Adicionar entrada de dados via input do usuário (sem precisar editar o CSV)
- Criar alertas quando uma categoria ultrapassar um limite de gasto mensal
- Migrar o banco para PostgreSQL como exercício de outro SGBD

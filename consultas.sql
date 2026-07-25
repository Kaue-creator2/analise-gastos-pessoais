-- ============================================
-- Consultas SQL - Analisador de Gastos Pessoais
-- Banco: gastos.db | Tabela: gastos
-- ============================================

-- 1. Total gasto por categoria (do maior para o menor)
SELECT categoria, SUM(valor) AS total
FROM gastos
GROUP BY categoria
ORDER BY total DESC;

-- 2. Gasto médio por categoria
SELECT categoria, AVG(valor) AS media
FROM gastos
GROUP BY categoria
ORDER BY media DESC;

-- 3. Os 5 maiores gastos individuais
SELECT data, categoria, descricao, valor
FROM gastos
ORDER BY valor DESC
LIMIT 5;

-- 4. Total gasto por mês
SELECT strftime('%Y-%m', data) AS mes, SUM(valor) AS total
FROM gastos
GROUP BY mes
ORDER BY mes;

-- 5. Quantidade de lançamentos por categoria
SELECT categoria, COUNT(*) AS quantidade
FROM gastos
GROUP BY categoria
ORDER BY quantidade DESC;

-- 6. Gastos acima da média geral (subquery)
SELECT data, categoria, descricao, valor
FROM gastos
WHERE valor > (SELECT AVG(valor) FROM gastos)
ORDER BY valor DESC;

-- 7. Percentual de cada categoria no total geral
SELECT
    categoria,
    SUM(valor) AS total,
    ROUND(100.0 * SUM(valor) / (SELECT SUM(valor) FROM gastos), 1) AS percentual
FROM gastos
GROUP BY categoria
ORDER BY percentual DESC;

-- 8. Buscar gastos por palavra-chave na descrição (LIKE)
SELECT * FROM gastos WHERE descricao LIKE '%Mercado%';

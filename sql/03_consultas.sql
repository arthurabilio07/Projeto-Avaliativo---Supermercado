
--// CONSULTAS DA CAMADA RAW //--

-- Conferir quantidade de registros
SELECT COUNT(*) AS quantidade_registros
FROM raw_vendas;


-- Conferir filiais existentes
SELECT DISTINCT branch
FROM raw_vendas;


-- Conferir cidades existentes
SELECT DISTINCT city
FROM raw_vendas;


-- Conferir linhas de produto existentes
SELECT DISTINCT product_line
FROM raw_vendas;


-- Conferir formas de pagamento existentes
SELECT DISTINCT payment
FROM raw_vendas;

--// CONSULTAS DA CAMADA TRATADA //--

-- 1. Receitas por filial
SELECT
    filial,
    SUM(valor_total) AS receita_total
FROM vendas_tratadas
GROUP BY filial
ORDER BY receita_total DESC;

-- 2. Quantidade de vendas por filial
SELECT
    filial,
    COUNT(*) AS quantidade_vendas
FROM vendas_tratadas
GROUP BY filial
ORDER BY quantidade_vendas DESC;

-- 3. Receita por linha de produto
SELECT
    filial,
    COUNT(*) AS quantidade_vendas
FROM vendas_tratadas
GROUP BY filial
ORDER BY quantidade_vendas DESC;

-- 4. Avaliação média por linha de produto
SELECT
    linha_produto,
    AVG(avaliacao) AS avaliacao_media
FROM vendas_tratadas
GROUP BY linha_produto
ORDER BY avaliacao_media DESC;

-- 5. Forma de pagamento mais utilizada
SELECT
    forma_pagamento,
    COUNT(*) AS quantidade
FROM vendas_tratadas
GROUP BY forma_pagamento
ORDER BY quantidade DESC;


-- 6. Valor médio das vendas
SELECT
    AVG(valor_total) AS valor_medio
FROM vendas_tratadas;

-- 7. Maior venda 
SELECT
    MAX(valor_total) AS maior_venda
FROM vendas_tratadas;

-- 8. Dia da semana com mais vendas
SELECT
    TRIM(TO_CHAR(data_venda, 'Day')) AS dia_semana,
    COUNT(*) AS quantidade_vendas
FROM vendas_tratadas
GROUP BY TRIM(TO_CHAR(data_venda, 'Day'))
ORDER BY quantidade_vendas DESC;

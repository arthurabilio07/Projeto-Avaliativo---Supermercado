# Projeto Avaliativo - Análise de Vendas de Supermercado

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de realizar uma análise de dados de vendas de um supermercado. A proposta foi aplicar etapas de banco de dados, SQL, Python, Pandas, tratamento de dados, estatística descritiva e visualização de informações.

O projeto foi desenvolvido utilizando PostgreSQL para armazenamento e consultas dos dados e Python com Pandas e Matplotlib para tratamento, análise e geração dos gráficos.

## Base de dados

A base utilizada foi a **Supermarket Sales**, disponibilizada pelo Kaggle.

Fonte: https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales

A base possui **1.000 registros** e **17 colunas**, contendo informações sobre vendas, clientes, produtos, formas de pagamento e avaliações.

Principais informações disponíveis:

- Número da venda
- Filial
- Cidade
- Tipo de cliente
- Gênero
- Linha de produto
- Preço unitário
- Quantidade
- Imposto
- Valor total
- Data e hora da venda
- Forma de pagamento
- Custo da mercadoria
- Margem percentual
- Receita bruta
- Avaliação

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- PostgreSQL
- DBeaver
- VS Code
- Git e GitHub

## Etapas do projeto

### 1. Importação e análise dos dados

A base original foi armazenada na camada Raw do PostgreSQL, mantendo os dados em seu formato original.

Também foi realizada uma análise inicial utilizando Pandas para verificar a quantidade de registros e colunas, tipos de dados, valores nulos, registros duplicados, valores únicos e estatísticas descritivas.

### 2. Consultas SQL

Foram realizadas consultas utilizando PostgreSQL para explorar os dados e obter informações como:

- Receita por filial
- Quantidade de vendas por filial
- Receita por linha de produto
- Avaliação média por linha de produto
- Formas de pagamento
- Valor médio das vendas
- Maior venda
- Quantidade de vendas por dia da semana

### 3. Tratamento dos dados

Os dados foram tratados utilizando Python e Pandas.

Foram realizadas conversões de tipos, padronização dos nomes das colunas e verificações de qualidade dos dados.

Também foram verificadas:

- Valores nulos
- Registros duplicados
- IDs de venda duplicados
- Quantidades
- Avaliações

Foi realizada ainda uma validação do valor total das vendas, comparando o valor original com o cálculo do preço unitário, quantidade e imposto.

Após o tratamento, os dados foram salvos em uma nova base:

```
data/processed/vendas_tratadas.csv
```

### 4. Estatística e análise

Foram utilizadas estatísticas descritivas e agrupamentos com Pandas para responder às perguntas propostas no projeto.

As análises consideraram as filiais, linhas de produtos, formas de pagamento, valores das vendas e dias da semana.

### 5. Visualização dos dados

Foram criados gráficos utilizando Matplotlib para representar os principais resultados encontrados na análise.

Os gráficos e arquivos com os resultados estão armazenados na pasta:


```
resultados/
```

### Principais resultados

1. A filial Giza apresentou a maior receita, com aproximadamente  110.568,71 .
2. A filial Alex apresentou a maior quantidade de vendas, com  340 vendas .
3. A linha de produto Food and beverages apresentou a maior receita, com aproximadamente  56.144,84 .
4. Food and beverages também apresentou a maior avaliação média, com aproximadamente  7,11 .
5. A forma de pagamento mais utilizada foi  Ewallet , com  345 vendas .
6. O valor médio das vendas foi aproximadamente  322,97 .
7. A maior venda registrada foi de  1.042,65 .
8. O sábado foi o dia da semana com maior quantidade de vendas, com  164 vendas .

## ETL e qualidade dos dados

O processo realizado no projeto possui relação com o conceito de ETL (Extract, Transform, Load).

**Extract:** os dados foram obtidos a partir do arquivo CSV original e armazenados na camada Raw.

**Transform:** foram realizadas conversões, padronização das colunas e verificações dos dados utilizando Python e Pandas.

**Load:** os dados tratados foram salvos em um novo arquivo CSV e também carregados na tabela de dados tratados do PostgreSQL.

A separação entre os dados originais e tratados permite manter a base original preservada e utilizar uma versão preparada para as análises.

### Estrutura do projeto

```Projeto
├── sql/
│   ├── 01_criar_banco.sql
│   ├── 02_criar_tabelas.sql
│   └── 03_consultas.sql
├── src/
│   ├── 01_leitura_dados.py
│   ├── 02_etl_vendas.py
│   └── 03_estatistica.py
├── data/
│   ├── raw/
│   └── processed/
├── resultados/
├── README.md
├── requirements.txt
└── .gitignore
```

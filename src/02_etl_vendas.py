import pandas as pd


# Leitura dos dados brutos
df = pd.read_csv("data/raw/SuperMarket_Analysis.csv")

# Conversão de tipos
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M:%S %p").dt.time

print("Tipos após conversão:")
print(df.dtypes)

df["dia_semana"] = df["Date"].dt.day_name()

# Padronização dos nomes das colunas
df = df.rename(columns={
    "Invoice ID": "id_venda",
    "Branch": "filial",
    "City": "cidade",
    "Customer type": "tipo_cliente",
    "Gender": "genero",
    "Product line": "linha_produto",
    "Unit price": "preco_unitario",
    "Quantity": "quantidade",
    "Tax 5%": "imposto",
    "Sales": "valor_total",
    "Date": "data_venda",
    "Time": "hora_venda",
    "Payment": "forma_pagamento",
    "cogs": "custo_mercadoria",
    "gross margin percentage": "margem_percentual",
    "gross income": "receita_bruta",
    "Rating": "avaliacao"
})

# Verificação de valores nulos
print("\nValores nulos:")
print(df.isnull().sum())

# Verificação de registros duplicados
print("\nRegistros duplicados:")
print(df.duplicated().sum())

# Verificação de IDs de venda duplicados
print("\nIDs de venda duplicados:")
print(df["id_venda"].duplicated().sum())

# Verificação das quantidades
print("\nQuantidade mínima:")
print(df["quantidade"].min())

# Verificação dos valores de avaliação
print("\nAvaliação mínima:")
print(df["avaliacao"].min())

print("\nAvaliação máxima:")
print(df["avaliacao"].max())

# Validação do valor total
valor_total_calculado = (
    df["preco_unitario"] * df["quantidade"] + df["imposto"]
)

diferencas = (
    df["valor_total"] - valor_total_calculado
).abs()

print("\nMaior diferença entre valor total original e calculado:")
print(diferencas.max())

print("\nQuantidade de valores com diferença:")
print((diferencas > 0.01).sum())

# Salvamento da base tratada
df.to_csv(
    "data/processed/vendas_tratadas.csv",
    index=False
)

print("\nBase tratada salva com sucesso!")
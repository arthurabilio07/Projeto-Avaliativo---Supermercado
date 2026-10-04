import os

import matplotlib.pyplot as plt
import pandas as pd

# Leitura da base tratada
df = pd.read_csv("data/processed/vendas_tratadas.csv")


# Conversão das colunas de data e hora
df["data_venda"] = pd.to_datetime(df["data_venda"])
df["hora_venda"] = pd.to_datetime(
    df["hora_venda"],
    format="%H:%M:%S"
).dt.time


# Estatísticas descritivas
print("ESTATÍSTICAS DESCRITIVAS")
print(df.describe())


# 1. Receita por filial
receita_filial = (
    df.groupby("filial")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRECEITA POR FILIAL")
print(receita_filial)


# 2. Quantidade de vendas por filial
vendas_filial = (
    df.groupby("filial")
    .size()
    .sort_values(ascending=False)
)

print("\nQUANTIDADE DE VENDAS POR FILIAL")
print(vendas_filial)


# 3. Receita por linha de produto
receita_produto = (
    df.groupby("linha_produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRECEITA POR LINHA DE PRODUTO")
print(receita_produto)


# 4. Avaliação média por linha de produto
avaliacao_produto = (
    df.groupby("linha_produto")["avaliacao"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAVALIAÇÃO MÉDIA POR LINHA DE PRODUTO")
print(avaliacao_produto)


# 5. Forma de pagamento mais utilizada
pagamentos = (
    df["forma_pagamento"]
    .value_counts()
)

print("\nFORMAS DE PAGAMENTO")
print(pagamentos)


# 6. Valor médio das vendas
valor_medio = df["valor_total"].mean()

print("\nVALOR MÉDIO DAS VENDAS")
print(valor_medio)


# 7. Maior venda
maior_venda = df["valor_total"].max()

print("\nMAIOR VENDA")
print(maior_venda)


# 8. Dia da semana com mais vendas
vendas_dia_semana = (
    df["data_venda"]
    .dt.day_name()
    .value_counts()
)

print("\nQUANTIDADE DE VENDAS POR DIA DA SEMANA")
print(vendas_dia_semana)


# Criação da pasta de resultados

os.makedirs("resultados", exist_ok=True)


# Salvamento dos resultados
receita_filial.to_csv("resultados/receita_por_filial.csv")
vendas_filial.to_csv("resultados/vendas_por_filial.csv")
receita_produto.to_csv("resultados/receita_por_linha_produto.csv")
avaliacao_produto.to_csv("resultados/avaliacao_por_linha_produto.csv")
pagamentos.to_csv("resultados/formas_pagamento.csv")
vendas_dia_semana.to_csv("resultados/vendas_por_dia_semana.csv")

print("\nResultados salvos na pasta resultados!")



# Criação dos gráficos

# Receita por filial
plt.figure()
receita_filial.plot(kind="bar")
plt.title("Receita por Filial")
plt.xlabel("Filial")
plt.ylabel("Receita")
plt.tight_layout()
plt.savefig("resultados/receita_por_filial.png")
plt.close()


# Quantidade de vendas por filial
plt.figure()
vendas_filial.plot(kind="bar")
plt.title("Quantidade de Vendas por Filial")
plt.xlabel("Filial")
plt.ylabel("Quantidade de Vendas")
plt.tight_layout()
plt.savefig("resultados/vendas_por_filial.png")
plt.close()


# Receita por linha de produto
plt.figure()
receita_produto.plot(kind="bar")
plt.title("Receita por Linha de Produto")
plt.xlabel("Linha de Produto")
plt.ylabel("Receita")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("resultados/receita_por_linha_produto.png")
plt.close()


# Avaliação média por linha de produto
plt.figure()
avaliacao_produto.plot(kind="bar")
plt.title("Avaliação Média por Linha de Produto")
plt.xlabel("Linha de Produto")
plt.ylabel("Avaliação Média")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("resultados/avaliacao_por_linha_produto.png")
plt.close()


# Formas de pagamento
plt.figure()
pagamentos.plot(kind="bar")
plt.title("Formas de Pagamento")
plt.xlabel("Forma de Pagamento")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig("resultados/formas_pagamento.png")
plt.close()


# Vendas por dia da semana
plt.figure()
vendas_dia_semana.plot(kind="bar")
plt.title("Quantidade de Vendas por Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Quantidade de Vendas")
plt.tight_layout()
plt.savefig("resultados/vendas_por_dia_semana.png")
plt.close()


print("Gráficos salvos com sucesso!")
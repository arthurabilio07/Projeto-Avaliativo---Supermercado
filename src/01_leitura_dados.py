import pandas as pd

df = pd.read_csv("data/raw/SuperMarket_Analysis.csv")

print("Primeiras linhas:")
print(df.head())

print("\nDimensões:")
print(df.shape)

print("\nColunas:")
print(df.columns)

print("\nTipos de dados:")
print(df.dtypes)

print("\nValores nulos:")
print(df.isnull().sum())

print("\nRegistros duplicados:")
print(df.duplicated().sum())

print("\nValores únicos:")
for coluna in df.columns:
    print(f"\n{coluna}:")
    print(df[coluna].unique())

print("\nEstatísticas descritivas:")
print(df.describe())
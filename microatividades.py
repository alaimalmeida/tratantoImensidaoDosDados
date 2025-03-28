import pandas as pd

# Definindo o nome do arquivo CSV
arquivo_csv = "dados.csv"

# Lendo o arquivo CSV
tabela = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')

print("Informações gerais do conjunto:")
print(tabela.info())

totalLinhas, totalColunas = tabela.shape
print(f"\nQuantidade de linhas: {totalLinhas}")
print(f"Quantidade de colunas: {totalColunas}")

print("\nQuantidade de valores nulos por coluna:")
print(tabela.isnull().sum())

print("\nTipo de dado de cada coluna:")
print(tabela.dtypes)

print("\nMemória utilizada pelo conjunto de dados:")    
print(tabela.memory_usage(deep=True))
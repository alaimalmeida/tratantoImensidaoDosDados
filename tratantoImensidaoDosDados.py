#  Importar a biblioteca Pandas
import pandas as pd

#  Definir o nome do arquivo CSV
arquivo_csv = "dados.csv"

#  Ler o conteúdo do CSV, incluindo parâmetros necessários
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')

#  Exibir as primeiras linhas do DataFrame para conferir a leitura dos dados
print("Visualização inicial dos dados:")
print(dados.head())

# 4. Exibir informações gerais sobre o DataFrame
print("\nInformações gerais do dataset:")
print(dados.info())

# 5. Primeiras linhas do arquivo
print("\nPrimeiras linhas do dataset:")
print(dados.head())

# 6. Ultimas linhas do arquivo
print("\nUltimas linhas do dataset:")
print(dados.tail())

# 7. Nova variável com os mesmos dados anteriores
novos_dados = dados.copy()
print(novos_dados)

# 8. Substituindo todos os valores nulos da coluna "Calories" por zero
novos_dados["Calories"].fillna(0, inplace=True)
print("Substituição de todos os valores nulos da coluna ‘Calories’ por 0")

# 9. Imprima o conjunto de dados para verificar se a mudança acima foi aplicada com sucesso
print("\nNovos dados:")
print(novos_dados)

# 10. Substituição dos valores nulos da coluna ‘Date’ por ‘1900/01/01’
novos_dados["Date"].fillna("1900/01/01", inplace=True)
print(novos_dados)

# 11. Transforme os dados da coluna ‘Date’ em datetime usando o método ‘to_datetime’;
novos_dados['Date'] = pd.to_datetime(novos_dados['Date'], format='%Y/%m/%d', errors='coerce')
print(novos_dados)

# 12. Substituir o valor '1900/01/01' por 'NaN' na coluna 'Date'
novos_dados['Date'].replace('1900/01/01', 'NaN', inplace=True)

# 13. Transformar novamente a coluna 'Date' para o formato datetime
novos_dados['Date'] = pd.to_datetime(novos_dados['Date'], format='%Y/%m/%d', errors='coerce')
print(novos_dados)


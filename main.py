import pandas as pd

# Abrindo e lendo o arquivo.txt
with open("palavras.txt", "r", encoding="utf-8-sig") as arquivo:
    # Capturando as palavras em uma lista sem o "\n" no final
    texto: list[str] = [palavra[:-1] for palavra in arquivo.readlines()]

# Declarando a varíavel da tabela, que irá receber um dict para cada linha
tabela = []

while len(texto) >= 6:
    # Criando um dicionário com as primeiras 6 linhas atuais e inserindo na tabela
    palavras = texto[:6]
    tabela.append({1: palavras[0], 2: palavras[1], 3: palavras[2],
                   4: palavras[3], 5: palavras[4], 6: palavras[5]})
    # Apagando as primeiras 6 palavras
    texto = texto[6:]

# Transformando a tabela em um DataFrame
tabela = pd.DataFrame(data=tabela)

# Gerando o arquivo em excel da tabela sem o cabeçalho e a coluna de índice
tabela.to_excel("tabela_de_palavras.xlsx", header=False, index=False)

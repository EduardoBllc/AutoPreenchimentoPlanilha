import pandas as pd
import random

# Abrindo e lendo o arquivo.txt
with open("palavras.txt", "r", encoding="utf-8-sig") as arquivo:
    # Recebendo as palavras em uma lista sem o "\n" no final e separando caso tenha mais de 1 palavra por linha
    lista_palavras: list[list[str] | str] = [palavra[:-1].split(" ") if palavra.count(" ") else palavra[:-1]
                                             for palavra in arquivo.readlines()]

# Certificando que todas as palavras estão separadas ou em listas de palavras
if [','] in lista_palavras:
    for item in lista_palavras:
        item.split(',')
if [';'] in lista_palavras:
    for item in lista_palavras:
        item.split(';')

terminacoes: list[str] = ['ão', 'om']

# Para cada item da lista_palavras(que pode ter tanto strings quanto listas por conta do split)
for item in lista_palavras:
    # Se o item for uma lista
    if type(item) == list:
        # Para cada palavra dessa lista
        for palavra in item:
            # Se a palavra tiver a terminação indicada e a não estiver repetida, adiciona a palavra na lista_palavras
            if palavra[-len(terminacoes[0]):] in terminacoes and lista_palavras.count(item) < 2:
                lista_palavras.append(palavra)
        # Remove a lista após tratamento
        lista_palavras.remove(item)
    # Se não for uma lista mas não estiver de acordo com as terminações indicadas ou estiver repetida, remove o item
    elif item[-len(terminacoes[0]):] not in terminacoes or lista_palavras.count(item) > 1:
        lista_palavras.remove(item)

# Embaralhando as palavras
random.shuffle(lista_palavras)

# Declarando a varíavel da tabela, que irá receber um dict para cada linha
tabela: list[dict[int:str]] = []

# Limitando em 5 para não gerar linhas incompletas
while len(lista_palavras) >= 5:

    # Criando um dicionário com as primeiras 5 linhas atuais e inserindo na tabela
    tabela.append({lista_palavras.index(palavra): palavra for palavra in lista_palavras[:5]})
    # Apagando as primeiras 5 palavras
    lista_palavras = lista_palavras[5:]

# Gerando o arquivo em excel da tabela sem o cabeçalho e a coluna de índice
pd.DataFrame(data=tabela).to_excel("tabela_de_palavras.xlsx", header=False, index=False)

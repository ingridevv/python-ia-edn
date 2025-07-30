"""

2- Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.


"""

import csv

print("========================= Escrita de Arquivo CSV ========================= ")

dados = [
    ['Ingrid', '20', 'São Paulo'],
    ['Gabriel', '23', 'São Paulo'],
    ['Carla', '30', 'Belo Horizonte']
]

# Solicitar nome do arquivo do usuário
arquivo = input("Qual o nome do arquivo?")

try: 
    with open(arquivo, 'w', newline='', encoding="utf-8") as arquivo_csv:
        escreva = csv.writer(arquivo_csv) 
        escreva.writerow(dados)
    print(f"Dados armazenados no arquivo: {arquivo} !")
except Exception as erro:
    print(f"Erro ao gravar arquivo, tente novamente. {erro} ")

print("================================================================================ ")
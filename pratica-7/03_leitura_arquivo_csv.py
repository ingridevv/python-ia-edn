"""
3- Leitura de Arquivo CSV  
Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:

* Solicite ao usuário o nome do arquivo CSV a ser lido.  
* Utilize o módulo `csv` para abrir o arquivo e ler os dados.  
* Exiba cada linha completa como uma lista.  
* Trate erros como arquivo inexistente ou problemas na leitura.

Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.

"""

print("========================= Leitura de Arquivo CSV ========================= ")

import csv

# Solicitar o nome do arquivo para o usuário
caminho_arquivo = input("Qual o nome do arquivo? (Ex.: pratica-7/dados.csv) ")

try: 
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_csv:
        leitura = csv.reader(arquivo_csv)
        for linha in leitura:
            print(linha)
except FileNotFoundError:
    print(f"Arquivo {caminho_arquivo} não encontrado.")
except Exception as erro:
    print(f"Erro ao ler arquivo: {erro}")



print("================================================================================ ")
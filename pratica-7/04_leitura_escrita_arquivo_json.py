"""
4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. 
Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.

"""

import json

print("========================= Leitura e Escrita de Arquivo JSON ========================= ")

# Lista de user com três campos
usuario = {
    "nome": "Ingrid",
    "idade": 20,
    "cidade": "Sâo Paulo"
}

# Solicitar nome do arquivo para o usuário
arquivo_user = input("Qual o nome do arquivo? (Ex.: dados.json) ")

try:
    # Escrever dados
    with open(arquivo_user, "w", encoding="utf-8") as arquivo:
        json.dump(usuario, arquivo, indent=4, ensure_ascii=False)

    # Leitura de dados
    with open(arquivo_user, "r", encoding="utf-8") as arquivo:
        carregar_dados = json.load(arquivo)

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")

print(carregar_dados)

print("================================================================================ ")
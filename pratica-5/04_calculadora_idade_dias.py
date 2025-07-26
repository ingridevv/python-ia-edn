"""
4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.

"""

from datetime import datetime # Importar biblioteca datetime

print("======================= Calculadora de Idade em Dias =======================")

# Solicita ano de nascimento do usuário
ano_nascimento = int(input("Em que ano você nasceu? "))

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year # Armazena na variável o ano atual
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365 # Desconsiderar anos bissextos
    return idade_anos, idade_dias

idade_anos, idade_dias = calcular_idade_em_dias(ano_nascimento)

print(f"Idade: {ano_nascimento} anos")
print(f"Idade em dias (desconsiderando bissextos): {idade_dias} dias")

print("==============================================")

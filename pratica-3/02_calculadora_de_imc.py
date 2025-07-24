"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"

"""

print("=================== Classificador de IMC =================== ")

# Solicitação dos dados do usuário
peso = float(input("Digite seu peso (em Kg): "))
altura = float(input("Digite sua altura (em Metros): "))


# Dicionário da Tabela IMC
tabela_imc = {
    18.5: "Abaixo do peso",
    25.0: "Peso normal",
    30.0: "Sobrepeso",
}

def calculadora_imc(peso, altura):
    return peso /( altura ** 2 ) # altura ao quadrado

imc = calculadora_imc(peso, altura)
print(f"Seu IMC é de: {imc:.2f}")

print("======================================")
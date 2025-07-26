"""
1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.

"""

print("======================= Calculadora de Gorjeta =======================")

# Função que realiza o cálculo final
def calculadora_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    total = valor_conta + gorjeta
    return gorjeta, total

# Laço de iteração para solicitar conta e gorjeta
while True:
    try:
        # Solicita ao usuário valor da conta e porcentagem da gorjeta
        valor_conta = float(input("Qual o valor da conta (Ex.: 100): "))
        porcentagem = int(input("Qual porcentagem da gorjeta? (ex: 10%, 15%, 20%)"))

        # Função para calcular
        gorjeta, total = calculadora_gorjeta(valor_conta, porcentagem)

        print("=================================================================================")
        print(f"Valor conta: R$ {valor_conta}")
        print(f"Gorjeta: {porcentagem}%: R% {gorjeta:.2f}")
        print("=================================================================================")
        print(f"Total a pagar: R$ {total:.2f}")

    except ValueError:
        print("Valor inserido é inválido.")
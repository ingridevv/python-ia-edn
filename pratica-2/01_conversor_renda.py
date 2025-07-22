"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.


"""

print("============ Conversor de Renda ============ \n")

def converterDolar(valorReais, taxaDolar):
    return valorReais / taxaDolar


def converterEuro(valorReais, taxaEuro):
    return valorReais / taxaEuro

def conversorDolarEuro():
    valorReais = 100.0
    taxaDolar = 5.20
    taxaEuro = 6.15

    dolar = converterDolar(valorReais, taxaDolar)
    euro = converterEuro(valorReais, taxaEuro)

    print(f"Conversões em dólar e euro para R$ {valorReais:.2f}:")
    print(f"O valor em dólar é de ${dolar:.2f}")
    print(f"O valor em euro é de €{euro:.2f}")


conversorDolarEuro()

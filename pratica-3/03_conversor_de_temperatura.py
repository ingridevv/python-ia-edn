"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

"""

print("=================== Conversor de Temperatura =================== ")

# Funções para a conversão 

def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9

def celsius_para_kelvin(c):
    return c + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Dicionário mapeando cada tipo de conversão a uma função

tabela_de_conversoes = {
    "Celsius para Fahrenheit": celsius_para_fahrenheit,
    "Fahrenheit para Celsius": fahrenheit_para_celsius,
    "Celsius para Kelvin": celsius_para_kelvin,
    "Kelvin para Celsius": kelvin_para_celsius,
    "Fahrenheit para Kelvin": fahrenheit_para_kelvin,
    "Kelvin para Fahrenheit": kelvin_para_fahrenheit,
}

print("""
  Celsius para Fahrenheit
  Fahrenheit para Celsius
  Celsius para Kelvin
  Kelvin para Celsius
  Fahrenheit para Kelvin
  Kelvin para Fahrenheit
""")

selecao_conversao = input("Escolha a conversão desejada conforme opções acima: ")
valor_conversao = float(input("Digite o valor que deseja converter: "))

match selecao_conversao:
    case "Celsius para Fahrenheit":
        resultado = celsius_para_fahrenheit(valor_conversao)
    case "Fahrenheit para Celsius":
        resultado = fahrenheit_para_celsius(valor_conversao)
    case "Celsius para Kelvin":
        resultado = celsius_para_kelvin(valor_conversao)
    case  "Kelvin para Celsius":
        resultado = kelvin_para_celsius(valor_conversao)
    case "Fahrenheit para Kelvin":
        resultado = fahrenheit_para_kelvin(valor_conversao)
    case "Kelvin para Fahrenheit":
        resultado = kelvin_para_fahrenheit(valor_conversao)
    case _:
        print("Tipo indefinido.")
        resultado = None

if resultado is not None:
    print(f"Resultado da conversão {selecao_conversao}: {resultado:.2f}")

print("======================================")
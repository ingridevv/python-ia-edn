"""
3- Calculadora de Volume
* Crie um programa que calcula o volume de uma caixa retangular. 
* Use as seguintes dimensões:

* Comprimento: 12 cm
* Largura: 14 cm
* Altura: 20 cm

*O programa deve calcular o volume e exibir o resultado em cm³.

"""

def calcularVolume(comprimento, largura, altura):
    return comprimento * largura * altura 

volumeRetangulo = calcularVolume(12, 14, 20)
print(volumeRetangulo + "cm^3")
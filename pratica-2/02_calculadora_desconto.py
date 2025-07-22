"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

"""

print("============ Calculadora de Desconto ============ \n")

produto = "Camiseta"
preco = 50.00
desconto = 20

def calcularDesconto(preco, desconto):
    return preco * (desconto / 100)

desconto =  calcularDesconto(preco, desconto)
precoFinal = preco - desconto

print(f"O preço final para a {produto} com desconto aplicado é de R$ {precoFinal:.2f}")
print(f"O desconto para a {produto} é de R$ {desconto:.2f}")

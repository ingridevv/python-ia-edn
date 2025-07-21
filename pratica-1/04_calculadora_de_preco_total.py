"""

4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. 
* Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

"""
print("Produto: Cadeira Infantil")
def precoTotal(preco, quantidade):
    return preco * quantidade

totalCompra = precoTotal(12.40, 3)
print("R$: ", totalCompra)
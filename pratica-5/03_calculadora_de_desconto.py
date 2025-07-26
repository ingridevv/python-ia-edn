"""
3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.

"""

print("======================= Calculadora de Desconto em Produto =======================")

# Dicionário que representa uma lista de produtos com desconto
produtos = [
    {"nome": "Macbook", "preco": 15630.45, "quantidade": 1, "desconto": 20},
    {"nome": "iPhone 15", "preco": 5058.18, "quantidade": 1, "desconto": 15},
    {"nome": "Magic Mouse", "preco": 568.21, "quantidade": 2, "desconto": 5},
]

# Função para calcular preço com desconto
def preco_final(preco, quantidade, desconto):
    total_original = preco * quantidade
    total_desconto = total_original * (desconto / 100)
    total_desconto_aplicado = total_original - total_desconto
    return total_desconto_aplicado
    
print("Produtos com Desconto Aplicado")
print("--------------------------------------------------------------")

# Laço de iteração para visualizar cada produto e respectivos descontos
for produto in produtos:
    nome = produto["nome"]
    preco = produto["preco"]
    quantidade = produto["quantidade"]
    desconto = produto["desconto"]

    valor_final = preco_final(preco, quantidade, desconto)

    # Irá apresentar neste formato cada produto com desconto aplicado
    print(f"{nome} - Qtd: {quantidade} - Desconto: {desconto}% - Total com desconto: R$ {valor_final:.2f}")
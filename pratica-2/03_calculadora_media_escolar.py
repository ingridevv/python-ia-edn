"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

"""

print("============ Calculadora de Média Escolar ============ \n")

nota_1 = 7.5
nota_2 = 8.0
nota_3 = 6.5

def calcularMediaEscolar(nota_1, nota_2, nota_3):
    return (nota_1 + nota_2 + nota_3) / 3

resultadoFinal = calcularMediaEscolar(nota_1, nota_2, nota_3)

print("===================================")
print(f"Nota 1: {nota_1} \n")
print(f"Nota 2: {nota_2} \n")
print(f"Nota 3: {nota_3} \n")
print(f"A média escolar do(a) aluno(a) é de: {resultadoFinal:.2f}")

print("===================================")
"""
4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

"""

print("=================== Verificador de Ano Bissexto =================== ")


ano = int(input("Digite o número do ano: "))


def bissexto(ano):
    return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

if bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto. ")



print("======================================")
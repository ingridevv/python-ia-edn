"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).

"""

print("=================== Classificador de Idade =================== ")

idade = int(input("Digite sua idade (em números): "))

# Dicionário das classificações etárias
faixas_etarias = [
    ("Criança (0-12 anos)", range(0, 12)),
    ("Adolescente (13-17 anos)", range(13, 18)),
    ("Adulto (18-59 anos)", range(18, 59)),
    ("Idoso (60 anos ou mais)", range(60, 100)),
]

# Laço que irá iterar cada item do dicionário
for classificacao, faixa in faixas_etarias:
    if idade in faixa:
        print(f"Classificação de idade é de : {classificacao}")
        break

print("======================================")
"""
4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.  

"""

print("======================= Números Inteiros =======================")

# Função para verificar se o número inteiro é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Laço de repetição para solicitar o número ao usuário
while True:
    numero = input("Digite um número inteiro (ou Fim/Sair para encerrar): ")
    if numero.lower() in ("fim", "sair"):
        print("Programa encerrado.")
        break

    # Converte a entrada para número e trata as exceções
    try: 
        entrada = int(numero)
        resultado = par_ou_impar(entrada)
        print(f"O número digitado: {entrada} é {resultado}.")
    except ValueError:
        print("Número inválido. Digite um número inteiro ou Fim para encerrar.")


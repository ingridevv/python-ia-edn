"""
1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.  

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.

"""
print("======================= Calculadora Simples =======================")

# Funções das operações

def soma(numero_A, numero_B):
    return numero_A + numero_B

def subtracao(numero_A, numero_B):
    return numero_A - numero_B

def multiplicacao(numero_A, numero_B):
    return numero_A * numero_B

def divisao(numero_A, numero_B):
    return numero_A / numero_B

# Laço de repetição while que irá solicitar os números ao usuário enquanto ele não digitar Sair
while True: 
    try: 
        numero_A = float(input("Digite um número: ")) 
        numero_B = float(input("Digite outro número: "))
        operacao = input("Escolha uma operação ( +, -, *, / ) ou Sair para encerrar: ")

        match operacao:
            case "+":
                resultado = soma(numero_A, numero_B)
            case "-":
                resultado = subtracao(numero_A, numero_B)
            case "*":
                resultado = multiplicacao(numero_A, numero_B)
            case "/":
                resultado = divisao(numero_A, numero_B)
            case "Sair":
                print("A calculadora será encerrada...")
                break
            case _:
                resultado = "Operação inválida."
        
        print("O resultado é: ", resultado)

    except ValueError:
        print("Entrada inválida. Digite um número real.")
    except ZeroDivisionError:
        print("Erro! não é possível dividir por zero.")
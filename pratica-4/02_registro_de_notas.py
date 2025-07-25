"""
2- Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro.  

"""

print("======================= Registro de Notas =======================")

notas = []

while True: 
    entrada = input("Digite a nota de um aluno (de 0 a 10) ou 'Fim' para encerrar: ")
    
    if entrada.lower() in ("fim", "sair"):
        break

    try:
        nota = int(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota fora do intervalo permitido (0 a 10).")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro de 0 a 10 ou 'Fim' para encerrar.")

print("Notas registradas:")
for nota in notas:
    print(nota)

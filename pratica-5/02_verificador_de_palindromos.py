"""
2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.

Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.

"""

print("======================= Verificador de Palíndromos =======================")

# Solicitar ao usuário frase ou palavra

while True: 
    frase_palavra = input("Insira uma palavra ou frase (ou digite Sair para encerrar): ")

    # Função que desconsidera maíusculas, espaços e sinais de pontuação
    def verificar_palindromo(frase_palavra):
        frase_palavra = frase_palavra.lower()
        frase_palavra = ''.join(caractere for caractere in frase_palavra if caractere.isalnum())
        return frase_palavra == frase_palavra[::-1]

    # Verificar se frase é palíndromo
    print(verificar_palindromo(frase_palavra))



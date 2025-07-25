"""
3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".  

"""

print("======================= Verificador de Senhas Fortes =======================")

# Função que aplica as condições da senha forte
def senha_forte(senha):
    if len(senha) < 8:
        return False
    tem_numero = any(caractere.isdigit() for caractere in senha)
    return tem_numero

# Laço de repetição para solicitar a senha do usuário e verificar as condições
while True:
    senha_user = input("Digite sua senha (ou Sair para encerrar): ")

    match senha_user.lower():
        case "sair":
            print("Programa encerrado.")
            break
        case _:
            match senha_forte(senha_user):
                case True:
                    print("Senha forte!")
                    break
                case False:
                    print("Senha fraca! Tente utilizar pelo menos 8 caracteres e um número.")
  
        

        
    
    
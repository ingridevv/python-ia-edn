"""
1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.

"""

import random
import string

def gerador_senha(length=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation 
    senha = ''.join(random.choice(caracteres) for _ in range(length))
    return senha

senha_gerada = gerador_senha(16)
print(f"A sua senha gerada é: {senha_gerada}")
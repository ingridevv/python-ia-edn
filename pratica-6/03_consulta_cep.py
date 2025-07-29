"""
3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.

"""

import requests 

def consulta_cep(cep):
    try: 
        url = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados = url.json()

        if dados.get("erro"):
            return "CEP não encontrado"
        
        cep = dados['cep']
        logradouro = dados['logradouro']
        bairro = dados['bairro']
        cidade = dados['localidade']
        estado = dados['uf']
        retorno_cep = f"CEP: {cep}\nLogradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade} \nEstado: {estado}"
        return retorno_cep
    except requests.exceptions.RequestException as erro:
        print(f"Erro de consumo de API: {erro}")

print("====================== Consulta CEP ====================== ")
print(consulta_cep(input("Digite o CEP: ")))
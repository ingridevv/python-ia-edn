"""
2- Gerador de Usuário Aleatório  
Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

* Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
* Mostre na tela: nome completo, e-mail e país do usuário.  
* O programa deve tratar possíveis erros de conexão ou falha na API.  

Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados.

"""

import requests # Importar biblioteca que realiza requisições HTTP 

def buscar_usuario():
    response = requests.get("https://randomuser.me/api/") # Link da API para consumo
    if response.status_code == 200:
        data = response.json()['results'][0] # Contém toda a resposta da API
        nome = f"{data['name']['first']} {data['name']['last']}" 
        email = data['email']
        pais = data['location']['country']
        print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")
    else:
        print(f"Código de Erro: {response.status_code}")

buscar_usuario() # Chamada da função

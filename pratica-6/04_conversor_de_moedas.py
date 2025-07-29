"""
4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.

"""
import requests
from datetime import datetime

def exibir_cotacao(moeda):
    moeda = moeda.upper() 
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
  
    try: 
        response = requests.get(url)
        data = response.json()

        chave = f"{moeda}BRL"
        if chave not in data:
            print("Código da moeda inválido.")
            return

        cotacao = data[chave]
        valor_atual = cotacao["bid"]
        valor_max = cotacao["high"]
        valor_min = cotacao["low"]
        data_hora = datetime.fromtimestamp(int(cotacao["timestamp"])).strftime('%d/%m/%Y %H:%M:%S')
        print(f"{moeda}/BRL | Atual: R${valor_atual} | Máx: R${valor_max} | Mín: R${valor_min} | Atualizado em: {data_hora}")
    except Exception as e:
        print("Erro ao consultar API.", e)

moeda = input("Qual o código da moeda que deseja converter (ex: USD, EUR, GBP)? ")
exibir_cotacao(moeda)

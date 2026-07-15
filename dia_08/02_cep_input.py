import requests

cep = input("Entre com um CEP:" )

url = "https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url.format(cep=cep)) 

if resposta.status_code == 200:
    print(resposta.json())


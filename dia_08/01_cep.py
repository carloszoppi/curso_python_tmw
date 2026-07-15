# %%
# !pip install requests
# o requests não estava funcionando porque estava instalado no anaconda
# mas o jupyter estava usando o python do windows, que não tinha o requests instalado. Então, para instalar o requests no jupyter, precisamos usar o comando !pip install requests, que instala o requests no python que está sendo usado pelo jupyter.

# mas ele também não funcionou, eu então troquei no canto 
# superior esquerdo do jupyter (lado interativo), o kernel de python do windows para o kernel de python do anaconda, que é o que tem o requests instalado. E aí funcionou.

# %%

import requests

url = "https://viacep.com.br/ws/01001000/json/"   #endereço de onde vou fazer a requisição, que é o site do ViaCEP, que é um serviço gratuito de consulta de CEPs.

resposta = requests.get(url)
# %%
resposta # só resposta não vai mostrar o que queremos. É preciso adicionar os argumentos para mostrar

# o status code 200 <Response [200]> significa que a requisição foi bem sucedida, ou seja, o servidor respondeu com sucesso à requisição. O status code 404 significa que a página não foi encontrada, ou seja, o servidor não encontrou o recurso solicitado. O status code 500 significa que houve um erro interno no servidor, ou seja, o servidor encontrou uma condição inesperada que o impediu de atender à requisição.

# %%

resposta.raw  # fala que é uma http response, mas não mostra o conteúdo da resposta. Para mostrar o conteúdo da resposta, precisamos usar o método .text ou .json().

# %%
resposta.text  # mostra o conteúdo da resposta em formato de string, que é um JSON, mas não é um dicionário. Para transformar em dicionário, precisamos usar o método .json().

# %%
resposta.json()  # mostra o conteúdo da resposta em formato de dicionário, que é o que queremos. O método .json() transforma o JSON em dicionário.


# %%
dados = resposta.json()  # armazena o conteúdo da resposta em formato de dicionário na variável dados.
type(dados)  # mostra o tipo da variável dados, que é um dicionário.


# %%
dados["cep"]  # acessa o valor da chave "cep" do dicionário dados, que é o CEP consultado.


# %%
# O código então pode ficar limpo assim, sem precisar ficar chamando o requests.get() e o .json() toda hora, porque já armazenamos o resultado em uma variável.

import requests
url = "https://viacep.com.br/ws/01001000/json/"   #endereço de onde vou fazer a requisição, que é o site do ViaCEP, que é um serviço gratuito de consulta de CEPs.
resposta = requests.get(url)
dados = resposta.json()  # armazena o conteúdo da resposta em formato de dicionário na variável dados.
dados 

# Ele está consultando o CEP 01001000, que é o CEP da Praça da Sé, em São Paulo. O resultado é um dicionário com as informações do endereço correspondente ao CEP consultado.

# %%

# Agora se eu quiser importar todos os dados de cada CEP baseado em uma lista 
# de CEPs, eu posso fazer um loop para percorrer a lista de CEPs e fazer a requisição para cada CEP, armazenando os resultados em uma lista de dicionários.

import requests   # para realizar requisições na web
import json       # para salvar os dados em um arquivo JSON
                  # para tratar json de listas/dicionários para arquivos e vice-versa
from tqdm import tqdm  # para mostrar uma barra de progresso durante o loop

ceps = ["01001000", "01310930", "20040002", "13331510"]  # lista de CEPs para consultar

url = "https://viacep.com.br/ws/{cep}/json/"   #endereço de onde vou fazer a requisição, que é o site do ViaCEP, que é um serviço gratuito de consulta de CEPs.
                                             # dá para paratrizar o número do cep na url, usando o {cep} como um placeholder, que será substituído pelo valor do cep na hora da requisição.
dados = []
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))  # faz a requisição para cada CEP da lista, substituindo o {cep} pelo valor do cep na hora da requisição.
    if resposta.status_code == 200:  # verifica se a requisição foi bem sucedida, ou seja, se o status code é 200. Se não for, significa que houve um erro na requisição e não vamos adicionar o resultado na lista de dados.
        dados.append(resposta.json()) # adiciona o resultado da requisição em formato de dicionário na lista de dados.

dados

# %%

print(dados)

# para salvar os dados em um arquivo JSON, podemos usar a biblioteca json do Python, que nos permite converter objetos Python em strings JSON e vice-versa.

with open("ceps.json", "w", encoding="utf-8") as open_file:  # abre o arquivo ceps.json em modo de escrita, que vai criar o arquivo se ele não existir, ou sobrescrever o arquivo se ele já existir.
    json.dump(dados, open_file, ensure_ascii=False, indent=4)  # escreve a lista de dicionários no arquivo ceps.json em formato JSON, com identação de 4 espaços para ficar mais legível.


# %%
# o arquivo foi salvo em local errado. Para evitar isso, podemos usar o caminho absoluto do arquivo, que é o caminho completo do arquivo no sistema operacional. Para isso, podemos usar a biblioteca os, que nos permite manipular caminhos de arquivos e diretórios.
# ou usar pathlib, que é uma biblioteca mais moderna e orientada a objetos para manipular caminhos de arquivos e diretórios.

from pathlib import Path

# Descobre a pasta onde este script atual está salvo
pasta_atual = Path(__file__).parent
caminho_salvamento = pasta_atual / "ceps.json"

# Abre e salva o arquivo no caminho correto
with open(caminho_salvamento, "w", encoding="utf-8") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

# %%


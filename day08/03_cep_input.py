# %%

import requests

cep = input('Entre com um CEP:')

url = 'https://viacep.com.br/ws/{cep}/json/'

response = requests.get(url.format(cep=cep))

dados = dict()

if response.status_code == 200:
    dados = response.json()

for chave, valor in dados.items():
    print(chave, '->', valor)
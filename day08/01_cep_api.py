# %%
import requests # Biblioteca para fazer requisições HTTP
import json # Biblioteca para trabalhar com JSON
from tqdm import tqdm # Biblioteca para mostrar o progresso da execução

ceps = [
    '01001-000',
    '01002-000',
    '01003-000',
    '01004-000',
    '01005-000',
    '01006-000',
    '01007-000',
    '01008-000',
    '01009-000',
    '01010-000',
]


url = 'https://viacep.com.br/ws/{cep}/json/' # URL com {cep} para ser substituido pelo cep
#
dados = []
for i in tqdm(ceps):
    requisicao = requests.get(url.format(cep=i)) # Fazendo a requisição para a API
    # Verifica se a requisição foi bem sucedida
    if requisicao.status_code == 200:
        dados.append(requisicao.json())

dados

with open('cep.json', 'w', encoding='utf-8') as open_file:
    json.dump(dados, open_file, indent=4, ensure_ascii=False) # Escrevendo os dados no arquivo JSON
    print("Dados salvos com sucesso!")

# %%
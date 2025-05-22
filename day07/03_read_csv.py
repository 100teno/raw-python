# %%
arquivo = "data.csv"

with open(arquivo) as open_file:
    conteudo = open_file.readlines()

print(conteudo)

for linha in conteudo:
    print(linha)

# %%
# Se o arquivo CSV tiver cabeçalho, você pode usar a biblioteca csv para ler o arquivo
dados = dict()

chaves = conteudo[0].strip("\n").split(";")
for c in chaves:
    dados[c] = [] # cria uma lista vazia para cada chave

for l in conteudo[1:]:
    
    valores = l.strip("\n").split(";")
    
    for i in range(0, len(valores)):

        dados[chaves[i]].append(valores[i])

# %%
# Dicionario com os dados de idades, em seguida calcula a media
idades = []
for i in dados["idade"]:
    idades.append(int(i))

media_idade = sum(idades) / len(idades)

print("Media de idades: ", media_idade)
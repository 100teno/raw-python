# %%

lista = [21, 
         "Gabriel Centeno",
         "Data Analyst",
         [1800, 2000, 2500],
         True
         ]

lista[3][1: ]

# %%

# Dicionário é uma coleção de pares chave-valor

dados_gabriel = {
    "nome": "Gabriel Centeno",                          ##chave = valor(string)
    "idade": 21,                                        ##chave = valor(int)
    "profissao": "Data Analyst",                        ##chave = valor(string)
    "salario": [1800, 2000, 2500],                      ##chave = valor(lista)
    "casado": True,                                     ##chave = valor(bool)
    "linguagens": ["Python", "SQL", "JavaScript"],      ##chave = valor(lista)
    "cargos": [                                         ##chave = valor(lista de dicionários)                   
        {"nome": "Data Analyst", "empresa":"Exata"},
        {"nome": "Estagiário", "empresa":"Exata"},
        {"nome": "Data Engineer", "empresa":"Amazon"},
        {"nome": "Data Manager", "empresa":"Amazon"}
        ]
}





# dados_gabriel["linguagens"].append("Java") // teste com método append
# print(dados_gabriel)
print(dados_gabriel)
print(dados_gabriel["linguagens"][-1])
print(dados_gabriel)["cargos"][-1]["empresa"]
# %%

dados_gabriel["estado civil"] = "casado" 

#%%

print("Chaves:",dados_gabriel.keys()) ## retorna as chaves do dicionário
print("Valores:",dados_gabriel.values()) ## retorna os valores do dicionário
print("Itens:",dados_gabriel.items()) ## retorna os pares chave-valor do dicionário 

#%%

for i in [10, 20, 30]:
    print(i)

# %%

for i in dados_gabriel:
    print(i, "->", dados_gabriel[i]) ## retorna os pares chave-valor do dicionário

# %%
dados_gabriel.items() ## retorna os pares chave-valor do dicionário

# %%
for chave, valor in dados_gabriel.items():
    print(chave, "->", valor) ## retorna os pares chave-valor do dicionário

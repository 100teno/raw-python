# %% 

# Uma maneira de definir listas


#print(idades)

# %%

gabriel = ["Gabriel", "Casado", 21, 1,"Casado", 1234.80]
print(gabriel)


type(gabriel)


#idade
print(gabriel[2])

#renda
print(gabriel[5])

# %%
idades =[28, 42, 43, 35, 39, 28, 38, 42]
# qtdLista = len(idades)

print("Soma idades:", sum(idades))

print("Media idades: ", sum(idades) / len(idades))

print("Menor Idade:", min(idades))

print("Maior Idade:", max(idades))

# %%
gabriel = ["Gabriel Centeno",  
           21, 
           1,
           "Casado", 
           1234.80,
           ["Dark Souls", "BloodBourne", "Elden Ring"]]

print("Tamanho de gabriel:", len(gabriel))

gabriel[5][2]

jogos = gabriel[5]
primeiro_jogo = jogos[0]
print(primeiro_jogo)

# %%

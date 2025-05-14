# Uma tupla é uma coleção de dados que não pode ser alterada
# Tuplas são imutáveis, ou seja, não podem ser alteradas após a criação
# Elas são definidas entre parênteses e podem conter diferentes tipos de dados
# Tuplas podem conter listas, dicionários e outras tuplas
# Garantindo a imutabilidade dos dados

# %%

dados_gabriel = [21, 1, "Casado", "Data Analyst"]
dados_gabriel

# %%

dados_gabriel.append("São Paulo")
dados_gabriel

# %%
# Criando uma tupla
# tupla_gabriel = 21, 1, "Casado", "Data Analyst" ## Forma mais comum de criar uma tupla
tupla_gabriel = (21,                              ## Outra forma de criar uma tupla
                 1, 
                 "Casado", 
                 "Data Analyst", 
                 ["Dark Souls 1", "Dark Souls 2", "Dark Souls 3"]) 
tupla_gabriel

print(type(tupla_gabriel))
print(tupla_gabriel)

# %%

tupla_gabriel[-1].append("Elden Ring")  # Só é possível alterar os dados dentro da lista
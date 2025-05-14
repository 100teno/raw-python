# Escreva um programa que solicite ao usuário frases. Para parar de solicitar frases,
# ele pode apenas apertar o "ENTER".

# Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.

# %%

dados = {}  # Dicionário para armazenar as frases e suas contagens

while True:
    # Solicita uma frase ao usuário
    entrada = input("Digite uma frase: ")
    if entrada == "":
        break

    if entrada not in dados:
        # Se a frase não estiver no dicionário, adiciona com contagem 1
        dados[entrada] = 1
    else:
        # Se a frase já estiver no dicionário, incrementa a contagem
        dados[entrada] += 1


items = list(dados.items())  # Obtém os itens do dicionário
items.sort(key=lambda x: x[-1], reverse=True)  # Ordena os itens

for i, j in items:
    # Exibe a frase e quantas vezes ela foi repetida
    print(i, "->", j)



# A função lambda é usada como chave de ordenação para o método sort()
# O método sort() ordena a lista de tuplas com base no último elemento (contagem) em ordem decrescente
# lambda x: x[-1] -> função lambda que retorna o último elemento de cada tupla
# x[-1] -> último elemento da tupla
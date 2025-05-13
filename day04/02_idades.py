#%%
idades = []

while True:
    idade = input("Digite a idade (ou 'sair' para encerrar): ")

    if idade == "":
        break

    idades.append(int(idade))

print("Idades digitadas:", idades)

media = sum(idades) / len(idades) 
minima = min(idades)
maxima = max(idades)
quantidade = len(idades)

print("Média das idades:", media)
print("Idade mínima:", minima) 
print("Idade máxima:", maxima)
print("Quantidade de idades:", quantidade)
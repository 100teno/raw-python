# %%
# for percorre os elementos de um objeto

nome = "Gabriel Centeno"

for i in nome:
    print(i)

# %%

numero = 2
max_numero = 100

for i in range(1,max_numero + 1):
    print(numero, "x", i, "=", numero * i )

# %%

#Quais numeros são divisíveis por 4 no intervalo de [4-100]

for i in range(4, 101): 
    if i % 4 == 0:
        print(i)
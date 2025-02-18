# O resultado do print com as variveis está incorreto, pois neste caso o input está retornando um valor em STRING, então o que acontece é uma "multiplicação" da string '2', por exemplo.

# numero = input('Entre com um número para encontrar o seu dobro: ')

# dobro = numero * 2
# print('O dobro de', numero, 'é', dobro)

# # teste de multiplicação string %%
# nome = 'Gabriel'
# nomes = nome * 3
# print(nomes)

# agora convertendo para int, a variável que era string %%

numero = input('Entre com um número para encontrar o seu dobro: ')
numero = int(numero)
dobro = numero * 2
print('O dobro de', numero, 'é', dobro)




# %%

# Escreva um programa que receba uma lista de números
# do usuário e conte quantas vezes um número específico aparece na lista
# Solicite ao usuário um nuúmero que exiba a contagem

#%%
lista = [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

numero = int(input("Digite um número: "))

# for i in lista:
#     if i == numero:
#         print (f"O número {numero} aparece {lista.count(numero)} vezes na lista")


contador = 0
for i in lista:
    if i == numero:
        contador += 1

print ("Quantidade de", numero, ":", contador)
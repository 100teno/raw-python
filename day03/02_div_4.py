# %%

#Quais numeros são divisíveis por 4 no intervalo de [4-100]

count = 4

while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)

    count += 1

print('The end!')
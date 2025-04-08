#Faça um programa que receba uma quantidade indefinida de valores correspondentes a "saldo em conta"
#mas quando o usuário apertar "enter" sem inserir valor, o programa para de receber os valores e exibe a soma de todos os valores digitados.
#%%
saldo_total = 0

while True:
    saldo = input("Digite o seu saldo: ")
    saldo_total += float(saldo)

print("A soma de todos valores é igual a: ", soma)




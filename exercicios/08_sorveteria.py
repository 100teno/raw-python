#%%
print('Bem vindo à minha sorveteria!')
input('Pressione 1 para ler o cardápio: ')

valor = float
valorCobertura = float

print('Tipos de sorvete: Casquinha(R$1,00), Cascão(R$2,50), Cestinha(R$4,00)')
print('Sabores de sorvete: Morango, Creme, Chocolate')
print('Coberturas: Caramelo (R$1,50), Morango(R$1,50), Chocolate(R$1,50), Sem cobertura(R$0,00)')

tipo = input('Escolha o tipo de sorvete: ')
sabor = input('Escolha o sabor do sorvete: ')
cobertura = input('Escolha a cobertura do sorvete: ')

if tipo == 'Casquinha':
    valor = 1.00
elif tipo == 'Cascão':
    valor = 2.50
elif tipo == 'Cestinha':
    valor = 4.00

if cobertura == 'Sem cobertura':
    valorCobertura = 0.00
else:
    valorCobertura = 1.50

print('O valor total do seu pedido é: ', valor + valorCobertura)


#%%

print('Bom dia! Qual agua deseja comprar?')

pedido = input('Deseja com gás ou sem gás?')


if pedido == 'sem gás':
    print('O seu pedido de água sem gás deu R$1,50, qual vai ser a forma de pagamento?')

if pedido == 'com gás':
    print('O seu pedido de água com gás deu R$2,50, qual vai ser a forma de pagamento?')
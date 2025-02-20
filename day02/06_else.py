
# %%
idade = input('Digite sua idade: ')
idade = int(idade)
pais = input('Digite seu país: ')

if idade >= 18 and pais == 'Brasil':
    print('Você mora no Brasil e tem mais de 18 anos, então pode beber.')
else:
    print('Você mora no Brasil e tem menos de 18 anos, então não pode beber.')
 
if idade >= 21 and pais != 'Brasil':
    print('Você não mora no Brasil mas tem mais de 21 anos, então pode beber.')
else:
    print('Você não mora no Brasil e não tem mais de 21 anos, então não pode beber.')

# %%

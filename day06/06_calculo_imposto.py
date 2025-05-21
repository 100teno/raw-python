# %%
# **kwarg são argumentos nomeados, ou seja, 
# você pode passar os argumentos de forma não ordenada.
# o **kwarg é um dicionário que contém todos os argumentos nomeados passados para a função
# sempre precisa ser o último argumento da função
# *args sempre serão uma lista ou tupla
# já o **kwarg sempre será um dicionário

def calc_imposto(preco:float, tx_base= 0.03 , **kwargs):
    
    imposto =  preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto
        
# %%

impostos_gerais = {
    'municipio': 0.01, 
    'estado'   : 0.005, 
    'nacional' : 0.001
}

calc_imposto(100, 0.03, **impostos_gerais, internacional=0.00001)
# calc_imposto(100, 0.03, municipio=0.01, estado=0.005, nacional=0.001)

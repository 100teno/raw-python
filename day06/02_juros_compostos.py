# %%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """juros_compostos serve para calcular o retorno financeiro de um investimento com aporte inicial, 
taxa de juros e número de anos.

Deve-se considerar o valor, a taxa de juros inicial e o número de anos  para calculo do valor a ser retornado.

aporte: 
    valor inicial investido (int)
taxa: 
    taxa de juros (float)
anos: 
    número de anos (int)
return:
    valor total após o número de anos (float)
    """
    return aporte * (1 + taxa) ** anos
 

# %%

juros_compostos(aporte = 1000, taxa = 0.13, anos = 4)

# %%

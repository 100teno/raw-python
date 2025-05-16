# %%
# funções são blocos de código que podem ser reutilizados
# funções são definidas com a palavra reservada def

def soma(a, b):
    """
    Função que soma dois números
    :param a: primeiro número
    :param b: segundo número
    :return: soma dos dois números
    """
    return a + b

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
soma(a,b)

# %%

def f(x): 
    resultado = 1 + x
    return(resultado)
# %%
f(10)

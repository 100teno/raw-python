# 05 - Estatísticas
# %%
def soma(a:float, b:float,) -> float:
    return a + b

def media(a:float, b:float) -> float:
    return soma(a, b) / 2

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

resultado = media(a, b)

print('A média entre', a, 'e', b, 'é:', resultado)
# %%
# exemplo de função passando um argumento opcional
# um argumento opcional é um argumento que pode ser omitido na chamada da função
# e precisa ser colocado depois dos argumentos obrigatórios.

def soma(a:float, b:float, c:float) -> float:
    return a + b

def media(a:float, b:float, c=0.0) -> float:
    return soma(a, b, c) / 3

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

resultado = media(a, b, c)

print('A média entre', a, ',', b, 'e', c ,'é:', resultado)

# %%
# exemplo de função passando uma lista como argumento dela

def soma(valores:list) -> float:
    return sum(valores)

def media(valores:list) -> float:
    return soma(valores) / len(valores)

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

resultado = media([a, b, c])

print('A média entre', a, ',', b, 'e', c ,'é:', resultado)

# %%
# *args é uma convenção para passar um número variável de argumentos para uma função
# o *args é uma tupla que contém todos os argumentos passados para a função
# sempre precisa ser o último argumento da função

def soma(a:float, b:float, *args) -> float:

    valores = [a, b] + list(args)
    return sum(valores)


def media(a:float, b:float, *args) -> float:

    return soma(a, b, *args) / (len(args) + 2)

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
d = float(input("Digite o quarto número: "))

print("Média", media(a, b, c, d))
# %%

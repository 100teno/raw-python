# %%
# Criando uma função que verifica se o número que o usuário digitou é par ou ímpar
def par_impar(numero:int):
    
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = int(input("Digite um número: "))

resultado = par_impar(numero)

print("O valor", numero, "é", resultado)

# %%

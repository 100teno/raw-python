# Construa um programa que realiza o sorteio de um numero entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado
# Caso o usuário acerte, dê os parabéns.

# %%
import random as rd

tentativas = 3


# criando uma função pra validar a entrada do usuário
# ela vai ficar em loop até o usuário digitar um número válido
# e retornar esse número
# a função vai usar o try/except para tratar erros de conversão
# e o if para validar se o número está entre 1 e 15
# a função vai usar o continue para voltar pro começo do loop
# e o break para sair do loop quando o número for válido
def get_input():
    while True:
        try:
            numero_usuario = int(input("Digite um número entre 1 e 15: "))

        except ValueError as err:
            print("Entrada inválida. Por favor, insira um número inteiro.")
            continue
        
        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("Número inválido. Tente novamente.")

# sorteando um número entre 1 e 15 utilizando a biblioteca random
# o número sorteado vai ser armazenado na variável numero_sorteado

numero_sorteado = rd.randint(1, 15)


# criando um loop for que vai rodar 3 vezes
# a cada iteração do loop, o usuário vai ter que digitar um número
# o número digitado vai ser armazenado na variável numero_usuario
# se o número digitado for igual ao número sorteado, o programa vai imprimir uma mensagem de parabéns e sair do loop

for i in range(tentativas):
    
    numero_usuario = get_input()

    if numero_sorteado == numero_usuario:
        print("Parabéns, Você acertou o número sorteado!")
        break

    elif numero_usuario > numero_sorteado:
        print("Seu chute foi maior que o número sorteado.")
    else:
        print("Seu chute foi menor que o número sorteado.")

else: 
    print("Suas tentativas acabaram. O número sorteado era", numero_sorteado)


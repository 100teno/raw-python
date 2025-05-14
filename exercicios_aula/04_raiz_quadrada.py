#exercicio 04 - Fazer um programa que receba um número inteiro e calcule a raiz quadrada e exiba o resultado
numero = input('Digite um numero inteiro para que possamos calcular sua raiz quadrada: ')
numero = int(numero)
raiz_quadrada = numero ** (1/2)
raiz_quadrada = round(raiz_quadrada, 4)
print('A raiz quadrada de', numero, 'é:', raiz_quadrada)
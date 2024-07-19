# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# Solicita ao usuário que digite um valor
num = int(input ('Insira um número: '))

# Verifica se o valor é positivo, negativo ou zero e imprime o resultado
if num > 0:
    print ('O valor é positivo!')

elif num < 0:
    print ('O valor é negativo!')    

else:
    print ('O valor é zero!')
# Faça um Programa que peça dois números e imprima o maior deles.

# Solicita ao usuário que digite dois números
num1 = int(input ('Insira o primeiro número: '))
num2 = int(input ('Insira o segundo número: '))

# Verifica qual dos dois números é maior e imprime o resultado
if num1 > num2:
    print (num1)

elif num1 < num2: 
    print (num2)

# Caso as entradas sejam números iguais
else: 
    print ('Inválido, pois os números são iguais.')   
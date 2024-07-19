# Faça um Programa que leia três números e mostre o maior deles.

# Solicita ao usuário que digite três números
num1 = int(input ('Insira o primeiro número: '))
num2 = int(input ('Insira o segundo número: '))
num3 = int(input ('Insira o terceiro número: '))

# Verifica qual dos três números é o maior e imprime o resultado
if num1 > num2 and num1 > num3:
    print (num1)

elif num2 > num1 and num2 > num3:
    print (num2)

else: 
    print (num3)   
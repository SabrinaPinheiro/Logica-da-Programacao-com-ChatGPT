# Faça um Programa que leia três números e mostre o maior e o menor deles.

# Solicita ao usuário que digite três números
num1 = int(input ('Insira o primeiro número: '))
num2 = int(input ('Insira o segundo número: '))
num3 = int(input ('Insira o terceiro número: '))

# Inicializa as variáveis dos números maior e menor
num_maior = num1
num_menor = num1

# Verifica o maior número
if num2 > num_maior:
    num_maior = num2

if num3 > num_maior:
    num_maior = num3

# Verifica o menor número
if num2 < num_menor:
    num_menor = num2

if num3 < num_menor:
    num_menor = num3

# Imprime o maior e o menor número
print(f"O maior número é: {num_maior}")
print(f"O menor número é: {num_menor}")  
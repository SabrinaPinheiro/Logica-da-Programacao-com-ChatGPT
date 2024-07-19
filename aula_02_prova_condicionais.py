# Crie um programa em Python para verificar se um número é positivo, negativo ou zero. 
# O programa deve solicitar ao usuário que insira um número e, em seguida, imprimir uma mensagem indicando a natureza do número.
# Se o número for maior que zero, exiba a mensagem "O número é positivo." 
# Se for menor que zero, exiba "O número é negativo." 
# Caso seja zero, a mensagem deve ser "O número é zero."
# Utilize estruturas condicionais e formatação com F-string para criar o programa de forma clara

# Solicita ao usuário que digite um número
num = float(input ('Digite um número: '))

# Verifica a natureza do número e imprime a mensagem correspondente
if num > 0:
    print (f'O número {num} é positivo.')

elif num < 0:
    print (f'O número {num} é negativo.')

# Caso o número seja zero, imprimi a mensagem correspondente   
else: 
    print (f'O número é zero.')   
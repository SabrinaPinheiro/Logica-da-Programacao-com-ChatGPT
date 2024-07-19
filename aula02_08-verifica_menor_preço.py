# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

# Solicita ao usuário que digite o preço dos três produtos
preco1 = float(input("Insira o preço do primeiro produto: R$ "))
preco2 = float(input("Insira o preço do segundo produto: R$ "))
preco3 = float(input("Insira o preço do terceiro produto: R$ "))

# Verifica qual produto tem o menor preço
if preco1 < preco2 and preco1 < preco3:
    preco_menor = preco1

elif preco2 < preco1 and preco2 < preco3:
    preco_menor = preco2

elif preco3 < preco1 and preco3 < preco2:
    preco_menor = preco3

# Imprime a mensagem com o preço do menor produto
print (f"Compre o produto de menor preço no valor de: R$ {preco_menor}")
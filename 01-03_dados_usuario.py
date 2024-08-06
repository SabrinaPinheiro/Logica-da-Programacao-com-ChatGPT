# Faça um programa que peça a idade, a altura, o cpf e o nome do usuário e imprima na tela a mensagem:
# Bem-vindo (usuário), seus dados foram cadastrados com sucesso. Idade = ‘’, altura = ‘’, cpf = ‘’.

print("Insira os seus dados abaixo")

nome = input ("Nome: ")
idade = input ("Idade: ")
altura = input ("Altura: ")
cpf = input ("CPF: ")

print (f"Bem-vindo {nome}, seus dados foram cadastrados com sucesso:")
print (f"Idade: {idade}")
print (f"Altura: {altura}")
print (f"CPF: {cpf}")

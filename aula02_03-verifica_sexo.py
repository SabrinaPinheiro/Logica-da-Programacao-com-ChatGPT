# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Outra letra qualquer - Sexo Inválido.

# Solicita ao usuário que digite uma letra
letra = input("Digite uma letra F ou M: ").strip().upper()

# Verifica se a letra é "F" ou "M" e imprime a mensagem correspondente
if letra == "F":
    print("Sexo Feminino")

elif letra == "M":
    print("Sexo Masculino")

else:
    print("Sexo Inválido")
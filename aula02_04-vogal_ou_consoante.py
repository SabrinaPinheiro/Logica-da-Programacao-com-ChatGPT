# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# Solicita ao usuário que digite uma letra
letra = input("Digite uma letra: ").strip().lower()

# Verifica se a letra é uma vogal ou consoante e imprime a mensagem correspondente
if letra in 'aeiou':
    print("A letra digitada é uma vogal.")

else:
    print("A letra digitada é uma consoante.")

# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez

# Solicita ao usuário que digite as duas notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da nota média do aluno
nota_media = (nota1 + nota2) / 2

# Verifica se a média alcançada e imprimi a mensagem correspondente
if nota_media == 10:    
    print ('Aprovado com Distinção')

elif nota_media >= 7:
    print ('Aprovado')

else:
    print ('Reprovado')


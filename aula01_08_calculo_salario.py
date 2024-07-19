# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input ('Quanto você ganha por hora: R$ '))
horas_trabalho = float(input ('Quantas horas você trabalhou no mês: '))
salario_mes = float(salario_hora * horas_trabalho)

print (f'O seu salário será de: R$ {salario_mes} reais')
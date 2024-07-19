# Você está criando um programa para calcular a área de um retângulo. 
# O programa deve solicitar ao usuário que forneça a base e a altura do retângulo. 
# Em seguida, o programa deve calcular a área usando a fórmula:
# Área=Base×Altura
# O programa deve exibir a área calculada.

# Solicita ao usuário que digite as medidas do retângulo
retangulo_base = float(input ('Insira a base do retângulo em metros: '))
retangulo_altura = float(input ('Insira a altura do retângulo em metros: '))

# Cálculo da área do retangulo
retangulo_area = float(retangulo_base * retangulo_altura)

# Imprimi a mensagem com a área do retângulo
print (f'A área do retângulo é igual a: {retangulo_area } m2')
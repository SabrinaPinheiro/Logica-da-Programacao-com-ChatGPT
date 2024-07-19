# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado1 = float(input ('Insira a medida lado 1 do quadrado em metros: '))
lado2 = float(input ('Insira a medida lado 2 do quadrado em metros: '))
area_quadrado = float(lado1 * lado2)
resultado = float(area_quadrado * 2)

print (f'O resultado é igual a: {resultado} m2')
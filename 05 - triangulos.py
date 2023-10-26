# Programa que classifica os triângulos.
# @author: Carlos Freitas

# entrada dos dados

lado_triangulo1 = float(input("Digite o primeiro valor do triângulo: "))
lado_triangulo2 = float(input("Digite o segundo valor do triângulo: "))
lado_triangulo3 = float(input("Digite o terceiro valor do triângulo: "))

#processamento e saída dos dados

if lado_triangulo1 == lado_triangulo2 == lado_triangulo3:
    print("O triângulo é equilátero.")
elif lado_triangulo1 == lado_triangulo2 or lado_triangulo1 == lado_triangulo3 or lado_triangulo2 == lado_triangulo3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")

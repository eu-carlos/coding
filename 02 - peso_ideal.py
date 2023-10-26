# Programa que calcula o peso ideal baseado no seu sexo e na sua altura.
# @author: Carlos Freitas

# entrada dos dados 

sexo = input('Digite H se você for homem ou M se você for mulher: ')
altura = float(input('Digite a sua altura: '))

# processamento e saída dos dados

peso_ideal_h = (72.7 * float(altura)) - 58
peso_ideal_m = (62.1 * float(altura)) - 44.7

if sexo == "H":
    print(f'O seu peso ideal é: {peso_ideal_h:.2f}kg')
elif sexo == "M":
    print(f'O seu peso ideal é: {peso_ideal_m:.2f}kg')
else:
    print("Por favor, digite apenas H para homem ou F para mulher")
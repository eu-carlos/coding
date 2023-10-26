'''

# Programa que calcula base e expoente e mostre o primeiro número (n1) elevado ao segundo número (n2).
# @author: Carlos Freitas


'''
# entrada de dados
base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

# processamento de dados
potencia = 1

for numeros in range(expoente):
    potencia *= base

# saida de dados
print(f'{base} elevado a {expoente} é igual a {potencia}.')

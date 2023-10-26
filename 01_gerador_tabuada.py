'''

# Programa que gera tabuada de qualquer número.
# @author: Carlos Freitas


'''

# entrada de dados
numero = int(input('Digite um número de <1> a <10>: '))
print(f'A tabuada de {numero} é: ')

# processamento de dados
for i in range(1, 10+1):
    resultado = numero * i

# saida de dados
    print(f'{numero} x {i} = {resultado}')
'''

# Programa que lê um número n e exibe na tela a sequência de Fibonacci com n elementos.
# @author: Carlos Freitas


'''
# entrada e processamento de dados
n = int(input('Quantos elementos da sequência de Fibonacci você quer calcular? '))
fibonacci = [1, 1]

for i in range(2, n):
    proximo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo)

# saida de dados
print(f'Sequência de Fibonacci com {n} elementos: {fibonacci}')

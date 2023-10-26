# programa que cálcula raiz quadrada de um número.
# @author: Carlos Freitas

# calcular raiz quadrada baseada na função de Newton e entrada de dados
numero = float(input("Digite um número para calcular sua raiz quadrada: "))
b = 2
p = (b + numero / b) / 2

# processamento de dados

while abs(b - p) >= 0.0001:
    b = p
    p = (b + numero / b) / 2

raiz_quadrada = p

# saida de dados

print(f'A raiz quadrada aproximada de {numero} é {raiz_quadrada:.2f}!')

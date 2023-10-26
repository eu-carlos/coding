# Programa que efetua a soma de todos os números ímpares que são múltiplos de 3.
# @author: Carlos Freitas

# entrada, processamento e saida de dados

soma = 0
num = 3

while num <= 500:
    soma += num
    num += 6

print(f"A soma dos números ímpares múltiplos de três de 1 a 500 é: {soma}")

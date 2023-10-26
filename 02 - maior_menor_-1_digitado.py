# Programa que lê números repetidamentes até que o valor seja -1.
# @author: Carlos Freitas

num = float(input('Digite um número: '))

menor = num
maior = num
soma = num

while num != -1:
    num = float(input('Digite um número: '))
    if num != -1:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
        soma += num

print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')
print(f'A soma dos valores é: {soma}')
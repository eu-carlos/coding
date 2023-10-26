'''

# Programa que verifica se o número é primo.
# @author: Carlos Freitas


'''
# entrada, processamento e saida de dados
num = int(input('Digite um número inteiro: '))

if num < 2:
    print('O número não é primo.')
else:
    primo = True
    for loop in range(2, num):
        if num % loop == 0:
            primo = False
            break

    if primo:
        print('O número é primo.')
    else:
        print('O número não é primo.')

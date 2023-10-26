'''
Programa que lê dois vetores com cinco elementos e gera um terceiro vetor de 10 elementos.

@author: Carlos Freitas

'''

# Recebe os elementos do primeiro vetor
vetor1 = [int(input(f"Elemento {i+1} do primeiro vetor: ")) for i in range(5)]

# Recebe os elementos do segundo vetor
vetor2 = [int(input(f"Elemento {i+1} do segundo vetor: ")) for i in range(5)]

# Gera o vetor intercalado
vetor_intercalado = []
index = 0
while index < len(vetor1):
    vetor_intercalado.append(vetor1[index])
    vetor_intercalado.append(vetor2[index])
    index += 1


# Imprime o vetor intercalado
print("Vetor intercalado:", vetor_intercalado)





'''

Exercicio antigo resolvido: 

list1 = []
for i in range(5):
    list_temp = []
    for j in range(5):
        list_temp.append(input('Insira um número: '))
    list1.append(list_temp)

# mostrando a matriz para o usuario

print('Matriz resultante: ')
for i in range(5):
    for j in range(5):
        print(list1[i][j], end=' | ')
    print()

# verificando se o número digitado pelo usuário pertence à matriz
valor = input('Digite um número para verificar: ')
pertence = False
for i in range (5):
    for j in range(5):
        if list1[i][j] == valor:
            pertence = True
            break

if pertence:
    print(f'O valor {valor} pertence a matriz. ')
else:
    print(f'O valor {valor} nao pertence a matriz. ')


'''
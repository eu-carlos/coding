# Programa que lê dois números e imprime o resultado da divisão inteira do primeiro pelo segundo, assim como o resto da divisão.
# @author: Carlos Freitas

# entrada de dados
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# processamento de dados
resultado = 0
resto = numero1

while resto >= numero2:
    resto = resto - numero2
    resultado = resultado + 1

# saida de dados
print(f"{numero1} dividido por {numero2} é igual a {resultado}. (resto da divisão: {resto}).")

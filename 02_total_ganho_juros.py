'''

# Programa que escreve o total ganho com juros no período.
# @author: Carlos Freitas


'''

# entrada de dados
deposito_inicial = float(input('Digite o valor do deposito inicial: '))
taxa_juros = float(input('Qual é a taxa de juros da poupança <em %>? '))

# processamento de dados
total_juros = 0

for mes in range(1, 24+1):
    juros = deposito_inicial * (taxa_juros / 100)
    dep_final = deposito_inicial + juros
    # saida de dados
    print(f'mes {mes}. Deposito: R${deposito_inicial:.2f} Juros: R${juros:.2f} - Total: R${dep_final:.2f}')
    # processamento de dados
    total_juros += juros
    deposito_inicial = dep_final

# saida de dados
print(f'Total de juros ganhos no período: R${total_juros:.2f}.')


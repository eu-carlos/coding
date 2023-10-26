# Programa que exibe o número de meses que a dívida será paga, o total pago e o total de juros pago.
# @author: Carlos Freitas

# entrada de dados

valor_divida = float(input('Digite o valor inicial da divida: '))
juros_mensal = float(input('Digite o valor do juros mensal: '))
valor_mensal_pago = float(input('Digite o valor mensal que sera pago: '))

# processamento de dados
meses = 0
pagamento_total = 0
juros_total = 0

while valor_divida > 0:
    juros_mes = valor_divida * (juros_mensal / 100)
    if valor_divida + juros_mes > valor_mensal_pago:
        valor_divida = valor_divida + juros_mes - valor_mensal_pago
        pagamento_total = pagamento_total + valor_mensal_pago
        juros_total = juros_total + juros_mes
    else :
        valor_mensal_pago = valor_divida + juros_mes
        valor_divida = 0
        pagamento_total = pagamento_total + valor_mensal_pago
        juros_total = juros_total + juros_mes
    meses += 1

# saida de dados

print(f'A dívida será paga em {meses} meses. O total pago será de R${pagamento_total:.2f} e o total de juros pago será de R${juros_total:.2f}.')




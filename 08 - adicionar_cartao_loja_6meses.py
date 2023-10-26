# Programa que calcula o desconto de 10% para clientes que gastarem R$ 100 ou mais e pagarem em dinheiro.
# Também será aceito cartões de débito e de crédito, além do parcelamento em até 3x no cartão de crédito.
# @author: Carlos Freitas

# entrada dos dados

valor_p = float(input('Digite o valor do produto comprado: '))
pagamento = input('Qual a forma de pagamento escolhida? <dinheiro>, <cheque> ou <cartão>  ')

# processamento e saída dos dados

if valor_p >=100 and pagamento == 'dinheiro':
    desconto = valor_p * 0.10
else:
    desconto = 0

valor_final = valor_p - desconto

if pagamento == 'cartão':
    funcao_cart = input('Selecione <débito> ou <crédito>: ')
    if pagamento == 'cartão' and funcao_cart == 'débito':
        print(f'O valor a ser pago é R$ {valor_p}')
    if pagamento == 'cartão' and funcao_cart == 'crédito':
        parcelas = int(input('Digite o número de parcelas (max 3): '))
        v_parcelas = valor_final / parcelas
        if parcelas >=1 and parcelas <=3:
            print(f'O valor de cada parcela é R$ {v_parcelas} e o total da compra é de {valor_final}')
        elif parcelas <=0 or parcelas >=4:
            print('Quantidade de parcelas inválida.')
        else:
            print(f'O valor final a ser pago é R$ {valor_p}')
elif pagamento == 'dinheiro' and valor_p >=100:
    print(f'Parabéns, você recebeu um desconto. O valor final é R$ {valor_final}')
elif pagamento == 'dinheiro' and valor_p <100:
    print(f'O valor a ser pago é R$ {valor_p}')
elif pagamento == 'cheque':
    print(f'O valor final é de R$ {valor_p}')
else:
    print('Forma de pagamento inválida.')
# Programa que calcula o desconto de 10% para clientes que gastarem R$ 100 ou mais e pagarem em dinheiro.
# @author: Carlos Freitas

# entrada dos dados

valor_p = float(input('Digite o valor do produto comprado: '))
pagamento = input('Qual a forma de pagamento escolhida? <dinheiro> ou <cheque> ')

# processamento dos dados

desconto_val = (valor_p * 0.10)
valor_final = valor_p - desconto_val

if valor_p >=100 and pagamento == 'dinheiro':
    print(f'Parabéns, você recebeu um desconto. O valor para pagamento é de {valor_final}.')
elif valor_p <=100 and pagamento == 'dinheiro':
    print(f'O valor para pagamento é de: R$ {valor_p}')
elif pagamento == 'cheque':
    print(f'O valor para pagamento é de: R$ {valor_p}')
elif pagamento != 'dinheiro' or 'cheque':
    print('Forma de pagamento inválida.')
else:
    print('fO valor a ser pago é de: {valor_p}')



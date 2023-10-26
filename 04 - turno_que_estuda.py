# Programa que responde de acordo com o turno que o usuário estuda.
# @author: Carlos Freitas

# entrada dos dados

turno = input('Digite o turno que você estuda <M> para matuino, <V> para vespertino ou <N> para noturno: ')

# processamento e saída dos dados

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido!')

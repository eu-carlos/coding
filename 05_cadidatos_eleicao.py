'''

# Programa que simula uma eleição.
# @author: Carlos Freitas


'''

# pre definição dos dados
candidato1 = 7
candidato2 = 9
candidato3 = 10

# entrada e processamento dos dados
num_eleitores = int(input('Quantas pessoas participarão da eleição? '))

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

for votos in range(num_eleitores):
    voto = int(input(f'Digite número <Messi <10>, <Halaand<9> ou <Ronaldo<7> do candidato escolhido pelo eleitor {votos+1}: '))

    if voto == candidato1:
        votos_candidato1 += 1
    elif voto == candidato2:
        votos_candidato2 += 1
    elif voto == candidato3:
        votos_candidato3 += 1
    else:
        print('Número ou nome de candidato inválido. Confira novamente as informações.')

# saida de dados
print(f'O candidato {candidato1} recebeu {votos_candidato1} votos.')
print(f'O candidato {candidato2} recebeu {votos_candidato2} votos.')
print(f'O candidato {candidato3} recebeu {votos_candidato3} votos.')

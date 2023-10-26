''' 
# Programa que calcula a média da idade da turma.
# @author: Carlos Freitas

'''

# entrada de dados e processamento de dados
n = int(input('Quantos alunos tem a turma? '))
idades = []

for alunos in range(n):
    idade = int(input(f'Digite a idade do aluno {alunos+1}: '))
    idades.append(idade)

media_idade = sum(idades) / len(idades)

# saida de dados
if 0 <= media_idade <= 25:
    print(f'A média de idade da turma é de {media_idade:.1f} anos. A turma é jovem.')
elif 26 <= media_idade <= 60:
    print(f'A média de idade da turma é de {media_idade:.1f} anos. A turma é adulta.')
elif media_idade > 60:
    print(f'A média de idade da turma é de {media_idade:.1f} anos. A turma é idosa.')
else:
    print('Não foi possível estabelecer a média de idade da turma.')

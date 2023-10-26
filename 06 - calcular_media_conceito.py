#  Programa que calcula a média e exibe o conceito do aluno no semestre.
#  @author: Carlos Freitas 

# entrada de dados

nota1 = float(input('Digite a nota obtida na primeira prova: '))
nota2 = float(input('Digite a nota obtida na segunda prova: '))

# processamento e saída de dados

media = (nota1 + nota2) / 2

if media >=9.0:
    print(f'Parabéns! A sua média é {media} e seu conceito obtido no semestre foi A!')
elif media >=7.5 and media <9.0:
    print(f'Muito bem! A sua média é {media} e seu conceito no semestre é B!')
elif media >=6.0 and media <7.5:
    print(f'Continue melhorando! A sua média é {media} e seu conceito no semestre é C!')
elif media >= 4.0 and media <= 6.0:
    print(f'Você precisa chegar lá! A sua média é {media} e seu conceito no semestre é D. =(( ')
else:
    print('Sua situação está complicada! Seu conceito no semestre é E. =((( ')
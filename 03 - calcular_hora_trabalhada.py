# Programa que calcula e mostra o total do seu salário com os descontos.
# @author: Carlos Freitas

# entrada dos dados

ganha_hora = float(input('Quanto você ganha por hora? '))
horas_mes = float(input('Quantas horas você trabalhou durante o mês? '))

# processamento dos dados

salario_bruto = ganha_hora * horas_mes
imposto_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

# saída dos dados

print(f'Seu salário bruto é: {salario_bruto}')
print(f'Seu desconto de imposto de renda é: {imposto_renda}')
print(f'Seu desconto de INSS é: {inss}')
print(f'Seu desconto do sindicato é: {sindicato}')
print(f'Seu salário líquido é: {salario_liquido}')
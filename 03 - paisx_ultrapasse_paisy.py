# Programa que calcula e escreve o número de anos necessários para que a população
# do país X ultrapasse ou iguale a população do país Y.
# @author: Carlos Freitas

# processamento de dados

pais_x = 70000
taxa_cresc_x = 0.035

pais_y = 180000
taxa_cresc_y = 0.015

anos = 0

while pais_x < pais_y:
    anos = anos + 1
    pais_x = pais_x + pais_x * taxa_cresc_x
    pais_y = pais_y + pais_y * taxa_cresc_y

# saida de dados

print(f'Serão necessários {anos} anos para que a população do país X se iguale ou ultrapasse a população do país Y.')

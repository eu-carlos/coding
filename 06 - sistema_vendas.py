# Programa que simula um sistema de vendas. 
# @author: Carlos Freitas

# base de dados

base_precos = {
    1: 5.50,
    2: 2.30, 
    3: 4.75, 
    4: 6.80, 
    5: 9.30
}

total_compras = 0

# entrada e processamento de dados
while True:
    codigo = int(input("Digite o codigo do produto <1 a 5>: "))
    if codigo == 0:
        break
    elif codigo not in base_precos:
        print("Codigo invalido. Por favor digite de <1 a 5> ou 0 para o total das compras.")
    else:
        quantidade = int(input("Digite a quantidade do produto comprada: "))
        preco = base_precos[codigo]
        total_vezes_comprado = quantidade * preco
        total_compras = total_compras + total_vezes_comprado
        # saida de dados
        print(f"Produto {codigo}: R${preco:.2f} x {quantidade} = R${total_vezes_comprado:.2f}")

# saida de dados
print(f"Total das compras: R${total_compras:.2f}")
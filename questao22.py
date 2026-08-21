nome = input("Digite o nome do cliente: ")
valor_compra = float(input("Digite o valor da compra: "))

if valor_compra <= 200:
    desconto = 0.10
elif valor_compra <= 500:
    desconto = 0.15
else:
    desconto = 0.20

valor_desconto = valor_compra * desconto
valor_total = valor_compra - valor_desconto

print()
print("Cliente:", nome)
print("Valor da compra:", valor_compra)
print("Desconto:", desconto * 100, "%")
print("Valor do desconto:", valor_desconto)
print("Valor total a pagar:", valor_total)

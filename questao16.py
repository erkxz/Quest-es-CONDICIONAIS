valor_compra = float(input("digite o valor de compra: "))
if valor_compra < 20:
    lucro = 0.45
else:
    lucro = 0.30
valor_venda = valor_compra + (valor_compra * lucro)
print("Valor de venda:", valor_venda)

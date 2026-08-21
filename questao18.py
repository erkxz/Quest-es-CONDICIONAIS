salario = float(input("Digite o salario bruto: "))

if salario <= 600:
    desconto = 0
elif salario <= 1200:
    desconto = 0.20
elif salario <= 2000:
    desconto = 0.25
else:
    desconto = 0.30

print("Desconto INSS:", salario * desconto)

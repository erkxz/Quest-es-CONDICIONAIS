altura = float(input("Digite a altura (m): "))
sexo = input("Digite o sexo (M/F): ").upper()

if sexo == "M":
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 47

print("Peso ideal:", peso)

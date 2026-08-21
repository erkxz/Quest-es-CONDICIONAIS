x = float(input("Digite o valor de x: "))

if x <= 1:
    resultado = 1
elif x <= 2:
    resultado = 2
elif x <= 3:
    resultado = x ** 2
else:
    resultado = x ** 3

print("f(x) =", resultado)

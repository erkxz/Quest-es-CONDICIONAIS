import math

valor = float(input("Digite um numero: "))
if valor > 0:
    print(valor ** 2)
elif valor < 0:
    print(math.sqrt(abs(valor)))

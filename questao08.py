import math

valor = float(input("digite um numero: "))
if valor > 0:
    print(valor ** 2)
elif valor < 0:
    print(math.sqrt(abs(valor)))

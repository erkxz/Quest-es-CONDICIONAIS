import math

n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))

if n1 == n2:
    print("cubo:", n1 ** 3, n2 ** 3)
elif n1 < n2:
    print("quadrado do menor:", n1 ** 2)
    print("raiz do maior:", math.sqrt(n2))
else:
    print("quadrado do menor:", n2 ** 2)
    print("raiz do maior:", math.sqrt(n1))

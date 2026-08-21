valor = int(input("digite um numero inteiro: "))
div3 = valor % 3 == 0
div5 = valor % 5 == 0

if (div3 or div5) and not (div3 and div5):
    print("divisivel por 3 ou 5, mas nao pelos dois")
else:
    print("nao atende a condicao")

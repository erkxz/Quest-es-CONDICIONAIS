numero = int(input("Digite o numero do mes: "))

meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho",
          "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

if 1 <= numero <= 12:
    print(meses[numero - 1])
else:
    print("Numero invalido")

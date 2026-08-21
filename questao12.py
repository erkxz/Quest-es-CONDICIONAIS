salario = float(input("Digite o salario: "))
prestacao = float(input("Digite o valor da prestacao: "))

if prestacao > salario * 0.20:
    print("Emprestimo nao concebido")
else:
    print("Emprestimo concebido")

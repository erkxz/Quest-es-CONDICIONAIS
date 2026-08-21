salario = float(input("digite o salario: "))
prestacao = float(input("digite o valor da prestacao: "))
if prestacao > salario * 0.20:
    print("emprestimo nao concebido")
else:
    print("emprestimo concebido")

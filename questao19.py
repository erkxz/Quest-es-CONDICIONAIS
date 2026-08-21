ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento

if idade < 16:
    print("Nao e eleitor")
elif idade < 18 or idade > 65:
    print("Eleitor facultativo")
else:
    print("Eleitor obrigatorio")

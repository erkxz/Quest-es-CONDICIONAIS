ano_atual = int(input("digite o ano atual: "))
ano_nascimento = int(input("digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento

if idade < 16:
    print("nao e eleitor")
elif idade < 18 or idade > 65:
    print("eleitor facultativo")
else:
    print("eleitor obrigatorio")

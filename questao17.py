idade = int(input("digite a idade do jogador: "))

if 5 <= idade <= 7:
    print("infantil A")
elif 8 <= idade <= 10:
    print("infantil B")
elif 11 <= idade <= 13:
    print("juvenil A")
elif 14 <= idade <= 17:
    print("juvenil B")
else:
    print("nao pertence a nenhuma categoria")

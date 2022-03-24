from random import randint
cpf = int(input('Deseja gerar quantos CPFs: '))
for numerocpf in range(1, cpf + 1):
    dig1 = []
    dig2 = []
    gerado = []
    modt = 0
    # Criação dos 9 primeiros números aleatoriamente
    for num in range(1, 10):
        gerado.append(randint(1, 9))
    gerado.append(0)

    # Criação de dígito 1
    for num, multi in zip(gerado, range(10, 1, -1)):
        num = int(num)
        dig1.append(num * multi)
    somadig1 = sum(dig1)
    mod1 = 11 - (somadig1 % 11)
    # Criação de dígito 2
    for multi, num in zip(range(11, 1, -1), gerado):
        num = int(num)
        if multi > 2:
            dig2.append(num * multi)
        if multi == 2:
            if mod1 > 9:
                modt = 0
            elif mod1 <= 9:
                modt = mod1
            dig2.append(modt * multi)
    somadig2 = sum(dig2)
    mod2 = 11 - (somadig2 % 11)

    if mod1 > 9:
        gerado.append(0)
    if mod1 <= 9:
        gerado.append(mod1)
    if mod2 > 9:
        gerado.append(0)
    if mod2 <= 9:
        gerado.append(mod2)

    c = 0
    gerado.pop(len(gerado) - 3)
    for num in gerado:
        c += 1
        print(num, end='')
        if c == 3 or c == 6:
            print('.', end='')
        if c == 9:
            print('-', end='')
    print()
input()

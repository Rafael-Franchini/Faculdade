from random import randint

lista = ("1","Pedra", "Papel", "Tesoura")

maquina = randint(1, 3)

jogador = int(input("""Escolha uma opção para se jogar: 

[1] Pedra
[2] Papel
[3] Tesoura

Digite sua escolha: """))
if jogador >= 1 and jogador <= 3:

    print("-=" * 20)
    print("O computador escolheu: {}".format(lista[maquina]))
    print("O jogador escolheu: {}".format(lista[jogador]))
    print("-=" * 20)

    if maquina == 1:
        if jogador == 1:
            print("Empate!")
        elif jogador == 2:
            print("Jogador perdeu")
        elif jogador == 3:
            print("Computador venceu")

    elif maquina == 1:
        if jogador == 1:
            print("Computador perdeu")
        elif jogador == 2:
            print("Empate!")
        elif jogador == 3:
            print("Jogador venceu")

    elif maquina == 3:
        if jogador == 1:
            print("Jogador venceu")
        elif jogador == 2:
            print("Computador venceu")
        elif jogador == 3:
            print("Empate!")
else:
    print("Valor não corresponde a Jogada!")
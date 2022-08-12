from random import randint

lista = ("Pedra", "Papel", "Tesoura")

maquina = randint(0, 2)

jogador = int(input("""Escolha uma opção para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura

Digite sua escolha: """))
if jogador >= 0 and jogador <= 2:

    print("-=" * 20)
    print("O computador escolheu: {}".format(lista[maquina]))
    print("O jogador escolheu: {}".format(lista[jogador]))
    print("-=" * 20)

    if maquina == 0:
        if jogador == 0:
            print("Empate!")
        elif jogador == 1:
            print("Jogador perdeu")
        elif jogador == 2:
            print("Computador venceu")

    elif maquina == 1:
        if jogador == 0:
            print("Computador perdeu")
        elif jogador == 1:
            print("Empate!")
        elif jogador == 2:
            print("Jogador venceu")

    elif maquina == 2:
        if jogador == 0:
            print("Jogador venceu")
        elif jogador == 1:
            print("Computador venceu")
        elif jogador == 2:
            print("Empate!")
else:
    print("Valor não corresponde a Jogada!")
from time import sleep

print('CALCULADORA DE NÚMEROS COMPLEXOS:')

print('\nInsira z1: ')
x1 = int(input("Re: "))
y1 = int(input("Im: "))

print('\nInsira z2: ')
x2 = int(input("Re: "))
y2 = int(input("Im: "))

z1 = complex(x1, y1)
z2 = complex(x2, y2)

print("\nz1:", z1)
print("z2:", z2)
op = 0
while op != 7:

    op = int(input(
        "\nOpções da calculadora:\n[1] Conjugado\n[2] Soma\n[3] Subtracão\n[4] Multiplicação\n[5] Divisão\n[6] Trocar valores\n[7] Sair\nCódigo da operação desejada: "))
    if op == 1:
        print("\nConjugado z1:", z1.conjugate())
        print("Conjugado z2:", z2.conjugate())
        sleep(2)
    elif op == 2:
        sz = z1 + z2
        print("\nSoma de", z1, "e", z2, "=", sz)
        sleep(2)
    elif op == 3:
        subz = z1 - z2
        print("\nSubtração de", z1, "e", z2, "=", subz)
        sleep(2)
    elif op == 4:
        mz = z1 * z2
        print("\nMultiplicação de", z1, "por", z2, "=", mz)
        sleep(2)
    elif op == 5:
        dz = z1 / z2
        print("\nDivisão de", z1, "por", z2, "=", dz)
        sleep(2)
    elif op == 6:
        print('\nInsira z1: ')
        x1 = int(input("Re: "))
        y1 = int(input("Im: "))

        print('\nInsira z2: ')
        x2 = int(input("Re: "))
        y2 = int(input("Im: "))

        z1 = complex(x1, y1)
        z2 = complex(x2, y2)

    elif op == 7:
        break
    else:
        print("\nERRO! Escolha uma opção válida.")
        sleep(2)






"""
ALEX DE ALMEIDA GOMEZ - 110009
DANILO HENRIQUE MULLER - 105918
FRANCISCO NEWTON NUNES DA SILVA - 109030
IAGO BERNARDINO DE ALMEIDA - 108848
OTAVIO AUGUSTO DELATORRE FADINI - 108999
RAFAEL ALEXANDRE LIMA FRANCHINI - 109179

"""

import numpy as np
import sympy as sp

# precisão
precisao = 0.000001
# valor inicial
chute = 2
# simbolo x
x = sp.symbols('x')
# função
f = x**3-x-4
# derivada da função
flinha = sp.diff(f)

erro = novoChute = 1

ite = 0

while True:
    ite += 1
    print("iteração =", ite)
    
    novoChute = chute - (f.subs(x,chute).evalf() / flinha.subs(x,chute).evalf())
    erro = abs(novoChute - chute) / abs(novoChute)
    print(novoChute)
    if erro > precisao:
        chute = novoChute
    else:
        break
    
print(chute)

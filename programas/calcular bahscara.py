# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

#recolhendo dados 
a=float(input("qual o valor de A: "))
b=float(input("qual o valor de B: "))
c=float(input("qual o valor de c: "))
#realizando operacoes
delta=b**2 -4*a*c
if delta <=0:
    print("delta invalido")
else : 
    x1=(-b+delta**(1/2))/2*a
    x2=(-b-delta**(1/2))/2*a
X1=round(x1,1)
X2=round(x2,1)
#apresentando resultados
print("X1:",X1 ,"X2:",X2)
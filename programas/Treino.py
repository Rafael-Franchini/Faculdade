print('programa para fazer listas')
list=[]
v=float(input('Digite um valor'))
list.append(v)
op=int(input('''Deseja continuar:
Sim[1]
Não[2]
:'''))
while op==1:
    v = float(input('Digite um valor'))
    list.append(v)
    op = int(input('''Deseja continuar:
    Sim[1]
    Não[2]
    :'''))
print(list)
for c,i enumerate(list):
    local=c
z=len(list)
op2=int(input('''menu de ações:
1 - para deletar o último elemento
2 - para deletar o elementoX da lista
3 - terminar edições e printar lista
:'''))
while op2==1 or op==2:
    op2 = int(input('''menu de ações:
    1 - para deletar o último elemento
    2 - para deletar o elementoX da lista
    3 - terminar edições e printar lista
    :'''))
    if op2==1:
        lista.pop(z)
    elif op2==2:
        lista.pop(input("x:"))
print('edicoes terminadas')
print(list)
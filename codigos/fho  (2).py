#realizando a leitura dos dados de entrada
metros=float(input("digite o tamanho em metros? "))

#realizando as operacoes
centimetros= metros * 100;
kilometros = metros / 1000;
milimetros = metros * 1000;
pes        = metros * 3.28;

#apresentando as respostas
print()
print(metros,"metros sao",centimetros,"centimetros")
print(metros,"metros sao",kilometros,"kilometros")
print(metros,"metros sao",milimetros,"milimetros")
print(metros,"metros sao",pes,"pes")


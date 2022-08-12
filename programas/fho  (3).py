#realizando a leitura de dados 
preco_inicial=float(input("digite o preco inicial do produto: "))
desconto     =int(input("digite o valor percentual do desconto: "))

#realizando as operacoes
preco_final = preco_inicial * (1 - desconto / 100)

#apresentado os resultados
print()
print("valor final do produto:R$",preco_final)

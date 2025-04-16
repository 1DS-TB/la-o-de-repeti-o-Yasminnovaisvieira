# Peça ao usuário um número e exiba sua tabuada de multiplicação de 1 a 10 usando um laço for.

numero = int(input("Digite um número para ver sua tabuada de 1 a 10: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

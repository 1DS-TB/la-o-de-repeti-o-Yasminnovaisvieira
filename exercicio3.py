# Peça ao usuário um número e exiba sua tabuada de multiplicação de 1 a 10 usando um laço for.

numero = int(input("Digite o número que deseja realizar a tabuada: "))

for i in range(1,11):
    resultado = numero * i

    print(f"{numero} X {i} = {resultado}")
# Peça ao usuário um número inteiro positivo e calcule seu fatorial usando um laço for ou while.

N = int(input("Digite um número inteiro positivo: "))

if N >= 0:
    fatorial = 1
    indice = 1

    while indice <= N:
        fatorial = fatorial * indice
        indice += 1
        print(fatorial)

    print(f"O fatorial de {N} é: {fatorial}")

elif N <= 0:
    print("INVALIDO")
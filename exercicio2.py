# Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 até N usando um laço while.

N = int(input("Digite um número positivo: "))

if N > 0:
    numero = 0
    soma = 0

    while numero <= N:
        soma += numero
        numero += 1

    print(f"O resultado da soma de 1 até {N} é: {soma}")

elif N <= 0:
    print("INVALIDO")
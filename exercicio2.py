# Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 até N usando um laço while.

n = int(input("Digite um número positivo: "))

if n > 0:
    numero = 1
    soma = 0

    while numero <= n:
        soma += numero
        numero += 1

    print(f"O resultado da soma de 1 até {n} é: {soma}")

else:
    print("INVALIDO")
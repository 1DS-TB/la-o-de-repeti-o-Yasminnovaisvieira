# Peça ao usuário um número inteiro positivo e calcule seu fatorial usando um laço for ou while. Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120.

numero = int(input("Digite um número inteiro positivo: "))

if numero > 0:
    fatorial = 1
    numero_inicial = numero #Apenas para o print.

    while numero > 0:
        fatorial = fatorial * numero
        numero = numero - 1

    print(f"O fatorial de {numero_inicial} é: {fatorial}")
else:
    print("INVALIDO")
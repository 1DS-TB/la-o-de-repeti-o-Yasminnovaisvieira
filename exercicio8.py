# Calcule a soma da série harmônica até N termos: S = 1 + 1/2 + 1/3 + ... + 1/N. Arredonde o resultado para 2 casas decimais.

numero = int(input("Digite um número: "))

resultado = 0

if numero > 0:
    for i in range(1, numero + 1):
        resultado += 1 / i
        print(f"{1 / i}", end=" + ")

    print(f"\nO resultado final da soma é: {resultado:.2f}")
else:
    print("INVALIDO")
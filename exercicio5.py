# Peça ao usuário um número e verifique se ele é primo usando um laço. Um número primo é divisível apenas por 1 e por ele mesmo.

N = int(input("Digite um número: "))
divisores = 0

if N <= 0:
    print("INVALIDO")

elif N == 1:
    print("1 não é primo")

else:
    for i in range(1, N + 1):
        if N % i == 0:
            divisores += 1

    if divisores == 2:
        print(f"{N} é primo")

    else:
        print(f"{N} não é primo")
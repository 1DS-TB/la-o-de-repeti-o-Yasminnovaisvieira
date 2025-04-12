# Peça ao usuário um número e verifique se ele é primo usando um laço. Um número primo é divisível apenas por 1 e por ele mesmo.

num = int(input("Digite um número: "))
divisores = 0

if num > 0:
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
        print(f"{num} é primo")
    else:
        print(f"{num} não é primo")
else:
    print("INVALIDO")
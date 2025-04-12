# Peça ao o usuário um numero N. E o utilize laços aninhados para imprimir o seguinte padrão : N = 5

N = int(input("Digite um número: "))

if N > 0:
    for num in range(1, N + 1):
        for i in range(1, num + 1):
            print(i, end="") #END é para que não quebre a linha no final.
        print("")

elif N <= 0:
    print("INVALIDO")
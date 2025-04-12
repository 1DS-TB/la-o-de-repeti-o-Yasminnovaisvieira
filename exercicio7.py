# Peça ao o usuário um numero N. E o utilize laços aninhados para imprimir o seguinte padrão : N = 5

n = int(input("Digite um número: "))

for num in range(1, n + 1):
    for i in range(1, num + 1):
        print(i, end="") #END é para que não quebre a linha no final.
    print("")
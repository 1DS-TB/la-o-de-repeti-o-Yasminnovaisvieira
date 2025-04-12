# Um número perfeito é aquele cuja soma de seus divisores (exceto ele mesmo) é igual a ele mesmo. Ex: 6 (1 + 2 + 3 = 6). Encontre todos os números perfeitos entre 1 e 10000 usando laços.

for num in range(1, 10001):
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i

    if soma_divisores == num:
        print(f"{num} é um número perfeito!")

# Implemente um algoritmo que encontre e imprima todos os números de Kaprekar em um intervalo definido pelo usuário (ex: 1 a 10000). Onde você irá solicitar os 2 numeros do intervalo.

num_inicial = int(input("Digite o número inicial do intervalo: "))
num_final = int(input("Digite o número final do intervalo: "))

if num_inicial < num_final:
    for k in range (num_inicial, num_final + 1):
        k2 = k ** 2
        k_string = str(k2)

        digitos = len(str(k))

        direita = k_string[-digitos:]
        esquerda = k_string[:-digitos]

        if esquerda == '':
            esquerda = '0'

        soma = int(esquerda) + int(direita)

        if soma == k:
            print(f"{k} é um número de Kaprekar!")

else:
    for k in range (num_final, num_inicial + 1):
        k2 = k ** 2
        k_string = str(k2)

        digitos = len(str(k))

        direita = k_string[-digitos:]
        esquerda = k_string[:-digitos]

        if esquerda == '':
            esquerda = '0'

        soma = int(esquerda) + int(direita)

        if soma == k:
            print(f"{k} é um número de Kaprekar!")
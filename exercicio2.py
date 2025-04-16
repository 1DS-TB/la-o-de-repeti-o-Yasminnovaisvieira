# Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 até N usando um laço while.

numero = int(input("Por favor, insira um número inteiro positivo: "))
soma = 0

if numero <= 0:
    print("INVALIDO")
    
else:
    numero += 1
    while numero > 1:
        numero -= 1
        soma+= numero

print(f"O resultado é: {soma}")

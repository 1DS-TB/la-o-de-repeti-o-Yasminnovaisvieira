# Peça ao usuário um número N e gere os primeiros N termos da sequência de Fibonacci usando um laço.
# Fibonacci: Começa com 0 e 1 e os próximos números são resultados das somas dos dois números anteriores.

n = int(input("Digite quantos termos da sequência de Fibonacci deseja: "))

x = 0
y = 1

for i in range(0, n):
    print(x, end=", ")
    z = x + y
    x = y
    y = z
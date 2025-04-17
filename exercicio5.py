# Peça ao usuário um número e verifique se ele é primo usando um laço. Um número primo é divisível apenas por 1 e por ele mesmo.

num = int(input("Digite um número: "))
divisor = 0

for i in range(1, num +1):
    if num % i == 0 and num >= 1:
        divisor +=1

if divisor == 2:
    print(f"{num} eh primo")
    
elif divisor <1:
    print("INVALIDO")
    
else:
    print(f"{num} nao eh primo")

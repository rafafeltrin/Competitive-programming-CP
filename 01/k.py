n = int(input())

def pa(n):
    return (1+n)*n/2

for i in range(n):
    entradas = list(map(int, input().split()))
    n = entradas[0]
    m = entradas[1]

    vezes = 0

    diferenca = abs(n-m)
    if diferenca != 0:
        while True:
            soma = pa(vezes)
            if soma>=diferenca and (soma-diferenca)%2 == 0:
                break
            else:
                vezes+=1

    print(vezes)







        


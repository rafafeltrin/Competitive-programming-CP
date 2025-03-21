casos = int(input())

def subsetsum(conjunto,soma):
    n = len(conjunto)
    for mask in range(1 << n):
        sum_ = 0
        for j in range(n):
            if mask & (1 << j):
                sum_ += conjunto[j]
        if sum_ == soma:
            return True
    return False


for _ in range(casos):
    soma = int(input())
    tamanho = int(input())
    conjunto = list(map(int,input().split()))
    
    if subsetsum(conjunto,soma):
        print("YES")
    else:
        print("NO")
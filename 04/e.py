n = int(input())

for i in range(n):
    entradas = list(map(int, input().split()))
    m = entradas[0]
    n = entradas[1]
    k = entradas[2]

    if m*n-1 == k:
        print("YES")
    else:
        print("NO")
import sys
sys.setrecursionlimit(2 * 10**5 + 10)

lista_adjacencia = [[] for _ in range(200005)]
subordinados = [0]*200005

def dfs(v):
    for i in lista_adjacencia[v]:
        dfs(i)
        subordinados[v] += subordinados[i] + 1

n = int(input())
chefes = list(map(int, input().split()))
for i in range(n-1):
    lista_adjacencia[chefes[i]].append(i + 2)
dfs(1)
for i in range(1, n + 1):
    print(subordinados[i], end=' ')
print()


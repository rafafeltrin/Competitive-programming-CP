#knapsack usando botton-up
def knapsack(valores, pesos, pesoTotal):
    n = len(pesos)
    dp = [[0 for _ in range(pesoTotal + 1)] for _ in range(n + 1)]

    for i in range(n+1):
        for j in range (pesoTotal + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif pesos[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], valores[i-1] + dp[i-1][j - pesos[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][pesoTotal]

n,w = map(int, input().split())
valores = []
pesos = []
for i in range(n):
    entrada = list(map(int, input().split()))
    valor = entrada[0]
    peso = entrada[1]
    qnt = entrada[2]
    for j in range(qnt):
        valores.append(valor)
        pesos.append(peso)

resultado = knapsack(valores, pesos, w)
print(resultado)
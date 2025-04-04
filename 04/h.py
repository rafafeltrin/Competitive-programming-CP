#knapsack usando botton-up
def knapsack(valores, pesos, usos_max, pesoTotal):
    dp = [[0]*(pesoTotal+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(pesoTotal+1):
            dp[i][j] = dp[i-1][j]

            for qtd in range(1, usos_max[i-1]+1):
                pesott = qtd*pesos[i-1]
                if pesott <= j:
                    dp[i][j] = max(dp[i][j], dp[i-1][j - pesott] + qtd*valores[i-1])
                else:
                    break
    return dp[n][pesoTotal]

n,w = map(int, input().split())
valores = []
pesos = []
uso_max = []

for i in range(n):
    entrada = list(map(int, input().split()))
    valor = entrada[0]
    peso = entrada[1]
    qnt = entrada[2]
    
    valores.append(valor)
    pesos.append(peso)
    uso_max.append(qnt)

print(knapsack(valores, pesos,uso_max, w))


"""
#knapsack usando botton-up
def knapsack(valores, pesos, pesoTotal, uso_max):
    n = len(valores)
    usos = [0] * n
    dp = [0] * (pesoTotal + 1)

    for i in range(n - 1, -1, -1):
        for j in range(1, pesoTotal + 1):
            if j - pesos[i] >= 0 and usos[i] < uso_max[i]:
                dp[j] = max(dp[j], valores[i] + dp[j - pesos[i]])
                usos[i] += 1
                
    print(usos)
    print(uso_max)
    print(dp)       
    return dp[pesoTotal]

n,w = map(int, input().split())
valores = []
pesos = []
uso_max = []

for i in range(n):
    entrada = list(map(int, input().split()))
    valor = entrada[0]
    peso = entrada[1]
    qnt = entrada[2]
    
    valores.append(valor)
    pesos.append(peso)
    uso_max.append(qnt)

print(knapsack(valores, pesos, w, uso_max))





"""
#Queremos determinar o número de maneiras de fazer uma soma que resute em n
#Utitilizando os números 1, 3, 5
#Vamos utilizar a técnica de dp topdown

def ways(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    if memo[n] != -1:
        return memo[n]

    memo[n] = ways(n - 1, memo) + ways(n - 3, memo) + ways(n - 5, memo)
    return memo[n]

if __name__ == "__main__":
    n = 995

    memo = [-1] * (n + 1)
    
    print(ways(n, memo))
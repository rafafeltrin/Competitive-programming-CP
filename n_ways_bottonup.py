

def ways(n):
    dp = [-1] * (n + 1)
    
    dp[0] = 1
    
    for i in range(1, n + 1):
        x = 0
        if i - 1 >= 0:
            x += dp[i - 1]
        if i - 3 >= 0:
            x += dp[i - 3]
        if i - 5 >= 0:
            x += dp[i - 5]
        dp[i] = x
            
    return dp[n]

if __name__ == "__main__":
    n = 100
    
    print(ways(n))
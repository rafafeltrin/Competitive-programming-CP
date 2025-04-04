n = int(input())

def funct(entradas, n):
    for i in range(len(entradas)):
        if entradas[i]%2 == 0:
            print('1')
            print(i+1)
            return
    if n == 1:
        print("-1")
    else:
        print('2')
        print("1 2")
    return


for i in range(n):
    m = int(input())
    entradas = list(map(int, input().split()))
    funct(entradas, m)

        
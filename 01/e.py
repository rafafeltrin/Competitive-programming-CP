n = int(input())

for i in range(n):
    t = int(input())

    array = list(map(int, input().split()))

    diferenca = sum(array) - len(array)
    if diferenca == 0 :
        print(0)
    elif diferenca < 0:
        print(1)
    else:
        print(diferenca)
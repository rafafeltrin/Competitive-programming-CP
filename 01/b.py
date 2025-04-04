n = int(input())

for i in range(n):
    t = int(input())

    array = list(map(int, input().split()))

    max = 0

    cont = 0

    for i in array:
        if i:
            cont = 0
        else:
            cont+=1
            if cont >= max:
                max = cont

    print(max)

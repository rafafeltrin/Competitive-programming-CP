n = int(input())

for i in range(n):
    t = int(input())

    array = list(map(int, input().split()))

    funciona = True

    if array[0]%2 == 0:
        man = "par"
    else:
        man = "impar"

    for i in array:
        if i%2 == 0:
            if man != "par":
                funciona = False
                break
        else:
            if man != "impar":
                funciona = False
                break
    
    if funciona:
        print("YES")
    else:
        print("NO")
import sys

entradas = list(map(int,sys.stdin.readline().split()))
tam = entradas[0]
casos = entradas[1]

pre_sum = []

for i in range(tam+1):
    pre_sum.append(0)


s_string = sys.stdin.readline()
j = 0

for i in range(1,tam):
    if s_string[j] == "A" and s_string[i] == "C":
        pre_sum[i+1] = pre_sum[j+1]+1
    else:
        pre_sum[i+1] = pre_sum[j+1]
    j+=1


for _ in range(casos):
    e = list(map(int,sys.stdin.readline().split()))
    l = e[0]
    r = e[1]

    print(pre_sum[r] - pre_sum[l])


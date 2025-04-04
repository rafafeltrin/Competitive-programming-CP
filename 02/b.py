from math import ceil, log

def getMid(s, e):
    return s + (e - s) // 2

def minUtil(st, start, end, l, r, node):
    if (l <= start and r >= end):
        return st[node]

    if (end < l or start > r):
        return float("inf")

    mid = getMid(start, end)
 
    return min(minUtil(st, start, mid, l, r,
                       2 * node + 1),
               minUtil(st, mid + 1, end, l,
                       r, 2 * node + 2))

def getMin(st, n, l, r):
    return minUtil(st, 0, n - 1, l, r, 0)


def constructSTUtil(arr, start, end, st, si):
    if (start == end):
        st[si] = arr[start]
        return arr[start]
 
    mid = getMid(start, end)
 
    st[si] = min(constructSTUtil(arr, start, mid, st,
                                 si * 2 + 1),
                 constructSTUtil(arr, mid + 1, end,
                                 st, si * 2 + 2))
 
    return st[si]

def constructST(arr, n):
    x = ceil(log(n, 2))

    max_size = 2 * pow(2, x) - 1

    st = [0]*max_size

    constructSTUtil(arr, 0, n - 1, st, 0)
    return st



t = int(input())

for i in range(t):
    input()
    entradas = list(map(int, input().split()))
    tamanho = entradas[0]
    m = entradas[1]

    array = list(map(int, input().split()))
    st = constructST(array, tamanho)
    k = i+1
    print(f"Case {k}:")
    
    for j in range(m):
        entradas = list(map(int,input().split()))
        
        r1 = entradas[0] - 1
        r2 = entradas[1] - 1

        if(r1!=r2):
            print(getMin(st,tamanho,r1,r2))
        else:
            print(array[r1])
    
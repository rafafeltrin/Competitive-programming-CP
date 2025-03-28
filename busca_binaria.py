import bisect

# Busca binaria iterativa
def binary_search_bisect(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1
    

if __name__ == "__main__":
    lista = [1, 2, 4, 4, 4, 7, 8]
    x = 10
    i = binary_search_bisect(lista, x)
    if i != -1:
        print(f"{x} está na lista na posição {i}")
    else:
        print(f"{x} não está na lista")
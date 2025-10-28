def calcular_area(altura, array):
    area = 0
    for i in array:
        x = i - altura
        if x > 0:
            area += x
    return area


def encontrar_altura(array, area_ideal, inicio, fim):
    meio = (inicio + fim) / 2

    if fim - inicio < 1e-4:
        return meio
    
    area = calcular_area(meio, array)
    if area < area_ideal:
        return encontrar_altura(array, area_ideal, inicio, meio)
    else:
        return encontrar_altura(array, area_ideal, meio, fim)

import sys
input = sys.stdin.read
data = input().split()

index = 0
while True:
    N = int(data[index])
    A = int(data[index + 1])
    index += 2

    if N == 0 and A == 0:
        break

    lista = list(map(int, data[index:index + N]))
    index += N

    if A == 0:
        print(":D")
        continue

    total_length = sum(lista)

    if total_length < A:
        print("-.-")
        continue
    
    if total_length == A:
        print(":D")
        continue

    resultado = encontrar_altura(lista, A, 0, max(lista))
    print(f"{resultado:.4f}")
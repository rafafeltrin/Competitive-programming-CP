def gerar_subconjuntos(arr):
    n = len(arr)
    subconjuntos = []
    for mask in range(1 << n):
        subset = [arr[i] for i in range(n) if mask & (1 << i)]
        subconjuntos.append(subset)
    return subconjuntos

# Exemplo de uso:
arr = [1, 2, 3, 4, 5]
print(gerar_subconjuntos(arr))
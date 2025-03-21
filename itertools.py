import itertools

def gerar_permutacoes(arr):
    return list(itertools.permutations(arr))
# Exemplo de uso:
arr = [1, 2, 3, 5, 6]
print(gerar_permutacoes(arr))
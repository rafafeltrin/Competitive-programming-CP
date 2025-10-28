def intercala(vetor, comeco, meio, fim, n_comparacoes=0) -> int:
    vetor_auxiliar = vetor[comeco:fim + 1]
    indice_esquerda = 0
    indice_direita = meio - comeco + 1

    for k in range(comeco, fim + 1):
        if indice_esquerda > meio - comeco:
            vetor[k] = vetor_auxiliar[indice_direita]
            indice_direita += 1
        elif indice_direita > fim - comeco:
            vetor[k] = vetor_auxiliar[indice_esquerda]
            indice_esquerda += 1
        elif vetor_auxiliar[indice_esquerda] > vetor_auxiliar[indice_direita]:
            vetor[k] = vetor_auxiliar[indice_esquerda]
            indice_esquerda += 1
        else:
            vetor[k] = vetor_auxiliar[indice_direita]
            indice_direita += 1
            n_comparacoes += (meio - comeco + 1) - indice_esquerda

    return n_comparacoes
def merge_sort(vetor, comeco, fim) -> int:
    if comeco < fim:
        meio = (comeco + fim) // 2
        n_comparacoes = merge_sort(vetor, comeco, meio)
        n_comparacoes += merge_sort(vetor, meio + 1, fim)
        n_comparacoes += intercala(vetor, comeco, meio, fim)
    else:
        n_comparacoes = 0
    return n_comparacoes

if "__main__" == __name__:
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        numeros_jogadores = list(map(int, input().split()))
        n_comparacoes = merge_sort(numeros_jogadores, 0, n - 1)
        print(n_comparacoes)
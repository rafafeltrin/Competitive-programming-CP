import math


def cesta_average(time):
    pontos_feitos = time[2]
    pontos_concedidos = time[3]
    if pontos_concedidos == 0:
        return pontos_feitos, 1
    return pontos_feitos, pontos_concedidos

def melhor_time(t1, t2):
    if t1[1] != t2[1]:
        return t1[1] > t2[1]
    num1, den1 = cesta_average(t1)
    num2, den2 = cesta_average(t2)
    cross1 = num1 * den2
    cross2 = num2 * den1
    if cross1 != cross2:
        return cross1 > cross2
    if t1[2] != t2[2]:
        return t1[2] > t2[2]
    return t1[0] < t2[0]

def intercala_rockts(vetor, comeco, meio, fim):
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
        elif vetor_auxiliar[indice_esquerda][1] > vetor_auxiliar[indice_direita][1]:
            vetor[k] = vetor_auxiliar[indice_esquerda]
            indice_esquerda += 1
        elif melhor_time(vetor_auxiliar[indice_esquerda], vetor_auxiliar[indice_direita]):
            vetor[k] = vetor_auxiliar[indice_esquerda]
            indice_esquerda += 1
        else:
            vetor[k] = vetor_auxiliar[indice_direita]
            indice_direita += 1

def merge_sort_rockts(rockts, comeco, fim):
    if comeco < fim:
        meio = (comeco + fim) // 2
        merge_sort_rockts(rockts, comeco, meio)
        merge_sort_rockts(rockts, meio + 1, fim)
        intercala_rockts(rockts, comeco, meio, fim)

if "__main__" == __name__:
    total_instancias = 0
    while True:
        n = int(input())
        if n == 0:
            break
        total_instancias += 1
        if total_instancias > 1:
            print()
        #todos os times começam com 0 pontos
        times_pontos = []
        for i in range(1,n+1):
            times_pontos.append([i,0,0,0])
        n_partidas = math.ceil(n*(n-1)/2)
        
        #print(times_pontos)
        for i in range(n_partidas):
            time1, pontos1, time2, pontos2 = map(int, input().split())

            times_pontos[time1-1][2] += pontos1
            times_pontos[time1-1][3] += pontos2

            times_pontos[time2-1][2] += pontos2
            times_pontos[time2-1][3] += pontos1

            if pontos1 > pontos2:
                times_pontos[time1-1][1] += 2
                times_pontos[time2-1][1] += 1
            elif pontos2 > pontos1:
                times_pontos[time2-1][1] += 2
                times_pontos[time1-1][1] += 1

            
        #print(times_pontos)
        merge_sort_rockts(times_pontos, 0, n-1)
        #print(times_pontos)
        print(f"Instancia {total_instancias}")
        print(' '.join(str(time[0]) for time in times_pontos))
        
            
entradas = list(map(int, input().split()))
n = entradas[0]
m = entradas[1]

matriz = []

for i in range(n):
    matriz.append(list(input()))

resposta = 0
if m > 1:
    for i in range(n):
        aux = 1

        for j in range(m):
            face = list('face')

            if(matriz[i][j] in face):
                face.remove(matriz[i][j])
                if(matriz[i][aux] in face):
                    face.remove(matriz[i][aux])
                    if (i+1<n):
                        if(matriz[i+1][j] in face):
                            face.remove(matriz[i+1][j])
                            if(matriz[i+1][aux] in face):
                                resposta+=1
            if aux+1<m:
                aux+=1

print(resposta)
import sys

pontos = []
p_set = set()
n = int(sys.stdin.readline())

saida = 0

for _ in range(n):
    entradas = list(map(int,sys.stdin.readline().split()))
    pontos.append((entradas[0],entradas[1]))
    p_set.add((entradas[0]*2,entradas[1]*2))

for x1,y1 in pontos:
    for x2,y2 in pontos:
        if (x1,y1) == (x2,y2):
            continue

        x3 = (x1+x2)
        y3 = (y1+y2)

        if (x3,y3) in p_set:
            saida +=1    

print(int(saida/2))
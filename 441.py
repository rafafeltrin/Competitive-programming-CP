saida = []
while True:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    
    tam = len(n)
    for i in range(1,tam-5):
        for j in range(i+1,tam-4):
            for k in range(j+1,tam-3):
                for l in range(k+1,tam-2):
                    for m in range(l+1,tam-1):
                        for o in range(m+1,tam):
                            saida.append(f"{n[i]} {n[j]} {n[k]} {n[l]} {n[m]} {n[o]}")
    
    saida.append("")
                            
saida.pop(len(saida)-1)

for i in saida:
    print(i)
pag = list(map(int, input().split(",")))

resultado = []
pap_sort = sorted(set(pag))

inicio = pap_sort[0]
final= pap_sort[0]

for n in range(1,len(pap_sort)):
    if pap_sort[n] == final+1:
        final = pap_sort[n]
    else:
        if inicio != final:
            resultado.append(f"{inicio}-{final}")
        else:
            resultado.append(f"{inicio}")
        inicio = pap_sort[n]
        final = pap_sort[n]

if inicio != final:
    resultado.append(f"{inicio}-{final}")
else:
    resultado.append(f"{inicio}")
print(",".join(resultado))
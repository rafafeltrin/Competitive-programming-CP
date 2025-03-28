def montante_final(montante_total, meses, juros, parcela):
    for i in range(meses):
        montante_total = montante_total * (1.0 + juros) - parcela
    return montante_total

def bisseccao(min_parcela,max_parcela, montante_total, meses, juros):
    mid = (max_parcela+min_parcela)/2
    valor = montante_final(montante_total,meses,juros,mid)
    
    if abs(valor) < 0.001:
        return mid
    elif valor > 0.0:
        return bisseccao(mid,max_parcela, montante_total, meses, juros)
    else:
        return bisseccao(min_parcela,mid, montante_total, meses, juros)

if __name__ == "__main__":
    montante_total = 1000
    meses = 2
    juros = 0.1
    min_parcela = 0.01
    max_parcela = (1.0 + juros) * montante_total

    resultado = bisseccao(min_parcela,max_parcela, montante_total, meses, juros)
    print(f"O valor da parcela é: {resultado:.2f}")

def potencia(x, p):
    if p == 0:
        return 1
    if p%2 == 0:
        metade = potencia(x, p//2)
        return metade * metade
    else:
        metade = potencia(x, (p-1)//2)
        return metade * metade * x


if __name__ == "__main__":
    x = 5
    p = 2
    print(f"A potencia {p} de {x} é {potencia(x, p)}")
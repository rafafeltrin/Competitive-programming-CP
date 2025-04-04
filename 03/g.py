n = int(input())

def solve(a,b,c):
    for x in range(-21,22):
        if (x*x <= c):
            for y in range(x+1,101):
                if ((x*x)+(y*y) <= c):
                    for z in range(y+1, 101):
                        if (x+y+z == a and x*y*z == b and (x*x)+(y*y)+(z*z) == c):
                            print(x,y,z)
                            return True
    return False
    

for _ in range(n):
    entradas = list(map(int,input().split()))
    a = entradas[0]
    b = entradas[1]
    c = entradas[2]

    if not solve(a,b,c):
        print("No solution.")

    




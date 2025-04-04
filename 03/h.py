"""
= int(input())

m_set = set()

letters = {}

palavras = []

for y in range(n):
    s = input()
    n = 0
    l_set = set()

    for j in s:
        if n < 3:
            if not (j in l_set):
                n+=1
                l_set.add(j)
                
                if j in m_set:
                    letters[j] = [letters[j][0]+1,letters[j][1].append(y)]
                else:
                    m_set.add(j)
                    letters[j] = [1,list()]
        else:
            print(s)
            for k in l_set:
                letters[j][0]+1
                letters[j][1].remove(y)
            break

print(m_set)
print(letters)
"""
import string

n = int(input())

palavras = []

for y in range(n):
    s = input()
    palavras.append(s)


al = list(map(chr, range(97, 123)))

maximo = 0

for i in range(25):
    for j in range(i+1,26):
        permi = {al[i],al[j]}

        total = 0

        for p in palavras:
            if set(p).issubset(permi):
                total += len(p)

        if total > maximo:
            maximo = total

print(maximo)


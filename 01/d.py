n = int(input())

name = "Timur"

for i in range(n):
    t_string = int(input())
    string = list(input())
    string_base = list(name)


    if t_string == 5:
        teste = True
        for i in string:
            if i in string_base:
                string_base.remove(i)
            else:
                print("NO")
                teste = False
                break
        if teste:
            print("YES")
    else:
        print("NO")
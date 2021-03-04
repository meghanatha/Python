n = int(input())
c=0
for i in range(n):
    l = []
    for j in range(i+1):
        c += 1
        l.append(c)
    print(*l)




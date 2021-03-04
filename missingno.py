
a = 45
n = int(input())
for i in range(n):
    s=0
    line = input()
    for j in line:
        s += int( j)
    print(a-s)
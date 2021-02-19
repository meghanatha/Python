N   = int(input())
arr = [int(i) for i in input().split()]
k   = int(input())          
while N:
    N = N-1
    k = arr[k]
    if k == 0:
        break
if not k :
    print("True")
else:
    print("False")
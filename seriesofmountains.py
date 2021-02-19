'''
A mountain sequence of the integer q and the integer v is a sequence of the form:

1, 1 + v, 1 + 2*v, 1 + 3*v ... q ... 1 + 3*v, 1 + 2*v, 1 + v, 1

For example the sequence for q = 10 and v = 3:
1, 4, 7, 10, 7, 4, 1

You have to find out if the given sequences are mountain sequences and of which integer v and q.
Input
Line 1: The length of all given sequences.
Line 2: The number of sequences n.
n lines: A sequence s.
Output
n lines: For every sequence s:
If s is a mountain sequence: The space-separated numbers v and q.
Else: "No Mountain Sequence".
Constraints
3 ≤ length ≤ 20
1 ≤ n ≤ 5
-100 ≤ q, v ≤ 100
Example
Input
11
2
1 2 3 4 5 6 5 4 3 2 1
1 3 5 7 9 11 9 7 5 3 1
Output
1 6
2 11
'''
length_of_all_sequences = int(input())
no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    mountain_series = [*map(int,input().split())]
    v = mountain_series[1]-mountain_series[0]
    q = mountain_series[len(mountain_series)//2]
    ok = True
    if mountain_series[0] != 1 or mountain_series[-1] != 1:
        ok = False
    if ok:
        for j in range(len(mountain_series)//2):
            if mountain_series[j+1] != mountain_series[j] +v or mountain_series[-j-2] != mountain_series[-j-1]+v:
                ok = False
                break
    if ok:
        print(v,q)
    else:
        print("No Mountain Sequence")
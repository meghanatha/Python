'''
The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
23
8
02 Test 2
Input
Expected output
234
16
03 Test 3
Input
Expected output 
654321
6
04 Test 4
Input
Expected output
75456332
49
'''
n = input()
print(int(n[0])**int(n[-1]))
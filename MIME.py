import sys
import math
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
files = []
for i in range(n):
    ext, mt = input().split()
    files.append([ext.lower(),mt])
for i in range(q):
    fname = input() # One file name per line.
    if '.' in fname:
        exten = fname.split('.')[-1]
        listt_no = 0
        pos = 0
        existing = False
        for ext, mt in files:
            if exten == ext:
                print(mt)
                existing = True
        if not existing:
            print("UNKNOWN")
    else:
        print("UNKNOWN")      
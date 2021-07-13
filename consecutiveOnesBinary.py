#!/usr/bin/env python3
import sys
n = int(sys.argv[1])
binary = bin(n)[2:]
#print(binary)
count = 0
one = 0
for i in binary:
    #print(i)
    if i=='1':
        count+=1
        one = max(count, one)
        #print(count, one)
    else:
        count=0
print(one)

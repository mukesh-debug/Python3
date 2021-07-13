#!/usr/bin/env python3
import sys
def print_rangoli(size):
    letter = [chr(97+i) for i in range(size-1,-1,-1)]
    f, s = "", ""
    for i in range(1,size+1):
        f=letter[:i]
        f="-".join(f)
        if i>0:
            s=letter[:abs(i-1)]
            s=s[::-1]
            s="-".join(s)
        if size==1:
            print(f)
        else:
            print(("{}-{}".format(f,s)).center((4*n-3),'-'))

    for i in range(size-1,0,-1):
        f = letter[:i]
        f1="-".join(f)
        if i >0:
            s = f[:(len(f)-1)]
            s=s[::-1]
            s="-".join(s)
        if size==1:
            print(f1)
        else:
            print(("{}-{}".format(f1,s)).center((4*n-3),'-'))





if __name__ == '__main__':
    n = int(sys.argv[1])
    print_rangoli(n)

#!/usr/bin/env python3
def truncateSentence(s, k):
        pos=[]
        for i in range(len(s)):
            if s[i]==' ':
                pos.append(i)
        if k<=(len(pos)):
            return s[:pos[k-1]]
        else:
            return s

if __name__=='__main__':
    string = input()
    k = int(input())
    print(truncateSentence(string, k))

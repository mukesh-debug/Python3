#!/usr/bin/env python3
import sys
def minion_game(s):
    vowel="AEIOU"
    k=0
    l=len(s)
    for i in range(l):
        if s[i] in vowel:
            k+=l-i
    cs=(l*(l+1)//2)-k


    if cs>k:
        print("Stuart {}".format(cs))
    elif cs<k:
        print("Kevin {}".format(k))
    else:
        print("Draw")


if __name__ == '__main__':
    s = sys.argv[1]
    minion_game(s)

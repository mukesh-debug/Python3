#!/usr/bin/env python3
def solve(s):
    s=s.split(" ")
    new = []
    print(s)
    for word in s:
        if word!='':
            if word[0].isalpha():
                word=word[0].upper()+word[1:]
        print(word)
        new.append(word)
    return (" ".join(new))

if __name__ == '__main__':

    s = input()

    result = solve(s)
    print(result)

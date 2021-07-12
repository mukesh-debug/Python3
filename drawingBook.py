#!/usr/bin/env python3
import sys


def pageCount(n,p):
    """
    This function is very easy to understand implementation to know minimum how
    many pages to turn either from forward or backward of the book to arrive at a specific page
    """
    last = abs((n-1)%2-2)
    sl = n-last
    book=[]
    book.append((0,1))
    book+=[(i+1,i+2) for i in range(1,sl,2)]
    if last==1:
        book.append((n,0))
    else:
        book.append((n-1,n))
    #return book
    #print(book)
    fturn, bturn = 0, 0
    # turning pages forward
    for i in range(len(book)):
        if p in book[i]:
            break
        else:
            fturn+=1

    #turning pages backward
    for i in range(len(book)-1, -1, -1):
        if p in book[i]:
            break
        else:
            bturn+=1
    #print("forward turns: {}, backward turns: {}".format(fturn, bturn))
    return min(fturn, bturn)

if __name__=='__main__':
    n = int(sys.argv[1]) #int(input("Enter count of total pages in book: "))
    p = int(sys.argv[2]) #int(input("Enter page number where you want to turn to: "))
    print(pageCount(n, p))

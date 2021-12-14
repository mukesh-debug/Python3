#!/usr/bin/env python3
import sys
def const_time_fun(n):
    """This function would take constant time to get the sum to any natural number"""
    return (n * (n+1)) / 2

if __name__ == '__main__':
    num = int(sys.argv[1])  
    print(const_time_fun(num))

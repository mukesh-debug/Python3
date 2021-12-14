#!/usr/bin/env python3
import sys
def quad_time_sum(n):
    """This func takes quadratic time of input size to get the sum."""
    s = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            s += 1
    return s

if __name__ == '__main__':
    num = int(sys.argv[1])
    print(quad_time_sum(num))

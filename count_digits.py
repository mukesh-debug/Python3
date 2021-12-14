#!/usr/bin/env python3
import sys
def count_digits(n):
    """To count the number of digits in the given number."""
    count = 0
    while n != 0:
        n //= 10 # If float division is performed here, the ans for '1234' would be 327 so keep in mind about the type of division
        count += 1
    return count

if __name__ == '__main__':
    print(count_digits(int(sys.argv[1])))


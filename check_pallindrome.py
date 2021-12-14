#!/usr/bin/env python3
import sys
def check_pallindrome(n):
    """This function checks if the input number is pallindrome or not."""
    str(n)
    if n == n[::-1]:
        # string[start:end:step]
        return True
    else:
        return False

def check_pallindrome_algo(n):
    """This func is algorithm to check if a number is pallindrom.
    and returns a boolean value confirming or denying about the same.
    """
    old = n
    reverse = 0
    while n != 0:
        # n % 10 will give last digit of the number
        reverse = reverse * 10 + n%10
        # n = n//10 will discard last digit of the number
        n //= 10
        
    #if old == reverse:
    #    return True
    #else:
    #    return False
    return old == reverse

if __name__ == '__main__':
    #print(check_pallindrome(sys.argv[1]))
    print(check_pallindrome_algo(int(sys.argv[1])))

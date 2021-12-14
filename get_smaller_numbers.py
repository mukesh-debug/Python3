#!/usr/bin/env python3
def get_smaller_elements(numbers, threshold):
    """This function will return a list of elements 
       smaller than threshold in order
    """
    result = []
    for number in numbers:
        if number < threshold:
            result.append(number)
    return result

if __name__ == '__main__':
    num_list = list(map(int, input().split()))
    limit = int(input())
    print(get_smaller_elements(num_list, limit))

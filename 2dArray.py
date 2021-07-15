#!/usr/bin/env python3

import sys
def maxSumHourglass(arr):
    """
    when sum of a Hourglass' values were not stored but instead max function
    was put to use negative sum got affected due to comparison with zero,
     which is greater than any negative number.
    """
    #Hmax=0
    harr=[]
    for i in range(4):
        hsum=0
        for j in range(3):
            hsum+=arr[i][j]+arr[i+2][j]
            if j==1:
                hsum+=arr[i+1][j]
        #print("hsum: ",hsum)
        harr.append(hsum)
        hsum2=0
        for j in range(1,4):
            hsum2+=arr[i][j]+arr[i+2][j]
            if j==2:
                hsum2+=arr[i+1][j]
        #print("hsum2: ",hsum2)
        harr.append(hsum2)

        hsum3=0
        for j in range(2,5):
            hsum3+=arr[i][j]+arr[i+2][j]
            if j==3:
                hsum3+=arr[i+1][j]
        #print("hsum3: ",hsum3)
        harr.append(hsum3)

        hsum4=0
        for j in range(3,6):
            hsum4+=arr[i][j]+arr[i+2][j]
            if j==4:
                hsum4+=arr[i+1][j]
        #print("hsum4: ",hsum4)
        harr.append(hsum4)

        #Hmax=max(Hmax, hsum, hsum2, hsum3, hsum4)
    return max(harr)




if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(maxSumHourglass(arr))

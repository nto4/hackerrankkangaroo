#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    #eğer 1.nin hızı 2.den büyük ve 1. önde ise karşılaşmazlar fast exit
    if v1 >= v2 and x1 >= x2:
        return "NO"
    #eğer 2.nin hızı 1. den küçük  ve aralarındaki mesafenin, hızları farkı ile modu 0 ise bir noktada karşılaşırlar
    elif (v2 < v1) and ((x2 - x1) % (v2 - v1)) == 0:
        return "YES"
    #eğer 
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

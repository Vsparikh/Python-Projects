#calculating 1 million digits of Pi using Chudnovsky algorithm

import math
from decimal import *
getcontext().prec = 1000000


def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k<n:
        pi += (Decimal(-1)**k)*(Decimal(math.factorial(6*k))/((math.factorial(k)**3)*(math.factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
        pi = pi * Decimal(10005).sqrt() / 4270934400
        pi = pi ** (-1)
        return pi

print(chudnovsky(1000000))

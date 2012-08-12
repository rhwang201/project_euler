# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math

def factor(n):
    """
    Returns a list of the prime factors of x.
    """
    if n == 1 or n == 2:
        return [n]
    for x in range(2,int(math.sqrt(n))):
        if n % x == 0:
            return factor(x) + factor(n/x)
    return [n]

print max(factor(600851475143))

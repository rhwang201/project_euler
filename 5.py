# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import fractions

#possible = range(1000000,5000000)
#divisors = range(11,20)
#topTier = []
#
#for el in possible:
#    if reduce(lambda x,y: x and y, [el % x == 0 for x in divisors]):
#        topTier.append(el)
#
#print min(topTier)

def lcm(x,y):
    return x*y / fractions.gcd(x,y)

divisors = range(2,20)

ret = 1
for x in divisors:
    ret = lcm(ret,x)
print ret

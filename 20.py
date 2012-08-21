#n! means n  (n  1)  ...  3  2  1
#
#For example, 10! = 10  9  ...  3  2  1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#Find the sum of the digits in the number 100!

import math

n = math.factorial(100)
strN = str(n)
s = reduce(lambda x,y: x+y,[int(strN[i]) for i in range(len(strN))])

print "The sum of digits of 100! is: {0}".format(s)

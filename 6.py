# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import math

sumOfSquares = reduce(lambda x,y: x + y, [x*x for x in range(1,101)])
squareOfSums = math.pow(reduce(lambda x,y: x + y, range(1,101)),2)
print "{0} - {1} = {2}".format(sumOfSquares,squareOfSums, squareOfSums - sumOfSquares)

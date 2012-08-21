#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 21000?

n = 2**1000
strN = str(n)
s = reduce(lambda x,y: x+y,[int(strN[i]) for i in range(len(strN))])

print "The sum of digits of 2^1000 is: {0}".format(s)

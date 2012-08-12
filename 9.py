# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Generate primes by Euclid's algorithm.
# a = k * (m^2 - n^2)
# b = k * (2mn)
# c = k * (m^2 + n^2)
# k,m,n > 0 and m > n

high = 30 
for m in range(1,high):
    for n in range(1,high - 1):
        for k in range(1,high):
            a = k * (m**2 - n**2)
            b = k * (2*m*n)
            c = k * (m**2 + n**2)
            if a + b + c == 1000 and a > 0:
                print a*b*c

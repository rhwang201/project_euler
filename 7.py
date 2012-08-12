# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

def sieve(n):
    primes = range(2,n+1)
    for i in primes:
        j = 2
        while i * j <= primes[-1]:
            if i * j in primes:
                primes.remove(i*j)
            j += 1
    return primes

primes = sieve(110000)
print len(primes)
print primes[10000]

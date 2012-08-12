# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

lower = 850
r = range(lower,999)
r.reverse()

found = []

for x in r:
    potentials = [x * y for y in r]

    for el in potentials:
        if str(el) == str(el)[::-1]:
            found.append(el)
            break

print max(found)

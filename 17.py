# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
# 
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with 
# British usage.

lenDict = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',
           7:'seven',8:'eight',9:'nine',10:'ten',20:'twenty',30:'thirty',
           40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
HUNDRED = 'hundred'
AND = 'and'
THOUSAND = 'thousand'

def numLen(n):
    """
    Returns the length of n written out.
    """
    if n in lenDict:
        return len(lenDict[n])
    if n >= 1000:
        return len(THOUSAND)
    elif n >= 100:
        return len(lenDict[n/100])+ len(HUNDRED)+ len(AND) + \
               len(lenDict[(n%100)/10*10]) + len(lenDict[n%10])
    elif n >= 10:
        return len(lenDict[(n/10)*10]) + len(lenDict[n%10])
    else:
        return -1

result = reduce(lambda x,y: x+y, [numLen(i) for i in range(1,1000)])
print "{0} letters are used in writing all numbers from 1 to 1000.".format(result)

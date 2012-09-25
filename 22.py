# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain
# a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938  53 = 49714.
#
# What is the total of all the name scores in the file?

letters = map(chr, range(65, 91))
values = range(1,27)

alphaDict = dict(zip(letters,values))
def alphaValue(name):
    return sum([alphaDict[letter] for letter in name])

with open('names.txt','r') as f:
    readNames = f.read().split(',')

names = []
for name in readNames:
    name = name.lstrip('"')
    name = name.rstrip('"')
    names.append(name)

names.sort()

result = 0
i = 1
for name in names:
    result += i * alphaValue(name)
    i += 1

print "The total of all name scores is {0}".format(result)

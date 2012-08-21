#Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
#
#How many routes are there through a 20x20 grid?

def routes(m,n):
    """
    Needs memoization to have reasonable runtime.
    Look up dict comprehensions.
    """
    memo = [[-1 for j in range(n+1)] for i in range(m+1)]
    if memo[m][n] == -1:
        if m == 0 and n != 0:
            memo[m][n] = 1
            return 1
        elif m != 0 and n == 0:
            memo[m][n] = 1
            return 1
        elif m == 1 and n == 1:
            memo[m][n] = 2
            return 2
        else:
            mem = routes(m-1,n) + routes(m,n-1)
            memo[m][n] = mem
            return mem
    else:
        print 'nice!'
        return memo[m][n]

print "Number of routes through a 20x20 grid: {0}".format(routes(20,20))

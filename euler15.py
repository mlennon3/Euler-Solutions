#copy/pasted from internet.  calculates nCr (n COMBINE r)
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return n
    num = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return num//denom

print ncr(40, 20)

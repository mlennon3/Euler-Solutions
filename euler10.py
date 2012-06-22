def primes(n):
    s=range(0,n+1)
    s[1]=0
    bottom=2
    top=n//bottom
    while (bottom*bottom<=n):
            while (bottom<=top):
                    if s[top]:
                            s[top*bottom]=0
                    top-=1
            bottom+=1
            top=n//bottom
    return [x for x in s if x]

i = 1
sum = 0
prime_list = primes(2000000)
a = len(prime_list)
while i <= a:
    last_prime = prime_list.pop()
    sum += last_prime
    print "i = %d" % i
    i += 1
    print "len(listy) is:"
    #print len(listy)
    print "last prime is: %d" % last_prime

print sum
        

from __future__ import division

def find_primes(number_to_search_to):
# populates a list of numbers, with all multiples of 2 and 3 removed
    i = 3
    j = 2
    nums_to_check = [2, 3]
    primes = [2, 3]
    while i < number_to_search_to:
        if j == 2:
            i = i + 2
            nums_to_check.append(i)
            primes.append(i)
            j = j + 1
        elif j == 3:
            nums_to_check.append(i)
            primes.append(i)
            j = j - 1
        elif j != 2 and j != 3:
            print "An error occured."
        i = i + 2
        
    """
    print " To start, primes was"
    print primes
    print "And nums_to_check was"
    print nums_to_check
    print "len(primes) is:"
    print len(primes)
    """


    j = 0
    while j < len(primes):
        k = 0
        while k < len(nums_to_check):
            if (nums_to_check[k] % primes[j] == 0) ^ (nums_to_check[k] / primes[j] == 1):
                if primes.count(nums_to_check[k]) > 0:
                    primes.remove(nums_to_check[k])
                    
            """print "At the end of k = %d primes was:" % k
            print "Meaning nums_to_check[k] was %d" % nums_to_check[k]
            print primes
            print "And j was:"
            print "Meaning primes[j] was: %d" % primes[j]"""
            
            k = k + 1
        j = j + 1
    """
    print "len(nums_to_check) is:"
    print len(nums_to_check)
    print "Primes ended as:" """
    print primes
    print len(primes)
how_many_primes = input("Primes up to what integer?")
find_primes(how_many_primes)


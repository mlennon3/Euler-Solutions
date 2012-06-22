from __future__ import division
from math import exp

def find_factors_of(factors_of, up_to):
    i = 2
    factors = []
    while i < up_to:
        if factors_of % i == 0:
            factors.append(i)
        i = i + 1
    return factors
#unfinished, hardly started.  should combine find_factors.py and findprimes.py

def is_it_a_prime(is_prime):
# populates a list of numbers, with all multiples of 2 and 3 removed
    i = 3
    j = 2
    nums_to_check = [2, 3]
    primes = [2, 3]
    while i < is_prime:
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
# removes multiples of the numbers in the generated list (nums_to_check) from a copy of that list (primes)
    j = 0
    while j < len(primes):
        k = 0
        while k < len(nums_to_check):
            if is_prime % primes[j] == 0 and is_prime == primes[j]:
                #it is prime
                return is_prime
                k = len(nums_to_check) + 1
                j = len(nums_to_check) + 1
            elif is_prime % primes[j] == 0:
                return False
                k = len(nums_to_check) + 1
                j = len(nums_to_check) + 1
            elif is_prime < primes[j] * primes[j]:
                #it is prime
                return is_prime
                k = len(nums_to_check) + 1
                j = len(nums_to_check) + 1
            elif (nums_to_check[k] % primes[j] == 0) ^ (nums_to_check[k] / primes[j] == 1):
                if primes.count(nums_to_check[k]) > 0:
                    primes.remove(nums_to_check[k])

            
            k = k + 1
        j = j + 1
    if j == len(primes):
        print "Guess it's prime."
#takes a list of numbers and divides its last numbers by its first numbers, eliminating and that are multiples of earlier numbers

def divide_and_conquer(possible_prime_list):
    i = 1
    factors_of_factors_removed = possible_prime_list
    while i < len(possible_prime_list):
        j = 0
        while j < len(factors_of_factors_removed):
            if (factors_of_factors_removed[(-i)] % factors_of_factors_removed[j] == 0) and (factors_of_factors_removed[(-i)] != factors_of_factors_removed[j]):
                #print "%d mod %d was zero.  %d removed." % (factors_of_factors_removed[(-i)], factors_of_factors_removed[j], factors_of_factors_removed[(-i)])
                factors_of_factors_removed.remove(possible_prime_list[(-i)])
                j = 0
                #print factors_of_factors_removed
            """print factors_of_factors_removed
            print "[(-i)] is: %d" % factors_of_factors_removed[(-i)]
            #print "[j] is: %d" % factors_of_factors_removed[j]
            print "j is"
            print j"""
            j = j + 1
        i = i + 1
    return factors_of_factors_removed
    
multiple = 600851475143

factor_list = find_factors_of(multiple, pow(multiple, .5))
reduced_list = divide_and_conquer(factor_list)
print reduced_list

i = 1
prime_factors = []
while i < len(reduced_list) + 1:
    x = is_it_a_prime(reduced_list[(-i)])
    if x:
        prime_factors.insert(0, x)
    i = i + 1
print "%d is the greatest prime factor of %d" % (prime_factors.pop(), multiple)

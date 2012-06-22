import math
palindromes = []
def are_halves_equal(first_half, second_half):
    two_digit = False
    one_digit = False
    if 10 <= second_half < 100:
        two_digit = True
    elif second_half < 10:
        one_digit = True
    second_half = "%d" % second_half
    second_half = second_half[::-1]
    if two_digit:
        second_half += "0"
    if one_digit:
        second_half += "00"
    """print "first_half, second_half in are_halves_equal:"
    print first_half, second_half"""
    if second_half == "%d" % first_half:
        return True
    else:
        return False
def multiplier():
    i = 999
    product = 0
    largest_palindrome = 0
    while i > 0:
        j = i
        while j > 0:
            product = i * j
            if product <= largest_palindrome:
                break
            first_half = get_first_half(product)
            second_half = get_second_half(product)
            if are_halves_equal(first_half, second_half):
                largest_palindrome = product
            #else:
                #print "%d not it..." % product
             
            j -= 1
        i -= 1
    return largest_palindrome
     
def get_first_half(product):
    if product < 100000:
        first_half = math.floor(product / 1000)
        #second_half = product % 100
        return first_half
    elif product >= 100000:
        first_half = math.floor(product / 1000)
        #second_half = product % 1000
        return first_half
def get_second_half(product):
    if product < 100000:
        #first_half = math.floor(product / 1000)
        second_half = product % 100
        return second_half
    elif product >= 100000:
        #first_half = math.floor(product / 1000)
        second_half = product % 1000
        return second_half
"""
p = input("Product?")
first_half = get_first_half(p)
print "first_half returns as:"
print first_half
second_half = get_second_half(p)
print "second_half returns as:"
print second_half
print are_halves_equal(first_half, second_half)"""
print multiplier()

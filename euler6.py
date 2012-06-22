import math

def sum_of_squares():
    i = 1
    sum = 0
    while i < 101:
        sum = sum + math.pow(i, 2)
        i += 1
    return sum

def square_of_sums():
    i = 1
    sum = 0
    while i < 101:
        sum = sum + i
        i += 1
    return math.pow(sum, 2)

print square_of_sums() - sum_of_squares()
        

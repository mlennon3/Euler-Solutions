i = 1
n = 30000
triangle_number = 0
list_of_t_numbers = []
while i < n:
    last_digit = i
    triangle_number += last_digit
    list_of_t_numbers.append(triangle_number)
    i += 1

j = 0
x = 500
largest_num_of_factors = 0
while j < len(list_of_t_numbers):
    list_of_factors = []
    k = 1
    while k < len(list_of_t_numbers) / 2:
        if list_of_t_numbers[j] % k == 0:
            list_of_factors.append(k)
            if len(list_of_factors) > largest_num_of_factors:
                largest_num_of_factors = len(list_of_factors)
            if len(list_of_factors) > x:
                print "list_of_factors has over %d items" % x
                print "This is the triangle number:"
                print list_of_t_numbers[j]
                j = len(list_of_t_numbers) + 1
                break
        k += 1
    j += 1
    if j == len(list_of_t_numbers):
        print"none found, found up to this many factors:"
        print largest_num_of_factors

    

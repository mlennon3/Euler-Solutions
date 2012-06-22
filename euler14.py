upper = input("to what number?")
greatest_count = 0
def calculator(i, count):
    if i == 1:
        return count
    elif i % 2 == 0:
        i /= 2
        return calculator(i, (count + 1))
    elif i % 2 == 1:
        i = (3 * i) + 1
        return calculator(i, (count + 1))

i = upper
greatest_count_starting_place = 0
while i > 0:
    if calculator(i, 0) > greatest_count:
        greatest_count = calculator(i, 0)
        greatest_count_starting_place = i
    i -= 1
print "The number with the most loops was: %d, with %d loops" % (greatest_count_starting_place, greatest_count)
    
    
        

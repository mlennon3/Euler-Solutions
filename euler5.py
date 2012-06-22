i = 0
x = 1
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
while i < len(numbers):
    x = x * (numbers[i - 3])
    i += 1
y = 2520
while y < x:
    j = len(numbers)
    while j >= 1:
        #print "Checking %d % %d" % y, numbers[j-1]
        if y % numbers[j-1] != 0:
            break
        elif y % numbers[j-1] == 0:
            if j == 1:
                print "%d is it!" %y
                j = 1
                y = x
            j -= 1
    y += 20

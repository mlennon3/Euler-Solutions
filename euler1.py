sum = 0
for i in range(0, 1000):
    if i % 3 == 0:
        sum = sum + i
    elif i % 5 == 0:
        sum = sum + i

print "%d" % sum
        

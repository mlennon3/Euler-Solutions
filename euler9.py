import math
a = 100
candidate_list = []
while a < 400:
    b = 0
    while b < 600:
        c = 200
        while c < 800:
            if (a + b + c) == 1000:
                #print a, b, c
                if (math.pow(a, 2) + math.pow(b, 2)) == math.pow(c, 2):
                    print "a, b, c:"
                    print a
                    print b
                    print c
                    print "Their multiple is:"
                    print a*b*c
                    break
            c += 1
        b += 1
    a += 1

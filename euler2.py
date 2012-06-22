i = 0
sequence = [1, 2]

while i < 50:
    newvar =  sequence[-1] + sequence[-2]
    sequence.append(newvar)
    if newvar > 400000000000000:
        sequence.remove(newvar)
    i = i + 1

##print sequence

sum = 0

evens_list = []
j = 0
while j < len(sequence):
    if sequence[j] % 2 == 0:
        evens_list.append(sequence[j])
    j = j + 1

##print evens_list
k = 0
while k < len(evens_list): 
    sum = sum + evens_list.pop()
    k + 1

print sum



    



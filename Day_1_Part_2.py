import math

counter = 0

pre_val = math.inf
file = open("test_list.txt","r")
list = [int(x) for x in file.read().split()]
window = 3
for r in range(len(list)-window+1):
    tot = sum(list[r:r + window])
    if tot > pre_val:
        counter = counter +1
    pre_val=tot
print(counter)




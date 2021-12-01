import math

counter = 0
pre_val = math.inf
file = open("test_list.txt","r")
list = [int(x) for x in file.read().split()]
for v in list:
    if v > pre_val:
        counter = counter + 1
    pre_val = v

print(counter)



directions = open('test-data.txt', 'r')

#thruster orientation
O = 'neutral'

#positions
H = 0
D = 0

for line in directions.read().split():
    if line == 'forward':
        O = 'forward'
    elif line == 'down':
        O = 'down'
    elif line == 'up':
        O = 'up'
    else:
        if O == 'forward':
            H = H + int(line)
        elif O == 'down':
            D = D + int(line)
        elif O == 'up':
            D = D - int(line)

print(H*D)
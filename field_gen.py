import random

def field_gen(size, level = 1):
    field = [[0 for x in range(size)] for y in range(size)]
    for coordinates in range(10):
        while True:
            x = random.randint(0,(size-1))
            y = random.randint(0,(size-1))
            if field[y][x] == 0:
                field[y][x] = -1
                break
    return field

def danger(field):
    

field = field_gen(7)
print (field[1][0])
print ('Mine amount', sum(row.count(-1) for row in field))
for x in range(6):
    print(field[x])
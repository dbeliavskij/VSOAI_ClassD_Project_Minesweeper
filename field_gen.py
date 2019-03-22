import random

def field_gen(size, level = 1):
    field = [[0 for x in range(size)] for y in range(size)]
    for bomb in range(5):
        while True:
            x = random.randint(0,(size-1))
            y = random.randint(0,(size-1))
            if field[y][x] == 0:
                field[y][x] = -1
                zone(field, x, y, size)
                break
    return field

def zone(field, x, y, size):
    area_x = ()
    area_y = ()
    if y == 0:
        area_y =(0, 2)
    elif y == size-1:
        area_y = (-1, 1)
    else:
        area_y= (-1, 2)
    if x  == 0:
        area_x =(0, 2)
    elif x == size-1:
        area_x = (-1, 1)
    else:
        area_x = (-1, 2)
    try:
        for warningy in range(area_y[0],area_y[1]):
            for warningx in range(area_x[0], area_x[1]):
                if field[y+warningy][x+warningx] != -1:
                    field[y+warningy][x+warningx] = field[y+warningy][x+warningx] + 1
                    print('Mine generated in:', x+warningx, y+warningy, 'Field value: ', field[y+warningy][x+warningx], 'For mine in:',x , y)
    except:
        print ("Failure", y, x)
    return field

size = 7
field = field_gen(size)
print (field[1][0])
print ('Mine amount', sum(row.count(-1) for row in field))
for y in range(size):
    print(field[y])
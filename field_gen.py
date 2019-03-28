import random
from config import field

def field_gen(size, level=1):
    field = [[0 for x in range(size)] for y in range(size)]
    if size ** 2 <= size*level:
        bomb_amount = size*level - size
    else:
        bomb_amount = size * level
    for _ in range(bomb_amount):  # generating defined amount of bombs
        while True:
            x = random.randint(0, (size-1))
            y = random.randint(0, (size-1))
            if field[y][x] == 0:
                field[y][x] = -1
                break
    look_bomb(field, size)
    return field


def look_bomb(field, size):
    for y in range(size):
        for x in range(size):
            if field[y][x] == -1:
                zone(field, x, y, size)


def zone(field, x, y, size):
    area_x = ()
    area_y = ()
    if y == 0:
        area_y = (0, 2)
    elif y == size-1:
        area_y = (-1, 1)
    else:
        area_y = (-1, 2)
    if x == 0:
        area_x = (0, 2)
    elif x == size-1:
        area_x = (-1, 1)
    else:
        area_x = (-1, 2)
    try:
        for warningy in range(area_y[0], area_y[1]):
            for warningx in range(area_x[0], area_x[1]):
                if field[y+warningy][x+warningx] != -1:
                    field[y+warningy][x+warningx] = field[y + warningy][x + warningx] + 1

    except IndexError:
        print("Failure", y, x)
    return field


def check_tile(coord, field):
    return field[coord['y']][coord['x']]


'''coord = {'x':1, 'y':1}
size = 3`
field = field_gen(size,3)
print ('Mine amount', sum(row.count(-1) for row in field))
for y in range(size):
    print(field[y])
print ('Value is ', check_tile(coord, field))'''

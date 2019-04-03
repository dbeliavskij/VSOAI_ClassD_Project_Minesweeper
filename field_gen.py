import random
import config


def field_gen(size):
    field = [[0 for x in range(size)] for y in range(size)]
    for _ in range(config.bomb_amount):
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
        for warn_y in range(area_y[0], area_y[1]):
            for warn_x in range(area_x[0], area_x[1]):
                if field[y+warn_y][x+warn_x] != -1:
                    field[y+warn_y][x+warn_x] = field[y+warn_y][x+warn_x] + 1

    except IndexError:
        print("Failure", y, x)
    return field


def check_tile(coord, field, count=False):
    if field[coord['y']][coord['x']] != -1 and count is True:
        config.tiles_opened += 1

    return field[coord['y']][coord['x']]


field = []

size = 8

level = 2

tiles_opened = 0

bomb_amount = 0
if size ** 2 <= size*level:
        bomb_amount = size*level - size
else:
        bomb_amount = size*level
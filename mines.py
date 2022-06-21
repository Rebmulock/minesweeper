import random as rd
from skeleton import size, area, pick_from

mines = size + 2
mine_area = []

for i in range(mines):
    random_position = rd.choice(pick_from)

    mine_area.append(random_position)

    area[random_position] = '#'

    pick_from.pop(pick_from.index(random_position))

for character in range(len(area)):
    if type(area[character]) == int:
        area[character] = 0
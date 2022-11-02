from tile import Tile
from level import Level
from direction import Direction

from config import TILES, RESOLUTION

def generate_map(map):
    return [[Tile(TILES[tile], colidable =  tile == "red", pos = (j * RESOLUTION, i * RESOLUTION)) for j, tile in enumerate(row)] for i, row in enumerate(map)]

temp = [["brown" for _ in range(16)] for _ in range(9)]
temp[0][0] = "red"
temp[0][-1] = "red"
temp[-1][0] = "red"
temp[-1][-1] = "red"

level_1 = generate_map(temp)

temp = [["brown" for _ in range(16)] for _ in range(9)]
for i in range(16): temp[0][i], temp[8][i] = "red", "red"
for j in range(9): temp[j][0] = "red"

level_2 = generate_map(temp)


temp = [["yellow" for _ in range(16)] for _ in range(9)]

level_3 = generate_map(temp)


temp = [["green" for _ in range(16)] for _ in range(9)]

level_4 = generate_map(temp)


temp = [["brown" for _ in range(16)] for _ in range(9)]

level_5 = generate_map(temp)



level_1 = Level(level_1)
level_2 = Level(level_2)
level_3 = Level(level_3)
level_4 = Level(level_4)
level_5 = Level(level_5)

level_1.set_bordering(level_2, Direction.LEFT)
level_2.set_bordering(level_1, Direction.RIGHT)

level_1.set_bordering(level_3, Direction.DOWN)
level_3.set_bordering(level_1, Direction.UP)

level_1.set_bordering(level_4, Direction.RIGHT)
level_4.set_bordering(level_1, Direction.LEFT)

level_1.set_bordering(level_5, Direction.UP)
level_5.set_bordering(level_1, Direction.DOWN)


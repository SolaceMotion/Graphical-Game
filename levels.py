from tile import Tile
from level import Level
from direction import Direction

from config import TILES, RESOLUTION
import level_1
import level_2
import level_3
import level_4
import level_5

def generate_map(map):
    return [[Tile(TILES[tile], colidable =  tile == "red", pos = (j * RESOLUTION, i * RESOLUTION)) for j, tile in enumerate(row)] for i, row in enumerate(map)]



_level_1 = Level(generate_map(level_1.level))
_level_2 = Level(generate_map(level_2.level))
_level_3 = Level(generate_map(level_3.level))
_level_4 = Level(generate_map(level_4.level))
_level_5 = Level(generate_map(level_5.level))

_level_1.set_bordering(_level_2, Direction.LEFT)
_level_2.set_bordering(_level_1, Direction.RIGHT)

_level_1.set_bordering(_level_3, Direction.RIGHT)
_level_3.set_bordering(_level_1, Direction.LEFT)

_level_3.set_bordering(_level_4, Direction.UP)
_level_4.set_bordering(_level_3, Direction.DOWN)

_level_1.set_bordering(_level_5, Direction.UP)
_level_5.set_bordering(_level_1, Direction.DOWN)
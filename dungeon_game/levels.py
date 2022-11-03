from tile import Tile
from level import Level
from direction import Direction
from enemy import Enemy

from config import TILES, RESOLUTION, BOSS_SPRITE, ENEMY_SPRITE, ENEMY2_SPRITE
import level_1
import level_2
import level_3
import level_4
import level_5

def generate_map(map):
    return [[Tile(TILES[tile], colidable =  tile == "red", pos = (j * RESOLUTION, i * RESOLUTION)) for j, tile in enumerate(row)] for i, row in enumerate(map)]

enemy_1 = Enemy(ENEMY_SPRITE, size = (RESOLUTION, RESOLUTION), pos=(100, 200), speed = 2,)
enemy_2 = Enemy(ENEMY2_SPRITE, size = (RESOLUTION, RESOLUTION), pos=(375, 200), speed = 4)
boss = Enemy(BOSS_SPRITE, size = (RESOLUTION*2, RESOLUTION*2), pos=(350, 175), speed = 6)

_level_1 = Level(generate_map(level_1.level))
_level_2 = Level(generate_map(level_2.level), enemy_1)
_level_3 = Level(generate_map(level_3.level))
_level_4 = Level(generate_map(level_4.level), enemy_2)
_level_5 = Level(generate_map(level_5.level), boss)

_level_1.set_bordering(_level_2, Direction.LEFT)
_level_2.set_bordering(_level_1, Direction.RIGHT)

_level_1.set_bordering(_level_3, Direction.RIGHT)
_level_3.set_bordering(_level_1, Direction.LEFT)

_level_3.set_bordering(_level_4, Direction.UP)
_level_4.set_bordering(_level_3, Direction.DOWN)

_level_1.set_bordering(_level_5, Direction.UP)
_level_5.set_bordering(_level_1, Direction.DOWN)
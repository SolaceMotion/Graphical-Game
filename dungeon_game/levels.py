from .tile import Tile
from .level import Level
from .direction import Direction
from .enemy import Enemy
from .boss import Boss
from .door import Door

from .config import TILES, DOOR, RESOLUTION, BOSS_SPRITE, ENEMY_SPRITE, ENEMY2_SPRITE, WIDTH
from . import level_1, level_2, level_3, level_4, level_5

from math import floor


def generate_map(map):
    return [[Tile(TILES[tile], colidable = tile == "red", pos = (j * RESOLUTION, i * RESOLUTION)) for j, tile in enumerate(row)] for i, row in enumerate(map)]

enemy_1 = Enemy(sprite=ENEMY_SPRITE, size = (RESOLUTION, RESOLUTION), pos=(100, 200), speed = 3)
enemy_2 = Enemy(sprite=ENEMY2_SPRITE, size = (RESOLUTION, RESOLUTION), pos=(375, 200), speed = 4)
boss = Boss(sprite=BOSS_SPRITE, size = (RESOLUTION*2, RESOLUTION*2), pos=(350, 175), speed = 6)

door = Door(sprite=DOOR, size = (RESOLUTION * 3, RESOLUTION * 2), pos=(floor(WIDTH / 2 - RESOLUTION*3/2) -4 , -49))

_level_1 = Level(generate_map(level_1.level), door=door)
_level_2 = Level(generate_map(level_2.level), enemy=enemy_1)
_level_3 = Level(generate_map(level_3.level))
_level_4 = Level(generate_map(level_4.level), enemy=enemy_2)
_level_5 = Level(generate_map(level_5.level), enemy=boss)

_level_1.set_bordering(_level_2, Direction.LEFT)
_level_2.set_bordering(_level_1, Direction.RIGHT)

_level_1.set_bordering(_level_3, Direction.RIGHT)
_level_3.set_bordering(_level_1, Direction.LEFT)

_level_3.set_bordering(_level_4, Direction.UP)
_level_4.set_bordering(_level_3, Direction.DOWN)

_level_1.set_bordering(_level_5, Direction.UP)
_level_5.set_bordering(_level_1, Direction.DOWN)

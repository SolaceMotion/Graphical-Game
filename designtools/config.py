from character import Character

class Tile(Character):
    def __init__(self, sprite: str, *, pos = (20, 20), colidable = False) -> None:
        size = (RESOLUTION, RESOLUTION)
        super().__init__(sprite, pos = pos, size = size, colidable = colidable)
        self.__vx = 0
        self.__vy = 0
        self.colidable = colidable


class Level:
    def __init__(self, map: list[list[Tile]]) -> None:
        self.map = map


# screen
WIDTH = 800
HEIGHT = 450
RESOLUTION = 50

# sprites
PLAYER_SPRITE = "sprites/player.png"
BOSS_SPRITE = "sprites/boss.png"
ENEMY_SPRITE = "sprites/enemy.png"
ENEMY2_SPRITE = "sprites/Enemy_2.png"

# tile sprites
BROWN_TILE = "sprites/bgr.tiles.brown.png"
RED_TILE = "sprites/bgr.tiles.dark_red.png"
YELLOW_TILE = "sprites/bgr.tiles.dark_yellow.png"
GREEN_TILE = "sprites/bgr.tiles.green.png"

def generate_map(map):
    return [[Tile(TILES[tile], colidable = tile == "red", pos = (j * RESOLUTION, i * RESOLUTION)) for j, tile in enumerate(row)] for i, row in enumerate(map)]

TILES = {"brown": BROWN_TILE, "red": RED_TILE, "yellow": YELLOW_TILE, "green": GREEN_TILE}

temp = [["brown" for _ in range(16)] for _ in range(9)]
map = generate_map(temp)

LEVEL = Level(map)
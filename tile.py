from config import RESOLUTION
from character import Character

class Tile(Character):
    def __init__(self, sprite: str, *, pos = (20, 20), colidable = False) -> None:
        size = (RESOLUTION, RESOLUTION)
        super().__init__(sprite, pos = pos, size = size, colidable = colidable)
        self.__vx = 0
        self.__vy = 0
        self.colidable = colidable
from tile import Tile
from enemy import Enemy
from direction import Direction


class Level:
    def __init__(self, map: list[list[Tile]], enemy: Enemy = None) -> None:
        self.map = map
        self.enemy = enemy
        self.left = None
        self.right = None
        self.up = None
        self.down = None

    def set_bordering(self, level, direction: Direction):
        if direction == Direction.LEFT: self.left = level
        if direction == Direction.RIGHT: self.right = level
        if direction == Direction.UP: self.up = level
        if direction == Direction.DOWN: self.down = level
    
    def get_bordering(self, direction: Direction):
        if direction == Direction.LEFT: return self.left
        if direction == Direction.RIGHT: return self.right
        if direction == Direction.UP: return self.up
        if direction == Direction.DOWN: return self.down
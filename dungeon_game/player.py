from .character import Character
from .config import WIDTH, HEIGHT, RESOLUTION


class Player(Character):
    def __init__(self, sprite: str, *, pos=(WIDTH/2-RESOLUTION/2, HEIGHT/2-RESOLUTION/2), size=(60, 60)):
        super().__init__(sprite, pos, size)
        self.points = 0

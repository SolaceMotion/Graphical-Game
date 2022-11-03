from .character import Character


class Player(Character):
    def __init__(self, sprite: str, *, pos = (800/2-60/2, 450/2-60/2), size = (60, 60)):
        super().__init__(sprite, pos, size)
        self.points = 0

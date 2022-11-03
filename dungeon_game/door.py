from .character import Character


class Door(Character):
    def __init__(self, sprite: str, *, size, pos, colidable = True):
        super().__init__(sprite, pos = pos, size = size, colidable = colidable)
        self.__vx = 0
        self.__vy = 0
        self.colidable = colidable

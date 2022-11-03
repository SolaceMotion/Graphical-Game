from .enemy import Enemy


class Boss(Enemy):
    def __init__(self, sprite: str, *, pos = (20, 20), size = (60, 60), speed) -> None:
        super().__init__(sprite, pos = pos, size = size, speed = speed)

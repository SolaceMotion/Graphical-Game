from character import Character


class Enemy(Character):
    def __init__(self, sprite: str, *, pos = (20, 20), size = (60, 60),speed = 5) -> None:
        super().__init__(sprite, pos = pos, size = size)
        self.speed = speed
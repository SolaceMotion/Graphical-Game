from character import Character


class Player(Character):
    def __init__(self, sprite: str, *, pos = (20, 20), size = (60, 60)) -> None:
        super().__init__(sprite, pos = pos, size = size)
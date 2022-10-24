from character import Character
class Player(Character):
    def __init__(self, *, pos = (20, 20), size = (60, 60)) -> None:
        super().__init__(pos = pos, size = size)
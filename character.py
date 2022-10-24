class Character:
    def __init__(self, *, pos = (20, 20), size = (60, 60)) -> None:
        self.__fatigue = False
        self.__x, self.__y = pos
        self.__vx = 3
        self.__vy = 3

        self.w, self.h = size
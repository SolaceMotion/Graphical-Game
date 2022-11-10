import pygame as p
from .direction import Direction
from .config import WIDTH, HEIGHT


class Character:
    def __init__(self, sprite: str, pos=(20, 20), size=(60, 60)) -> None:
        self._x, self._y = pos
        self.__vx = 1
        self.__vy = 1
        self.__sprite = self.load_sprite(sprite, size)
        self._rect = p.Rect(pos, size)
        self.__w, self.__h = size

    def get_sprite(self) -> p.Surface: return self.__sprite
    def get_rect(self) -> p.Rect: return self._rect
    def get_pos(self): return (self._x, self._y)

    def set_pos(self, pos):
        self._x, self._y = pos
        self.set_rect(pos)

    def set_rect(self, pos):
        self._rect = p.Rect(pos, (self.__w, self.__h))

    def load_sprite(self, sprite: p.Surface, size) -> p.Surface:
        sprite = p.image.load(sprite)
        sprite = p.transform.scale(sprite, size)
        return sprite

    def collision(self, character) -> bool:
        # Check collision
        return character.colidable and p.Rect.colliderect(self._rect, character.get_rect())

    def move(self, direction: Direction, dt: float, map):
        pre_move = self.get_pos()
        if direction == Direction.UP:
            self._y -= self.__vy * dt / 10
        if direction == Direction.DOWN:
            self._y += self.__vy * dt / 10
        if direction == Direction.LEFT:
            self._x -= self.__vx * dt / 10
        if direction == Direction.RIGHT:
            self._x += self.__vx * dt / 10

        door = False
        if self._y < 0:
            door = Direction.UP
        if self._y > HEIGHT - self.__h:
            door = Direction.DOWN
        if self._x < 0:
            door = Direction.LEFT
        if self._x > WIDTH - self.__w:
            door = Direction.RIGHT

        # Check collisions on current map
        self.set_rect(self.get_pos())
        for row in map:
            for tile in row:
                if self.collision(tile):
                    self.set_pos(pre_move)

        # Prevent from going outside play area
        self._x = self._x % (WIDTH - self.__w)
        self._y = self._y % (HEIGHT - self.__h)

        return door

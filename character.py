import pygame as p
from direction import Direction

from config import WIDTH, HEIGHT


class Character:
    def __init__(self, sprite: str, *, pos = (20, 20), size = (60, 60)) -> None:
        self.__fatigue = False
        self.__x, self.__y = pos
        self.__vx = 1
        self.__vy = 1
        self.__sprite = self.load_sprite(sprite, size)
        self.__rect = p.Rect(pos, size)
        self.__w, self.__h = size

    def get_sprite(self): return self.__sprite
    def get_rect(self): return self.__rect
    def set_pos(self, pos): self.__x, self.__y = pos
    def get_pos(self): return (self.__x, self.__y)

    def get_rect(self): return self.__rect

    def load_sprite(self, sprite, size):
        sprite = p.image.load(sprite)
        sprite = p.transform.scale(sprite, size)
        return sprite

            
    def collision(self, tile, direction: Direction, dt: float) -> None:

        # check collision
        if tile.wall and p.Rect.colliderect(self.__rect, tile.get_rect()):
            
            if direction == Direction.UP:
                self.__y += self.__vy * dt / 10

            if direction == Direction.DOWN:
                self.__y -= self.__vy * dt / 10

            if direction == Direction.LEFT:
                self.__x += self.__vx * dt / 10

            if direction == Direction.RIGHT:
                self.__x -= self.__vx * dt / 10
                
            
    def move(self, direction: Direction, dt: float, map):
        if direction == Direction.UP    : self.__y -= self.__vy * dt / 10
        if direction == Direction.DOWN  : self.__y += self.__vy * dt / 10
        if direction == Direction.LEFT  : self.__x -= self.__vx * dt / 10
        if direction == Direction.RIGHT : self.__x += self.__vx * dt / 10

        door = False
        if self.__y < 0:
            door = Direction.UP
        if self.__y > HEIGHT - self.__h:
            door = Direction.DOWN
        if self.__x < 0:
            door = Direction.LEFT
        if self.__x > WIDTH - self.__w:
            door = Direction.RIGHT
        
        # Prevent from going outside play area
        self.__x = self.__x % (WIDTH - self.__w)
        self.__y = self.__y % (HEIGHT - self.__h)
        
        self.__rect = p.Rect(self.get_pos(), (self.__w, self.__h))

        # Check collisions on current map
        for row in map:
            for tile in row:
                self.collision(tile, direction, dt)

        return door
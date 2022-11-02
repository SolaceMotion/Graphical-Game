import pygame as p


class Character:
    def __init__(self, sprite: str, *, pos = (20, 20), size = (60, 60), colidable = False) -> None:
        self.__x, self.__y = pos
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

    def collision(self, character) -> None:
        # check collision
        return character.colidable and p.Rect.colliderect(self.__rect, character.get_rect())
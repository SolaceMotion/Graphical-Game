from config import RESOLUTION
from character import Character
from player import Player
import pygame as p

class Tile(Character):
    def __init__(self, sprite: str, wall: bool, *, pos = (20, 20)) -> None:
        size = (RESOLUTION, RESOLUTION)
        super().__init__(sprite, pos = pos, size = size)
        self.wall = wall
        self.__vx = 0
        self.__vy = 0
        
            
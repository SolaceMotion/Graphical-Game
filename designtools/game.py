import pygame as p
from direction import Direction
from player import Player
from state import State

from config import RESOLUTION, PLAYER_SPRITE


class Game:
    def __init__(self, clock: p.time.Clock, fps: int = 60) -> None:
        self.clock = clock
        self.player = Player(PLAYER_SPRITE, size = (RESOLUTION, RESOLUTION))
        self.fps = fps
        self.now = p.time.get_ticks()
        self.previous = p.time.get_ticks()
        self.state = State.ON_MAP

    def tick(self, screen: p.Surface):
        if self.state == State.ON_MAP:
            self.clock.tick(self.fps)
            keys_pressed = self.read_input()
            self.draw_sceen(screen)

    def read_input(self):
        return p.key.get_pressed()

    def draw_sceen(self, screen: p.Surface):
        for row in self.current_level.map:
            for tile in row:
                screen.blit(tile.get_sprite(), tile.get_pos())
import pygame as p
from direction import Direction
from player import Player

from config import RESOLUTION, PLAYER_SPRITE


class Game:
    def __init__(self, clock: p.time.Clock, fps: int = 60) -> None:
        self.clock = clock
        self.player = Player(PLAYER_SPRITE, size = (RESOLUTION, RESOLUTION))
        self.fps = fps
        self.now = p.time.get_ticks()
        self.previous = p.time.get_ticks()

    def start_game(self):
        pass

    def tick(self, screen: p.Surface):
        self.clock.tick(self.fps)
        dt = self.update_time()
        keys_pressed = self.read_input()
        self.handle_movement(keys_pressed, dt)
        screen.blit(self.player.get_sprite(), self.player.get_pos())

    def update_time(self):
        dt = self.now - self.previous
        self.previous = self.now
        self.now = p.time.get_ticks()
        return dt

    def handle_movement(self, pressed, dt: float):
        if pressed[p.K_UP]    : self.player.move(Direction.UP, dt)
        if pressed[p.K_DOWN]  : self.player.move(Direction.DOWN, dt)
        if pressed[p.K_LEFT]  : self.player.move(Direction.LEFT, dt)
        if pressed[p.K_RIGHT] : self.player.move(Direction.RIGHT, dt)
        #if pressed[p.K_SPACE] : self.player.jump() # TODO Make a jump function.

    def read_input(self):
        return p.key.get_pressed()

    def end_game(self):
        pass

    def init_lvl(self, level):
        pass

    def change_lvl(self, level):
        pass

    def draw_sceen(self):
        pass

    def start_clock(self):
        pass

    def stop_clock(self):
        pass
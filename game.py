import pygame as p
from player import Player
from config import RESOLUTION
class Game:
    def __init__(self, clock: p.time.Clock, fps: int = 60) -> None:
        self.clock = clock
        self.player = Player(size = (RESOLUTION, RESOLUTION))
        self.fps = fps

    def start_game(self):
        pass

    def tick(self):
        self.clock.tick(self.fps)

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
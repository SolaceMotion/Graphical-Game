import pygame as p
from direction import Direction
from player import Player
from state import State

from config import RESOLUTION, PLAYER_SPRITE
from levels import level_1


class Game:
    def __init__(self, clock: p.time.Clock, fps: int = 60) -> None:
        self.clock = clock
        self.player = Player(PLAYER_SPRITE, size = (RESOLUTION, RESOLUTION))
        self.fps = fps
        self.now = p.time.get_ticks()
        self.previous = p.time.get_ticks()
        self.current_level = level_1
        self.state = State.ON_MAP

    def start_game(self):
        pass

    def tick(self, screen: p.Surface):
        if self.state == State.ON_MAP:
            self.clock.tick(self.fps)
            dt = self.update_time()
            keys_pressed = self.read_input()
            self.handle_movement(keys_pressed, dt)
            self.draw_sceen(screen)
            screen.blit(self.player.get_sprite(), self.player.get_pos())

    def update_time(self):
        dt = self.now - self.previous
        self.previous = self.now
        self.now = p.time.get_ticks()
        return dt

    def handle_movement(self, pressed, dt: float):
        door = False
        map = self.current_level.map

        if pressed[p.K_UP]    : door = self.player.move(Direction.UP, dt, map)
        if pressed[p.K_DOWN]  : door = self.player.move(Direction.DOWN, dt, map)
        if pressed[p.K_LEFT]  : door = self.player.move(Direction.LEFT, dt, map)
        if pressed[p.K_RIGHT] : door = self.player.move(Direction.RIGHT, dt, map)

        if door: self.change_lvl(self.current_level.get_bordering(door))

    def read_input(self):
        return p.key.get_pressed()

    def end_game(self):
        pass

    def change_lvl(self, level):
        self.current_level = level

    def draw_sceen(self, screen: p.Surface):
        for row in self.current_level.map:
            for tile in row:
                screen.blit(tile.get_sprite(), tile.get_pos())

    def start_clock(self):
        pass

    def stop_clock(self):
        pass
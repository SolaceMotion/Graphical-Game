import pygame as p
from direction import Direction
from player import Player
from state import State
from combat import Combat

from config import RESOLUTION, PLAYER_SPRITE, ENEMY_HEALTH
from levels import _level_1


class Game:
    def __init__(self, clock: p.time.Clock, fps: int = 60) -> None:
        self.clock = clock
        self.player = Player(PLAYER_SPRITE, size = (RESOLUTION, RESOLUTION))
        self.fps = fps
        self.now = p.time.get_ticks()
        self.previous = p.time.get_ticks()
        self.current_level = _level_1
        self.state = State.ON_MAP

    def tick(self, screen: p.Surface):
        if self.state == State.ON_MAP:
            self.clock.tick(self.fps)
            dt = self.update_time()
            keys_pressed = self.read_input()
            self.handle_movement(keys_pressed, dt)
            self.draw_sceen(screen)
            screen.blit(self.player.get_sprite(), self.player.get_pos())
            if self.current_level.enemy != None:
                if self.current_level.enemy.alive:
                    screen.blit(self.current_level.enemy.get_sprite(), self.current_level.enemy.get_pos())
                    if self.player.collision(self.current_level.enemy):
                        self.state = State.IN_COMBAT
        
        if self.state == State.IN_COMBAT:
            current_pos = self.player.get_pos()
            combat = Combat(self.player, self.current_level.enemy)
            combat.run_combat(self.clock, self.fps, screen)
            if self.current_level.enemy.alive or self.player.points == ENEMY_HEALTH * 3:
                self.state = State.ON_MAP
                self.end_game()
            else:
                self.player.set_pos(current_pos)
                self.state = State.ON_MAP


    def update_time(self):
        dt = self.now - self.previous
        self.previous = self.now
        self.now = p.time.get_ticks()
        return dt

    def handle_movement(self, pressed, dt: float):
        door = False
        map = self.current_level.map

        if pressed[p.K_UP]:
            entering = self.player.move(Direction.UP, dt, map)
            if entering: door = entering
        if pressed[p.K_DOWN]:
            entering = self.player.move(Direction.DOWN, dt, map)
            if entering: door = entering
        if pressed[p.K_LEFT]:
            entering = self.player.move(Direction.LEFT, dt, map)
            if entering: door = entering
        if pressed[p.K_RIGHT]:
            entering = self.player.move(Direction.RIGHT, dt, map)
            if entering: door = entering

        if door: self.change_lvl(self.current_level.get_bordering(door))

    def read_input(self):
        return p.key.get_pressed()

    def change_lvl(self, level):
        self.current_level = level

    def draw_sceen(self, screen: p.Surface):
        for row in self.current_level.map:
            for tile in row:
                screen.blit(tile.get_sprite(), tile.get_pos())

    def end_game(self):
        self.state = State.GAME_OVER
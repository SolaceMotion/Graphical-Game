import pygame as p

from .direction import Direction
from .player import Player
from .state import State
from .combat import Combat

from .config import RESOLUTION, PLAYER_SPRITE, ENEMY_HEALTH, FONT, WIDTH, HEIGHT
from .levels import _level_1


class Game:
    def __init__(self, clock: p.time.Clock, fps: int = 60):
        self.clock = clock
        self.player = Player(PLAYER_SPRITE, size=(RESOLUTION, RESOLUTION))
        self.fps = fps
        self.now = p.time.get_ticks()
        self.previous = p.time.get_ticks()
        self.current_level = _level_1
        self.state = State.ON_MAP
        self.font = p.font.SysFont(FONT, 25)

    def render_text(self, text: str) -> p.Surface:
        return self.font.render(text, True, (255, 255, 255))

    def tick(self, screen: p.Surface):
        pre_move = self.player.get_pos()

        if self.state == State.ON_MAP:
            self.clock.tick(self.fps)
            dt = self.update_time()
            keys_pressed = self.read_input()
            self.handle_movement(keys_pressed, dt)
            self.draw_sceen(screen)
            screen.blit(self.player.get_sprite(), self.player.get_pos())

            # Render door if all goons are not yet defeated
            if self.current_level == _level_1 and self.player.points != ENEMY_HEALTH * 2:
                txt = self.render_text(
                    "This door unlocks when all goons are defeated.")

                screen.blit(self.current_level.door.get_sprite(),
                            self.current_level.door.get_pos())

                if self.player.collision(self.current_level.door):
                    self.player.set_pos(pre_move)
                    screen.blit(txt, ((WIDTH - txt.get_width()) /
                                2, (HEIGHT - txt.get_height()) / 2))

            # If there is an enemy on current level
            if self.current_level.enemy != None:
                # Make enemy move towards player
                self.current_level.enemy.move(self.player)

                # Render enemy if they are alive
                if self.current_level.enemy.alive:
                    screen.blit(self.current_level.enemy.get_sprite(),
                                self.current_level.enemy.get_pos())

                    # If player collides with enemy, begin combat state
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

    def update_time(self) -> float:
        dt = self.now - self.previous
        self.previous = self.now
        self.now = p.time.get_ticks()
        return float(dt)

    def handle_movement(self, pressed, dt: float):
        door = False
        map = self.current_level.map

        if pressed[p.K_UP]:
            entering = self.player.move(Direction.UP, dt, map)
            if entering:
                door = entering
        if pressed[p.K_DOWN]:
            entering = self.player.move(Direction.DOWN, dt, map)
            if entering:
                door = entering
        if pressed[p.K_LEFT]:
            entering = self.player.move(Direction.LEFT, dt, map)
            if entering:
                door = entering
        if pressed[p.K_RIGHT]:
            entering = self.player.move(Direction.RIGHT, dt, map)
            if entering:
                door = entering

        if door:
            self.change_lvl(self.current_level.get_bordering(door))

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

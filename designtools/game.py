import pygame as p

from config import LEVEL, Level, temp, generate_map


class Game:
    def __init__(self) -> None:
        self.now = p.time.get_ticks()
        self.previous = p.time.get_ticks()
        self.current_level = LEVEL
        self.map = temp
        self.clock = p.time.Clock()

    def tick(self, screen: p.Surface):
        self.draw_sceen(screen)
    
    def handle_change(self, click):
        for i, row in enumerate(self.current_level.map):
            for j, tile in enumerate(row):
                if p.Rect.colliderect(tile.get_rect(), click):
                    self.update_map(i, j)
    
    def update_map(self, i, j):
        if self.map[i][j] == "brown":
            self.map[i][j] = "red"
        elif self.map[i][j] == "red":
            self.map[i][j] = "brown"
        self.current_level = Level(generate_map(self.map))

    def draw_sceen(self, screen: p.Surface):
        for row in self.current_level.map:
            for tile in row:
                screen.blit(tile.get_sprite(), tile.get_pos())
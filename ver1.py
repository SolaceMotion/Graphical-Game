import pygame as p
from pygame.draw import rect
from enum import Enum, auto

clock = p.time.Clock()
prev = p.time.get_ticks()


WIDTH = 900
HEIGHT = 600

RES = 15
screen = p.display.set_mode((900, 600))

FPS = 60

class Game:
    def __init__(self):
        #Each level is an element in this matrix. Each level is in turn also a matrix of aspect ratio 16:9.
        self.levels = [None for _ in range(10)]
        self.__running = True

        p.init()

    def set_level(self):
        #Create Test level

        cols = WIDTH // RES
        rows = HEIGHT // RES

        grid = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(None)
            grid.append(row)

        for i in range(rows):
            for j in range(cols):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                    rect(screen, (178, 200, 60), p.Rect(j*RES, i*RES, RES, RES))
                else:
                    rect(screen, (0, 140, 60), p.Rect(j*RES, i*RES, RES, RES))
        self.levels[0] = grid
                

    @property
    def is_running(self):
        return self.__running


    def quit_game(self):
        self.__running = not self.__running

    
class Dir(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

class Player:
    def __init__(self):
        self.__fatigue = False
        self.__x = 20
        self.__y = 20
        self.__vx = 3
        self.__vy = 3

        self.w = 60
        self.h = 60
    
    def draw(self):
        rect(screen, (0, 128, 255), p.Rect(self.__x, self.__y, self.w, self.h))
    
    def update_pos(self, direction, dt: float):
        # Prevent from going outside play area
        self.__x = self.__x % WIDTH 
        self.__y = self.__y % HEIGHT
        
        if direction == Dir.UP:
            self.__y -= self.__vy * dt / 10
        if direction == Dir.DOWN:
            self.__y += self.__vy * dt / 10
        if direction == Dir.RIGHT:
            self.__x += self.__vx * dt / 10
        if direction == Dir.LEFT:
            self.__x -= self.__vx * dt / 10


    def handle_movement(self, pressed, dt: float):
        if pressed[p.K_UP]: self.update_pos(Dir.UP, dt)
        if pressed[p.K_DOWN]: self.update_pos(Dir.DOWN, dt)
        if pressed[p.K_LEFT]: self.update_pos(Dir.LEFT, dt)
        if pressed[p.K_RIGHT]: self.update_pos(Dir.RIGHT, dt)
        if pressed[p.K_SPACE]: self.jump()

    def jump(self):
       pass 

g = Game()
player = Player()

while g.is_running:
    screen.fill((0,0,0))
    clock.tick(FPS)

    now = p.time.get_ticks()
    dt = now - prev
    prev = now
    for event in p.event.get():
        if event.type == p.QUIT:
            g.quit_game()

    press_event = p.key.get_pressed()
    player.handle_movement(press_event, dt)
    g.set_level()
    player.draw()

    p.display.flip()
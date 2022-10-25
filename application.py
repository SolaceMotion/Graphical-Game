import pygame as p
from game import Game


class Application:
    def __init__(self, width: int, height: int, clock: p.time.Clock) -> None:
        self.__running = True
        self.clock = clock
        self.width = width
        self.height = height
        self.resolution = (width, height)

    def init_game(self):
        self.game = Game(self.clock)

    def run(self):
        self.init_game()
        screen = p.display.set_mode(self.resolution)
        while self.is_running:
            screen.fill((0, 0, 0))
            self.game.tick(screen)
            p.display.flip()
            for event in p.event.get():
                if event.type == p.QUIT:
                    self.close_app()

    @property
    def is_running(self):
        return self.__running

    def main_menu(self):
        pass

    def close_app(self):
        self.__running = not self.__running
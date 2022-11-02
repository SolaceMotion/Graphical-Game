from fileinput import filename
from config import HEIGHT, WIDTH
import pygame as p
from game import Game

class Application:
    def __init__(self, width: int, height: int, filename: str) -> None:
        self.__running = True
        self.width = width
        self.height = height
        self.resolution = (width, height)
        self.start_game = False
        self.filename = filename

    def init_game(self):
        self.game = Game()

    def run(self):
        self.init_game()
        screen: p.Surface = p.display.set_mode(self.resolution)
            
        while self.is_running:
            screen.fill((0, 0, 0))
            self.game.tick(screen)
            p.display.flip()

            for event in p.event.get():
                if event.type == p.MOUSEBUTTONDOWN:
                    click = p.Rect(p.mouse.get_pos(), (1, 1))
                    self.game.handle_change(click)
                
                if event.type == p.QUIT:
                    with open(self.filename, 'w') as file:
                        file.write("level = " + str(self.game.map))
                    self.close_app()

        p.quit()

    @property
    def is_running(self):
        return self.__running

    def close_app(self):
        self.__running = not self.__running
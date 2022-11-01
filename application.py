from config import HEIGHT
from config import WIDTH
import pygame as p
from game import Game
from config import SCREEN


class Application:
    def __init__(self, width: int, height: int, clock: p.time.Clock) -> None:
        self.__running = True
        self.clock = clock
        self.width = width
        self.height = height
        self.resolution = (width, height)

    def init_game(self):
        # Show menu
        

        self.game = Game(self.clock)

    def run(self):
        self.init_game()
        screen = p.display.set_mode(self.resolution)
        while self.is_running:
            screen.fill((0, 0, 0))
            self.game.tick(screen)
            self.main_menu()
            p.display.flip()
            for event in p.event.get():

                if event.type == p.MOUSEBUTTONDOWN and p.mouse.get_pos()[0] > WIDTH / 20 - 100 and p.mouse.get_pos()[1] :
                    print("F")
                if event.type == p.QUIT:
                    self.close_app()

        p.quit()

    @property
    def is_running(self):
        return self.__running

    def main_menu(self):
        p.init()
        font = p.font.SysFont("ComicSans", 35)
        text = font.render("Play Game", True, (255,255,255))
        SCREEN.fill((30,30,30))

        p.draw.rect(SCREEN, (10,10,10), p.Rect(WIDTH/2-100, HEIGHT/2-50,200,50))

        SCREEN.blit(text,(WIDTH / 2 -80, HEIGHT / 2 - 50))

    def close_app(self):
        self.__running = not self.__running
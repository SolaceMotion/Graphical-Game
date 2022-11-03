from config import HEIGHT, WIDTH
import pygame as p
from game import Game
from state import State

class Application:
    def __init__(self, width: int, height: int, clock: p.time.Clock) -> None:
        self.__running = True
        self.clock = clock
        self.width = width
        self.height = height
        self.resolution = (width, height)
        self.start_game = False

    def init_game(self):
        self.game = Game(self.clock)

    def run(self):
        self.init_game()
        screen: p.Surface = p.display.set_mode(self.resolution)
            
        while self.is_running:
            screen.fill((0, 0, 0))
            if self.game.state == State.GAME_OVER:
                pass
            
            # Show menu
            if not self.start_game:
                self.main_menu(screen)
            else:
                # Render and continue time if game is not paused
                self.game.tick(screen)

            p.display.flip()
 
            for event in p.event.get():
                pressed = p.key.get_pressed()

                #Start if box is clicked or return key is pressed
                if (event.type == p.MOUSEBUTTONDOWN and self.box_rect.x <= p.mouse.get_pos()[0] <= self.box_rect.x + self.box_rect.w and self.box_rect.y <= p.mouse.get_pos()[1] <= self.box_rect.y + self.box_rect.h) or pressed[p.K_RETURN]:
                    self.start_game = True
                
                if pressed[p.K_ESCAPE]:
                    self.start_game = False
                    #Display a pause menu and stop game time, now only displays main menu again
                    
                if event.type == p.QUIT:
                    self.close_app()

        p.quit()

    @property
    def is_running(self):
        return self.__running

    def main_menu(self, screen: p.Surface):
        p.init()
        font = p.font.SysFont("ComicSans", 35)
        text = font.render("Play Game", True, (255,255,255))
        screen.fill((30,30,30))

        #Store a rect object to use for checking if user clicks within region of the box on menu
        self.box_rect = p.Rect(WIDTH / 2 - 100, HEIGHT/2 - 50, 200, 50)
        
        p.draw.rect(screen, (10,10,10), self.box_rect)
        screen.blit(text,(WIDTH / 2 -80, HEIGHT / 2 - 50))
    
    def game_over(self):
        pass

    def close_app(self):
        self.__running = not self.__running
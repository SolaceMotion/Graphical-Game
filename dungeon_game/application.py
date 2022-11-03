import pygame as p

from .game import Game
from .state import State

from .config import HEIGHT, WIDTH, FONT, ENEMY_HEALTH


class Application:
    def __init__(self, width: int, height: int, clock: p.time.Clock) -> None:
        p.init()
        self.__running = True
        self.clock = clock
        self.width = width
        self.height = height
        self.resolution = (width, height)
        self.start_game = False
        self.font = p.font.SysFont(FONT, 35)

    def init_game(self):
        self.game = Game(self.clock)

    def run(self):
        self.init_game()
        screen: p.Surface = p.display.set_mode(self.resolution)
            
        while self.is_running:
            screen.fill((0, 0, 0))
            
            # Show menu
            if not self.start_game:
                self.main_menu(screen)
            else:
                if self.game.state == State.GAME_OVER:
                    self.game_over(screen)
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
        text = self.render_text("Play Game")
        screen.fill((30,30,30))

        #Store a rect object to use for checking if user clicks within region of the box on menu
        self.box_rect = p.Rect(WIDTH / 2 - 100, HEIGHT/2 - 50, 200, 50)
        
        p.draw.rect(screen, (10,10,10), self.box_rect)
        screen.blit(text,(WIDTH / 2 -80, HEIGHT / 2 - 50))
    
    def game_over(self, screen: p.Surface):
        game_over_txt = self.render_text("Game over!")
        if self.game.player.points == ENEMY_HEALTH * 3:
            winner_txt = self.render_text("Congratulations! You win.")
        else:
            winner_txt = self.render_text("You lose!")
        score_txt = self.render_text(f"score: {self.game.player.points}")

        game_over_size = game_over_txt.get_width()
        winner_size = winner_txt.get_width()
        score_size = score_txt.get_width()

        screen.blit(game_over_txt, ((WIDTH - game_over_size) // 2, HEIGHT // 2 - 100))
        screen.blit(winner_txt, ((WIDTH - winner_size) // 2, HEIGHT // 2 - 50))
        screen.blit(score_txt, ((WIDTH - score_size) // 2, HEIGHT // 2))

    def render_text(self, text: str) -> p.Surface:
        return self.font.render(text, True, (255, 255, 255))

    def close_app(self):
        self.__running = not self.__running
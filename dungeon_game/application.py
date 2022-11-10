import pygame as p

from .game import Game
from .state import State

from .config import FONT, ENEMY_HEALTH, ICON


class Application:
    def __init__(self, width: int, height: int, clock: p.time.Clock) -> None:
        p.init()
        p.display.set_caption('Banoras castle')
        p.display.set_icon(p.image.load(ICON))
        self.__running = True
        self.clock = clock
        self.width = width
        self.height = height
        self.resolution = (width, height)
        self.start_game = False
        self.font = p.font.SysFont(FONT, 35)

    def run(self):
        self.game = Game(self.clock)
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
                    self.display_score(screen)

            p.display.flip()

            for event in p.event.get():
                pressed = p.key.get_pressed()

                # Start if box is clicked or return key is pressed
                if (event.type == p.MOUSEBUTTONDOWN and self.box_rect.x <= p.mouse.get_pos()[0] <= self.box_rect.x + self.box_rect.w and self.box_rect.y <= p.mouse.get_pos()[1] <= self.box_rect.y + self.box_rect.h) or pressed[p.K_RETURN]:
                    self.start_game = True

                if pressed[p.K_ESCAPE]:
                    self.start_game = False
                    # Display a pause menu and stop game time, now only displays main menu again

                if event.type == p.QUIT:
                    self.close_app()

        p.quit()

    @property
    def is_running(self):
        return self.__running

    def display_score(self, screen: p.Surface):
        points = self.game.player.points
        text = self.render_text(f"Score: {str(points)}")
        screen.blit(text, (10, 2))

    def main_menu(self, screen: p.Surface):
        screen.fill((30, 30, 30))
        text = self.render_text("Play Game")

        # Store a rect object to use for checking if user clicks within region of the box on menu
        self.box_rect = p.Rect(self.width / 2 - 100,
                               self.height / 2 - 50, 200, 50)

        p.draw.rect(screen, (10, 10, 10), self.box_rect)
        screen.blit(text, ((self.width - text.get_width()) / 2,
                    (self.height - text.get_height()) / 2 - 28))

        objective_txt1 = self.render_text(
            "Your objective is to defeat all the enemies")
        objective_txt2 = self.render_text(
            "scattered around the map. Good luck!")

        screen.blit(objective_txt1, ((
            self.width - objective_txt1.get_width()) / 2, self.height / 2 + 20))
        screen.blit(objective_txt2, ((
            self.width - objective_txt2.get_width()) / 2, self.height / 2 + 60))

    def game_over(self, screen: p.Surface):
        game_over_txt = self.render_text("Game Over!")
        # 45 points to beat the game
        if self.game.player.points == ENEMY_HEALTH * 3:
            win_txt = "Congratulations, You Win! :D"
        else:
            win_txt = "Sorry, You Lost! :("

        winner_txt = self.render_text(win_txt)
        score_txt = self.render_text(f"Final Score: {self.game.player.points}")

        game_over_size = game_over_txt.get_width()
        winner_size = winner_txt.get_width()
        score_size = score_txt.get_width()

        screen.blit(game_over_txt, ((self.width - game_over_size) //
                    2, self.height // 2 - 100))
        screen.blit(winner_txt, ((self.width - winner_size) //
                    2, self.height // 2 - 50))
        screen.blit(
            score_txt, ((self.width - score_size) // 2, self.height // 2))

    def render_text(self, text: str) -> p.Surface:
        return self.font.render(text, True, (255, 255, 255))

    def close_app(self):
        self.__running = not self.__running

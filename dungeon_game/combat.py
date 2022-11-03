import pygame
from pygame.locals import*
import random

from .config import HEIGHT, WIDTH, ENEMY_HEALTH

from .player import Player
from .enemy import Enemy

#Combat state
class Combat():
    def __init__(self, player: Player, enemy: Enemy):
        self.width, self.height = (WIDTH, HEIGHT)
        self.road_w = int(self.width // 2)
        self.road_mark = int(self.width // 80)
        self.left_lane = int(self.width // 2 - self.road_w // 4)
        self.right_lane = int(self.width // 2 + self.road_w // 4)
        self.player = player
        self.player.set_pos((self.width // 2 + self.road_w // 4, int(self.height * 4 //5)))
        self.enemy = enemy
        self.enemy.set_pos((self.left_lane, -50))
        self.running = True

    def draw(self, screen: pygame.Surface):
        screen.fill((100, 250, 150))
        pygame.draw.rect(screen,(155,150,150),(self.width//2 - self.road_w//2, 0, self.road_w, self.height ))
        pygame.draw.rect(screen,(255,255,60),(self.width//2 - self.road_mark//2, 0, self.road_mark, self.height ))
        pygame.draw.rect(screen,(255,255,255),(self.width//2 - self.road_w//2 + self.road_mark*2, 0, self.road_mark, self.height ))
        pygame.draw.rect(screen,(255,255,255),(self.width//2 +  self.road_w//2 - self.road_mark*3, 0, self.road_mark, self.height ))

    def run_combat(self, clock: pygame.time.Clock, fps: int, screen: pygame.Surface):

        points = 0
        while self.running:
            clock.tick(fps)

            if self.player.collision(self.enemy):
                break
            elif points >= ENEMY_HEALTH:
                self.enemy.alive = False
                break

            x, y = self.enemy.get_pos()
            y += self.enemy.speed
            self.enemy.set_pos((x, y))

            if self.enemy.get_pos()[1] >= self.height:
                points += 1
                #Increase speed every 5th point
                if points % 5 == 0:
                    self.enemy.speed += 3
                x, y = self.enemy.get_pos()
                y = -100
                self.enemy.set_pos((x, y))
                lane = random.randint(0,1)
                if lane == 0:
                    self.enemy.set_pos((self.left_lane, -50))
                else:
                    self.enemy.set_pos((self.right_lane, -50))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    quit()
                if event.type == KEYDOWN:
                    if event.key in [K_a, K_LEFT]:
                        self.player.set_pos((self.left_lane, self.height*4//5))
                    if event.key in [K_d, K_RIGHT]:
                        self.player.set_pos((self.right_lane, self.height*4//5))
            self.draw(screen)


            screen.blit(self.player.get_sprite(),self.player.get_pos())
            screen.blit(self.enemy.get_sprite(), self.enemy.get_pos())
            pygame.display.update()

        self.player.points += points

import pygame
from pygame.locals import*
import random
from config import PLAYER_SPRITE, BOSS_SPRITE


from player import Player
from enemy import Enemy

pygame.init()

class Combat():
    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.width, self.height = (1200, 800)
        self.road_w = int(self.width / 2)
        self.road_mark = int(self.width / 80)
        self.left_lane = self.width / 2 - self.road_w / 4
        self.right_lane = self.width / 2 + self.road_w / 4
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.running = True

        self.tree_loc = self.player.get_pos()
        self.tree_loc = self.width / 2 + self.road_w / 4, self.height * 0.8
        self.enemy_boll_loc = self.enemy.get_pos()
        self.enemy_boll_loc = self.left_lane, self.height * 0.2

    def draw(self):
        self.screen.fill((100, 250, 150))
        pygame.draw.rect(self.screen,(155,150,150),(self.width/2 - self.road_w/2, 0, self.road_w, self.height ))
        pygame.draw.rect(self.screen,(255,255,60),(self.width/2 - self.road_mark/2, 0, self.road_mark, self.height ))
        pygame.draw.rect(self.screen,(255,255,255),(self.width/2 - self.road_w/2 + self.road_mark*2, 0, self.road_mark, self.height ))
        pygame.draw.rect(self.screen,(255,255,255),(self.width/2 +  self.road_w/2 - self.road_mark*3, 0, self.road_mark, self.height ))


    def run_Combat(self):
        a = 1
        b = 1
        while self.running:
            if self.enemy_boll_loc [0] == self.tree_loc[0] and self.enemy_boll_loc [1] == self.tree_loc[1] - 80:
                print('GAME OVER, YOU LOST!', 'Game points:', a)
                break
            elif a >= 30:
                print('congrats you have achieved the highest points')
                break

            #self.enemy_boll_loc[1] += a
            x, y = self.enemy.get_pos()
            y +=a
            self.enemy.set_pos((x, y))

            if self.enemy_boll_loc[1] >= 800:
                b +=1
                if b % 3 == 0:
                    a += 4
                print (b,a)
                self.enemy_boll_loc[1] = -100
                lane = random.randint(0,1)
                if lane == 0:
                    self.enemy_boll_loc.center = self.left_lane, self.height * 0.2
                else:
                    self.enemy_boll_loc.center = self.right_lane, self.height * 0.2
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key in [K_a, K_LEFT]:
                        self.tree_loc = self.tree_loc.move([-int(self.road_w/2), 0])
                    if event.key in [K_d, K_RIGHT]:
                        self.tree_loc = self.tree_loc.move([int(self.road_w/2), 0])
            Combat.draw()


            self.screen.blit(self.player.get_sprite(),self.tree_loc)
            self.screen.blit(self.enemy.get_sprite(), self.enemy_boll_loc)
            #pygame.display.update()


        pygame.quit()
def main():
    combat = Combat(Player(PLAYER_SPRITE), Enemy(BOSS_SPRITE))
    combat.run_Combat()

main()
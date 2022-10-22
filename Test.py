import pygame
from pygame.locals import*
import random
pygame.init()

size = width,height = (1200, 800)
road_w = int(width/2)
road_mark = int(width/80)
left_lane = width/2 - road_w/4
right_lane = width/2 + road_w/4
running = True
screen = pygame.display.set_mode((size))
screen.fill((100, 250, 150))
pygame.draw.rect(screen,(155,150,150),(width/2 - road_w/2, 0, road_w, height ))
pygame.draw.rect(screen,(255,255,60),(width/2 - road_mark/2, 0, road_mark, height ))
pygame.draw.rect(screen,(255,255,255),(width/2 - road_w/2 + road_mark*2, 0, road_mark, height ))
pygame.draw.rect(screen,(255,255,255),(width/2 +  road_w/2 - road_mark*3, 0, road_mark, height ))


pygame.display.update()
tree = pygame.image.load('boll.png')
tree_loc = tree.get_rect()
tree_loc.center = width/2 + road_w/4, height*0.8

enemy_boll = pygame.image.load('boll2.png')
enemy_boll_loc = tree.get_rect()
enemy_boll_loc.center = left_lane, height*0.2
a = 1
b = 1
while running:
    if enemy_boll_loc [0] == tree_loc[0] and enemy_boll_loc [1] == tree_loc[1] - 80:
        print('GAME OVER, YOU LOST!', 'Game points:', a)
        break
    elif a >= 30:
        print('congrats you have achieved the highest points')
        break

    enemy_boll_loc[1] += a

    if enemy_boll_loc[1] >= 800:
        b +=1
        if b % 3 == 0:
            a += 4
        print (b,a)
        enemy_boll_loc[1] = -100
        lane = random.randint(0,1)
        if lane == 0:
            enemy_boll_loc.center = left_lane, height * 0.2
        else:
            enemy_boll_loc.center = right_lane, height * 0.2
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                tree_loc = tree_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                tree_loc = tree_loc.move([int(road_w/2), 0])

    road_w = int(width / 2)
    road_mark = int(width / 80)
    screen = pygame.display.set_mode((size))
    screen.fill((100, 250, 150))
    pygame.draw.rect(screen, (155, 150, 150), (width / 2 - road_w / 2, 0, road_w, height))
    pygame.draw.rect(screen, (255, 255, 60), (width / 2 - road_mark / 2, 0, road_mark, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_w / 2 + road_mark * 2, 0, road_mark, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_w / 2 - road_mark * 3, 0, road_mark, height))

    screen.blit(tree, tree_loc)
    screen.blit(enemy_boll, enemy_boll_loc)
    pygame.display.update()


pygame.quit()

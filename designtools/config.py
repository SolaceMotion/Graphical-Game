from pygame.display import set_mode 

# screen
WIDTH = 800
HEIGHT = 450
RESOLUTION = 50

SCREEN = set_mode((WIDTH, HEIGHT))

# sprites
PLAYER_SPRITE = "./../sprites/player.png"
BOSS_SPRITE = "./../sprites/boss.png"
ENEMY_SPRITE = "./../sprites/enemy.png"
ENEMY2_SPRITE = "./../sprites/Enemy_2.png"

# tile sprites
BROWN_TILE = "./../sprites/bgr.tiles.brown.png"
RED_TILE = "./../sprites/bgr.tiles.dark_red.png"
YELLOW_TILE = "./../sprites/bgr.tiles.dark_yellow.png"
GREEN_TILE = "./../sprites/bgr.tiles.green.png"

TILES = {"brown": BROWN_TILE, "red": RED_TILE, "yellow": YELLOW_TILE, "green": GREEN_TILE}
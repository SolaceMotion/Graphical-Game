from .character import Character
from .player import Player
from math import sqrt, pow

class Enemy(Character):
    def __init__(self, sprite: str, *, pos = (20, 20), size = (60, 60), speed = 5):
        super().__init__(sprite, pos = pos, size = size)
        self.speed = speed
        self.colidable = True
        self.alive = True
        self.speed_factor = 0
    
    def distance_to_player(self, player: Player) -> tuple[float]:
        x, y = self.get_pos()
        p_x, p_y = player.get_pos()
        
        dx = p_x - x
        dy = p_y - y

        distance = sqrt(pow(dx, 2) + pow(dy, 2))
        #Normalized direction vector
        dx = dx / (distance - self.speed_factor)
        dy = dy / (distance - self.speed_factor)

        #Make enemy approach player faster if player keeps running away.
        self.speed_factor += 0.05

        return distance, dx, dy

    def move(self, player: Player):
        dist, dx, dy = self.distance_to_player(player)

        #If player is within 235 pixels range (currently, enemy is able to phase through objects).
        if dist.__le__(235):
            #Move towards player...
            self._x += dx
            self._y += dy
            #...and update rect
            self.set_rect((self._x, self._y))


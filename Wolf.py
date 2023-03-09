import pygame
import random
import math

class Wolf(pygame.sprite.Sprite):

    def __init__(self, coordonnee, game):
        super().__init__()
        self.vitesse = 1
        self.image = pygame.image.load('images/wolf.png') 
        self.game = game
        self.image = pygame.transform.scale(self.image, (25, 25)) 

        self.rect = self.image.get_rect()
        self.rect.x = coordonnee[0] - 15
        self.rect.y = coordonnee[1] - 15

        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)


    def remove(self):
        self.game.all_wolf.remove(self)


    def get_nearest_rabbit(self):
        distance_min = None
        pos_min = None
        for lapin in self.game.all_rabbit:
            distance = math.dist((self.rect.x, self.rect.y), (lapin.rect.x, lapin.rect.y))
            if distance_min == None or distance < distance_min:
                distance_min = distance
                pos_min = (lapin.rect.x, lapin.rect.y)
        return (distance_min, pos_min)


    def deplacement(self):
        if not self.game.check_collision(self, self.game.all_rabbit):
            if self.game.all_rabbit:
                distance, position = self.get_nearest_rabbit()
                if distance < 200:
                    direction = pygame.math.Vector2(position) - self.position
                    self.position += direction.normalize() * self.vitesse
                    self.rect.x = round(self.position.x)
                    self.rect.y = round(self.position.y)
            else:
                pass

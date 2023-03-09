import pygame
import random 
import math

class Rabbit(pygame.sprite.Sprite):

    def __init__(self, coordonnee, game):
        super().__init__()
        self.vitesse = 1
        self.image = pygame.image.load('images/rabbit.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = coordonnee[0] - 15 #-15 pour que le lapin soit au centre de la souris
        self.rect.y = coordonnee[1] - 15

        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)


    def remove(self):
        self.game.all_rabbit.remove(self)


    def get_nearest_food(self):
        distance_min = None
        pos_min = None
        for food in self.game.all_food:
            distance = math.dist((self.rect.x, self.rect.y), (food.rect.x, food.rect.y))
            if distance_min == None or distance < distance_min:
                distance_min = distance
                pos_min = (food.rect.x, food.rect.y)
        return distance_min, pos_min


    def deplacement(self):

        if not self.game.check_collision(self, self.game.all_wolf):
            if self.game.all_food:
                distance, position = self.get_nearest_food()
                if distance < 300:
                    direction = pygame.math.Vector2(position) - self.position
                    self.position += direction.normalize() * self.vitesse
                    self.rect.x = round(self.position.x)
                    self.rect.y = round(self.position.y)

        else:
            self.remove()


    def mange(self):
        self.game.ajout_lapin((self.rect.x, self.rect.y))

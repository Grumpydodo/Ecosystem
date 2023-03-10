import pygame
from Wolf import Wolf
from Rabbit import Rabbit
from Food import Food

class Game:

    def __init__(self):
        
        self.spawner = 0 # initialise l'apparition a 0 donc -> loup

        self.all_wolf = pygame.sprite.Group()
        self.all_rabbit = pygame.sprite.Group() 
        self.all_food = pygame.sprite.Group()


    def check_collision(self, sprite, group):
        """Permet de vérifier si un object rentre en colision avec un groupe d'oject"""
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def ajout_lapin(self, coordonnee):
        """Permet de faire apparaitre un lapin """
        self.all_rabbit.add(Rabbit(coordonnee, self))


    def ajout_loup(self, coordonnee):
        """ Permet de faire apparaitre un loup"""
        self.all_wolf.add(Wolf(coordonnee, self))


    def ajout_food(self, coordonnee):
        """ Permet de faire apparaitre de la nourriture"""
        self.all_food.add(Food(coordonnee, self))


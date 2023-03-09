import pygame
import random 
import math

class Rabbit(pygame.sprite.Sprite):

    def __init__(self, coordonnee, game):
        super().__init__()

        self.game = game

        self.vitesse = 1

        self.image = pygame.image.load('images/rabbit.png')
        self.image = pygame.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect()
        self.rect.x = coordonnee[0] - 15 # -15 pour que le lapin soit au centre de la souris
        self.rect.y = coordonnee[1] - 15

        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.direction = pygame.math.Vector2(self.rect.x, self.rect.y)


    def remove(self):
        """ Supprime le lapin (son sprite) de la simulation (de la liste) """
        self.game.all_rabbit.remove(self)


    def get_nearest_food(self):
        """ Recupere la distance et position de la nourriture la plus proche """
        distance_min = None
        pos_min = None
        for food in self.game.all_food: # Parcours tout les food dans la simulation
            distance = math.dist((self.rect.x, self.rect.y), (food.rect.x, food.rect.y)) #Calcul distance
            if distance_min == None or distance < distance_min: # Vérif si plus proche
                distance_min = distance
                pos_min = (food.rect.x, food.rect.y)
        return distance_min, pos_min


    def deplacement(self):
        """Permet le déplacement d'un lapin """
        if not self.game.check_collision(self, self.game.all_wolf): # Vérif si en collision avec un loup
            if self.game.all_food: # Vérif si il y a de la nourriture dans la simlation 
                distance, position = self.get_nearest_food() # recupere distance et position food plus proche
                if distance < 300: # Si trop loin le lapin ne s'y deplace pas 
                    direction = pygame.math.Vector2(position) - self.position
                    self.position += direction.normalize() * self.vitesse
                    self.rect.x = round(self.position.x)
                    self.rect.y = round(self.position.y)
                else:
                    self.deplacementRandom()
            else: 
                self.deplacementRandom()

        else: # si le lapin est en colision avec un loup il meurt
            self.remove()


    def deplacementRandom(self):
        """ Permet un deplacement au hasard """
        initR = random.randint(0, 5)

        if initR == 0:
            self.direction = pygame.math.Vector2((random.randint(0,1000), random.randint(0,600))) - self.position # direction au hasard

        self.position += self.direction.normalize() * (self.vitesse / 2) # on veux qu'il se deplace moins vite
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)


    def mange(self):
        """ Le lapin se reproduit """
        self.game.ajout_lapin((self.rect.x, self.rect.y))




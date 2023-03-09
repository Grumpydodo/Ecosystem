import pygame
import random
import math

class Wolf(pygame.sprite.Sprite):

    def __init__(self, coordonnee, game):
        super().__init__()

        self.game = game

        self.vitesse = 1

        self.image = pygame.image.load('images/wolf.png') 
        self.image = pygame.transform.scale(self.image, (25, 25)) 


        self.rect = self.image.get_rect()
        self.rect.x = coordonnee[0] - 15 # -15 pour centrer par rapport a la taille du sprite
        self.rect.y = coordonnee[1] - 15

        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.direction = pygame.math.Vector2(self.rect.x, self.rect.y)


    def remove(self):
        """ Supprime le loup (son sprite) de la simulation (de la liste) """
        self.game.all_wolf.remove(self)


    def get_nearest_rabbit(self):
        """ Renvoie la distance ainsi que les coordonnées du lapin le plus proche """
        distance_min = None
        pos_min = None
        for lapin in self.game.all_rabbit: # Parcours tout lapin dans la simulation 
            distance = math.dist((self.rect.x, self.rect.y), (lapin.rect.x, lapin.rect.y)) # Calcul la distance
            if distance_min == None or distance < distance_min: # Vérif si plus proche
                distance_min = distance
                pos_min = (lapin.rect.x, lapin.rect.y)
        return (distance_min, pos_min)

    
    def deplacement(self):
        """ Permet le déplacement du loup """
        if not self.game.check_collision(self, self.game.all_rabbit):
            if self.game.all_rabbit: # Vérif si il y a au moins un lapin dans la simulation
                distance, position = self.get_nearest_rabbit() # Récupére distance | position plus proche lapin
                if distance < 200: # Le loup ne s'y approche que a partir d'une certaine distance
                    self.direction = pygame.math.Vector2(position) - self.position
                    self.position += self.direction.normalize() * self.vitesse
                    self.rect.x = round(self.position.x)
                    self.rect.y = round(self.position.y)
                else:
                    self.deplacementRandom()
            else:
                self.deplacementRandom()


    def deplacementRandom(self):
        """ Permet un deplacement au hasard """
        initR = random.randint(0, 5)

        if initR == 0:
            self.direction = pygame.math.Vector2((random.randint(0,1000), random.randint(0,600))) - self.position # direction au hasard

        self.position += self.direction.normalize() * (self.vitesse / 2) # on veux qu'il se deplace moins vite
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)
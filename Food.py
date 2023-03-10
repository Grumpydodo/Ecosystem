import pygame


class Food(pygame.sprite.Sprite):

    def __init__(self, coordonnee, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('images/food.png')
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = coordonnee[0] - 15 #-25 pour que le lapin soit au centre de la souris
        self.rect.y = coordonnee[1] - 15


    def remove(self):
        """ Supprime food de la simulation"""
        self.game.all_food.remove(self)

    
    def deplacement(self):
        """ Permet de vérifier si un lapin rentre en contact et de supprimer la nourriture dans ce cas"""
        self.horsMap()
        for lapin in self.game.check_collision(self, self.game.all_rabbit): # Vérif si en colision avec un lapin
            lapin.mange() # fait apparaitre le lapin 
            self.remove() # Supprime la nourriture de la simulation


    def horsMap(self):
        """ Vérifie si l'object est toujours dans la map ou si il en est sortie
        si il est sortie le supprime"""
        if self.rect.y < 0 or self.rect.y > 650 or self.rect.x < 0 or self.rect.x > 950:
            self.remove()

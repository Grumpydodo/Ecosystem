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
        self.game.all_food.remove(self)

    
    def deplacement(self):
        for lapin in self.game.check_collision(self, self.game.all_rabbit):
            lapin.mange()
            self.remove()

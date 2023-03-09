import pygame
import time

from Game import Game


pygame.init()

clock = pygame.time.Clock()
FPS = 60

# génére la fenetre
pygame.display.set_caption("Ecosystem")
ecran = pygame.display.set_mode((1080, 650))

# Pour ajouter un fond d'écran
fondEcran = pygame.image.load('images/grass.jpg')
fondEcran = pygame.transform.scale(fondEcran, (1080,650))

#Bouton pour selectionner le spawn des loups
wolf_button = pygame.image.load('images/icon_wolf.png')
wolf_button = pygame.transform.scale(wolf_button, (50,50))
wolf_button_rect = wolf_button.get_rect()
wolf_button_rect.x = 1000
wolf_button_rect.y = 25

#Bonton pour selectionner le spawn des lapins
rabbit_button = pygame.image.load('images/icon_rabbit.png')
rabbit_button = pygame.transform.scale(rabbit_button, (50,50))
rabbit_button_rect = rabbit_button.get_rect()
rabbit_button_rect.x = 1000
rabbit_button_rect.y = 125

#Bouton pour electionner le spawn de la nourriture
food_button = pygame.image.load('images/icon_food.png')
food_button = pygame.transform.scale(food_button, (50,50))
food_button_rect = food_button.get_rect()
food_button_rect.x = 1000
food_button_rect.y = 225


game = Game()

while True:

    #appliquer le fond d'écran
    ecran.blit(fondEcran, (0,0))

    # ajoute les boutons a l'écran
    ecran.blit(wolf_button, wolf_button_rect)
    ecran.blit(rabbit_button, rabbit_button_rect)
    ecran.blit(food_button, food_button_rect)

    #faire se déplacer tout les lapins
    for lapin in game.all_rabbit:
        lapin.deplacement()

    # afficher tout les lapins
    game.all_rabbit.draw(ecran)


    #faire se déplacer tout les loups
    for loup in game.all_wolf:
        loup.deplacement()

    #Afficher tout les loups
    game.all_wolf.draw(ecran)


    #faire s'update toute les nourritures
    for nourriture in game.all_food:
        nourriture.deplacement()

    #affichage nourriture
    game.all_food.draw(ecran)

    # MAJ ecran
    pygame.display.flip()

    # parcours tout les events
    for event in pygame.event.get():

        # event fenetre fermer 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture de la fenetre")

        # detecte si on clic sur la fenetre 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #on recupere la position du clic
            position_clic = pygame.mouse.get_pos() 
            
            if rabbit_button_rect.collidepoint(position_clic):
                game.spawner = 0
            
            elif wolf_button_rect.collidepoint(position_clic):
                game.spawner = 1

            elif food_button_rect.collidepoint(position_clic):
                game.spawner = 2

            else:
                if game.spawner == 0:
                    game.ajout_lapin(position_clic)
                
                elif game.spawner == 1:
                    game.ajout_loup(position_clic)
                
                elif game.spawner == 2:
                    game.ajout_food(position_clic)
    clock.tick(FPS)


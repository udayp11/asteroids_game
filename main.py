import pygame
from constants import *

from players import Player




def main():
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

   
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)



    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    


    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for objects in updatable:
            objects.update(dt)


        for objects in drawable:
            objects.draw(screen)
            
        pygame.display.flip()
        

        dt = (clock.tick(60))/1000

    

if __name__ == "__main__":
    main()
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import player as PlayerClass
from constants import *

def main():
    test = pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player = PlayerClass.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    print(f"{test[0]} tests passed \n{test[1]} tests failed")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill('black')
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()

import pygame
from constants import *
from circleshape import *
from player import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('#000000')
        player.draw(screen)
        pygame.display.flip()
        #limiting fps to 60
        time_passed=clock.tick(60)
        dt = time_passed/1000
    

if __name__ == "__main__":
    main()
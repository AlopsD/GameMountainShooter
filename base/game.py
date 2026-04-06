import pygame

from base.menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        window = pygame.display.set_mode((600,480))

    def run(self, ):
        pygame.init()
        self.window = pygame.display.set_mode((600, 480))

        while True:

            menu = Menu()
            
            # for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #       pygame.quit()
            #      quit()


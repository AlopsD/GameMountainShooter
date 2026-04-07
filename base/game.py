import pygame
from base.const import WIN_WIDTH, WIN_HEIGHT
from base.menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WIN_HEIGHT,WIN_WIDTH))

    def run(self, ):

        while True:

            menu = Menu(self.window)
            menu.run()
            pass

            # for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #       pygame.quit()
            #      quit()


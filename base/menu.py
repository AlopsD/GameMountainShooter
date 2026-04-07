import pygame

class Menu:
    def __init__(self, window):
        self.window = None
        self.surf = pygame.image.load('diretorio')
        self.rect = self.surf.get_rect(left = 0, right=0)

    def run(self, ):
        self.window.blit(source=self.surf, dest=self.rect)
        pygame.display.flip()
        pass
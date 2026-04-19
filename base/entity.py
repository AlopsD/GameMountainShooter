from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        direct = str
        if name[0:2] == 'pl':
            direct = 'player'
        if name[0:2] == 'le':
            direct = 'level'

        self.surf = pygame.image.load('./asset/'+ direct +'/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left = position[0], top = position[1])
        self.mask = pygame.mask.from_surface(self.surf)
        self.speed = 0


    @abstractmethod
    def move(self,):
        pass
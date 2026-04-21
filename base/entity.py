from abc import ABC, abstractmethod

import pygame.image

from base.const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        direct = ''
        if name[0:2] == 'pl':
            direct = 'player'
        if name[0:2] == 'le':
            direct = 'level'
        if name[0:2] == 'en':
            direct = 'enemy'

        self.surf = pygame.image.load('./asset/'+ direct +'/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left = position[0], top = position[1])
        self.mask = pygame.mask.from_surface(self.surf)
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]


    @abstractmethod
    def move(self,):
        pass
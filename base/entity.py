from abc import ABC, abstractmethod

import pygame.image

from base.const import ENTITY_HEALTH, PREFIX_DIRECTORY, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        direct = PREFIX_DIRECTORY.get(name[0:3]) #verifica o diretorio do nome
        if direct is None:
            raise ValueError(f'invalid directory : {name}')


        self.surf = pygame.image.load(f'./asset/{direct}/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect(left = position[0], top = position[1])
        self.mask = pygame.mask.from_surface(self.surf)
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_damage = 'None'


    @abstractmethod
    def move(self,):
        pass
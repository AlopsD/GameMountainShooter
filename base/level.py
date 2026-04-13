import pygame

from base.entity import Entity
from base.entity_factory import Entity_factory


class Level:
    def __init__(self, window, name, game_option):
        self.window = window
        self.name = name
        self.game_mode = game_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(Entity_factory.get_entity('level_bg'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.flip()
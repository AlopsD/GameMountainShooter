from base.const import ENTITY_SPEED
from base.entity import Entity

class Player_Shot(Entity):
    def __init__(self, name: str, position: tuple, directory: str):
        super().__init__(name, position, directory)


    def move(self,):
        self.rect.centerx += ENTITY_SPEED[self.name]
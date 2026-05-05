from base.const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY, PREFIX_DIRECTORY
from base.enemy_shot import Enemy_Shot
from base.entity import Entity

class Enemy(Entity):
    def __init__(self, name:str, position: tuple, directory:str):
        super().__init__(name, position, directory)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return Enemy_Shot(f'shot_{self.name}',(self.rect.centerx, self.rect.centery), PREFIX_DIRECTORY['shot'])
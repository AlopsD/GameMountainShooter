from base.const import WIN_WIDTH, ENTITY_SPEED
from base.entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple, directory: str):
        super().__init__(name, position, directory)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
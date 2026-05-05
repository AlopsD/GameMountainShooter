import pygame

from base.const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOT, ENTITY_SHOT_DELAY, PREFIX_DIRECTORY
from base.entity import Entity
from base.player_shot import Player_Shot


class Player(Entity):
    def __init__(self, name : str, position : tuple, directory : str):
        super().__init__(name, position, directory)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]


    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[PLAYER_KEY_SHOT[self.name]]:
                return Player_Shot(f'shot_{self.name}',(self.rect.centerx, self.rect.centery), PREFIX_DIRECTORY['shot'])

import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from base.const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTIONS, EVENT_ENEMY, SPAWN_TIME
from base.entity import Entity
from base.entity_factory import Entity_factory


class Level:
    def __init__(self, window, name, game_option):
        self.timeout = 2000
        self.window = window
        self.name = name
        self.game_mode = game_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(Entity_factory.get_entity('level_bg',))
        self.entity_list.append(Entity_factory.get_entity('player1'))

        if game_option in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(Entity_factory.get_entity('player2'))

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self, ):
        #pygame.mixer_music.load(f'./asset/sounds/{self.name}.mp3')
        #pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemy1','enemy2','enemy3','enemy4'))
                    self.entity_list.append(Entity_factory.get_entity(choice))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10,5) )
            self.level_text(14,f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10,WIN_HEIGHT - 35) )
            self.level_text(14, f'entidade: {len(self.entity_list)}', COLOR_WHITE, (10,WIN_HEIGHT - 20) )

            pygame.display.flip()

    def level_text(self, text_size: int, text:str , text_color : tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(left = text_position[0], top = text_position[1])
        self.window.blit(text_surface, text_rect)

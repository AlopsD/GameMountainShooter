import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from base.const import C_WHITE, WIN_HEIGHT, MENU_OPTIONS, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL, DISPLAY_NAME
from base.enemy import Enemy
from base.entity import Entity
from base.entity_factory import Entity_factory
from base.entity_mediator import Entity_Mediator
from base.player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_option : str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        print(name, )

        self.game_mode = game_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(Entity_factory.get_entity(self.name))
        player = Entity_factory.get_entity('player1')
        player.score = player_score[0]
        self.entity_list.append(player)

        if game_option in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            player = Entity_factory.get_entity('player2')
            player.score = player_score[1]

            self.entity_list.append(player)

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        #pygame.mixer_music.load(f'./asset/sounds/{self.name}.mp3')
        #pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'player1':
                    self.level_text(14, f'Player 1 Health: {ent.health} | Score {ent.score}', C_GREEN, (10,20))
                if ent.name == 'player2':
                    self.level_text(14, f'Player 2 Health: {ent.health} | Score {ent.score}', C_CYAN, (10,40))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemy1','enemy2','enemy3','enemy4'))
                    self.entity_list.append(Entity_factory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'player2':
                                player_score[1] = ent.score
                        return True
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False

            self.level_text(14, f'{DISPLAY_NAME[self.name]} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            self.level_text(14,f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidade: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            Entity_Mediator.verify_collision(entity_list= self.entity_list)
            Entity_Mediator.verify_health(entity_list= self.entity_list)

    def level_text(self, text_size: int, text:str , text_color : tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(left = text_position[0], top = text_position[1])
        self.window.blit(text_surface, text_rect)

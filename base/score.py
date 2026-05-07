import sys
from datetime import datetime
from quopri import ESCAPE

import pygame
from pygame.constants import KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from pygame import Rect
from pygame import Surface

from base.const import C_YELLOW, SCORE_POS, MENU_OPTIONS, C_WHITE
from base.db_proxy import DB_PROXY


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/background/score_bg.png').convert_alpha()
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def save(self, menu_return: str, player_score: list[int]):
        pygame.mixer.music.load('./asset/sound/menu_sound.wav')
        pygame.mixer.music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)

        db_proxy = DB_PROXY('db_score')
        name = ''
        while True:
            self.score_text(48, 'YOU WIN !!!', C_YELLOW, SCORE_POS['Title'])
            pygame.display.flip()

            if menu_return == MENU_OPTIONS[0]:
                score = player_score[0]
                text = 'Enter player 1 name: (4 characters)'
            if menu_return == MENU_OPTIONS[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team name: (4 characters)'
            if menu_return == MENU_OPTIONS[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player 1 name: (4 characters)'
                if player_score[1] <= player_score[2]:
                    score = player_score[1]
                    text = 'Enter Player 2 name: (4 characters)'

            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name':name, 'score':score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])

            pygame.display.flip()



    def show(self):
        # score_option = 1
        pygame.mixer.music.load('./asset/sound/menu_sound.wav')
        pygame.mixer.music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE',C_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME       SCORE           DATE    ', C_YELLOW, SCORE_POS['Label'])

        db_proxy = DB_PROXY('db_score')
        list_score = db_proxy.retrieve_top_10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score

            self.score_text(20, f'{name}       {score :05d}         {date}', C_YELLOW, SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return False
            pygame.display.flip()
            pass

    def score_text(self, text_size:int, text:str, text_color:tuple, text_position:tuple):
        text_font: Font = pygame.font.SysFont(name ='Lucida Sans Typewriter', size = text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center = text_position)

        self.window.blit(source=text_surf, dest=text_rect)
def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H:%M')
    current_data = current_datetime.strftime('%d/%m/%Y')
    return f'{current_time} - {current_data}'
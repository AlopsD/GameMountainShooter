#C
import pygame

COLOR_ORANGE = (255,128,0)
COLOR_WHITE = (255,255,255)

#E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {'level_bg0':0,'level_bg1':1,'level_bg2':2,'level_bg3':3,'level_bg4':4, 'player1': 3, 'player2' : 3, 'enemy1':5,'enemy2': 4,'enemy3': 6,'enemy4':3}

#M

MENU_OPTIONS = ('NEW GAME 1P','NEW GAME 2P - COOPERATIVE', 'NEW GAME 2P - COMPETITIVE', 'GAME OVER','QUIT')

#P

PLAYER_KEY_UP = {'player1': pygame.K_UP, 'player2' : pygame.K_w}

PLAYER_KEY_DOWN = {'player1': pygame.K_DOWN, 'player2': pygame.K_s}

PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT, 'player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT, 'player2': pygame.K_d}


#S

SPAWN_TIME = 4800

#W
WIN_WIDTH = 576
WIN_HEIGHT = 324
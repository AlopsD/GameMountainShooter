#C
import pygame

COLOR_ORANGE = (255,128,0)
COLOR_WHITE = (255,255,255)

#E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'level_bg0':0,
    'level_bg1':1,
    'level_bg2':2,
    'level_bg3':3,
    'level_bg4':4,
    'player1': 3,
    'player2' : 3,
    'shot_player1': 4,
    'shot_player2': 4,
    'enemy1':5,
    'enemy2': 5,
    'enemy3': 6,
    'enemy4':5,
    'shot_enemy1':8,
    'shot_enemy2': 8,
    'shot_enemy3': 8,
    'shot_enemy4':8}

ENTITY_HEALTH = {
    'level_bg0':999,
    'level_bg1':999,
    'level_bg2':999,
    'level_bg3':999,
    'level_bg4':999,
    'player1': 300,
    'player2': 300,
    'shot_player1': 1,
    'shot_player2': 1,
    'enemy1':50,
    'enemy2':70,
    'enemy3':30,
    'enemy4':25,
    'shot_enemy1':1,
    'shot_enemy2':1,
    'shot_enemy3':1,
    'shot_enemy4':1}

ENTITY_SHOT_DELAY = {'player1': 16, 'player2': 20, 'enemy1':17,'enemy2':15,'enemy3':14, 'enemy4':18}

#M

MENU_OPTIONS = ('NEW GAME 1P','NEW GAME 2P - COOPERATIVE', 'NEW GAME 2P - COMPETITIVE', 'GAME OVER','QUIT')

#P

PLAYER_KEY_UP = {'player1': pygame.K_UP, 'player2' : pygame.K_w}

PLAYER_KEY_DOWN = {'player1': pygame.K_DOWN, 'player2': pygame.K_s}

PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT, 'player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT, 'player2': pygame.K_d}

PLAYER_KEY_SHOT = {'player1':pygame.K_RCTRL,'player2':pygame.K_LCTRL}



PREFIX_DIRECTORY = {'ene':'enemy','pla':'player','lev':'level', 'sho':'shot'}
#S

SPAWN_TIME = 4800

#W
WIN_WIDTH = 576
WIN_HEIGHT = 324
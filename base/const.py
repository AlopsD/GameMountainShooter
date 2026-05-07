
import pygame

#W
WIN_WIDTH = 576
WIN_HEIGHT = 324

#C
C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 255, 0)
C_CYAN = (0, 255, 255)
C_RED = (255, 0, 0)


COUNT_FILE_LEVEL = { 'level1':5,
    'level2':4, 'level3':10, 'level4':4, 'level5':4, 'level6':5, }


#D

DISPLAY_NAME = {
    'level1':'Level 1',
    'level2':'Level 2',
    'level3':'Level 3',
    'level4':'Level 4',
    'level5':'Level 5',
    'level6':'Level 6', }
#E
EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'level_bg0':0,
    'level_bg1':1,
    'level_bg2':2,
    'level_bg3':3,
    'level_bg4':4,
    'level_bg5':4.5,
    'level_bg6':5,
    'level_bg7':5.5,
    'level_bg8':6,
    'level_bg9':6.5,
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
    'level_bg5':999,
    'level_bg6':999,
    'level_bg7':999,
    'level_bg8':999,
    'level_bg9':999,
    'player1': 300,
    'player2': 300,
    'shot_player1': 1,
    'shot_player2': 1,
    'enemy1':50,
    'enemy2':70,
    'enemy3':60,
    'enemy4':55,
    'shot_enemy1':1,
    'shot_enemy2':1,
    'shot_enemy3':1,
    'shot_enemy4':1}

ENTITY_SHOT_DELAY = {'player1': 16, 'player2': 20, 'enemy1':17,'enemy2':15,'enemy3':14, 'enemy4':18}

ENTITY_DAMAGE ={
    'level_bg0':0,
    'level_bg1':0,
    'level_bg2':0,
    'level_bg3':0,
    'level_bg4':0,
    'level_bg5':0,
    'level_bg6':0,
    'level_bg7':0,
    'level_bg8':0,
    'level_bg9':0,
    'player1': 1,
    'player2' : 1,
    'shot_player1': 25,
    'shot_player2': 25,
    'enemy1':1,
    'enemy2':1,
    'enemy3':1,
    'enemy4':1,
    'shot_enemy1':15,
    'shot_enemy2': 15,
    'shot_enemy3': 15,
    'shot_enemy4':15
}

ENTITY_SCORE ={
    'level_bg0':0,
    'level_bg1':0,
    'level_bg2':0,
    'level_bg3':0,
    'level_bg4':0,
    'level_bg5':0,
    'level_bg6':0,
    'level_bg7':0,
    'level_bg8':0,
    'level_bg9':0,
    'player1': 0,
    'player2' : 0,
    'shot_player1': 0,
    'shot_player2': 25,
    'enemy1':40,
    'enemy2':50,
    'enemy3':75,
    'enemy4':100,
    'shot_enemy1':1,
    'shot_enemy2': 1,
    'shot_enemy3': 1,
    'shot_enemy4':1
}

#M

MENU_OPTIONS = ('NEW GAME 1P','NEW GAME 2P - COOPERATIVE', 'NEW GAME 2P - COMPETITIVE', 'SCORE','QUIT')

#P

PLAYER_KEY_UP = {'player1': pygame.K_UP, 'player2' : pygame.K_w}

PLAYER_KEY_DOWN = {'player1': pygame.K_DOWN, 'player2': pygame.K_s}

PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT, 'player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT, 'player2': pygame.K_d}

PLAYER_KEY_SHOT = {'player1':pygame.K_RCTRL,'player2':pygame.K_LCTRL}



PREFIX_DIRECTORY = {
    'enemy1':'enemy',
    'enemy2':'enemy',
    'enemy3':'enemy',
    'enemy4':'enemy',
    'player1' :'player',
    'player2':'player',
    'shot':'shot',
    'level1': 'level/level1',
    'level2': 'level/level2',
    'level3': 'level/level3'}

#S

SPAWN_TIME = 4800
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0:(WIN_WIDTH / 2, 110),
             1:(WIN_WIDTH / 2, 130),
             2:(WIN_WIDTH / 2, 150),
             3:(WIN_WIDTH / 2, 170),
             4:(WIN_WIDTH / 2, 190),
             5:(WIN_WIDTH / 2, 210),
             6:(WIN_WIDTH / 2, 230),
             7:(WIN_WIDTH / 2, 250),
             8:(WIN_WIDTH / 2, 270),
             9:(WIN_WIDTH / 2, 290),
             }
#T

TIMEOUT_STEP = 100 #ms
TIMEOUT_LEVEL = 20000 #ms
#W
#WIN_WIDTH = 576
#WIN_HEIGHT = 324
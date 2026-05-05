import pygame
from base.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from base.level import Level
from base.menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

    def run(self, ):

        while True:

            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[3]]:
                player_score = [0,0]
                level = Level(self.window, 'level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'level2', menu_return, player_score)
                    level_return = level.run(player_score)
            elif menu_return == MENU_OPTIONS[4]:
                pygame.quit()
                quit()
            else:
                pass


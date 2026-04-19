from base.background import Background
from base.const import WIN_WIDTH, WIN_HEIGHT
from base.player import Player


class Entity_factory:

    @staticmethod
    def get_entity(entity_type: str, position = (0,0)):
        match entity_type:
            case 'level_bg':
                list_bg = []
                for i in range (5):
                    list_bg.append(Background('level_bg' + str(i), (0,0)))
                    list_bg.append(Background('level_bg' + str(i), (WIN_WIDTH,0)))
                return list_bg
            case 'player1':
                return  Player('player1', (10, WIN_HEIGHT / 2 - 25))
            case 'player2':
                return  Player('player2', (10, WIN_HEIGHT / 2 + 25))
from base.background import Background
from base.const import WIN_WIDTH


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
from base.entity import Entity


class Level:
    def __init__(self, window, name, game_option):
        self.window = window
        self.name = name
        self.game_mode = game_option
        self.entity_list: list[Entity] = []

    def run(self, ):
        pass
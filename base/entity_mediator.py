from base import enemy_shot
from base.const import WIN_WIDTH
from base.enemy import Enemy
from base.enemy_shot import Enemy_Shot
from base.entity import Entity
from base.player import Player
from base.player_shot import Player_Shot


class Entity_Mediator:

    @staticmethod
    def __verify_collision_window(ent : Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, Player_Shot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, Enemy_Shot):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list(Entity)):
        if enemy.last_damage == 'shot_player1':
            for ent in entity_list:
                if ent.name == 'player1':
                    ent.score += enemy.score

        elif enemy.last_damage == 'shot_player2':
            for ent in entity_list:
                if ent.name == 'player2':
                    ent.score += enemy.score

    @staticmethod
    def __verify_collision_entity(ent_um, ent_dois):
        valid_collision = False
        if isinstance(ent_um, Enemy) and  isinstance(ent_dois, Player_Shot):
            valid_collision = True

        elif isinstance(ent_um, Player_Shot) and isinstance(ent_dois, Enemy):
            valid_collision = True

        elif isinstance(ent_um, Player) and isinstance(ent_dois, Enemy_Shot):
            valid_collision = True

        elif isinstance(ent_um, Enemy_Shot) and isinstance(ent_dois, Player):
            valid_collision = True


        if valid_collision:
            if (ent_um.rect.right >= ent_dois.rect.left and
                    ent_um.rect.left <= ent_dois.rect.right and
                    ent_um.rect.bottom >= ent_dois.rect.top and
                    ent_um.rect.top <= ent_dois.rect.bottom):

                ent_um.health -= ent_dois.damage
                ent_dois.health -= ent_um.damage
                ent_um.last_damage = ent_dois.name
                ent_dois.last_damage = ent_um.name
                pass

    @staticmethod
    def verify_collision(entity_list: list(Entity)):
        for i in range(len(entity_list)):
            entity_um = entity_list[i]
            Entity_Mediator.__verify_collision_window(entity_um)
            for j in range(len(entity_list)):
                entity_dois = entity_list[j]
                Entity_Mediator.__verify_collision_entity(entity_um, entity_dois)

    @staticmethod
    def verify_health(entity_list : list(Entity)):
        for  ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    Entity_Mediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
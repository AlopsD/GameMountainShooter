from base.const import WIN_WIDTH
from base.enemy import Enemy
from base.enemy_shot import Enemy_Shot
from base.entity import Entity
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
    def verify_collision(entity_list: list(Entity)):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            Entity_Mediator.__verify_collision_window(test_entity)


    @staticmethod
    def verify_health(entity_list : list(Entity)):
        for  ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
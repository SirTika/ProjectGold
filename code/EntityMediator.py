from wsgiref.validate import validator

import pygame

from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.Point import Point
from code.const import WIN_HEIGHT, EVENT_ENEMY, EVENT_POINT


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy) or isinstance(ent, Point):
            if ent.rect.top > WIN_HEIGHT:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False

        if isinstance(ent1, Player):
            if isinstance(ent2, Enemy) or isinstance(ent2, Point):
                valid_interaction = True

        if valid_interaction:
            if ent1.rect.colliderect(ent2.rect):
                if isinstance(ent2, Point):
                    ent1.score += 1

                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_damage = ent2.name
                ent2.last_damage = ent1.name

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Player):
                    ent.health = 0
                    for entity in entity_list:
                        entity.speed = 0
                        pygame.time.set_timer(EVENT_ENEMY, 999999)
                        pygame.time.set_timer(EVENT_POINT, 999999)
                entity_list.remove(ent)

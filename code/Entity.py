from abc import ABC, abstractmethod

import pygame.image

from code.const import ENTITY_HEALTH, ENTITY_DAMAGE


class Entity(ABC):
    ENTITY_SCALE = 8

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        original_size = self.surf.get_size()
        self.size = (original_size[0] * self.ENTITY_SCALE, original_size[1] * self.ENTITY_SCALE)
        self.surf = pygame.transform.scale(self.surf, self.size)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_damage = None

    @abstractmethod
    def move(self):
        pass

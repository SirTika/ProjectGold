from abc import ABC, abstractmethod

import pygame.image

from code.const import ENTITY_SCALE


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

    @abstractmethod
    def move(self):
        pass

    def kill(self):
        pass

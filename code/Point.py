import random
import pygame
from code.Entity import Entity
from code.const import ENTITY_SPEED


class Point(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED[self.name]
        self.score_value = 1 if name == 'coin' else 5 if name == 'coin_bag' else 0

    def move(self):
        self.rect.centery += self.speed

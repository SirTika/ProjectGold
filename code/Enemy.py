import random

import pygame

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_HEIGHT, ENTITY_DAMAGE


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.damage = ENTITY_DAMAGE[self.name]
        if self.name == 'shiv':
            self.speed = random.randint(3, 6)
        else:
            self.speed = ENTITY_SPEED[self.name]

    def move(self):
        self.rect.centery += self.speed

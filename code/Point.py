import random
import pygame
from code.Entity import Entity
from code.const import WIN_HEIGHT, ENTITY_SPEED


class Point(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        if self.name == 'coin':
            self.speed = random.randint(5, 9)
        else:
            self.speed = ENTITY_SPEED[self.name]

    def move(self):
        self.rect.centery += self.speed
        if self.rect.top >= WIN_HEIGHT:
            self.rect.top = -self.rect.height
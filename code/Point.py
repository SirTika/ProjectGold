import random
import pygame
from code.Entity import Entity
from code.const import WIN_HEIGHT, ENTITY_SPEED


class Point(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED[self.name]

    def move(self):
        self.rect.centery += self.speed

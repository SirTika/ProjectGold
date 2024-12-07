import random

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_HEIGHT


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        if self.name == 'shiv':
            self.speed = random.randint(5, 9)
        else:
            self.speed = ENTITY_SPEED[self.name]

    def move(self):
        self.rect.centery += self.speed

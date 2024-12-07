import pygame

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_WIDTH


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.original_surf = self.surf
        self.flipped_surf = pygame.transform.flip(self.surf, True, False)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
            self.surf = self.original_surf
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            self.surf = self.flipped_surf

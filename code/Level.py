import pygame.image

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.const import WIN_WIDTH, WIN_HEIGHT


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name

        self.bg_surf = pygame.image.load('./asset/background.png')
        self.bg_surf = pygame.transform.scale(self.bg_surf, (WIN_WIDTH, WIN_HEIGHT))
        self.bg_rect = self.bg_surf.get_rect(left=0, top=0)

        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(''))



    def run(self):
        while True:
            self.window.blit(self.bg_surf, self.bg_rect)
            for entity in self.entity_list:
                entity.move()
                self.window.blit(entity.surf, entity.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
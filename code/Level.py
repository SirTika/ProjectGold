import random
import pygame.image
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.const import WIN_WIDTH, WIN_HEIGHT, EVENT_ENEMY, EVENT_POINT


class Level:

    def __init__(self, window, name):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.bg_surf = pygame.image.load('./asset/background.png')
        self.bg_surf = pygame.transform.scale(self.bg_surf, (WIN_WIDTH, WIN_HEIGHT))
        self.bg_rect = self.bg_surf.get_rect(left=0, top=0)
        self.entity_list = []

        # Criação do jogador
        player = EntityFactory.get_entity('Player')
        if player:
            self.entity_list.append(player)

        # Definindo o tempo de intervalo para o spawn dos inimigos
        pygame.time.set_timer(EVENT_ENEMY, 1300)
        pygame.time.set_timer(EVENT_POINT, 1200)

    def run(self):
        # Música de fundo
        pygame.mixer_music.load('./asset/music.ogg')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            # Mover as entidades
            for entity in self.entity_list:
                entity.move()

            # Desenhar o fundo
            self.window.blit(self.bg_surf, self.bg_rect)

            # Desenhar as entidades
            for entity in self.entity_list:
                self.window.blit(entity.surf, entity.rect)

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # Gerenciar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == EVENT_ENEMY:
                    # Escolher aleatoriamente entre 2 "Shiv" ou 1 "Cannonball"
                    if random.random() < 0.80:  # 80% de chance de 2 "Shiv"
                        for _ in range(2):  # Spawn de 2 "Shiv"
                            self.entity_list.append(EntityFactory.get_entity('Shiv'))
                    else:  # 20% de chance de 1 "Cannonball"
                        self.entity_list.append(EntityFactory.get_entity('Cannonball'))

                if event.type == EVENT_POINT:
                    if random.random() < 0.80:
                        self.entity_list.append(EntityFactory.get_entity('Coin'))
                    else:
                        self.entity_list.append(EntityFactory.get_entity('Coin_Bag'))

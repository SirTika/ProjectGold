import random
import pygame.image
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.const import WIN_WIDTH, WIN_HEIGHT, EVENT_ENEMY, EVENT_POINT, GREEN_4, GREEN_2, GREEN_3


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.bg_surf = pygame.image.load('./asset/background.png')
        self.bg_surf = pygame.transform.scale(self.bg_surf, (WIN_WIDTH, WIN_HEIGHT))
        self.bg_rect = self.bg_surf.get_rect(left=0, top=0)
        self.entity_list = []

        self.player = EntityFactory.get_entity('Player')
        if self.player:
            self.entity_list.append(self.player)

        pygame.time.set_timer(EVENT_ENEMY, 1300)
        pygame.time.set_timer(EVENT_POINT, 1300)

        self.font = pygame.font.Font('./asset/slkscr.ttf', 30)
        self.game_over_font = pygame.font.Font('./asset/slkscr.ttf', 50)

    def run(self):
        pygame.mixer_music.load('./asset/music.ogg')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            if self.player.health <= 0:
                self.player.is_game_over = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == EVENT_ENEMY and not self.player.is_game_over:
                    if random.random() < 0.80:
                        for _ in range(2):
                            self.entity_list.append(EntityFactory.get_entity('Shiv'))
                    else:
                        self.entity_list.append(EntityFactory.get_entity('Cannonball'))

                if event.type == EVENT_POINT and not self.player.is_game_over:
                    if random.random() < 0.90:
                        self.entity_list.append(EntityFactory.get_entity('Coin'))
                    else:
                        self.entity_list.append(EntityFactory.get_entity('Coin_Bag'))

                if self.player.is_game_over and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

            if not self.player.is_game_over:
                for entity in self.entity_list:
                    entity.move()

                EntityMediator.verify_collision(entity_list=self.entity_list)
                EntityMediator.verify_health(entity_list=self.entity_list)

            self.window.blit(self.bg_surf, self.bg_rect)

            for entity in self.entity_list:
                self.window.blit(entity.surf, entity.rect)

            if not self.player.is_game_over:
                score_text = self.font.render(f"Score: {self.player.score}", True, GREEN_3)
                self.window.blit(score_text, (10, 10))
            else:

                game_over_text = self.game_over_font.render("GAME OVER", True, GREEN_4)
                score_text = self.font.render(f"Final Score: {self.player.score}", True, GREEN_3)
                restart_text = self.font.render("Press ENTER to return to menu", True, GREEN_4)

                self.window.blit(game_over_text, game_over_text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2 - 50)))
                self.window.blit(score_text, score_text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2 + 10)))
                self.window.blit(restart_text, restart_text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2 + 70)))

            pygame.display.flip()

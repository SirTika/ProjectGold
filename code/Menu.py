import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, WIN_HEIGHT, TITTLE_WIDTH, TITTLE_HEIGHT, GREEN_4, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window

        #bg image
        self.bg_surf = pygame.image.load('./asset/menu.png')
        self.bg_surf = pygame.transform.scale(self.bg_surf, (WIN_WIDTH, WIN_HEIGHT))
        self.bg_rect = self.bg_surf.get_rect(left = 0, top = 0)

        #title image
        self.tittle_surf = pygame.image.load('./asset/title.png')
        self.tittle_surf = pygame.transform.scale(self.tittle_surf, ((TITTLE_WIDTH, TITTLE_HEIGHT)))
        self.tittle_rect = self.tittle_surf.get_rect(center = (WIN_WIDTH / 2, WIN_HEIGHT / 4))

        #font silkscreen
        self.font_path = './asset/slkscr.ttf'




    def run(self):
        #bg music
        pygame.mixer_music.load('./asset/music.ogg')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(self.bg_surf, self.bg_rect)
            self.window.blit(self.tittle_surf, self.tittle_rect)

            #text
            #self.menu_text(35, "Start Game", (GREEN_4), (180, 420))

            for i in range(len(MENU_OPTION)):
                self.menu_text(35, MENU_OPTION[i], (GREEN_4), (60, 420 + 50 * i))


            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    #text
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font(self.font_path, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft = text_center_pos)
        self.window.blit(source = text_surf, dest = text_rect)
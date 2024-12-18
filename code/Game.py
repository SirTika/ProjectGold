from code.Level import Level
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:  # start game
                level = Level(self.window, 'Level')
                level_return = level.run()
            elif menu_return == MENU_OPTION[1]:  # exit game
                pygame.quit()
                quit()
            else:
                pass

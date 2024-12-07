import random

import pygame

# window size
WIN_WIDTH = 896
WIN_HEIGHT = 736

# title size
TITTLE_WIDTH = 530
TITTLE_HEIGHT = 90

# text color
GREEN_1 = 213, 248, 216
GREEN_2 = 114, 162, 114
GREEN_3 = 32, 89, 72
GREEN_4 = 0, 22, 23

# text menu
MENU_OPTION = ('Start Game',
               'Score',
               'Exit Game')

# entity scale
ENTITY_SCALE = 8

# entity speed
ENTITY_SPEED = {
    'player_idle': 7,
    'shiv': lambda: random.randint(5, 9),
    'cannonball': 4,
    'coin': 7,
    'coin_bag': 10
}

# entity HEALTH
ENTITY_HEALTH = 1

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_POINT = pygame.USEREVENT + 1

ENTITY_SPAWN = (-1 * WIN_HEIGHT)

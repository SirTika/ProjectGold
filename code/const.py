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
               'Exit Game')

# entity scale
ENTITY_SCALE = 8

# entity speed
ENTITY_SPEED = {
    'player_idle': 7,
    'shiv': lambda: random.randint(3, 5),
    'cannonball': 3,
    'coin': 4,
    'coin_bag': 8
}

# entity HEALTH
ENTITY_HEALTH = {
    'player_idle': 1,
    'shiv': 2,
    'cannonball': 2,
    'coin': 1,
    'coin_bag': 1
}

# entity damage
ENTITY_DAMAGE = {
    'player_idle': 1,
    'shiv': 1,
    'cannonball': 1,
    'coin': 0,
    'coin_bag': 0
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_POINT = pygame.USEREVENT + 1

ENTITY_SPAWN_HEIGHT = (-100)

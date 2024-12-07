import random

from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.Point import Point
from code.const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPAWN


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Player':
                return Player('player_idle', ((WIN_WIDTH / 2) - 64, 545))
            case 'Shiv':
                return Enemy('shiv', (random.randint(0, 866),ENTITY_SPAWN))
            case 'Cannonball':
                return Enemy('cannonball', (random.randint(0, 786),ENTITY_SPAWN))
            case 'Coin':
                return Point('coin', (random.randint(0, 866),ENTITY_SPAWN))
            case 'Coin_Bag':
                return Point('coin_bag', (random.randint(0, 786),ENTITY_SPAWN))
            case _:
                return None

from code.Entity import Entity


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position = (0, 0)):
        match entity_name:
            case 'Level1':
                return [Entity(name='player_idle', position = (100, 100))]
            case _:
                return[]
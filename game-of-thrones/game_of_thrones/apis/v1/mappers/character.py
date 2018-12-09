from kim import field

from .base import BaseMapper

from game_of_thrones.models import Character


class CharacterMapper(BaseMapper):

    __type__ = Character

    name = field.String()

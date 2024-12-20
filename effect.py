from classes import *
from role import *
from battle import *

class Effect:
    name : str
    def __init__(self, name : str) -> None:
        self.name = name
    def happens(self, battle : Battle) -> None:
        pass

class RoleEffect(Effect):
    def canHappen(self, battle : Battle) -> bool:
        return True

class RedHeroEffect(RoleEffect):
    def canHappen(self, battle : Battle) -> bool:
        return battle.red.hero.canBeSelected()
    def happens(self, battle : Battle) -> None:
        pass

class BlueHeroEffect(RoleEffect):
    def canHappen(self, battle : Battle) -> bool:
        return battle.blue.hero.canBeSelected()
    def happens(self, battle : Battle) -> None:
        pass

class RedMinionEffect(RoleEffect):
    pass
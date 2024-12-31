from classes import *
from role import *
from battle import *

class Effect:
    name : str
    def __init__(self, name : str) -> None:
        self.name = name
        return
    def canHappen(self, battle : Battle) -> bool:
        return True
    pass

class HeroEffect(Effect):
    name : str
    isred : bool
    def __init__(self, name : str, isred : bool) -> None:
        super(HeroEffect, self).__init__(name)
        self.isred = isred
        return
    def canHappen(self, battle : Battle) -> bool:
        if self.isred:
            return battle.red.hero.canBeSelected()
        else:
            return battle.blue.hero.canBeSelected()

class MinionsEffect(Effect):
    name : str
    isred : bool
    number : int
    def __init__(self, name : str, isred : bool, number : int) -> None:
        super(MinionsEffect, self).__init__(name)
        self.isred = isred
        self.number = number
        return
    def canHappen(self, battle : Battle, roles : list[Role]) -> bool:
        # 检查是否能对指定的角色产生影响的代码应在外部实现；原则上，一定存在一种对角色的选择使其合法。
        return True

class BattleEffect(Effect):
    name : str
    def __init__(self, name : str) -> None:
        self.name = name
from role import *

class Effect:
    name : str
    def __init__(self, name : str) -> None:
        self.name = name
        return
    def canHappen(self) -> bool:
        return True
    def happens(self) -> None:
        return
    pass

class HeroEffect(Effect):
    name : str
    isred : bool
    def __init__(self, name : str, isred : bool) -> None:
        Effect.__init__(self, name)
        self.isred = isred
        return
    def canHappen(self, hero : Role) -> bool:
        return hero.canBeSelected()
    def happens(self, hero : Role) -> None:
        return

class MinionsEffect(Effect):
    name : str
    isred : bool
    number : int
    def __init__(self, name : str, isred : bool, number : int) -> None:
        Effect.__init__(self, name)
        self.isred = isred
        self.number = number
        return
    def canHappen(self, roles : list[Role]) -> bool:
        # 检查是否能对指定的角色产生影响的代码应在外部实现；原则上，一定存在一种对角色的选择使其合法。
        return True
    def happens(self, roles : list[Role]) -> None:
        return

class DeckEffect(Effect):
    name : str
    def __init__(self, name : str) -> None:
        Effect.__init__(self, name)
    def canHappen(self, reddeck : list[object], bluedeck : list[object]) -> bool:
        return True
    def happens(self, reddeck : list[object], bluedeck : list[object]) -> None:
        reddeck.append(1)
        return
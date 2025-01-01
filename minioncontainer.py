# MinionContainer 初代代码，仅用于测试effect。待后期完善.
from minion import *

class MinionContainer:
    minions : list[Minion]
    def __init__(self, minions : list[Minion] = []) -> None:
        self.minions = minions
        return
    def add(self, minions : list[Minion]) -> None:
        self.minions = self.minions + minions
        return 
    def delete(self, minions : list[Minion]) -> bool:
        for minion in minions:
            if minion in self.minions:
                self.minions.remove(minion)
                minions.remove(minion)
        return len(minions)
from classes import *
from effect import *

class EffectContainer:
    name : str
    effects : list[Effect]
    def __init__(self, name: str, effects: list[Effect]) -> None:
        self.name = name
        self.effects = effects
    def canHappen(self, battle : Battle) -> bool:
        flag : bool = True
        for effect in self.effects:
            flag = flag and effect.canHappen(battle)
            if not flag:
                break
        return flag
    def happen(self) -> None:
        for effect in self.effects:
            effect.happen(battle)
            return
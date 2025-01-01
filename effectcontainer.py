from effect import *

class EffectContainer:
    name : str
    effects : list[Effect]
    def __init__(self, name: str, effects: list[Effect]) -> None:
        self.name = name
        self.effects = effects
    def canHappen(self, redhero : Role, bluehero : Role, redminions : list[Role], blueminions : list[Role], reddeck : list[object], bluedeck : list[object]) -> bool:
        flag : bool = True
        for effect in self.effects:
            if isinstance(effect, HeroEffect):
                if effect.isred:
                    flag = flag and effect.canHappen(redhero)
                else:
                    flag = flag and effect.canHappen(bluehero)
            elif isinstance(effect, MinionsEffect):
                if effect.isred:
                    flag = flag and effect.canHappen(redminions)
                else:
                    flag = flag and effect.canHappen(blueminions)
            elif isinstance(effect, DeckEffect):
                effect.canHappen(reddeck, bluedeck)
            if not flag:
                break
        return flag
    def happens(self, redhero : Role, bluehero : Role, redminions : list[Role], blueminions : list[Role], reddeck : list[object], bluedeck : list[object]) -> None:
        for effect in self.effects:
            if isinstance(effect, HeroEffect):
                if effect.isred:
                    effect.happens(redhero)
                else:
                    effect.happens(bluehero)
            elif isinstance(effect, MinionsEffect):
                if effect.isred:
                    effect.happens(redminions)
                else:
                    effect.happens(blueminions)
            elif isinstance(effect, DeckEffect):
                effect.happens(reddeck, bluedeck)
        return
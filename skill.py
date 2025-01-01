from effectcontainer import *

class Skill(EffectContainer):
    def __init__(self, name: str, effects: list[Effect]) -> None:
        EffectContainer.__init__(self, name, effects)
        return
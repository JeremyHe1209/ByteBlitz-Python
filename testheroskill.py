from effect import *
from skill import *

class TestHeroEffect1(HeroEffect):
    pass
class TestHeroEffect2(MinionsEffect):
    pass
class TestHeroEffect3(BattleEffect):
    pass

class TestHeroSkill(Skill):
    def __init__(self) -> None:
        Skill.__init__(self, "testheroskill", [TestHeroEffect1(), TestHeroEffect2(), TestHeroEffect3()])
        return
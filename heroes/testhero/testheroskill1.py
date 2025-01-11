from effect import *
from skill import *

class TestHeroEffect1(HeroEffect):
    pass
class TestHeroEffect2(MinionsEffect):
    pass
class TestHeroEffect3(DeckEffect):
    pass

class TestHeroSkill1(Skill):
    def __init__(self) -> None:
        Skill.__init__(self, "TestHeroSkill1", [TestHeroEffect1("TestHeroEffect1", True), TestHeroEffect2("TestHeroEffect2", True, 1), TestHeroEffect3("TestHeroEffect3")])
        return
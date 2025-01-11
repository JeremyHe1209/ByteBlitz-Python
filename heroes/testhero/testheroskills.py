from skillcontainer import *
from testheroskill1 import TestHeroSkill1
from testheroskill2 import TestHeroSkill2
from testheroskill3 import TestHeroSkill3

class TestHeroSkills(SkillContainer):
    def __init__(self) -> None:
        SkillContainer.__init__(self, [TestHeroSkill1(), TestHeroSkill2(), TestHeroSkill3()])
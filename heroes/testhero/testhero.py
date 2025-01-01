import sys
sys.path.append('.')
from hero import *
from testheroskill import TestHeroSkill

class TestHero(Hero):
    def __init__(self) -> None:
        Hero.__init__(self, "testhero", 1, 1, 1, 1, [], Mood(), Ability(), TestHeroSkill())
        return
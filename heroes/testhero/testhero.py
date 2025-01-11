import sys
sys.path.append('.')
from hero import *
from testheroskills import TestHeroSkills

class TestHero(Hero):
    def __init__(self) -> None:
        Hero.__init__(self, "testhero", 1, 1, 1, 1, FigureContainer(), Mood(), Ability(), TestHeroSkills())
        return
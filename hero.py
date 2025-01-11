from role import *
from figurecontainer import *
from mood import *
from ability import *
from skillcontainer import *

class Hero(Role):
    skills : SkillContainer
    def __init__(
        self,
        name: str,
        legalattacktimes: int,
        attack: int,
        health: int,
        roleid: int,
        figures: FigureContainer,
        mood : Mood,
        ability : Ability,
        skills : SkillContainer
    ) -> None:
        Role.__init__(self, name, legalattacktimes, attack, health, roleid, figures, mood, ability)
        self.skills = skills
        self.ahstates.insert([self.ability.getBuff()])
        return
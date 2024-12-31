from classes import *
from role import *
from mood import *
from ability import *
from skill import *

class Hero(Role):
    mood : Mood
    ability : Ability
    skill : Skill
    def __init__(
        self,
        name: str,
        legalattacktimes: int,
        attack: int,
        health: int,
        roleid: int,
        newfigures: list[str],
        mood : Mood,
        ability : Ability,
        skill : Skill
    ) -> None:
        Role.__init__(self, name, legalattacktimes, attack, health, roleid, newfigures)
        self.mood = mood
        self.ability = ability
        self.skill = skill
        self.buffcontainer.insert(self.ability.getBuff())
        return
    def updateAbility(self, abilities: dict[str, int]) -> None:
        self.buffcontainer.remove("abilitybuff")
        self.ability.update(abilities)
        self.buffcontainer.insert(self.ability.getBuff())
        return
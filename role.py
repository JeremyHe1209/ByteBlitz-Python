from buffcontainer import *
from figurecontainer import *
from mood import *
from ability import *

class Role:
    name: str = ""
    legalattacktimes: int = 0
    ahstates: BuffContainer = BuffContainer([])
    roleid: int = 0
    isdead: bool = 0
    figures: FigureContainer = FigureContainer()
    mood : Mood
    ability : Ability
    def __init__(self, name: str, legalattacktimes: int, attack: int, health: int, roleid: int, figures: FigureContainer, mood : Mood, ability : Ability) -> None:
        self.name = name
        self.legalattacktimes = legalattacktimes
        self.ahstates = BuffContainer([Buff(attack, health, False, "initahpair")])
        self.roleid = roleid
        self.isdead = False
        self.figures = figures
        self.mood = mood
        self.ability = ability
        return
    def die(self) -> None:
        self.isdead = True
        # To do
        return
    def update(self, attackdiff: int, healthdiff: int) -> None:
        self.ahstates.update(attackdiff, healthdiff)
        if self.ahstates.total.health == 0:
            self.die()
        return
    def updateAbility(self, abilities: dict[str, int]) -> None:
        self.ahstates.remove(["abilitybuff"])
        self.ability.update(abilities)
        self.ahstates.insert([self.ability.getBuff()])
        return

from classes import *
from buff import *

class Score:
    score: int = 0
    grade: int = 0
    scoretograde: list[int] = []
    gradetobuff: list[Buff] = {}
    name: str = ""
    buffname: str = ""
    def __init__(self, name: str) -> None:
        self.score = 0
        self.grade = 0
        self.scoretograde = []
        self.name = name
        self.buffname = name + "attacktimetemporarybuff"
        for i in range(3):
            self.scoretograde.append(0)
        for i in range(2):
            self.scoretograde.append(1)
        for i in range(2):
            self.scoretograde.append(2)
        for i in range(3):
            self.scoretograde.append(3)
        for i in range(5):
            self.scoretograde.append(4)
        self.gradetobuff = [
            Buff(0, 0, True, self.buffname), Buff(1, 0, True, self.buffname),
            Buff(2, 1, True, self.buffname), Buff(3, 2, True, self.buffname),
            Buff(4, 4, True, self.buffname), Buff(6, 6, True, self.buffname)
        ]
        return
    def getBuff(self) -> Buff:
        buff = self.gradetobuff[self.grade]
        return Buff(buff.attack, buff.health, buff.isTemporary, buff.name)
    def updateGrade(self) -> None:
        if self.score >= 15:
            self.grade = 5
        self.grade = self.scoretograde[self.score]
        return
    def update(self, diff: int) -> None:
        self.score += diff
        if self.score < 0:
            self.score = 0
        self.updateGrade()
        return

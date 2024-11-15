from buff import *

class Score:
    score: int = 0
    grade: int = 0
    scoretograde: [int] = []
    gradetobuff: [Buff] = {}
    name: str = ""
    def __init__(self, name) -> None:
        self.score = 0
        self.grade = 0
        self.name = name
        self.scoretograde = []
        for i in range(2):
            self.scoretograde.append(0)
        for i in range(2):
            self.scoretograde.append(1)
        for i in range(3):
            self.scoretograde.append(2)
        for i in range(3):
            self.scoretograde.append(3)
        for i in range(5):
            self.scoretograde.append(4)
        self.gradetobuff = [
            Buff(0, 0),
            Buff(1, 0),
            Buff(2, 1),
            Buff(3, 2),
            Buff(4, 4),
            Buff(6, 6)
        ]
        return
    def getBuff(self) -> Buff:
        return self.gradetobuff[self.grade]
    def updateGrade(self) -> None:
        if self.score >= 15:
            self.grade = 5
        self.grade = self.scoretograde[self.grade]
        return
    def update(self, diff: int) -> None:
        self.score += diff
        if self.score < 0:
            self.score = 0
        self.updateGrade()
        return

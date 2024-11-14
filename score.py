from ahpair import *

class Score:
    score: int = 0
    grade: int = 0
    scoretograde: [int] = []
    gradetobuff: [AHPair] = {}
    name: str = ""
    buffname: str = ""
    def __init__(self, name: str) -> None:
        self.score = 0
        self.grade = 0
        self.scoretograde = []
        self.name = name
        self.buffname = name + "temratebuff"
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
            AHPair(0, 0, True, self.buffname),
            AHPair(1, 0, True, self.buffname),
            AHPair(2, 1, True, self.buffname),
            AHPair(3, 2, True, self.buffname),
            AHPair(4, 4, True, self.buffname),
            AHPair(6, 6, True, self.buffname)
        ]
        return
    def getBuff(self) -> AHPair:
        return self.gradetobuff[self.grade]
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

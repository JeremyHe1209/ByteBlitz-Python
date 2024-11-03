class Score:
    score: int = 0
    grade: int = 0
    scoretograde: [int] = []
    gradetobuff: [[int]] = {}
    def __init__(self) -> None:
        self.score = 0
        self.grade = 0
        self.scoretograde = []
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
            [0, 0], [1, 0], [2, 1],
            [3, 2], [4, 4], [6, 6]
        ]
        return
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

from classes import *
from score import *

class Ability:
    k: float = 0
    limit: float = 0
    value: float = 0
    abilities: dict[str, bool] = {}
    keys: list[str] = []
    def __init__(self) -> None:
        self.k = 0
        self.limit = 0
        self.keys = ["Search", "DP", "String", "Math", "DS", "Graph", "Geometry", "Misc"]
        self.abilities = {}
        for key in self.keys:
            self.abilities[key] = Score(key)
        return
    def updateValue(self) -> None:
        sumabilities: int = 0
        sumpowerdiff: float = 0
        for key in self.keys:
            sumabilities += self.abilities[key].score
            if self.abilities[key].score < self.limit:
                sumpowerdiff -= (self.abilities[key].score - self.limit) ** 2
            else:
                sumpowerdiff += (self.abilities[key].score - self.limit) ** 2
        self.value = self.k * sumabilities + sumpowerdiff
        return
    def update(self, abilities: dict[str, int]) -> bool:
        flag: bool = False
        for key in abilities.keys():
            if key not in self.keys:
                flag = True
            else:
                self.abilities[key].update(abilities[key])
        self.updateValue()
        return flag
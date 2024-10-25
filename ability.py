class Ability:
    k: float = 0
    lmt: float = 0
    abilities: {str: int} = {}
    keys: [str] = []
    def __init__(self) -> None:
        self.k = 0
        self.lmt = 0
        self.keys = ["Search", "DP", "String", "Math", "DS", "Graph", "Geometry", "Misc"]
        self.abilities = {}
        for key in self.keys:
            self.abilities[key] = 0
        return
    def update(self, keys: [str] = [], diff: [int] = []) -> bool:
        flag: bool = False
        for ind in range(len(keys)):
            key: int = keys[ind]
            if key in self.keys:
                self.abilities[key] += diff[ind]
                if self.abilities[key] < 0:
                    self.abilities[key] = 0
            else:
                flag = True
        return flag
    def getValue(self) -> float:
        sumabilities: int = 0
        sumpowerdiff: float = 0
        for key in self.keys:
            sumabilities += self.abilities[key]
            if self.abilities[key] < self.lmt:
                sumpowerdiff -= (self.abilities[key] - self.lmt) ** 2
            else:
                sumpowerdiff += (self.abilities[key] - self.lmt) ** 2
        return self.k * sumabilities + sumpowerdiff
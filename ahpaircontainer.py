from ahpair import *

class AHPairContainer:
    attack: int = 0
    health: int = 0
    temrateahpairs: [AHPair] = []
    intemrateahpairs: [AHPair] = []
    def __init__(self, ahpairs: [AHPair]) -> None:
        self.attack = 0
        self.health = 0
        self.temrateahpairs = []
        self.intemrateahpairs = []
        self.insert(ahpairs)
        return
    def insert(self, newahpairs: [AHPair]) -> None:
        for newahpair in newahpairs:
            self.attack += newahpair.attack
            self.health += newahpair.health
            if newahpair.isTemerate:
                temrateahpairs.append(newahpair)
            else:
                intemrateahpairs.append(newahpair)
        return
    def remove(self, names: [str]) -> None:
        for temrateahpair in self.temrateahpairs:
            if temrateahpair.name in names:
                self.attack -= temrateahpair.attack
                self.health -= temrateahpair.health
                self.temrateahpairs.remove(temrateahpair)
        return
    def update(self, attackdiff: int, healthdiff: int) -> None:
        if attackdiff < 0:
            for i in range(len(self.temrateahpairs)):
                if attackdiff + self.temrateahpairs[i].attack >= 0:
                    self.temrateahpair[i].attack += attackdiff
                    attackdiff = 0
                    break
                attack += self.temrateahpair[i].attack
                self.temrateahpair[i].attack = 0
        if attackdiff < 0:
            for i in range(len(self.intemrateahpairs)):
                if attackdiff + self.intemrateahpairs[i].attack >= 0:
                    self.intemrateahpair[i].attack += attackdiff
                    attackdiff = 0
                    break
                attack += self.intemrateahpair[i].attack
                self.intemrateahpair[i].attack = 0
        if attackdiff < 0:
            attackdiff = 0
        if healthdiff < 0:
            for i in range(len(self.temrateahpairs)):
                if healthdiff + self.temrateahpairs[i].health >= 0:
                    self.temrateahpair[i].health += healthdiff
                    healthdiff = 0
                    break
                health += self.temrateahpair[i].health
                self.temrateahpair[i].health = 0
        if healthdiff < 0:
            for i in range(len(self.intemrateahpairs)):
                if healthdiff + self.intemrateahpairs[i].health >= 0:
                    self.intemrateahpair[i].health += healthdiff
                    healthdiff = 0
                    break
                health += self.intemrateahpair[i].health
                self.intemrateahpair[i].health = 0
        if healthdiff < 0:
            healthdiff = 0
        self.insert(AHPair(attackdiff, healthdiff, False, "intemeratebuff"))
        return

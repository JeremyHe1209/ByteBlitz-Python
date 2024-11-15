from ahpair import *

class AHPairContainer:
    total: AHPair
    decreaselazy: AHPair
    temrateahpairs: [AHPair] = []
    intemrateahpairs: [AHPair] = []
    def __init__(self, ahpairs: [AHPair]) -> None:
        self.total = AHPair(0, 0, False, "total")
        self.decreaselazy = AHPair(0, 0, False, "total")
        self.temrateahpairs = []
        self.intemrateahpairs = []
        self.insert(ahpairs)
        return
    def insert(self, newahpairs: [AHPair]) -> None:
        for newahpair in newahpairs:
            self.total.attack += newahpair.attack
            self.total.health += newahpair.health
            if newahpair.isTemerate:
                temrateahpairs.append(newahpair)
            else:
                intemrateahpairs.append(newahpair)
        return
    def remove(self, names: [str]) -> None:
        for temrateahpair in self.temrateahpairs:
            if temrateahpair.name in names:
                self.temrateahpairs.remove(temrateahpair)
                if self.decreaselazy.attack + temrateahpair.attack < 0:
                    self.decreaselazy.attack += temrateahpair.attack
                    temrateahpair.attack = 0
                else:
                    temrateahpair.attack += self.decreaselazy.attack
                    self.decreaselazy.attack = 0
                if self.decreaselazy.health + temrateahpair.health < 0:
                    self.decreaselazy.health += temrateahpair.health
                    temrateahpair.health = 0
                else:
                    temrateahpair.health += self.decreaselazy.health
                    self.decreaselazy.health = 0
                self.total.attack -= temrateahpair.attack
                self.total.health -= temrateahpair.health
        return
    def update(self, attackdiff: int, healthdiff: int) -> None:
        if attackdiff + self.total.attack < 0:
            attackdiff = -self.total.attack
        if healthdiff + self.total.health < 0:
            healthdiff = -self.total.health
        self.total.attack += attackdiff
        self.total.health += healthdiff
        if attackdiff < 0:
            self.decreaselazy.attack += attackdiff
            attackdiff = 0
        if healthdiff < 0:
            self.decreaselazy.health += healthdiff
            healthdiff = 0
        self.insert(AHPair(attackdiff, healthdiff, False, "intemperatebuff"))
        return

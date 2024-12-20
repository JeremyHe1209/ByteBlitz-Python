from classes import *
from buff import *

class BuffContainer:
    total: Buff = Buff(0, 0, False, "total")
    decreaselazy: Buff = Buff(0, 0, False, "decreaselazy")
    temporarybuffs: list[Buff] = []
    lastingbuffs: list[Buff] = []
    def __init__(self, buffs: list[Buff]) -> None:
        self.total = Buff(0, 0, False, "total")
        self.decreaselazy = Buff(0, 0, False, "decreaselazy")
        self.temporarybuffs = []
        self.lastingbuffs = []
        self.insert(buffs)
        return
    def insert(self, newbuffs: list[Buff]) -> None:
        for newbuff in newbuffs:
            self.total.attack += newbuff.attack
            self.total.health += newbuff.health
            if newbuff.isTemporary:
                self.temporarybuffs.append(newbuff)
            else:
                self.lastingbuffs.append(newbuff)
        return
    def remove(self, names: list[str]) -> None:
        removeindexes: list[int] = []
        for ind in range(len(self.temporarybuffs)):
            if self.temporarybuffs[ind].name in names:
                temporarybuff: Buff = Buff(0, 0, True, "")
                temporarybuff.attack = self.temporarybuffs[ind].attack
                temporarybuff.health = self.temporarybuffs[ind].health
                temporarybuff.name = self.temporarybuffs[ind].name
                removeindexes.append(ind)
                if self.decreaselazy.attack + temporarybuff.attack < 0:
                    self.decreaselazy.attack += temporarybuff.attack
                    temporarybuff.attack = 0
                else:
                    temporarybuff.attack += self.decreaselazy.attack
                    self.decreaselazy.attack = 0
                if self.decreaselazy.health + temporarybuff.health < 0:
                    self.decreaselazy.health += temporarybuff.health
                    temporarybuff.health = 0
                else:
                    temporarybuff.health += self.decreaselazy.health
                    self.decreaselazy.health = 0
                self.total.attack -= temporarybuff.attack
                self.total.health -= temporarybuff.health
        for ind in range(len(removeindexes)):
            self.temporarybuffs.pop(removeindexes[ind] - ind)
        return
    def update(self, attackdiff: int, healthdiff: int) -> None:
        if attackdiff + self.total.attack < 0:
            attackdiff = -self.total.attack
        if healthdiff + self.total.health < 0:
            healthdiff = -self.total.health
        if attackdiff < 0:
            self.total.attack += attackdiff
            self.decreaselazy.attack += attackdiff
            attackdiff = 0
        if healthdiff < 0:
            self.total.health += healthdiff
            self.decreaselazy.health += healthdiff
            healthdiff = 0
        self.insert([Buff(attackdiff, healthdiff, False, "lastingbuff")])
        return

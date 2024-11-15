from ahpaircontainer import *

class Role:
    legalattacktimes: int = 0
    ahstates: AHPairContainer = AHPairContainer([])
    roleid: int = 0
    isdead: bool = 0
    keys: [str] = []
    figures: {str : bool} = {}
    def __init__(self, legalattacktimes: int, attack: int, health: int, roleid: int, newfigures: [str]) -> None:
        self.legalattacktimes = legalattacktimes
        self.ahstates = AHPairContainer([AHPair(attack, health, False, "initahpair")])
        self.roleid = roleid
        self.isdead = False
        self.keys = ["hero", "defensive", "firewall", "hidden", "debug"]
        self.figures = {}
        for key in self.keys:
            self.figures[key] = False
        self.giveFigures(newfigures)
        return
    def update(self, attackdiff: int, healthdiff: int) -> None:
        self.ahstates.update(attackdiff, healthdiff)
        if self.ahstates.total.health == 0:
            self.isdead = True
        return
    def giveFigures(self, newfigures: [str]) -> bool:
        flag: bool = False
        for newfigure in newfigures:
            if newfigure in self.figures:
                self.figures[newfigure] = True
            else:
                flag = True
        return flag

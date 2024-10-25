class Role:
    legalattacktimes: int = 0
    attack: int = 0
    health: int = 0
    roleid: int = 0
    isdead: bool = 0
    keys: [str] = []
    figures: {str : bool} = {}
    def __init__(self, legalattacktimes: int, attack: int, health: int, roleid: int, newfigures: [str]) -> None:
        self.legalattacktimes = legalattacktimes
        self.attack = attack
        self.health = health
        self.roleid = roleid
        self.isdead = False
        self.keys = ["hero", "defensive", "firewall", "hidden", "debug"]
        self.figures = {}
        for key in self.keys:
            self.figures[key] = False
        self.giveFigures(newfigures)
        return
    def update(self, attackdiff: int, healthdiff: int) -> None:
        self.attack += attackdiff
        self.health += healthdiff
        if self.attack < 0:
            self.attack = 0
        if self.health < 0:
            self.health = 0
            self.isdead = False
        return
    def giveFigures(self, newfigures: [str]) -> bool:
        flag: bool = False
        for newfigure in newfigures:
            if newfigure in self.figures:
                self.figures[newfigure] = True
            else:
                flag = True
        return flag
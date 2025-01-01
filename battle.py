from team import *

class Battle:
    red : Team # self
    blue : Team
    def __init__(self, redhero : Hero, bluehero : Hero) -> None:
        self.red = Team(redhero)
        self.blue = Team(bluehero)
        return
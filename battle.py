from classes import *
from team import *

class Battle:
    red : Team # self
    blue : Team
    def __init__(self) -> None:
        self.red = Team()
        self.blue = Team()
        return
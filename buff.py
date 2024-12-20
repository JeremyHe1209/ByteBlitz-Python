from classes import *

class Buff:
    attack: int = 0
    health: int = 0
    istemporary: bool = False
    name: str = ""
    def __init__(self, attack: int, health: int, istemporary: bool, name: str) -> None:
        self.attack = attack
        self.health = health
        self.istemporary = istemporary
        self.name = name
        return

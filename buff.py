class Buff:
    health: int
    attack: int
    def __init__(self, health: int, attack: int) -> None:
        self.health = health
        self.attack = attack
        return
    def __add__(self, other):
        return Buff(self.health + other.health, self.attack + other.attack)

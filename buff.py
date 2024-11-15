class Buff:
    attack: int = 0
    health: int = 0
    isTemporary: bool = False
    name: str = ""
    def __init__(self, attack: int, health: int, isTemporary: bool, name: str) -> None:
        self.attack = attack
        self.health = health
        self.isTemporary = isTemporary
        self.name = name
        return

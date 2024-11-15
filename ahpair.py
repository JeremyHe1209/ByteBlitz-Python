class AHPair:
    attack: int = 0
    health: int = 0
    isTemperate: bool = False
    name: str = ""
    def __init__(
        self, attack: int, health: int, isTemerate: int, name: str
    ) -> None:
        self.attack = attack
        self.health = health
        self.isTemerate = isTemerate
        self.name = name
        return

class AHPair:
    attack: int = 0
    health: int = 0
    istemporary: bool = False
    name: str = ""
    def __init__(self, attack: int, health: int, istemporary: int, name: str) -> None:
        self.attack = attack
        self.health = health
        self.istemporary = istemporary
        self.name = name
        return

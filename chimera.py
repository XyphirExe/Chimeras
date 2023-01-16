from attack import Attack
from ability import Ability

class Chimera:

    def __init__(self, health: int, attacks:list[Attack, Attack, Attack, Attack], ability: Ability) -> None:
        self.sprite = None
        self.health = health
        self.attack
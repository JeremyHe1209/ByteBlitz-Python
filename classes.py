class Buff:
    pass
class BuffContainer:
    pass
class Role:
    pass
class Effect:
    pass
class Score:
    pass
class Ability:
    pass
class Mood:
    pass
class Skill:
    pass
class Card:
    pass
class Minion(Role):
    pass
class MagicCard(Card):
    pass
class MinionCard(Card, Minion):
    pass
class CardContainer:
    pass
class CardGroup(CardContainer):
    pass
class Hand(CardContainer):
    pass
class Deck(CardContainer):
    pass
class CardPair:
    pass
class CardPairContainer:
    pass
class CardLibrary(CardPairContainer):
    pass
class MinionContainer:
    pass
class Fray(MinionContainer):
    pass
class Team:
    pass
class Battle:
    pass
class Hero(Role):
    pass
class HeroContainer:
    pass
class HeroLibrary(HeroContainer):
    pass
class Player:
    pass
class Game:
    pass

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Union, Dict, Any, Tuple, Type, Set, Callable
import random

# < =======================================================
# < 
# < =======================================================

class Game:

    events = []
    players = []
    enemies = []
    rules = []
    
    def handle_event(self, event: str, *args, **kwargs) -> None:
        if hasattr(self, f"on_{event}"):
            getattr(self, f"on_{event}")(*args, **kwargs)

    def add_rule(self, rule: PlayabilityCondition) -> None:
        if rule not in self.rules:
            self.rules.append(rule)

    def can_play_card(self, player: Player, card: Card, target: Optional[Union[Player, Enemy]] = None) -> PlayabilityResult:
        result = PlayabilityResult(playable = True)
        for rule in self.rules:
            rule_result = rule.check(player, card, target)
            if not rule_result.playable:
                result.playable = False
                result.reasons.extend(rule_result.reasons)
        for rule in player.rules:
            rule_result = rule.check(player, card, target)
            if not rule_result.playable:
                result.playable = False
                result.reasons.extend(rule_result.reasons)
        for rule in card.rules:
            rule_result = rule.check(player, card, target)
            if not rule_result.playable:
                result.playable = False
                result.reasons.extend(rule_result.reasons)
        return result

    def process_events(self) -> None:
        while self.events:
            event = self.events.pop(0)
            self.handle_event(event.name, *event.args, **event.kwargs)

class Entity(ABC):
    rules: List[PlayabilityCondition] = []

class Event:
    def __init__(self, name: str = "", args: Optional[List[Any]] = None, kwargs: Optional[Dict[str, Any]] = None) -> None:
        self.name = name
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}

class Card:

    rules: List[PlayabilityCondition] = []

class Potion:
    pass

class Player(Entity):


    def emit(self, name: str, *args, **kwargs) -> None:
        event = Event(name = name, args = args, kwargs = kwargs)

class Enemy(Entity):
    pass

class Effect(ABC):
    pass

class PlayabilityResult:
    def __init__(self, playable: bool, reasons: list[str]) -> None:
        self.playable = playable
        self.reasons = reasons or []
    
    def add_restriction(self, reason: str) -> None:
        self.playable = False
        self.reasons.append(reason)
    
class PlayabilityCondition(ABC):
    @abstractmethod
    def check(self, player: Player, card: Card, target: Optional[Union[Player, Enemy]] = None) -> PlayabilityResult:
        pass

class CostCondition(PlayabilityCondition):
    def check(self, player: Player, card: Card, target: Optional[Union[Player, Enemy]] = None) -> PlayabilityResult:
        result = PlayabilityResult(playable = True)
        if player.mana < card.cost:
            result.add_restriction("Not enough mana")
        return result

class CardTypeCondition(PlayabilityCondition):
    def __init__(self, card_type: str) -> None:
        self.card_type = card_type

    def check(self, player: Player, card: Card, target: Optional[Union[Player, Enemy]] = None) -> PlayabilityResult:
        result = PlayabilityResult(playable = True)
        if card.type != self.card_type:
            result.add_restriction(f"Card type must be {self.card_type}")
        return result

game = Game()
game.add_rule(CostCondition())

player = Player()
player.name = "Player One"
player.health = 20
player.mana = 10
player.deck = []

enemy = Enemy()
enemy.name = "Enemy One"
enemy.health = 15
enemy.rules.append(CardTypeCondition("Spell"))

card = Card()
card.name = "Test Card"
card.description = "This is a test card"
card.cost = 1
card.type = "Spell"
card.rarity = "Common"
card.power = 2
card.effects = []
card.rules.append()

effect = Effect()
effect.name = "Test Effect"
effect.description = "This is a test effect"
effect.type = "Damage"
effect.value = 3
effect.target = "Enemy"

card.effects.append(effect)
player.deck.append(card)
game.players.append(player)
game.enemies.append(enemy)

def main() -> None:
    while True:
        player = game.players[0]
        enemy = game.enemies[0]
        card = player.deck[0]
        result = game.can_play_card(player, card, enemy)
        if result.playable:
            print(f"{player.name} can play {card.name} on {enemy.name}.")
            player.emit("play_card", card, enemy)
        else:
            print(f"{player.name} cannot play {card.name} on {enemy.name}: {', '.join(result.reasons)}.")

if __name__ == "__main__":
    main()
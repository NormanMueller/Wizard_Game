from typing import Dict, List, Type
from cards import Cards


class Player:
    def __init__(self, name: str, position: int):
        self.name: str = name
        self.cards: Type[Cards] = []
        self.guess: int = 0
        self.card_in_play: Type[Cards] = None
        self.winning_rounds: int = 0
        self.points: int = 0
        self.position: int = position

    def draw_cards(self, turn: int, cards: Type[Cards]):
        try:
            self.cards = [next(cards) for i in range(turn)]
        except StopIteration:
            cards.generator_itam = cards.generator()
            self.cards = [next(cards) for i in range(turn)]

    def playerguess(self, turn: int, guesses_before: int) -> int:
        player_cards_print = f" Player: {self.name}, Cards : {self.cards}"
        print(player_cards_print)

        number_wins = int(input("Guess number of rounds you win "))
        self.guess = number_wins
        return number_wins

    def play_card(self):
        player_cards_print = f" Player: {self.name}, Cards : {self.cards}"
        print(player_cards_print)

        play_card_indx = int(input("play a card from your hand via index "))
        print(self.cards[play_card_indx])

        self.card_in_play = self.cards[play_card_indx]

    def delete_card(self):
        self.cards.remove(self.card_in_play)

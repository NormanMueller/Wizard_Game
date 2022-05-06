from pickle import NONE
from turtle import position
from cards import Cards
from player import Player
import collections

import random

# to:DO Decorateur füt prints , pytests, def remove hand_card, obj printouts
# dataclass


class Game:
    def __init__(self, player_count_input, player_names, cards=Cards()):
        self.turn = 1
        self.cards = cards
        self.guesses_player_before = None
        self.player_count_input = player_count_input
        self.player_names = player_names
        self.player_list = []
        self.create_player_instances()


    def create_player_instances(self):
        for player_nr in range(self.player_count_input):
            self.player_list.append(Player(self.player_names[player_nr], player_nr))


    def rotate_start_player(self):
        a_list = collections.deque(self.player_list)
        a_list.rotate(1)
        self.player_list = list(a_list)
        i=0
        for player in self.player_list:
            player.position = i
            i += 1


    def initilize_turn(self):
        self.rotate_start_player()
        for player in self.player_list:
            player.draw_cards(self.turn, self.cards.generator_itam)


    def player_guess_number_wins(self):
        guesses_number = 0
        for indx, player in enumerate(self.player_list):
            if indx != len(self.player_list):
                guesses_number += player.playerguess(self.turn, guesses_number)
            else:
                player.playerguess(self.turn, guesses_number)


    def eval_which_player_wins_round(self):
        get_start_player_card_type = self.player_list[0].card_in_play

        winner_through_wizard = [
            p for p in self.player_list if p.card_in_play[1] == "Z"
        ]

        if winner_through_wizard != []:
            winner = next(
                filter(
                    lambda x: x.name == winner_through_wizard[0].name, self.player_list
                )
            )
            winner.winning_rounds += 1
            return winner

        winner_through_high_card = [
            p
            for p in self.player_list
            if p.card_in_play[1] == get_start_player_card_type[1]
        ]
        
        winner = max(winner_through_high_card, key=lambda p: p.card_in_play[0])
        winner.winning_rounds += 1
        return winner


    def eval_player_points(self):
        def check_if_player_guesses_are_right(player):
            if player.winning_rounds == player.guess:
                return True

        for player in self.player_list:
            if check_if_player_guesses_are_right(player):  # right number of guesses
                player.points += 20 + player.guess * 10
            elif player.winning_rounds != player.guess:  # wrong number of guesses
                player.points -= abs(player.winning_rounds - player.guess) * 10


    def cleanup_end_turn(self):
        for player in self.player_list:
            player.cards = []
            player.guess = 0
            player.card_in_play = None
            player.winning_rounds = 0


    def set_player_order(self, winning_player):
        new_player_order = []
        start_player = next(
            filter(lambda x: x.name == winning_player.name, self.player_list)
        )
        new_player_order.append(start_player)

        for pos in range(1, self.player_count_input):
            next_pos = winning_player.position + pos
            if next_pos > self.player_count_input - 1:
                next_pos = abs(self.player_count_input  - next_pos )
            next_player = next(filter(lambda x: x.position == next_pos, self.player_list))
            new_player_order.append(next_player)

        self.player_list = new_player_order


    def main_method(self):
        while True:
            self.initilize_turn()
            self.player_guess_number_wins()

            for _ in range(self.turn):
                for player in self.player_list:
                    player.play_card()

                winning_player = self.eval_which_player_wins_round()
                self.set_player_order(winning_player)

                for player in self.player_list:
                    player.delete_card()

            self.eval_player_points()
            self.cleanup_end_turn()
            self.turn += 1


x = Game(3, ["norm", "nico", "damir"])
x.main_method()


from multiprocessing import get_start_method
from typing import Dict, List, Type
import pytest
from unittest import mock
from pytest import MonkeyPatch
from src.Wizard_Game.main import Game
from src.Wizard_Game.player import Player
import builtins
from src.Wizard_Game.cards import Cards
from unittest.mock import Mock, patch, MagicMock
import unittest


class TestGame(unittest.TestCase):
    def setUp(self):

        self.game = Game(2, ["X", "Y"])
        self.game.player_list[0].card_in_play = (5, "diamonds")
        self.game.player_list[1].card_in_play = (9, "diamonds")

        self.game2 = Game(3, ["X", "Y", "Z"])

    def test_create_player_instances(self):
        # then
        self.assertEqual(len(self.game.player_list), 2)
        self.assertEqual(self.game.player_list[0].name, "X")
        self.assertEqual(self.game.player_list[1].name, "Y")

    def test_rotate_start_player(self):
        # when
        self.game.rotate_start_player()

        # then
        self.assertEqual(self.game.player_list[0].name, "Y")
        self.assertEqual(self.game.player_list[1].name, "X")

    def test_initilize_player_2(self):
        # when
        with mock.patch.object(Player, 'draw_cards'):
            self.game.initilize_turn()

    # then
            Player.draw_cards.assert_called()
            assert Player.draw_cards.call_count == 2

    def test_initilize_player_3(self):
        # when
        with mock.patch.object(Player, 'draw_cards'):
            self.game2.initilize_turn()

    # then
            Player.draw_cards.assert_called()
            assert Player.draw_cards.call_count == 3

    def test_player_guess_number_wins(self):
        # when
        with mock.patch.object(Player, 'playerguess'):
            self.game2.player_guess_number_wins()

        # then
            Player.playerguess.assert_called()
            assert Player.playerguess.call_count == 3

    def test_eval_which_player_wins_round(self):

        self.game.eval_which_player_wins_round()
        self.assertEqual(
            self.game.player_list[0].card_in_play, (5, "diamonds"))
        self.assertEqual(
            self.game.player_list[1].card_in_play, (9, "diamonds"))
        print(self.game.player_list[1].card_in_play)
        self.assertEqual(self.game.player_list[0].winning_rounds, 0)

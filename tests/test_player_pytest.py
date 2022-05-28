from typing import Dict, List, Type
import pytest
from unittest import mock
from pytest import MonkeyPatch
from src.Wizard_Game.player import Player
import builtins


class TestPlayer:

    def test_draw_cards_one(self, generator_itam, draw_one_card):
        # given
        turn = 1
        card = generator_itam

        # when
        player = Player("NORM", 1)

        # then
        player.draw_cards(turn, card)
        assert player.cards == draw_one_card

    def test_draw_cards_three(self, generator_itam, draw_three_card):
        # given
        turn = 3
        card = generator_itam

        # when
        player = Player("NORM", 1)
        player.draw_cards(turn, card)

        # then
        assert player.cards == draw_three_card

    def test_playerguess(self, draw_one_card):
        # given
        turn = 0
        guesses_before = 0
        player = Player("NORM", 1)
        # when'

        # then
        with mock.patch.object(builtins, 'input', lambda _: '1'):
            assert player.playerguess(turn, guesses_before) == 1

    def test_play_card_first(self, draw_one_card):
        # given
        player = Player("NORM", 1)
        player.cards = draw_one_card

        # then
        with mock.patch.object(builtins, 'input', lambda _: '0'):
            player.play_card()
            assert player.card_in_play == draw_one_card[0]

    def test_play_card_second(self, draw_three_card):
        # given
        player = Player("NORM", 1)
        player.cards = draw_three_card

        # then
        with mock.patch.object(builtins, 'input', lambda _: '1'):
            player.play_card()
            assert player.card_in_play == draw_three_card[1]

    def test_delete_card(self, draw_one_card):
        # given
        player = Player("NORM", 1)
        player.cards = draw_one_card

        # then
        with mock.patch.object(builtins, 'input', lambda _: '0'):
            player.play_card()
            player.delete_card()
            assert player.cards == []

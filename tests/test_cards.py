from typing import Dict, List, Type
import pytest
from unittest import mock
from pytest import MonkeyPatch
import builtins
from src.Wizard_Game.cards import Cards


class TestCards:

    def test_generator(self, draw_three_card):
        cards = Cards()
        with mock.patch('random.shuffle', return_value=None):
            assert next(cards.generator_itam) == cards.card_list[0]

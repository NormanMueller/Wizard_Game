import pytest
from src.Wizard_Game.player import Player


@pytest.fixture()
def generator_itam():
    return iter([("diamonds", 5), ("diamonds", 6), ("diamonds", 7)])


@pytest.fixture
def draw_one_card():
    return[("diamonds", 5)]


@pytest.fixture(autouse=True)
def draw_three_card():
    return [("diamonds", 5), ("diamonds", 6), ("diamonds", 7)]


@pytest.fixture()
def player_diamonds():
    player = Player("NORM", 1)
    player.card_in_play = [("diamonds", 5)]
    return player


@pytest.fixture()
def player_z():
    player = Player("NORM", 1)
    player.card_in_play = [("Z", 0)]
    return player

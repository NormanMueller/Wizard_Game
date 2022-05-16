import pytest


@pytest.fixture()
def generator_itam():
    return iter([("diamonds", 5), ("diamonds", 6), ("diamonds", 7)])

@pytest.fixture
def draw_one_card():
    return[("diamonds", 5)]

@pytest.fixture()
def draw_three_card():
    return [("diamonds", 5), ("diamonds", 6), ("diamonds", 7)]
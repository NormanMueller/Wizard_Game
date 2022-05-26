from typing import Dict, List, Type, Tuple
import random


class Cards:
    def __init__(self):
        self.diamonds: List[Tuple] = [(x, "diamonds") for x in range(1, 11)]
        self.spades: List[Tuple] = [(x, "pik") for x in range(1, 11)]
        self.clover: List[Tuple] = [(x, "clover") for x in range(1, 11)]
        self.hearts: List[Tuple] = [(x, "hearts") for x in range(1, 11)]
        self.Z: List[Tuple] = [(0, "Z") for x in range(1, 5)]
        self.N: List[Tuple] = [(0, "N") for x in range(1, 5)]
        self.card_list: List[Tuple] = (
            self.diamonds +
            self.spades +
            self.clover +
            self.hearts +
            self.N +
            self.Z)
        self.generator_itam = self.generator()

    def generator(self):
        random.shuffle(self.card_list)
        for i in self.card_list:
            yield i

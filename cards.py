import random


class Cards:
    def __init__(self):
        self.diamonds = [(x, "diamonds") for x in range(1,11)]
        self.spades = [(x, "pik") for x in range(1,11)]
        self.clover = [(x, "clover") for x in range(1,11)]
        self.hearts = [(x, "hearts") for x in range(1,11)]
        self.Z = [(0, "Z") for x in range(1,5)]
        self.N = [(0, "N") for x in range(1,5)]
        self.card_list = self.diamonds + self.spades + self.clover + self.hearts +self.N + self.Z
        self.generator_itam = self.generator()


    def generator(self):
        random.shuffle(self.card_list)            
        for i in self.card_list:
                yield i
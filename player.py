from pickle import FALSE


class Player:
    def __init__(self, name, position):
        self.name = name
        self.cards = []
        self.guess = 0
        self.card_in_play = None
        self.winning_rounds = 0
        self.points = 0
        self.position = position


    def draw_cards(self, turn, cards):
        try: 
            self.cards = [next(cards) for i in range(turn)]
        except StopIteration:
            cards.generator_itam = cards.generator()
            self.cards = [next(cards) for i in range(turn)]



    def playerguess(self, turn, guesses_before)
        player_cards_print = f" Player: {self.name}, Cards : {self.cards}"
        print(player_cards_print)

        while True:
            number_wins = int(input("Guess number of rounds you win "))
            if number_wins + guesses_before == turn:
                print("Not a valid number of guesses ")
            else:
                break
        
        print(number_wins)
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

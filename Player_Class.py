class Player:

    # Initializer
    def __init__(self, player_name, card1, card2):
        self.score = 0
        self.name = player_name
        self.cards = [card1, card2]

    # Loops through list and adds up values
    def tallyScore(self):
        total = 0
        for card in self.cards:
            total += card
        self.score = total
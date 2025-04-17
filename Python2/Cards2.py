SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        #self.suit_index = 0

    def __eq__(self, other):
        if self.rank == other.rank and self.suit == other.suit:
            return True
        return False

    def __lt__(self, other):
        if RANKS.index(self.rank) < RANKS.index(other.rank):
            return True
        if (RANKS.index(self.rank) == RANKS.index(other.rank) 
            and SUITS.index(self.suit) < SUITS.index(other.suit)):
            
            return True
            
        return False
        
    def __gt__(self, other):
        if RANKS.index(self.rank) > RANKS.index(other.rank):
            return True
        if (RANKS.index(self.rank) == RANKS.index(other.rank) 
            and SUITS.index(self.suit) > SUITS.index(other.suit)):
            
            return True
            
        return False

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"

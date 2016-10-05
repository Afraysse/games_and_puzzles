""" Deck of Playing Cards """
# encode the ranks and suits to permit card comparison 
# map the integer codes onto words 

class Card:
    """ Defines a single card."""

    # 'narf' keeps track of the 0th element in the list
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + "of " + self.suits[self.suit])

    # method that houses the logic of ordering 
    def cmp(self, other):
        """ Checks suits for ordering."""
        if self.suit > other.suit: return 1 
        if self.suit < other.suit: return -1 
        # if suits are the same, check rank 
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1 
        # if ranks are the same, it's a tie
        return 0

    # with this ordering, Aces are lower than 2s

    # define six special methods
    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other): 
        return self.cmp(other) != 0

class Deck: 
    """ Defines a deck of cards."""

    def __init__(self):
        self.cards = []

        # populate deck 
        for suit in range(4):   # enumerates suits from 0 to 3      
            for rank in range(1, 14):     # enumerates ranks from 1 to 13
                self.cards.append(Card(suit, rank))

        # total number of times the body is executed is fifty-two

red_deck = Deck()
blue_deck = Deck()













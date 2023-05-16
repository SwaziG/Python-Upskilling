class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return(self.ranks[self.rank]+ " of " + self.suits[self.suit])

    def cmp(self, other):
       # check the suits
       if self.suit > other.suit: return 1
       if self.suit < other.suit: return -1 
       # Suits are the same, no need to write i == . . . Check ranks
       if self.rank > other.rank: return 1
       if self.rank < other.rank: return -1
       # Ranks are the same . . . It's a tie (same card)
       return 0

    def __eq__(self, other):
        """Are the two calls equal to one another"""
        return self.cmp(other) == 0
    
    def __le__(self, other):
         """Is self <= other"""
         return self.cmp(other) == 0
    
    def __ge__(self, other):
         """Is self >= other"""
         return self.cmp(other) == 0
    
    def __gt__(self, other):
         """Is self > other"""
         return self.cmp(other) == 0
    
    def __lt__(self, other):
         """Is self < other"""
         return self.cmp(other) == 0
    
    def __ne__(self, other):
         """Is self != other"""
         return self.cmp(other) == 0
    
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s
    
    # def shuffle(self):
    #     import random
    #     rng = random.Random()           # Create a random generator
    #     num_cards = len(self.cards)
    #     for i in range (num_cards):
    #         j = rng.randrange(i,num_cards)
    #         (self.cards[i],self.cards[j]) = (self.cards[j], self.cards[i])

    def shuffle(self):
        import random
        rng = random.Random()           # Create a random generator
        rng.shuffle(self.cards)         # uUse its shuffle method

# Card1 = Card(2,5)
# print (Card1)

red_deck = Deck()
blue_deck = Deck()
print (blue_deck)
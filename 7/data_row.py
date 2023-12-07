from hand import Hand

class DataRow:
    def __init__(self, hand: Hand, bid: int, hand_repr: str):
        self.hand = hand
        self.bid = bid
        self.hand_repr = hand_repr

    def __lt__(self, other):
        return self.hand < other.hand

    def __repr__(self):
        return self.hand_repr + " " + str(self.bid)
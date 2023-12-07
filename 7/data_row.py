from hand import Hand

class DataRow:
    def __init__(self, hand: Hand, bid: int):
        self.hand = hand
        self.bid = bid

    def __lt__(self, other):
        return self.hand < other.hand

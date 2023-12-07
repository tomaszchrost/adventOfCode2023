from data import Data
from data_row import DataRow
from hand import Hand


class DataParser:
    def __init__(self, file_name):
        self.file_name = file_name
        self._calculate_data()

    def _calculate_data(self):
        with open(self.file_name) as f:
            file_contents = f.readlines()
        data_rows = []
        for line in file_contents:
            hand_string, bid_string = line.split()
            bid = int(bid_string)
            hand = []
            for card in hand_string:
                if card == "T":
                    hand.append(10)
                elif card == "J":
                    hand.append(11)
                elif card == "Q":
                    hand.append(12)
                elif card == "K":
                    hand.append(13)
                elif card == "A":
                    hand.append(14)
                else:
                    hand.append(int(card))
            data_row = DataRow(Hand(hand), bid)
            data_rows.append(data_row)
        self.data = Data(data_rows)

    def _calculate_data(self):
        with open(self.file_name) as f:
            file_contents = f.readlines()
        data_rows = []
        for line in file_contents:
            hand_string, bid_string = line.split()
            bid = int(bid_string)
            hand = []
            for card in hand_string:
                if card == "T":
                    hand.append(10)
                elif card == "J":
                    hand.append(1)
                elif card == "Q":
                    hand.append(12)
                elif card == "K":
                    hand.append(13)
                elif card == "A":
                    hand.append(14)
                else:
                    hand.append(int(card))
            data_row = DataRow(Hand(hand), bid, hand_string)
            data_rows.append(data_row)
        self.data = Data(data_rows)
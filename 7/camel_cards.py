from data import Data
from data_parser import DataParser


class CamelCards:
    def __init__(self, data):
        self.data: Data = data

    def get_total_winnings(self):
        self.data.data_rows.sort()
        total_winnings = 0
        for i in range(len(self.data.data_rows)):
            total_winnings += self.data.data_rows[i].bid * (i + 1)
        return total_winnings


def main():
    data_parser = DataParser("star1.dat")
    camel_cards = CamelCards(data_parser.data)
    print(camel_cards.get_total_winnings())


if __name__ == "__main__":
    main()

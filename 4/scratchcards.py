from functools import cache

from data_parser import DataParser


class Scratchcards:

    def __init__(self, data):
        self.data = data

    @staticmethod
    def get_points_for_scratch_card(scratch_card):
        points = 0
        for my_number in scratch_card.my_numbers:
            if my_number in scratch_card.winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        return points

    @cache
    def get_points_for_scratch_card_star2(self, scratch_card_index):
        number_of_wins = 0
        scratch_card_count = 1
        for my_number in self.data.scratch_cards[scratch_card_index].my_numbers:
            if my_number in self.data.scratch_cards[scratch_card_index].winning_numbers:
                number_of_wins += 1
        for i in range(1, number_of_wins + 1):
            scratch_card_count += self.get_points_for_scratch_card_star2(scratch_card_index + i)
        return scratch_card_count

    def sum_points(self):
        sum_of_points = 0
        for scratch_card in self.data.scratch_cards:
            sum_of_points += self.get_points_for_scratch_card(scratch_card)

        return sum_of_points

    def sum_points_star2(self):
        sum_of_points = 0
        for i in range(len(self.data.scratch_cards) - 1, -1, -1):
            sum_of_points += self.get_points_for_scratch_card_star2(i)

        return sum_of_points


def main():
    data = DataParser.parse_date("star1.dat")
    scratchcards = Scratchcards(data)
    sum_of_points = scratchcards.sum_points()

    print(sum_of_points)

    sum_of_points = scratchcards.sum_points_star2()
    print(sum_of_points)


if __name__ == "__main__":
    main()

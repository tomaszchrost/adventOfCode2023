from data import Data
from scratch_card import ScratchCard


class DataParser:
    @staticmethod
    def parse_date(file_name):
        file_contents = None
        with open(file_name) as f:
            file_contents = f.readlines()

        scratch_cards = []
        for line in file_contents:
            winning_number_string, my_number_string = line.split("|")

            winning_numbers = winning_number_string.split()[2:]
            winning_numbers = [int(winning_number) for winning_number in winning_numbers]

            my_numbers = my_number_string.split()
            my_numbers = [int(my_number) for my_number in my_numbers]

            scratch_card = ScratchCard(winning_numbers, my_numbers)
            scratch_cards.append(scratch_card)

        return Data(scratch_cards)

import math

from data_parser import DataParser


class GearRatios:

    def __init__(self, data):
        self.data = data

    def get_number_from_data(self, i, start_j, end_j):
        number = 0
        multiplier = 10 ** (end_j - start_j - 1)
        for schematic_space in self.data[i][start_j:end_j]:
            number += schematic_space.value * multiplier
            multiplier /= 10
        return int(number)

    def check_for_symbol_with_boundary_check(self, i, j):
        if (i < 0
                or i >= len(self.data)
                or j < 0
                or j >= len(self.data[i])):
            return False
        else:
            return self.data[i][j].has_symbol

    def check_space_is_adjacent_to_symbol(self, i, j):
        for i2 in range(i - 1, i + 2):
            for j2 in range(j - 1, j + 2):
                if self.check_for_symbol_with_boundary_check(i2, j2):
                    return True
        return False

    def check_number_is_adjacent_to_symbol(self, i, start_j, end_j):
        for j in range(start_j, end_j):
            if self.check_space_is_adjacent_to_symbol(i, j):
                return True
        return False

    def get_number_value(self, i, start_j, end_j):
        value = self.get_number_from_data(i, start_j, end_j)
        if self.check_number_is_adjacent_to_symbol(i, start_j, end_j):
            return value
        else:
            return 0

    def get_sum_of_part_numbers(self):
        sum_of_part_numbers = 0
        for i in range(len(self.data)):
            start_j = 0
            index_in_number = False
            for j in range(len(self.data[i])):
                schematic_space = self.data[i][j]
                if schematic_space.value is not None and not index_in_number:
                    index_in_number = True
                    start_j = j
                elif schematic_space.value is None and index_in_number:
                    index_in_number = False
                    sum_of_part_numbers += self.get_number_value(i, start_j, j)

                if schematic_space.value is not None and index_in_number and j == (len(self.data[i]) - 1):
                    sum_of_part_numbers += self.get_number_value(i, start_j, j + 1)
        return sum_of_part_numbers


def main():
    data_parser = DataParser("star1.dat")
    data = data_parser.parse_data()
    gear_ratios = GearRatios(data.engine_schematic)
    print(gear_ratios.get_sum_of_part_numbers())


if __name__ == "__main__":
    main()

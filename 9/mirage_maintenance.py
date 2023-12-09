from typing import List

from data import Data
from data_parser import DataParser

class MirageMaintenance:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def all_values_in_list_are_zero(value_list: List):
        for value in value_list:
            if value != 0:
                return False
        return True

    def calculate_differences_from_list(self, value_list: List):
        differences = []
        for i in range(len(value_list) - 1):
            differences.append(value_list[i + 1] - value_list[i])
        return differences

    def get_next_in_sequence(self, sequence_with_differences: List[List[int]]):
        next_in_sequence = 0
        for i in range(len(sequence_with_differences) - 2, -1, -1):
            next_in_sequence = sequence_with_differences[i][-1] + next_in_sequence
        return next_in_sequence

    def get_previous_in_sequence(self, sequence_with_differences: List[List[int]]):
        previous_in_sequence = 0
        for i in range(len(sequence_with_differences) - 2, -1, -1):
            previous_in_sequence = sequence_with_differences[i][0] - previous_in_sequence
        return previous_in_sequence

    def get_sum_of_extrapolated_values(self):
        sum_of_values = 0
        for history in self.data.histories:
            difference_list: List[List[int]] = [history.history]
            while not self.all_values_in_list_are_zero(difference_list[-1]):
                difference_list.append(self.calculate_differences_from_list(difference_list[-1]))
            sum_of_values += self.get_next_in_sequence(difference_list)
        return sum_of_values

    def get_sum_of_extrapolated_values_star2(self):
        sum_of_values = 0
        for history in self.data.histories:
            difference_list: List[List[int]] = [history.history]
            while not self.all_values_in_list_are_zero(difference_list[-1]):
                difference_list.append(self.calculate_differences_from_list(difference_list[-1]))
            sum_of_values += self.get_previous_in_sequence(difference_list)
        return sum_of_values


def main():
    data_parser: DataParser = DataParser("data.dat")
    data: Data = data_parser.get_data()
    mirage_maintenance = MirageMaintenance(data)
    print(mirage_maintenance.get_sum_of_extrapolated_values())
    print(mirage_maintenance.get_sum_of_extrapolated_values_star2())


if __name__ == "__main__":
    main()

from data_parser import DataParser
from data import Data
from race import Race

class WaitForIt:
    def __init__(self, data):
        self.data = data

    def determine_product_of_number_of_ways(self):
        product_of_values = 1
        for race in self.data.races:
            value_to_return = 0
            for i in range(1, race.time):
                if i * (race.time - i) > race.distance:
                    half_of_time = race.time // 2
                    value_to_return = (half_of_time - i) * 2
                    if race.time % 2 == 0:
                        value_to_return += 1
                    else:
                        value_to_return += 2
                    break
            product_of_values *= value_to_return
        return product_of_values


def main():
    data = DataParser.get_data("data.dat")
    wait_for_it = WaitForIt(data)
    print(wait_for_it.determine_product_of_number_of_ways())


if __name__ == "__main__":
    main()

from data import Data
from race import Race

class DataParser:

    @staticmethod
    def get_data(file_name):
        with open(file_name) as f:
            file_contents = f.readlines()
        times = [int(value) for value in file_contents[0].split()[1:]]
        distances = [int(value) for value in file_contents[1].split()[1:]]
        races = []
        for i in range(len(times)):
            races.append(Race(times[i], distances[i]))
        data = Data(races)
        return data

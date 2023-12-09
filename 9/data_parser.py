from data import Data
from history import History


class DataParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_data(self):
        with open(self.file_name) as f:
            file_contents = f.readlines()

        histories = []
        for line in file_contents:
            histories.append(History([int(x) for x in line.split()]))

        data = Data(histories)
        return data

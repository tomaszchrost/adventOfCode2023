from data import Data
from pipe import Pipe


class DataParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_data(self):
        with open(self.file_name) as f:
            file_contents = f.readlines()

        pipes = []
        for line in file_contents:
            pipes.append([Pipe(pipe) for pipe in line.strip()])

        data = Data(pipes)
        return data

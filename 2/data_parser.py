from data import Data
from game import Game
from revealed_cubes import RevealedCubes

import colour


class DataParser:
    file_name = None
    file_contents = None
    data = None

    def __init__(self, file_name):
        self.file_name = file_name

    def _read_data_from_file(self):
        with open(self.file_name) as f:
            self.file_contents = f.readlines()

    def _get_game_from_line(self, line):
        game = Game()
        game_number_string, reveals_string = line.split(":")
        game.game_number = int(game_number_string.split()[-1])

        reveals = reveals_string.split(";")
        for reveal in reveals:
            game.reveals.append(self._get_revealed_cubes_from_string(reveal))
        return game

    @staticmethod
    def _get_revealed_cubes_from_string(reveal_string):
        reveal = RevealedCubes()
        for cube_reveal in reveal_string.split(','):
            cube_number_string, cube_colour_string = cube_reveal.split()
            reveal.cubes[colour.get_colour_from_string(cube_colour_string)] = int(cube_number_string)

        return reveal

    def _parse_data(self):
        data: Data = Data()
        for line in self.file_contents:
            data.games.append(self._get_game_from_line(line))
        self.data = data

    def parse_data(self):
        self._read_data_from_file()
        self._parse_data()
        return self.data

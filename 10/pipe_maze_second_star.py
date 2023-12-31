from data_parser import DataParser
from data import Data
from pipe import Pipe
import utils.list_utils as list_utils

class PipeMaze:

    WEST_CONNECTING_PIPES = (
        Pipe.HORIZONTAL_PIPE,
        Pipe.NINETY_DEGREE_PIPE_NORTH_AND_WEST,
        Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_WEST,
        Pipe.STARTING_POSITION
    )

    EAST_CONNECTING_PIPES = (
        Pipe.HORIZONTAL_PIPE,
        Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_EAST,
        Pipe.NINETY_DEGREE_PIPE_NORTH_AND_EAST,
        Pipe.STARTING_POSITION
    )

    NORTH_CONNECTING_PIPES = (
        Pipe.VERTICAL_PIPE,
        Pipe.NINETY_DEGREE_PIPE_NORTH_AND_EAST,
        Pipe.NINETY_DEGREE_PIPE_NORTH_AND_WEST,
        Pipe.STARTING_POSITION
    )

    SOUTH_CONNECTING_PIPES = (
        Pipe.VERTICAL_PIPE,
        Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_EAST,
        Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_WEST,
        Pipe.STARTING_POSITION
    )

    def __init__(self, data):
        self.data: Data = data

    def find_starting_point(self):
        for i in range(len(self.data.pipes)):
            for j in range(len(self.data.pipes[i])):
                if self.data.pipes[i][j] == Pipe.STARTING_POSITION:
                    return i, j

    def connects_upwards(self, i, j):
        if i - 1 < 0:
            return False

        current_pipe = self.data.pipes[i][j]
        next_pipe = self.data.pipes[i - 1][j]
        return ((current_pipe == Pipe.STARTING_POSITION
                or current_pipe == Pipe.VERTICAL_PIPE
                or current_pipe == Pipe.NINETY_DEGREE_PIPE_NORTH_AND_EAST
                or current_pipe == Pipe.NINETY_DEGREE_PIPE_NORTH_AND_WEST)
            and (next_pipe == Pipe.STARTING_POSITION
                or next_pipe == Pipe.VERTICAL_PIPE
                or next_pipe == Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_EAST
                or next_pipe == Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_WEST))

    def connects_downwards(self, i, j):
        if i + 1 >= len(self.data.pipes):
            return False

        current_pipe = self.data.pipes[i][j]
        next_pipe = self.data.pipes[i + 1][j]
        return ((current_pipe == Pipe.STARTING_POSITION
                 or current_pipe == Pipe.VERTICAL_PIPE
                 or current_pipe == Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_WEST
                 or current_pipe == Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_EAST)
            and (next_pipe == Pipe.STARTING_POSITION
                 or next_pipe == Pipe.VERTICAL_PIPE
                 or next_pipe == Pipe.NINETY_DEGREE_PIPE_NORTH_AND_WEST
                 or next_pipe == Pipe.NINETY_DEGREE_PIPE_NORTH_AND_EAST))

    def connects_leftwards(self, i, j):
        if j - 1 < 0:
            return False

        current_pipe = self.data.pipes[i][j]
        next_pipe = self.data.pipes[i][j - 1]
        return ((current_pipe == Pipe.STARTING_POSITION
                 or current_pipe == Pipe.HORIZONTAL_PIPE
                 or current_pipe == Pipe.NINETY_DEGREE_PIPE_NORTH_AND_WEST
                 or current_pipe == Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_WEST)
            and (next_pipe == Pipe.STARTING_POSITION
                 or next_pipe == Pipe.HORIZONTAL_PIPE
                 or next_pipe == Pipe.NINETY_DEGREE_PIPE_NORTH_AND_EAST
                 or next_pipe == Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_EAST))

    def connect_rightwards(self, i, j):
        if j + 1 >= len(self.data.pipes[i]):
            return False

        current_pipe = self.data.pipes[i][j]
        next_pipe = self.data.pipes[i][j + 1]
        return ((current_pipe == Pipe.STARTING_POSITION
                 or current_pipe == Pipe.HORIZONTAL_PIPE
                 or current_pipe == Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_EAST
                 or current_pipe == Pipe.NINETY_DEGREE_PIPE_NORTH_AND_EAST)
            and (next_pipe == Pipe.STARTING_POSITION
                 or next_pipe == Pipe.HORIZONTAL_PIPE
                 or next_pipe == Pipe.NINETY_DEGREE_PIPE_SOUTH_AND_WEST
                 or next_pipe == Pipe.NINETY_DEGREE_PIPE_NORTH_AND_WEST))

    def find_connecting_pipes(self, i, j):
        connecting_pipes = []

        if self.connects_upwards(i, j):
            connecting_pipes.append((i - 1, j))
        if self.connects_downwards(i, j):
            connecting_pipes.append((i + 1, j))
        if self.connect_rightwards(i, j):
            connecting_pipes.append((i, j + 1))
        if self.connects_leftwards(i, j):
            connecting_pipes.append((i, j - 1))

        return connecting_pipes

    def get_visited_locations(self):
        visited_locations = []
        start_i, start_j = self.find_starting_point()
        visited_locations.append((start_i, start_j))
        connecting_locations = self.find_connecting_pipes(start_i, start_j)
        while connecting_locations:
            new_connecting_locations = []
            for connecting_location in connecting_locations:
                visited_locations.append(connecting_location)
                connecting_pipes = self.find_connecting_pipes(*connecting_location)
                new_connecting_locations.extend(connecting_pipes)

            connecting_locations = list(filter(lambda x: (x not in visited_locations), new_connecting_locations))
        return visited_locations

    def _find_not_enclosed_locations(self, not_enclosed_locations, visited_locations, i, j):
        if (i, j) not in visited_locations and (i, j) not in not_enclosed_locations:
            not_enclosed_locations.append((i, j))
            list_index = list_utils.ListIndex(i, j)
            orthogonal_adjacent_locations = list_utils.get_orthogonal_locations(list_index, self.data.pipes)
            return [(x.i, x.j) for x in orthogonal_adjacent_locations]
        else:
            return []

    def find_not_enclosed_locations(self):
        not_enclosed_locations = []
        visited_locations = self.get_visited_locations()

        locations_to_check = []
        for i in range(0, len(self.data.pipes)):
            for j in [0, len(self.data.pipes[i]) - 1]:
                locations_to_check.append((i, j))
        for j in range(0, len(self.data.pipes[0])):
            for i in [0, len(self.data.pipes) - 1]:
                locations_to_check.append((i, j))

        while len(locations_to_check) > 0:
            i = locations_to_check[0][0]
            j = locations_to_check[0][1]
            locations_to_check.extend(self._find_not_enclosed_locations(not_enclosed_locations, visited_locations, i, j))
            locations_to_check.pop(0)

        count = 0
        for i in range(1, len(self.data.pipes), 2):
            for j in range(1, len(self.data.pipes[i]), 2):
                if (i, j) not in visited_locations and (i, j) not in not_enclosed_locations:
                    count += 1
                    print('\033[92m' + self.data.pipes[i][j].value + '\033[0m', end="")
                elif (i, j) in visited_locations:
                    print('\033[93m' + self.data.pipes[i][j].value + '\033[0m', end="")
                else:
                    print(self.data.pipes[i][j].value, end="")
            print()
        return count

    def expand_data(self):
        new_data = []
        new_data_row = [Pipe.EXPANDED_POINT]
        for j in range(0, len(self.data.pipes[0])):
            new_data_row.append(Pipe.EXPANDED_POINT)
            new_data_row.append(Pipe.EXPANDED_POINT)
        new_data.append(new_data_row)

        for i in range(0, len(self.data.pipes) - 1):
            new_data_row = []
            new_data_row.append(Pipe.EXPANDED_POINT)

            for j in range(0, len(self.data.pipes[i]) - 1):
                new_data_row.append(self.data.pipes[i][j])
                if (self.data.pipes[i][j] in self.EAST_CONNECTING_PIPES
                        and self.data.pipes[i][j + 1] in self.WEST_CONNECTING_PIPES):
                    new_data_row.append(Pipe.HORIZONTAL_PIPE)
                else:
                    new_data_row.append(Pipe.EXPANDED_POINT)

            new_data_row.append(self.data.pipes[i][-1])
            new_data_row.append(Pipe.EXPANDED_POINT)
            new_data.append(new_data_row)

            new_data_row = [Pipe.EXPANDED_POINT]
            for j in range(0, len(self.data.pipes[0])):
                if (self.data.pipes[i][j] in self.SOUTH_CONNECTING_PIPES
                        and self.data.pipes[i + 1][j] in self.NORTH_CONNECTING_PIPES):
                    new_data_row.append(Pipe.VERTICAL_PIPE)
                else:
                    new_data_row.append(Pipe.EXPANDED_POINT)
                new_data_row.append(Pipe.EXPANDED_POINT)
            new_data.append(new_data_row)

        new_data_row = []
        new_data_row.append(Pipe.EXPANDED_POINT)

        for j in range(0, len(self.data.pipes[-1]) - 1):
            new_data_row.append(self.data.pipes[-1][j])
            if (self.data.pipes[-1][j] in self.EAST_CONNECTING_PIPES
                    and self.data.pipes[-1][j + 1] in self.WEST_CONNECTING_PIPES):
                new_data_row.append(Pipe.HORIZONTAL_PIPE)
            else:
                new_data_row.append(Pipe.EXPANDED_POINT)

        new_data_row.append(self.data.pipes[-1][-1])
        new_data_row.append(Pipe.EXPANDED_POINT)
        new_data.append(new_data_row)

        new_data_row = [Pipe.EXPANDED_POINT]
        for j in range(0, len(self.data.pipes[-1])):
            new_data_row.append(Pipe.EXPANDED_POINT)
            new_data_row.append(Pipe.EXPANDED_POINT)
        new_data.append(new_data_row)

        self.data.pipes = new_data



def main():
    data_parser = DataParser("data.dat")
    data = data_parser.get_data()
    pipe_maze = PipeMaze(data)
    pipe_maze.expand_data()
    print(pipe_maze.find_not_enclosed_locations())


if __name__ == "__main__":
    main()

from data_parser import DataParser
from data import Data
from pipe import Pipe


class PipeMaze:

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

    def get_steps_away(self):
        visited_locations = []
        start_i, start_j = self.find_starting_point()
        visited_locations.append((start_i, start_j))
        connecting_locations = self.find_connecting_pipes(start_i, start_j)
        steps = 0
        while connecting_locations:
            steps += 1
            new_connecting_locations = []
            for connecting_location in connecting_locations:
                visited_locations.append(connecting_location)
                connecting_pipes = self.find_connecting_pipes(*connecting_location)
                new_connecting_locations.extend(connecting_pipes)

            connecting_locations = list(filter(lambda x: (x not in visited_locations), new_connecting_locations))
        return steps


def main():
    data_parser = DataParser("data.dat")
    data = data_parser.get_data()
    pipe_maze = PipeMaze(data)

    print(pipe_maze.get_steps_away())


if __name__ == "__main__":
    main()
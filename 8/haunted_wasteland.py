from data import Data
from data import Instruction
from data import Node
from data_parser import DataParser

class HauntedWasteland:

    def __init__(self, data):
        self.data = data

    def get_step_count(self):
        current_node: Node = self.data.get_starting_node()
        steps = 0
        while current_node.node_name != "ZZZ":
            print(current_node.node_name)
            instruction: Instruction = self.data.get_next_instruction()
            current_node = self.data.traverse(current_node, instruction)
            steps += 1
        return steps


def main():
    data_parser = DataParser("testdata.dat")
    data: Data = data_parser.get_data()

    haunted_wasteland = HauntedWasteland(data)
    print(haunted_wasteland.get_step_count())


if __name__ == "__main__":
    main()
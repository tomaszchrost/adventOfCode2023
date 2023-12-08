import typing

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
            instruction: Instruction = self.data.get_next_instruction()
            current_node = self.data.traverse(current_node, instruction)
            steps += 1
        return steps

    @staticmethod
    def all_nodes_are_end_nodes(nodes):
        for node in nodes:
            if node.node_name[2] != "Z":
                return False
        return True

    def get_ghost_step_count(self):
        current_nodes: typing.List[Node] = self.data.get_starting_nodes()
        steps = 0
        while not self.all_nodes_are_end_nodes(current_nodes):
            instruction: Instruction = self.data.get_next_instruction()
            for i in range(len(current_nodes)):
                current_nodes[i] = self.data.traverse(current_nodes[i], instruction)
            steps += 1
        return steps


def main():
    data_parser = DataParser("testdata.dat")
    data: Data = data_parser.get_data()

    haunted_wasteland = HauntedWasteland(data)
    #print(haunted_wasteland.get_step_count())
    print(haunted_wasteland.get_ghost_step_count())


if __name__ == "__main__":
    main()
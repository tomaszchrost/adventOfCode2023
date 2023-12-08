from data import Data
from data import Node
from data import Instruction


class DataParser:

    instruction_mapping = {"L": Instruction.LEFT, "R": Instruction.RIGHT}

    def __init__(self, file_name: str):
        self.file_name = file_name

    @staticmethod
    def get_instruction_from_string(instruction_string):
        return DataParser.instruction_mapping.get(instruction_string)

    def get_data(self):
        with open(self.file_name) as f:
            file_contents = f.readlines()
        instructions_string = file_contents[0][:-1]

        instructions = [self.get_instruction_from_string(ins) for ins in instructions_string]

        nodes = []
        for line in file_contents[2:]:
            line = line.replace(",", "")
            line = line.replace("(", "")
            line = line.replace(")", "")

            node_name, _, left_node_name, right_node_name = line.split()

            node = Node(node_name, left_node_name, right_node_name)
            nodes.append(node)

        data = Data(instructions, nodes)
        return data

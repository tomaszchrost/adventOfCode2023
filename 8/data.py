import enum
import typing


class Node:
    def __init__(self, node_name, left_node_name, right_node_name):
        self.node_name = node_name
        self.left_node_name = left_node_name
        self.right_node_name = right_node_name


class Instruction(enum.Enum):
    LEFT = 0
    RIGHT = 1


class Data:

    def __init__(self, instructions: typing.List[Instruction], nodes: typing.List[Node]):
        self.nodes = nodes
        self.instructions = instructions
        self._instruction_step = 0

    def traverse(self, node, instruction):
        for next_node in self.nodes:
            if instruction == Instruction.LEFT:
                if next_node.node_name == node.left_node_name:
                    return next_node
            elif instruction == Instruction.RIGHT:
                if next_node.node_name == node.right_node_name:
                    return next_node
        return None

    def get_next_instruction(self):
        instruction = self.instructions[self._instruction_step]
        self._instruction_step = (self._instruction_step + 1) % len(self.instructions)
        return instruction

    def get_starting_node(self):
        for node in self.nodes:
            if node.node_name == "AAA":
                return node
        return None

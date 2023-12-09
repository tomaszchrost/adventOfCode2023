import enum
import typing


class Node:
    def __init__(self, node_name, left_node_name, right_node_name):
        self.node_name = node_name
        self.left_node_name = left_node_name
        self.right_node_name = right_node_name
        self.left_node = None
        self.right_node = None

    def __repr__(self):
        return "Node(" + self.node_name + ", " + self.left_node_name + ", " + self.right_node_name + ")"


class Instruction(enum.Enum):
    LEFT = 0
    RIGHT = 1


class Data:

    def __init__(self, instructions: typing.List[Instruction], nodes: typing.List[Node]):
        self.nodes = nodes
        self._optimise_nodes()
        self.instructions = instructions
        self._instruction_step = 0

    def traverse(self, node, instruction):
        if instruction == Instruction.LEFT:
            return node.left_node
        elif instruction == Instruction.RIGHT:
            return node.right_node
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

    def get_starting_nodes(self):
        starting_nodes = []
        for node in self.nodes:
            if node.node_name[2] == "A":
                starting_nodes.append(node)
        return starting_nodes

    def _optimise_nodes(self):
        for node in self.nodes:
            for next_node in self.nodes:
                if next_node.node_name == node.left_node_name:
                    node.left_node = next_node
                if next_node.node_name == node.right_node_name:
                    node.right_node = next_node

    def reset_instructions(self):
        self._instruction_step = 0

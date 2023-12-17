from typing import List
from pipe import Pipe


class Data:
    def __init__(self, pipes: List[List[Pipe]]):
        self.pipes = pipes

from colour import Colour
from typing import Dict


class RevealedCubes:
    cubes: Dict[Colour, int]

    def __init__(self):
        self.cubes = {}

from revealed_cubes import RevealedCubes
from typing import List


class Game:
    game_number: int
    reveals: List[RevealedCubes]

    def __init__(self):
        self.reveals = []

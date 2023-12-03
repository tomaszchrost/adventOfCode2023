from enum import Enum
from typing import Dict


class Colour(Enum):
    BLUE = 1
    RED = 2
    GREEN = 3


string_to_colour = {
    'blue': Colour.BLUE,
    'red': Colour.RED,
    'green': Colour.GREEN
}


def get_colour_from_string(colour_string):
    return string_to_colour[colour_string]

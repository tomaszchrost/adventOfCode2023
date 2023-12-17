from __future__ import annotations
from typing import List


def is_index_valid_in_list(list_index: ListIndex, list_to_check: List):
    if list_index.i < 0 or list_index.i >= len(list_to_check):
        return False
    elif list_index.j < 0 or list_index.j >= len(list_to_check[list_index.i]):
        return False
    return True


def _get_orthogonal_location(list_index: ListIndex, list_for_locations: List):
    if is_index_valid_in_list(list_index, list_for_locations):
        return list_index
    return None


def get_orthogonal_locations(list_index: ListIndex, list_for_locations: List):
    list_indexes = []
    for i in range(-1, 2, 2):
        new_list_index = _get_orthogonal_location(ListIndex(list_index.i + i, list_index.j), list_for_locations)
        if new_list_index is not None:
            list_indexes.append(new_list_index)
    for j in range(-1, 2, 2):
        new_list_index = _get_orthogonal_location(ListIndex(list_index.i, list_index.j + j), list_for_locations)
        if new_list_index is not None:
            list_indexes.append(new_list_index)

    return list_indexes


class ListIndex:
    def __init__(self, i, j):
        self.i = i
        self.j = j

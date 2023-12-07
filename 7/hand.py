from __future__ import annotations
import collections
import heapq
import typing


class Hand:
    def __init__(self, card_values: typing.List[int]):
        self.card_values = card_values
        self._calculate_card_counts()

    def _calculate_card_counts(self):
        self.card_counts = heapq.nlargest(2, collections.Counter(self.card_values).values())

    def __lt__(self, other: Hand):
        max_counts = self.card_counts
        other_max_counts = other.card_counts

        if max_counts[0] < other_max_counts[0]:
            return True
        elif max_counts[0] > other_max_counts[0]:
            return False
        elif max_counts[1] < other_max_counts[1]:
            return True
        elif max_counts[1] > other_max_counts[1]:
            return False
        else:
            for i in range(len(self.card_values)):
                if self.card_values[i] < other.card_values[i]:
                    return True
                elif self.card_values[i] > other.card_values[i]:
                    return False
        return False

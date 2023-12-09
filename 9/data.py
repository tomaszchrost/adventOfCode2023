import typing

from history import History


class Data:
    def __init__(self, histories: typing.List[History]):
        self.histories = histories

import typing
from data_row import DataRow


class Data:
    def __init__(self, data_rows: typing.List[DataRow]):
        self.data_rows = data_rows

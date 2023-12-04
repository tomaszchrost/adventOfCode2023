from data import Data
from shematic_space import SchematicSpace


class DataParser:
    UNICODE_VALUE_0 = 48
    UNICODE_VALUE_9 = 57
    UNICODE_VALUE_FULL_STOP = 46

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_contents = None
        self.data = None

    def _read_data_from_file(self):
        with open(self.file_name) as f:
            self.file_contents = f.readlines()

    def _parse_data(self):
        data = Data()
        data.engine_schematic = []
        for line in self.file_contents:
            line = line.strip()
            engine_schematic_row = []
            for character in line:
                unicode_value = ord(character)
                if self.UNICODE_VALUE_0 <= unicode_value <= self.UNICODE_VALUE_9:
                    engine_schematic_row.append(SchematicSpace(has_symbol=False, value=int(character)))
                elif unicode_value == self.UNICODE_VALUE_FULL_STOP:
                    engine_schematic_row.append(SchematicSpace(has_symbol=False, value=None))
                else:
                    engine_schematic_row.append(SchematicSpace(has_symbol=True, value=None))
            data.engine_schematic.append(engine_schematic_row)
            self.data = data

    def parse_data(self):
        self._read_data_from_file()
        self._parse_data()
        return self.data

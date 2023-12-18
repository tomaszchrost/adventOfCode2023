from city_block import CityBlock


class DataParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_data(self):
        with open(self.file_name) as f:
            file_contents = f.readlines()

        data = []
        for line in file_contents:
            data.append([CityBlock(int(character)) for character in line.strip()])

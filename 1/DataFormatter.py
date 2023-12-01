class DataFormatter:

    data_file = None
    data = None

    def __init__(self, data_file):
        self.data_file = data_file

    def replace_spelt_numbers_with_numbers(self):
        new_data = []
        for line in self.data:
            for key, value in self.spelt_numbers.items():
                line.replace(key, str(value))
            new_data.append(line)
        self.data = new_data


    def read_raw_data(self):
        with open(self.data_file) as f:
            self.data = f.readlines()

    def get_formatted_data_for_first_star(self):
        self.read_raw_data()
        return self.data



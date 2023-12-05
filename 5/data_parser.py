from data import Data
from seed_range import SeedRange
from source_destination_range import SourceDestinationRange


class DataParser:
    def __init__(self):
        self.data = None

    @staticmethod
    def parse_seeds():
        with open("seeds.dat") as f:
            f_contents_seeds = f.readline()

        seeds = f_contents_seeds.split()
        seeds = [int(seed) for seed in seeds]
        return seeds

    @staticmethod
    def parse_seed_ranges():
        with open("seeds.dat") as f:
            f_contents_seeds = f.readline()
        split_seeds = f_contents_seeds.split()
        seed_ranges = []
        for i in range(0, len(split_seeds), 2):
            seed_value = int(split_seeds[i])
            range_value = int(split_seeds[i + 1])
            seed_range = SeedRange(seed_value, range_value)
            seed_ranges.append(seed_range)
        return seed_ranges

    @staticmethod
    def parse_mapping_file(file_name):
        with open(file_name) as f:
            f_contents = f.readlines()

        mapping_list = []
        for line in f_contents:
            destination, source, range = line.split()
            source_destination_range = SourceDestinationRange(int(source), int(destination), int(range))
            mapping_list.append(source_destination_range)
        return mapping_list

    def parse_data(self):
        seeds = self.parse_seeds()
        seed_ranges = self.parse_seed_ranges()
        seeds_to_soil = self.parse_mapping_file("seeds_to_soil.dat")
        soil_to_fertilizer = self.parse_mapping_file("soil_to_fertilizer.dat")
        fertilizer_to_water = self.parse_mapping_file("fertilizer_to_water.dat")
        water_to_light = self.parse_mapping_file("water_to_light.dat")
        light_to_temperature = self.parse_mapping_file("light_to_temperature.dat")
        temperature_to_humidity = self.parse_mapping_file("temperature_to_humidity.dat")
        humidity_to_location = self.parse_mapping_file("humidity_to_location.dat")

        data = Data(seeds, seeds_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature,
                    temperature_to_humidity, humidity_to_location, seed_ranges)

        self.data = data


    def parse_data_star2(self):
        self.parse_data()
        self.parse_seed_ranges()


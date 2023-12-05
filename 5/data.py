from source_destination_range import SourceDestinationRange


class Data:
    def __init__(self, seeds, seeds_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature,
                 temperature_to_humidity, humidity_to_location, seed_ranges=None):
        self.seeds = seeds
        self.seeds_to_soil = seeds_to_soil
        self.soil_to_fertilizer = soil_to_fertilizer
        self.fertilizer_to_water = fertilizer_to_water
        self.water_to_light = water_to_light
        self.light_to_temperature = light_to_temperature
        self.temperate_to_humidity = temperature_to_humidity
        self.humidity_to_location = humidity_to_location
        self.seed_ranges = seed_ranges

        self.mapping_list = [self.seeds_to_soil, self.soil_to_fertilizer, self.fertilizer_to_water, self.water_to_light,
                             self.light_to_temperature, self.temperate_to_humidity, self.humidity_to_location]

import math

from data_parser import DataParser
from seed_mapped_values import SeedMappedValues
from seed_mapping import SeedMapping
from source_destination_range import SourceDestinationRange
from typing import List

class IfYouGiveASeedAFertilizer:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def map_value(value, mappings: List[SourceDestinationRange]):
        for mapping in mappings:
            if mapping.source_range_start <= value <= mapping.source_range_end:
                return value + mapping.difference_between_source_and_destination

        return value

    def get_min_location(self):
        mapped_seeds = []
        for seed in self.data.seeds:
            mapped_value = seed
            for mapping in self.data.mapping_list:
                mapped_value = self.map_value(mapped_value, mapping)
            mapped_seeds.append(mapped_value)
        return min(mapped_seeds)

    @staticmethod
    def map_value_ranges(seed_mapped_values: SeedMappedValues, mappings: List[SourceDestinationRange]):
        for mapping in mappings:

            new_seed_mappings = []
            for seed_mapping in seed_mapped_values.seed_mappings:

                # get actual start and end of mapping after mapping is applied
                mapping_start = mapping.source_range_start - seed_mapping.map_by
                mapping_end = mapping.source_range_end - seed_mapping.map_by

                if (seed_mapping.start_value <= mapping_start <= seed_mapping.end_value
                        or mapping_start <= seed_mapping.start_value <= mapping_end):

                    start_range = max(seed_mapping.start_value, mapping_start)
                    end_range = min(seed_mapping.end_value, mapping_end)

                    difference = seed_mapping.map_by + mapping.difference_between_source_and_destination

                    new_seed_mapping = SeedMapping(start_range, end_range, difference)
                    new_seed_mappings.append(new_seed_mapping)

                    if start_range > seed_mapping.start_value:
                        lower_range_seed_mapping = SeedMapping(seed_mapping.start_value, start_range - 1,
                                                               seed_mapping.map_by)

                        new_seed_mappings.append(lower_range_seed_mapping)

                    if end_range < seed_mapping.end_value:
                        upper_range_seed_mapping = SeedMapping(end_range + 1, new_seed_mapping.end_value,
                                                               seed_mapping.map_by)
                        new_seed_mappings.append(upper_range_seed_mapping)

                else:
                    new_seed_mappings.append(seed_mapping)

            seed_mapped_values.seed_mappings = new_seed_mappings

    def get_min_location_for_seed_ranges(self):
        seed_mapped_values_list = []
        for seed_range in self.data.seed_ranges:
            seed_mapped_values = SeedMappedValues(seed_range.seed_value, seed_range.range_value)
            for mappings in self.data.mapping_list:
                self.map_value_ranges(seed_mapped_values, mappings)
            seed_mapped_values_list.append(seed_mapped_values)

        min_value = math.inf
        for seed_mapped_values in seed_mapped_values_list:
            for seed_mapping in seed_mapped_values.seed_mappings:
                value = seed_mapping.start_value + seed_mapping.map_by
                if value < min_value:
                    min_value = value
        return min_value


def main():
    data_parser = DataParser()
    data_parser.parse_data()
    if_you_give_a_seed_a_fertilizer = IfYouGiveASeedAFertilizer(data_parser.data)
    print(if_you_give_a_seed_a_fertilizer.get_min_location())
    print(if_you_give_a_seed_a_fertilizer.get_min_location_for_seed_ranges())


if __name__ == "__main__":
    main()

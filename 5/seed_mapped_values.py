from seed_mapping import SeedMapping


class SeedMappedValues:
    def __init__(self, seed_value=None, range_value=None):
        if seed_value is None and range_value is None:
            self.seed_mappings = []
        else:
            self.seed_mappings = [SeedMapping(seed_value, seed_value + range_value - 1, 0)]

class SourceDestinationRange:
    def __init__(self, source_range_start, destination_range_start, range_length):
        self.source_range_start = source_range_start
        self.destination_range_start = destination_range_start
        self.range_length = range_length
        self.source_range_end = source_range_start + range_length - 1
        self.difference_between_source_and_destination = destination_range_start - source_range_start

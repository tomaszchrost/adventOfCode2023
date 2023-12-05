import pytest
from if_you_give_a_seed_a_fertilizer import IfYouGiveASeedAFertilizer
from seed_mapped_values import SeedMappedValues
from seed_mapping import SeedMapping
from source_destination_range import SourceDestinationRange

def test_map_value_ranges_in_the_middle():
    seed_mapped_values = SeedMappedValues()
    seed_mapped_values.seed_mappings.append(SeedMapping(10, 100, 8))
    source_destination_range = SourceDestinationRange(30, 40, 20)

    if_you_give_a_seed_a_fertilizer = IfYouGiveASeedAFertilizer(None)

    if_you_give_a_seed_a_fertilizer.map_value_ranges(seed_mapped_values, [source_destination_range])

    assert seed_mapped_values.seed_mappings[0].start_value == 22
    assert seed_mapped_values.seed_mappings[0].end_value == 42
    assert seed_mapped_values.seed_mappings[0].map_by == 18

    assert seed_mapped_values.seed_mappings[1].start_value == 10
    assert seed_mapped_values.seed_mappings[1].end_value == 21
    assert seed_mapped_values.seed_mappings[1].map_by == 8

    assert seed_mapped_values.seed_mappings[2].start_value == 43
    assert seed_mapped_values.seed_mappings[2].end_value == 100
    assert seed_mapped_values.seed_mappings[2].map_by == 8


def test_map_value_ranges_above_range():
    seed_mapped_values = SeedMappedValues()
    seed_mapped_values.seed_mappings.append(SeedMapping(10, 30, 8))
    source_destination_range = SourceDestinationRange(30, 40, 20)

    if_you_give_a_seed_a_fertilizer = IfYouGiveASeedAFertilizer(None)

    if_you_give_a_seed_a_fertilizer.map_value_ranges(seed_mapped_values, [source_destination_range])

    assert seed_mapped_values.seed_mappings[0].start_value == 22
    assert seed_mapped_values.seed_mappings[0].end_value == 30
    assert seed_mapped_values.seed_mappings[0].map_by == 18

    assert seed_mapped_values.seed_mappings[1].start_value == 10
    assert seed_mapped_values.seed_mappings[1].end_value == 21
    assert seed_mapped_values.seed_mappings[1].map_by == 8

    assert len(seed_mapped_values.seed_mappings) == 2


def test_map_value_ranges_below_range():
    seed_mapped_values = SeedMappedValues()
    seed_mapped_values.seed_mappings.append(SeedMapping(30, 100, 8))
    source_destination_range = SourceDestinationRange(30, 40, 20)

    if_you_give_a_seed_a_fertilizer = IfYouGiveASeedAFertilizer(None)

    if_you_give_a_seed_a_fertilizer.map_value_ranges(seed_mapped_values, [source_destination_range])

    assert seed_mapped_values.seed_mappings[0].start_value == 30
    assert seed_mapped_values.seed_mappings[0].end_value == 42
    assert seed_mapped_values.seed_mappings[0].map_by == 18

    assert seed_mapped_values.seed_mappings[1].start_value == 43
    assert seed_mapped_values.seed_mappings[1].end_value == 100
    assert seed_mapped_values.seed_mappings[1].map_by == 8

    assert len(seed_mapped_values.seed_mappings) == 2

def test_map_value_ranges_outside_range():
    seed_mapped_values = SeedMappedValues()
    seed_mapped_values.seed_mappings.append(SeedMapping(10, 20, 8))
    source_destination_range = SourceDestinationRange(30, 40, 20)

    if_you_give_a_seed_a_fertilizer = IfYouGiveASeedAFertilizer(None)

    if_you_give_a_seed_a_fertilizer.map_value_ranges(seed_mapped_values, [source_destination_range])

    assert seed_mapped_values.seed_mappings[0].start_value == 10
    assert seed_mapped_values.seed_mappings[0].end_value == 20
    assert seed_mapped_values.seed_mappings[0].map_by == 8

    assert len(seed_mapped_values.seed_mappings) == 1


def test_map_value_ranges_fully_in_range():
    seed_mapped_values = SeedMappedValues()
    seed_mapped_values.seed_mappings.append(SeedMapping(10, 20, 8))
    source_destination_range = SourceDestinationRange(0, 10, 100)

    if_you_give_a_seed_a_fertilizer = IfYouGiveASeedAFertilizer(None)

    if_you_give_a_seed_a_fertilizer.map_value_ranges(seed_mapped_values, [source_destination_range])

    assert seed_mapped_values.seed_mappings[0].start_value == 10
    assert seed_mapped_values.seed_mappings[0].end_value == 20
    assert seed_mapped_values.seed_mappings[0].map_by == 18

    assert len(seed_mapped_values.seed_mappings) == 1

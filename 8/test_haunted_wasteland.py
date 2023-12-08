from data import Node
from haunted_wasteland import HauntedWasteland


def test_all_nodes_are_end_nodes():
    nodes = [Node("AAZ", "XXX", "XXX"),
             Node("ZAZ", "XXX", "XXX"),
             Node("ZZZ", "XXX", "XXX")]
    assert HauntedWasteland.all_nodes_are_end_nodes(nodes)

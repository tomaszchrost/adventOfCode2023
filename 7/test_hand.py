from hand import Hand

def test_lt_hand():
    hand_one = Hand([1, 1, 1, 1, 1])
    hand_two = Hand([1, 1, 6, 1, 1])

    assert hand_one < hand_two